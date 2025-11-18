import os
import tempfile
from src.qr_generator import generate_qr, generate_qr_bytes
from PIL import Image


def test_generate_png_file():
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    tmp.close()
    path = tmp.name
    try:
        generate_qr("https://example.com", path, box_size=8)
        assert os.path.exists(path)
        with Image.open(path) as img:
            assert img.format == 'PNG'
            assert img.size[0] > 0 and img.size[1] > 0
    finally:
        os.remove(path)


def test_generate_bytes_return_png():
    b = generate_qr_bytes("hello bytes", box_size=6)
    assert isinstance(b, (bytes, bytearray))
    # Basic sanity: bytes should start with PNG header
    assert b[:8] == b"\x89PNG\r\n\x1a\n"
