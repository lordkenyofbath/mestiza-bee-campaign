# Mestiza Bee Campaign – Streamlit App

Quick way to host + share the full campaign plan as an interactive page + printable PDF.

## Files
- `campaign.html`  – the single-page plan (drop your final version here)
- `app.py`         – tiny Streamlit wrapper
- `requirements.txt` – only needs streamlit

## Deploy in 2 min
1. Fork / clone this repo.
2. Drop your final `campaign.html` in the same folder.
3. Go to [share.streamlit.io](https://share.streamlit.io) → Deploy → pick the repo.
4. Share the Streamlit URL (https://*.streamlit.app) – visitors can read online or download the HTML for PDF printing.

## Local test
```bash
pip install -r requirements.txt
streamlit run app.py
