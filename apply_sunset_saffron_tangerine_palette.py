# -*- coding: utf-8 -*-
import os, re

# Sunset Saffron & Electric Tangerine Palette
# Deep Royal Plum (#140A24 / #1E0F38), Bright Sunset Saffron (#FF5E14 / #FF7A29), Honey Gold (#FFB800), Neon Mint (#00E599), Sunny Pearl White (#FFFBF5 / #FFFFFF)

# 1. UPDATE styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace CSS variables
css = css.replace("--jamun: #0F172A;", "--jamun: #1E0F38;")
css = css.replace("--jamun-deep: #0A0F1D;", "--jamun-deep: #140A24;")
css = css.replace("--jamun-soft: #1E293B;", "--jamun-soft: #2F1754;")
css = css.replace("--kesar: #C59B27;", "--kesar: #FF5E14;")
css = css.replace("--kesar-hot: #B3861B;", "--kesar-hot: #E64A00;")
css = css.replace("--kesar-hover: #D4AF37;", "--kesar-hover: #FF7A29;")
css = css.replace("--pista: #059669;", "--pista: #00E599;")
css = css.replace("--pista-dark: #047857;", "--pista-dark: #00B377;")
css = css.replace("--malai: #FFFFFF;", "--malai: #FFFFFF;")
css = css.replace("--paper: #F8FAFC;", "--paper: #FFFBF5;")
css = css.replace("--paper-card: #FFFFFF;", "--paper-card: #FFFFFF;")
css = css.replace("--ink: #0F172A;", "--ink: #1A0D2E;")
css = css.replace("--ink-80: #334155;", "--ink-80: #331E56;")
css = css.replace("--ink-60: rgba(15, 23, 42, 0.7);", "--ink-60: rgba(26, 13, 46, 0.7);")
css = css.replace("--ink-30: rgba(15, 23, 42, 0.3);", "--ink-30: rgba(26, 13, 46, 0.28);")
css = css.replace("--line: #E2E8F0;", "--line: rgba(26, 13, 46, 0.08);")
css = css.replace("--line-dark: rgba(255, 255, 255, 0.12);", "--line-dark: rgba(255, 255, 255, 0.16);")
css = css.replace("--line-gold: rgba(197, 155, 39, 0.35);", "--line-gold: rgba(255, 94, 20, 0.35);")

# Global replacements in styles.css
css = css.replace("#0F172A", "#1E0F38")
css = css.replace("#0A0F1D", "#140A24")
css = css.replace("#1E293B", "#2F1754")
css = css.replace("#C59B27", "#FF5E14")
css = css.replace("#B3861B", "#E64A00")
css = css.replace("#D4AF37", "#FF7A29")
css = css.replace("#059669", "#00E599")
css = css.replace("rgba(15, 23, 42", "rgba(30, 15, 56")
css = css.replace("rgba(10, 15, 29", "rgba(20, 10, 36")
css = css.replace("rgba(197, 155, 39", "rgba(255, 94, 20")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated styles.css with Sunset Saffron & Electric Tangerine")

# 2. UPDATE index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace :root tokens in index.html
html = html.replace("--jamun:#0F172A;", "--jamun:#1E0F38;")
html = html.replace("--jamun-deep:#0A0F1D;", "--jamun-deep:#140A24;")
html = html.replace("--jamun-soft:#1E293B;", "--jamun-soft:#2F1754;")
html = html.replace("--kesar:#C59B27;", "--kesar:#FF5E14;")
html = html.replace("--kesar-hot:#B3861B;", "--kesar-hot:#E64A00;")
html = html.replace("--kesar-hover:#D4AF37;", "--kesar-hover:#FF7A29;")
html = html.replace("--pista:#059669;", "--pista:#00E599;")
html = html.replace("--pista-dark:#047857;", "--pista-dark:#00B377;")
html = html.replace("--malai:#FFFFFF;", "--malai:#FFFFFF;")
html = html.replace("--paper:#F8FAFC;", "--paper:#FFFBF5;")
html = html.replace("--ink:#0F172A;", "--ink:#1A0D2E;")
html = html.replace("--ink-80:#334155;", "--ink-80:#331E56;")
html = html.replace("--ink-60:rgba(15,23,42,.7);", "--ink-60:rgba(26,13,46,.7);")
html = html.replace("--ink-30:rgba(15,23,42,.3);", "--ink-30:rgba(26,13,46,.28);")
html = html.replace("--line:#E2E8F0;", "--line:rgba(26,13,46,.08);")
html = html.replace("--line-dark:rgba(255,255,255,.12);", "--line-dark:rgba(255,255,255,.16);")

# Global replacements in index.html
html = html.replace("#0F172A", "#1E0F38")
html = html.replace("#0A0F1D", "#140A24")
html = html.replace("#1E293B", "#2F1754")
html = html.replace("#C59B27", "#FF5E14")
html = html.replace("#B3861B", "#E64A00")
html = html.replace("#D4AF37", "#FF7A29")
html = html.replace("#059669", "#00E599")
html = html.replace("rgba(15, 23, 42", "rgba(30, 15, 56")
html = html.replace("rgba(10, 15, 29", "rgba(20, 10, 36")
html = html.replace("rgba(197, 155, 39", "rgba(255, 94, 20")
html = html.replace("rgba(197,155,39", "rgba(255,94,20")

# Update hero background overlay in index.html
html = html.replace(
    "background: radial-gradient(circle at 50% 35%, rgba(15, 23, 42, 0.45) 0%, rgba(10, 15, 29, 0.72) 65%, rgba(10, 15, 29, 0.95) 100%);",
    "background: radial-gradient(circle at 50% 35%, rgba(30, 15, 56, 0.42) 0%, rgba(20, 10, 36, 0.7) 65%, rgba(20, 10, 36, 0.94) 100%);"
)
html = html.replace(".hero{position:relative;background:#0A0F1D;", ".hero{position:relative;background:#140A24;")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html and franq-franchise-website.html")

# 3. UPDATE ALL OTHER HTML FILES
all_html = [
    "about.html", "franchises.html", "find-franchise.html", "book-consultation.html",
    "develop-brand.html", "develop-scale.html", "franchise-marketing.html"
]

for filename in all_html:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("#0F172A", "#1E0F38")
        content = content.replace("#0A0F1D", "#140A24")
        content = content.replace("#1E293B", "#2F1754")
        content = content.replace("#C59B27", "#FF5E14")
        content = content.replace("#B3861B", "#E64A00")
        content = content.replace("#D4AF37", "#FF7A29")
        content = content.replace("#059669", "#00E599")
        content = content.replace("rgba(15, 23, 42", "rgba(30, 15, 56")
        content = content.replace("rgba(10, 15, 29", "rgba(20, 10, 36")
        content = content.replace("rgba(197, 155, 39", "rgba(255, 94, 20")
        content = content.replace("rgba(197,155,39", "rgba(255,94,20")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated palette in {filename}")

# 4. UPDATE generate_brand_pages.py
with open("generate_brand_pages.py", "r", encoding="utf-8") as f:
    gbp = f.read()

gbp = gbp.replace("#0F172A", "#1E0F38")
gbp = gbp.replace("#0A0F1D", "#140A24")
gbp = gbp.replace("#1E293B", "#2F1754")
gbp = gbp.replace("#C59B27", "#FF5E14")
gbp = gbp.replace("#B3861B", "#E64A00")
gbp = gbp.replace("#D4AF37", "#FF7A29")
gbp = gbp.replace("#059669", "#00E599")
gbp = gbp.replace("rgba(15, 23, 42", "rgba(30, 15, 56")
gbp = gbp.replace("rgba(10, 15, 29", "rgba(20, 10, 36")
gbp = gbp.replace("rgba(197, 155, 39", "rgba(255, 94, 20")
gbp = gbp.replace("rgba(197,155,39", "rgba(255,94,20")

with open("generate_brand_pages.py", "w", encoding="utf-8") as f:
    f.write(gbp)

print("Updated generate_brand_pages.py with Sunset Saffron & Electric Tangerine")
