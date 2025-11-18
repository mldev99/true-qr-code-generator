# True QR Code Generator (Python)

A small, standalone QR code generator in Python. Provides a simple Python API and a CLI to generate QR codes as PNG images.

Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

Quick start

Install dependencies:

```powershell
pip install -r requirements.txt
```

Generate a QR code from the CLI:

```powershell
python .\scripts\qr_cli.py --text "https://example.com" --out example.png
```

Use from Python:

```python
from src.qr_generator import generate_qr
generate_qr("Hello world", "qrcode.png")
```

Tests

```powershell
python -m pytest -q
```

License: MIT (use as you like)
