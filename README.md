# 📦 QR Code Generator (Python + Streamlit)

A simple and interactive **QR Code Generator** built using **Python** and **Streamlit**.  
This tool lets users generate QR codes from text or URLs, customize settings, and download the generated QR image instantly.

---

## 📑 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Screenshots](#-screenshots)
- [Troubleshooting](#-troubleshooting)
- [Contributors](#-contributors)
- [License](#-license)

---

## 🧩 Introduction

This project provides a lightweight and user-friendly web application for generating QR codes.  
Users can enter any text or URL, and the app will instantly create a downloadable QR code image.

The app is powered by **Streamlit**, making it browser-based, responsive, and easy to deploy.

---

## ✨ Features

✔ Generate QR codes from text or URLs  
✔ Download the QR code as a PNG image  
✔ Customize QR size, border, and color  
✔ Mobile-friendly interface  
✔ No backend required — fully client-side via Streamlit

---

## 🛠 Tech Stack

- **Python 3.x**
- **Streamlit**
- **qrcode**
- **Pillow (PIL)**

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit qrcode pillow
```

---

## ▶ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open the local development URL shown in the terminal (usually `http://localhost:8501/`).

Enter any text/URL → Customize options → Download QR Code!

---

## 📂 Project Structure

```
.
├── scripts/
│   └── qr_cli.py
│
├── src/
│   ├── __pycache__/
│   └── qr_generator.py
│
├── tests/
│   ├── __pycache__/
│   └── test_qr_generator.py
│
├── README.md
├── requirements.txt
└── streamlit_app.py
```

---


---

## ⚙ Configuration

You can modify QR settings inside `app.py`:

```python
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
```

Adjust:
- **Version** → Complexity  
- **Box size** → Pixel size  
- **Border** → Margin thickness  
- **Colors** → Fill and background  

---

## 📸 Screenshots

(Add your own images in the `assets/` folder.)

```
![Demo](assets/sample_qr.png)
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Streamlit not launching | Check Python PATH / reinstall Streamlit |
| QR not generating | Ensure text field is not empty |
| Image not downloading | Enable pop-ups or check browser settings |

---

## 👨‍💻 Contributors

- **Your Name** – Developer & Maintainer  
Contributions are welcome! Feel free to open issues or pull requests.

---

## 📄 License

This project is licensed under the **MIT License**.  
You may use, modify, and distribute this project freely.
