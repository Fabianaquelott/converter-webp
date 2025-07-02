import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

RESOLUTION_LABELS = ["@1x", "@2x", "@desktop"]

def calculate_sizes(original_width, original_height):
    desktop_w, desktop_h = original_width, original_height
    x2_w, x2_h = desktop_w // 2, desktop_h // 2
    x1_w, x1_h = x2_w // 2, x2_h // 2
    return {
        "@1x": (x1_w, x1_h),
        "@2x": (x2_w, x2_h),
        "@desktop": (desktop_w, desktop_h),
    }

def update_sizes_fields(filepath):
    try:
        img = Image.open(filepath)
        w, h = img.size
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir a imagem: {e}")
        return

    sizes = calculate_sizes(w, h)

    for label in RESOLUTION_LABELS:
        width_var = resolution_fields[label]["width"]
        height_var = resolution_fields[label]["height"]
        width_var.set(str(sizes[label][0]))
        height_var.set(str(sizes[label][1]))

def convert_image(cwebp_path, filepath, selected, output_folder, quality):
    filename = os.path.splitext(os.path.basename(filepath))[0]

    for label, data in selected.items():
        if not data["enabled"].get():
            continue

        try:
            width = int(data["width"].get())
            height = int(data["height"].get())
        except ValueError:
            messagebox.showerror("Erro", f"Tamanho inválido para {label}. Use apenas números.")
            return False

        output_path = os.path.join(output_folder, f"{filename}{label}.webp")
        cmd = [
            cwebp_path,
            "-q", str(quality),
            "-resize", str(width), str(height),
            filepath,
            "-o", output_path
        ]

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Erro", f"Falha na conversão: {e}")
            return False

    return True

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
    if filepath:
        file_var.set(filepath)
        update_sizes_fields(filepath)

def choose_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_var.set(folder)

def choose_cwebp():
    exe_path = filedialog.askopenfilename(filetypes=[("Executável cwebp", "cwebp.exe")])
    if exe_path:
        cwebp_var.set(exe_path)

def start_conversion():
    cwebp_path = cwebp_var.get()
    filepath = file_var.get()
    output_folder = output_var.get()
    quality = quality_var.get()

    if not cwebp_path or not os.path.isfile(cwebp_path):
        messagebox.showerror("Erro", "Selecione o executável cwebp.exe válido.")
        return

    if not filepath.endswith(".png"):
        messagebox.showerror("Erro", "Selecione uma imagem .png válida.")
        return

    if not output_folder:
        messagebox.showerror("Erro", "Selecione uma pasta de saída.")
        return

    try:
        q = int(quality)
        if not (0 <= q <= 100):
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Insira um valor de qualidade entre 0 e 100.")
        return

    if all(not data["enabled"].get() for data in resolution_fields.values()):
        messagebox.showwarning("Aviso", "Selecione ao menos uma resolução.")
        return

    loading = tk.Toplevel(root)
    loading.title("Aguarde")
    loading.geometry("200x80")
    loading.resizable(False, False)
    loading.grab_set() 
    tk.Label(loading, text="Convertendo, por favor aguarde...").pack(expand=True, pady=20)
    root.update()

    success = convert_image(cwebp_path, filepath, resolution_fields, output_folder, q)

    loading.destroy()

    if success:
        messagebox.showinfo("Sucesso", f"Conversão concluída!\nArquivos salvos em:\n{output_folder}")

root = tk.Tk()
root.title("Conversor PNG para WebP")

file_var = tk.StringVar()
output_var = tk.StringVar()
quality_var = tk.StringVar(value="85")
cwebp_var = tk.StringVar()
resolution_fields = {}

frame_cwebp = tk.Frame(root)
tk.Label(frame_cwebp, text="Executável cwebp.exe:").pack(side="left", padx=5)
tk.Entry(frame_cwebp, textvariable=cwebp_var, width=50).pack(side="left", padx=5)
tk.Button(frame_cwebp, text="Selecionar", command=choose_cwebp).pack(side="left", padx=5)
frame_cwebp.pack(pady=10)

tk.Label(root, text="Imagem PNG:").pack(pady=5)
tk.Entry(root, textvariable=file_var, width=60).pack(padx=10)
tk.Button(root, text="Selecionar Imagem", command=browse_file).pack(pady=5)

tk.Label(root, text="Qualidade da imagem (0-100):").pack(pady=5)
tk.Entry(root, textvariable=quality_var, width=10, justify="center").pack()

tk.Label(root, text="Resoluções e tamanhos (calculados a partir da imagem):").pack(pady=10)
for label in RESOLUTION_LABELS:
    frame = tk.Frame(root)
    enabled = tk.BooleanVar(value=True)
    width_var = tk.StringVar()
    height_var = tk.StringVar()

    tk.Checkbutton(frame, text=label, variable=enabled, width=6).pack(side="left", padx=5)
    tk.Label(frame, text="Largura:").pack(side="left")
    tk.Entry(frame, textvariable=width_var, width=6).pack(side="left", padx=3)
    tk.Label(frame, text="Altura:").pack(side="left")
    tk.Entry(frame, textvariable=height_var, width=6).pack(side="left", padx=3)
    frame.pack(pady=2)

    resolution_fields[label] = {
        "enabled": enabled,
        "width": width_var,
        "height": height_var,
    }

tk.Label(root, text="Pasta de saída:").pack(pady=5)
tk.Entry(root, textvariable=output_var, width=60).pack(padx=10)
tk.Button(root, text="Selecionar Pasta", command=choose_output_folder).pack(pady=5)

tk.Button(root, text="Converter", command=start_conversion, bg="#4CAF50", fg="white").pack(pady=10)

root.mainloop()
