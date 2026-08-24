# -*- coding: utf-8 -*-
import os, re

# 1. UPDATE styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace CSS variables
css = css.replace("--jamun: #0F172A;", "--jamun: #062C22;")
css = css.replace("--jamun: #25103C;", "--jamun: #062C22;")
css = css.replace("--jamun-deep: #080D1A;", "--jamun-deep: #041D16;")
css = css.replace("--jamun-deep: #180825;", "--jamun-deep: #041D16;")
css = css.replace("--jamun-soft: #1E293B;", "--jamun-soft: #0C4234;")
css = css.replace("--jamun-soft: #3B1C5C;", "--jamun-soft: #0C4234;")
css = css.replace("--kesar: #F59E0B;", "--kesar: #EAB308;")
css = css.replace("--kesar: #FFB020;", "--kesar: #EAB308;")
css = css.replace("--kesar-hot: #D97706;", "--kesar-hot: #CA8A04;")
css = css.replace("--kesar-hot: #FFB020;", "--kesar-hot: #CA8A04;")
css = css.replace("--kesar-hover: #FBBF24;", "--kesar-hover: #FACC15;")
css = css.replace("--kesar-hover: #FFBA36;", "--kesar-hover: #FACC15;")
css = css.replace("--pista: #10B981;", "--pista: #10B981;")
css = css.replace("--pista-dark: #047857;", "--pista-dark: #059669;")
css = css.replace("--malai: #F8FAFC;", "--malai: #F8FAFC;")
css = css.replace("--paper: #F8FAFC;", "--paper: #F7FAF8;")
css = css.replace("--ink: #0F172A;", "--ink: #0A1C16;")
css = css.replace("--ink-80: #1E293B;", "--ink-80: #16382D;")
css = css.replace("--ink-60: rgba(15, 23, 42, 0.68);", "--ink-60: rgba(10, 28, 22, 0.68);")
css = css.replace("--ink-30: rgba(15, 23, 42, 0.28);", "--ink-30: rgba(10, 28, 22, 0.28);")
css = css.replace("--line: rgba(15, 23, 42, 0.09);", "--line: rgba(10, 28, 22, 0.09);")
css = css.replace("--line-dark: rgba(248, 250, 252, 0.14);", "--line-dark: rgba(248, 250, 252, 0.14);")
css = css.replace("--line-gold: rgba(245, 158, 11, 0.35);", "--line-gold: rgba(234, 179, 8, 0.35);")

# Global color string replacements in CSS
css = css.replace("#0F172A", "#062C22")
css = css.replace("#080D1A", "#041D16")
css = css.replace("#1E293B", "#0C4234")
css = css.replace("#F59E0B", "#EAB308")
css = css.replace("#D97706", "#CA8A04")
css = css.replace("#FBBF24", "#FACC15")
css = css.replace("rgba(15, 23, 42", "rgba(6, 44, 34")
css = css.replace("rgba(8, 13, 26", "rgba(4, 29, 22")
css = css.replace("rgba(245, 158, 11", "rgba(234, 179, 8")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated styles.css with Forest Emerald & Champagne Gold")

# 2. UPDATE index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace :root tokens in index.html
html = html.replace("--jamun:#0F172A;", "--jamun:#062C22;")
html = html.replace("--jamun-deep:#080D1A;", "--jamun-deep:#041D16;")
html = html.replace("--jamun-soft:#1E293B;", "--jamun-soft:#0C4234;")
html = html.replace("--kesar:#F59E0B;", "--kesar:#EAB308;")
html = html.replace("--kesar-hot:#D97706;", "--kesar-hot:#CA8A04;")
html = html.replace("--kesar-hover:#FBBF24;", "--kesar-hover:#FACC15;")
html = html.replace("--pista:#10B981;", "--pista:#10B981;")
html = html.replace("--pista-dark:#047857;", "--pista-dark:#059669;")
html = html.replace("--malai:#F8FAFC;", "--malai:#F8FAFC;")
html = html.replace("--paper:#F8FAFC;", "--paper:#F7FAF8;")
html = html.replace("--ink:#0F172A;", "--ink:#0A1C16;")
html = html.replace("--ink-80:#1E293B;", "--ink-80:#16382D;")
html = html.replace("--ink-60:rgba(15,23,42,.68);", "--ink-60:rgba(10,28,22,.68);")
html = html.replace("--ink-30:rgba(15,23,42,.28);", "--ink-30:rgba(10,28,22,.28);")
html = html.replace("--line:rgba(15,23,42,.09);", "--line:rgba(10,28,22,.09);")
html = html.replace("--line-dark:rgba(248,250,252,.14);", "--line-dark:rgba(248,250,252,.14);")

# Global color replacements in index.html
html = html.replace("#0F172A", "#062C22")
html = html.replace("#080D1A", "#041D16")
html = html.replace("#1E293B", "#0C4234")
html = html.replace("#F59E0B", "#EAB308")
html = html.replace("#D97706", "#CA8A04")
html = html.replace("#FBBF24", "#FACC15")
html = html.replace("rgba(15, 23, 42", "rgba(6, 44, 34")
html = html.replace("rgba(8, 13, 26", "rgba(4, 29, 22")
html = html.replace("rgba(245, 158, 11", "rgba(234, 179, 8")
html = html.replace("rgba(245,158,11", "rgba(234,179,8")
html = html.replace("rgba(37, 16, 60", "rgba(6, 44, 34")
html = html.replace("rgba(24, 8, 37", "rgba(4, 29, 22")

# Update hero background overlay in index.html
html = html.replace(
    "background: radial-gradient(circle at 50% 35%, rgba(37, 16, 60, 0.38) 0%, rgba(24, 8, 37, 0.65) 65%, rgba(24, 8, 37, 0.9) 100%);",
    "background: radial-gradient(circle at 50% 35%, rgba(6, 44, 34, 0.4) 0%, rgba(4, 29, 22, 0.68) 65%, rgba(4, 29, 22, 0.92) 100%);"
)
html = html.replace(".hero{position:relative;background:#180825;", ".hero{position:relative;background:#041D16;")

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
        content = content.replace("#0F172A", "#062C22")
        content = content.replace("#080D1A", "#041D16")
        content = content.replace("#1E293B", "#0C4234")
        content = content.replace("#F59E0B", "#EAB308")
        content = content.replace("#D97706", "#CA8A04")
        content = content.replace("#FBBF24", "#FACC15")
        content = content.replace("rgba(15, 23, 42", "rgba(6, 44, 34")
        content = content.replace("rgba(8, 13, 26", "rgba(4, 29, 22")
        content = content.replace("rgba(245, 158, 11", "rgba(234, 179, 8")
        content = content.replace("rgba(245,158,11", "rgba(234,179,8")
        content = content.replace("rgba(37, 16, 60", "rgba(6, 44, 34")
        content = content.replace("rgba(24, 8, 37", "rgba(4, 29, 22")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated palette in {filename}")

# 4. UPDATE generate_brand_pages.py
with open("generate_brand_pages.py", "r", encoding="utf-8") as f:
    gbp = f.read()

gbp = gbp.replace("#0F172A", "#062C22")
gbp = gbp.replace("#080D1A", "#041D16")
gbp = gbp.replace("#1E293B", "#0C4234")
gbp = gbp.replace("#F59E0B", "#EAB308")
gbp = gbp.replace("#D97706", "#CA8A04")
gbp = gbp.replace("#FBBF24", "#FACC15")
gbp = gbp.replace("rgba(15, 23, 42", "rgba(6, 44, 34")
gbp = gbp.replace("rgba(8, 13, 26", "rgba(4, 29, 22")
gbp = gbp.replace("rgba(245, 158, 11", "rgba(234, 179, 8")
gbp = gbp.replace("rgba(245,158,11", "rgba(234,179,8")

with open("generate_brand_pages.py", "w", encoding="utf-8") as f:
    f.write(gbp)

print("Updated generate_brand_pages.py with Forest Emerald & Champagne Gold")
