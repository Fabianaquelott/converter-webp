<h1 align="center">🖼️ PNG to Responsive WebP Converter</h1>

<p align="center">
  A lightweight tool to convert PNG images into responsive <code>.webp</code> formats with multiple resolutions.<br>
  Optimized for modern websites that demand fast, flexible image delivery.
</p>

<hr/>

<h2>🚀 Features</h2>
<ul>
  <li>Converts <code>.png</code> files into optimized <code>.webp</code></li>
  <li>Creates multiple sizes (e.g., <code>@1x</code>, <code>@2x</code>, <code>@desktop</code>)</li>
  <li>Improves page speed and responsiveness</li>
  <li>Use as a Python script or compile to <code>.exe</code> for Windows</li>
</ul>

<hr/>

<h2>🧰 Requirements (Script Version)</h2>
<p>Make sure you have Python 3.7+ installed, then install the required package:</p>

<pre><code>pip install pillow</code></pre>

<p><strong>⚠️ Important:</strong> The script also requires <code>cwebp.exe</code> from Google's WebP tools. You must:</p>
<ul>
  <li>Download it from <a href="https://developers.google.com/speed/webp/download" target="_blank">https://developers.google.com/speed/webp/download</a></li>
  <li>Place <code>cwebp.exe</code> in the same folder as <code>conversor.py</code>, or ensure it is available in your system's <code>PATH</code></li>
</ul>

<hr/>

<h2>📁 How to Use the Script (Python Version)</h2>
<ol>
  <li>Place your <code>.png</code> images inside the <strong>input/</strong> folder</li>
  <li>Ensure <code>cwebp.exe</code> is available as described above</li>
  <li>Run the script:</li>
</ol>

<pre><code>python conversor.py</code></pre>

<p>The converted images will appear in the <strong>output/</strong> folder with various responsive sizes:</p>
<ul>
  <li><code>@1x</code></li>
  <li><code>@2x</code></li>
  <li><code>@desktop</code></li>
</ul>

<hr/>

<h2>🪄 How to Compile to EXE (Windows)</h2>

<p>This allows you to run the converter without needing Python installed:</p>

<ol>
  <li>Install PyInstaller:</li>
</ol>
<pre><code>pip install pyinstaller</code></pre>

<ol start="2">
  <li>Compile the script:</li>
</ol>
<pre><code>pyinstaller --onefile --icon=icon.ico conversor.py</code></pre>

<p>The compiled executable will be located in the <strong>dist/</strong> folder. To run it:</p>

<pre><code>./dist/conversor.exe</code></pre>

<p><strong>Reminder:</strong> Make sure <code>cwebp.exe</code> is located in the same folder as the EXE, or is accessible via <code>PATH</code>.</p>

<hr/>

<h2>🖼️ Output Example</h2>

<p>If your source file is <code>logo.png</code>, the script will generate:</p>

<pre><code>
output/
├── logo@1x.webp
├── logo@2x.webp
└── logo@desktop.webp
</code></pre>
