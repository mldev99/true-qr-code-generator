import streamlit as st
from src.qr_generator import generate_qr_bytes

st.set_page_config(page_title="True QR Code Generator", page_icon="🔳")
st.title("True QR Code Generator")

text = st.text_area("Text or URL to encode", value="https://example.com", height=120)
col1, col2 = st.columns(2)
box_size = col1.slider("Box size", 2, 40, 10)
border = col2.slider("Border", 0, 10, 4)
fill = st.color_picker("Fill color", "#000000")
back = st.color_picker("Background color", "#ffffff")

if st.button("Generate QR"):
    if not text:
        st.error("Please enter text or URL to encode.")
    else:
        try:
            png_bytes = generate_qr_bytes(text, box_size=box_size, border=border, fill_color=fill, back_color=back)
            st.image(png_bytes, caption="QR Code", use_column_width=False)
            st.download_button("Download PNG", data=png_bytes, file_name="qr.png", mime="image/png")
        except Exception as exc:
            st.exception(exc)

st.markdown("---")
st.write("Or use the CLI: `python scripts/qr_cli.py --text \"https://example.com\" --out qr.png`")
