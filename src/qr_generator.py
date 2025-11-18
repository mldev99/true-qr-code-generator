from io import BytesIO
import qrcode
from PIL import Image


def generate_qr(data: str, output_path: str, box_size: int = 10, border: int = 4,
                fill_color: str = "black", back_color: str = "white") -> str:
    """Generate a QR code from `data` and save it to `output_path` (PNG).

    Returns the `output_path` on success.
    """
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")
    img.save(output_path, format="PNG")
    return output_path


def generate_qr_bytes(data: str, box_size: int = 10, border: int = 4,
                      fill_color: str = "black", back_color: str = "white") -> bytes:
    """Generate a QR code and return PNG bytes (in-memory)."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


__all__ = ["generate_qr", "generate_qr_bytes"]
