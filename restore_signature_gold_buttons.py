# -*- coding: utf-8 -*-
import os, re

# Restore Signature Kesar Gold for Buttons and Brand Accents: #FFB020 (hover: #FFBA36)

# 1. UPDATE styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("--kesar: #FF5E14;", "--kesar: #FFB020;")
css = css.replace("--kesar-hot: #E64A00;", "--kesar-hot: #FFB020;")
css = css.replace("--kesar-hover: #FF7A29;", "--kesar-hover: #FFBA36;")
css = css.replace("rgba(255, 94, 20", "rgba(255, 176, 32")
css = css.replace("#FF5E14", "#FFB020")
css = css.replace("#FF7A29", "#FFBA36")
css = css.replace("#E64A00", "#FFB020")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Restored button color in styles.css")

# 2. UPDATE index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("--kesar:#FF5E14;", "--kesar:#FFB020;")
html = html.replace("--kesar-hot:#E64A00;", "--kesar-hot:#FFB020;")
html = html.replace("--kesar-hover:#FF7A29;", "--kesar-hover:#FFBA36;")
html = html.replace("rgba(255, 94, 20", "rgba(255, 176, 32")
html = html.replace("rgba(255,94,20", "rgba(255,176,32")
html = html.replace("#FF5E14", "#FFB020")
html = html.replace("#FF7A29", "#FFBA36")
html = html.replace("#E64A00", "#FFB020")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Restored button color in index.html & franq-franchise-website.html")

# 3. UPDATE ALL OTHER HTML FILES
all_html = [
    "about.html", "franchises.html", "find-franchise.html", "book-consultation.html",
    "develop-brand.html", "develop-scale.html", "franchise-marketing.html"
]

for filename in all_html:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("--kesar: #FF5E14;", "--kesar: #FFB020;")
        content = content.replace("--kesar-hot: #E64A00;", "--kesar-hot: #FFB020;")
        content = content.replace("--kesar-hover: #FF7A29;", "--kesar-hover: #FFBA36;")
        content = content.replace("rgba(255, 94, 20", "rgba(255, 176, 32")
        content = content.replace("rgba(255,94,20", "rgba(255,176,32")
        content = content.replace("#FF5E14", "#FFB020")
        content = content.replace("#FF7A29", "#FFBA36")
        content = content.replace("#E64A00", "#FFB020")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Restored button color in {filename}")

# 4. UPDATE generate_brand_pages.py
with open("generate_brand_pages.py", "r", encoding="utf-8") as f:
    gbp = f.read()

gbp = gbp.replace("#FF5E14", "#FFB020")
gbp = gbp.replace("#FF7A29", "#FFBA36")
gbp = gbp.replace("#E64A00", "#FFB020")
gbp = gbp.replace("rgba(255, 94, 20", "rgba(255, 176, 32")
gbp = gbp.replace("rgba(255,94,20", "rgba(255,176,32")

with open("generate_brand_pages.py", "w", encoding="utf-8") as f:
    f.write(gbp)

print("Restored button color in generate_brand_pages.py")
