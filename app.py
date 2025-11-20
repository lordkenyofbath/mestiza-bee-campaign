import streamlit as st
import base64, pathlib, platform

HTML = pathlib.Path("campaign.html").read_text(encoding="utf-8")

st.set_page_config(page_title="Bee-Campaign Plan", layout="centered")
st.title("📄 Mestiza de Indias – Campaign Plan")
st.components.v1.html(HTML, height=600, scrolling=True)

# Browser-side download (no extra libs)
b64 = base64.b64encode(HTML.encode()).decode()
st.download_button(
    label="⬇️ Download HTML file",
    data=HTML,
    file_name="mestiza-bee-campaign.html",
    mime="text/html"
)

st.info("Open the HTML file → Ctrl+P → Save as PDF")
