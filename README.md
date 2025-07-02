Claro! Aqui está um `README.md` em inglês, com uma apresentação bonita usando HTML dentro do Markdown, e explicações claras de uso tanto do script `.py` quanto da versão `.exe` compilada.

---

````markdown
<h1 align="center">🖼️ PNG to Responsive WebP Converter</h1>

<p align="center">
  A simple Python script to convert PNG images into responsive <code>.webp</code> formats with multiple sizes.<br>
  Ideal for optimizing websites and delivering the right image size to each screen.
</p>

<hr/>

## 🚀 Features

- ✅ Converts `.png` images into `.webp`
- ✅ Generates multiple resolutions (e.g., `@1x`, `@2x`, `@desktop`)
- ✅ Improves page load performance for responsive websites
- ✅ Works as a Python script or standalone `.exe` executable

---

## 🧰 Requirements (for script use)

Make sure you have Python 3.7+ installed.

Install the required libraries:

```bash
pip install pillow
````

---

## 📁 How to Use (Python Script)

1. Place your `.png` images inside the `input/` folder.
2. Run the script:

```bash
python conversor.py
```

3. The output images will be saved to the `output/` folder in WebP format with different sizes:

   * `@1x` (e.g., 480px)
   * `@2x` (e.g., 768px)
   * `@desktop` (e.g., 1200px)

---

## 🪄 How to Compile to .EXE

> 💡 Useful if you want to run the tool on Windows without installing Python.

1. Make sure you have **PyInstaller** installed:

```bash
pip install pyinstaller
```

2. Run this command to generate the `.exe`:

```bash
pyinstaller --onefile --icon=icon.ico conversor.py
```

3. The compiled `.exe` will be located in the `dist/` folder.

To run:

```bash
./dist/conversor.exe
```

It will behave the same as the Python version — looking for PNGs in `input/` and saving to `output/`.

---

## 🖼️ Output Naming Example

If you have a file named `logo.png`, the script will generate:

```
output/
├── logo@1x.webp
├── logo@2x.webp
└── logo@desktop.webp
```

---

## 💡 Tip: HTML Usage with srcSet

Use the images responsively in your HTML like this:

```html
<img
  src="/images/logo@1x.webp"
  srcset="/images/logo@1x.webp 480w,
          /images/logo@2x.webp 768w,
          /images/logo@desktop.webp 1200w"
  sizes="(max-width: 600px) 480px,
         (max-width: 1024px) 768px,
         1200px"
  alt="Logo"
/>
```

---

## 📄 License

MIT — Feel free to use, share, and improve!

---

```

---

Se quiser que eu gere o conteúdo direto no seu arquivo local ou personalize mais (como sufixos, tamanhos, caminhos, ícone do `.exe`, etc.), posso te ajudar com isso também.
```
