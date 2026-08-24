# -*- coding: utf-8 -*-
import os, re

# Deep Midnight Charcoal & Jet Slate Palette:
# Deep Dark: #080B10 / #0E121A / #181F2C
# Gold Buttons: #FFB020 / #FFBA36 (Kept intact!)
# Electric Mint: #00E599
# Crisp White / Paper: #FFFFFF / #F6F7F9

# 1. UPDATE styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace CSS variables
css = css.replace("--jamun: #1E0F38;", "--jamun: #0E121A;")
css = css.replace("--jamun-deep: #140A24;", "--jamun-deep: #080B10;")
css = css.replace("--jamun-soft: #2F1754;", "--jamun-soft: #181F2C;")
css = css.replace("--paper: #FFFBF5;", "--paper: #F6F7F9;")
css = css.replace("--ink: #1A0D2E;", "--ink: #0E121A;")
css = css.replace("--ink-80: #331E56;", "--ink-80: #222938;")
css = css.replace("--ink-60: rgba(26, 13, 46, 0.7);", "--ink-60: rgba(14, 18, 26, 0.68);")
css = css.replace("--ink-30: rgba(26, 13, 46, 0.28);", "--ink-30: rgba(14, 18, 26, 0.28);")
css = css.replace("--line: rgba(26, 13, 46, 0.08);", "--line: rgba(14, 18, 26, 0.08);")

# Global replacements of dark hexes in styles.css
css = css.replace("#1E0F38", "#0E121A")
css = css.replace("#140A24", "#080B10")
css = css.replace("#2F1754", "#181F2C")
css = css.replace("rgba(30, 15, 56", "rgba(14, 18, 26")
css = css.replace("rgba(20, 10, 36", "rgba(8, 11, 16")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated styles.css with Midnight Charcoal & Jet Slate")

# 2. UPDATE index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace :root tokens in index.html
html = html.replace("--jamun:#1E0F38;", "--jamun:#0E121A;")
html = html.replace("--jamun-deep:#140A24;", "--jamun-deep:#080B10;")
html = html.replace("--jamun-soft:#2F1754;", "--jamun-soft:#181F2C;")
html = html.replace("--paper:#FFFBF5;", "--paper:#F6F7F9;")
html = html.replace("--ink:#1A0D2E;", "--ink:#0E121A;")
html = html.replace("--ink-80:#331E56;", "--ink-80:#222938;")
html = html.replace("--ink-60:rgba(26,13,46,.7);", "--ink-60:rgba(14,18,26,.68);")
html = html.replace("--ink-30:rgba(26,13,46,.28);", "--ink-30:rgba(14,18,26,.28);")
html = html.replace("--line:rgba(26,13,46,.08);", "--line:rgba(14,18,26,.08);")

# Global replacements in index.html
html = html.replace("#1E0F38", "#0E121A")
html = html.replace("#140A24", "#080B10")
html = html.replace("#2F1754", "#181F2C")
html = html.replace("rgba(30, 15, 56", "rgba(14, 18, 26")
html = html.replace("rgba(20, 10, 36", "rgba(8, 11, 16")

# Update hero background overlay in index.html
html = html.replace(
    "background: radial-gradient(circle at 50% 35%, rgba(30, 15, 56, 0.42) 0%, rgba(20, 10, 36, 0.7) 65%, rgba(20, 10, 36, 0.94) 100%);",
    "background: radial-gradient(circle at 50% 35%, rgba(14, 18, 26, 0.42) 0%, rgba(8, 11, 16, 0.7) 65%, rgba(8, 11, 16, 0.94) 100%);"
)
html = html.replace(".hero{position:relative;background:#140A24;", ".hero{position:relative;background:#080B10;")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html & franq-franchise-website.html")

# 3. UPDATE ALL OTHER HTML FILES
all_html = [
    "about.html", "franchises.html", "find-franchise.html", "book-consultation.html",
    "develop-brand.html", "develop-scale.html", "franchise-marketing.html"
]

for filename in all_html:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("#1E0F38", "#0E121A")
        content = content.replace("#140A24", "#080B10")
        content = content.replace("#2F1754", "#181F2C")
        content = content.replace("rgba(30, 15, 56", "rgba(14, 18, 26")
        content = content.replace("rgba(20, 10, 36", "rgba(8, 11, 16")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated dark colors in {filename}")

# 4. UPDATE generate_brand_pages.py
with open("generate_brand_pages.py", "r", encoding="utf-8") as f:
    gbp = f.read()

gbp = gbp.replace("#1E0F38", "#0E121A")
gbp = gbp.replace("#140A24", "#080B10")
gbp = gbp.replace("#2F1754", "#181F2C")
gbp = gbp.replace("rgba(30, 15, 56", "rgba(14, 18, 26")
gbp = gbp.replace("rgba(20, 10, 36", "rgba(8, 11, 16")

with open("generate_brand_pages.py", "w", encoding="utf-8") as f:
    f.write(gbp)

print("Updated generate_brand_pages.py with Midnight Charcoal & Jet Slate")
