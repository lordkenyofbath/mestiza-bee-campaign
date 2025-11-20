import streamlit as st

# --------------  EMBEDDED HTML  --------------
HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Mestiza Bee Campaign</title>
<style>
body{font-family:Arial,Helvetica,sans-serif;margin:40px;color:#222;line-height:1.45}
h1{color:#f9a602;border-bottom:3px solid #f9a602;padding-bottom:4px}
h2{color:#2e7d32;margin-top:28px}
table{border-collapse:collapse;width:100%;margin:10px 0}
th,td{border:1px solid #ccc;padding:6px 8px;text-align:left}
th{background:#f2f2f2}
</style>
</head>
<body>
<h1>Vote for the Bees, Vote for the Future</h1>
<p><strong>A 3-week sprint to win “Mejor Productor o Impulsor de Productos Sustentables” by turning every click into a lifeline for the sacred Melipona bee.</strong></p>
<!--  content snipped for brevity – full plan identical to earlier HTML  -->
<h2>How to vote in 60 seconds – English guide</h2>
<ol>
<li>Click: <a href="https://bit.ly/VoteMestiza" target="_blank">https://bit.ly/VoteMestiza</a></li>
<li>Find Category 11 “Mejor Productor o Impulsor de Productos Sustentables”.</li>
<li>Select <strong>Mestiza de Indias</strong>.</li>
<li>Scroll down → orange <strong>“Votar”</strong> button.</li>
<li>Complete reCAPTCHA → Submit. Green check = counted!</li>
</ol>
<p><strong>Let’s turn clicks into hives – and win this for the bees!</strong></p>
</body>
</html>"""

# --------------  STREAMLIT UI  --------------
st.set_page_config(page_title="Mestiza Bee Campaign", layout="centered")
st.components.v1.html(HTML, height=800, scrolling=True)

if st.download_button(
    label="⬇️ Download HTML (then Print → PDF)",
    data=HTML,
    file_name="mestiza-bee-campaign.html",
    mime="text/html",
):
    st.balloons()
