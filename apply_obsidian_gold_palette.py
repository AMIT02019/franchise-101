# -*- coding: utf-8 -*-
import os, re

# 1. UPDATE styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace CSS variables
css = css.replace("--jamun: #062C22;", "--jamun: #0E1015;")
css = css.replace("--jamun-deep: #041D16;", "--jamun-deep: #08090C;")
css = css.replace("--jamun-soft: #0C4234;", "--jamun-soft: #181B22;")
css = css.replace("--kesar: #EAB308;", "--kesar: #F5A623;")
css = css.replace("--kesar-hot: #CA8A04;", "--kesar-hot: #E08A00;")
css = css.replace("--kesar-hover: #FACC15;", "--kesar-hover: #FFC043;")
css = css.replace("--pista: #10B981;", "--pista: #10B981;")
css = css.replace("--pista-dark: #059669;", "--pista-dark: #059669;")
css = css.replace("--malai: #F8FAFC;", "--malai: #FFFFFF;")
css = css.replace("--paper: #F7FAF8;", "--paper: #F4F5F7;")
css = css.replace("--paper-card: #FFFFFF;", "--paper-card: #FFFFFF;")
css = css.replace("--ink: #0A1C16;", "--ink: #0E1015;")
css = css.replace("--ink-80: #16382D;", "--ink-80: #1E222B;")
css = css.replace("--ink-60: rgba(10, 28, 22, 0.68);", "--ink-60: rgba(14, 16, 21, 0.68);")
css = css.replace("--ink-30: rgba(10, 28, 22, 0.28);", "--ink-30: rgba(14, 16, 21, 0.28);")
css = css.replace("--line: rgba(10, 28, 22, 0.09);", "--line: rgba(14, 16, 21, 0.08);")
css = css.replace("--line-dark: rgba(248, 250, 252, 0.14);", "--line-dark: rgba(255, 255, 255, 0.12);")
css = css.replace("--line-gold: rgba(234, 179, 8, 0.35);", "--line-gold: rgba(245, 166, 35, 0.35);")

# Global color replacements in CSS
css = css.replace("#062C22", "#0E1015")
css = css.replace("#041D16", "#08090C")
css = css.replace("#0C4234", "#181B22")
css = css.replace("#EAB308", "#F5A623")
css = css.replace("#CA8A04", "#E08A00")
css = css.replace("#FACC15", "#FFC043")
css = css.replace("rgba(6, 44, 34", "rgba(14, 16, 21")
css = css.replace("rgba(4, 29, 22", "rgba(8, 9, 12")
css = css.replace("rgba(234, 179, 8", "rgba(245, 166, 35")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated styles.css with Obsidian Black & Electric Amber Gold")

# 2. UPDATE index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace :root tokens in index.html
html = html.replace("--jamun:#062C22;", "--jamun:#0E1015;")
html = html.replace("--jamun-deep:#041D16;", "--jamun-deep:#08090C;")
html = html.replace("--jamun-soft:#0C4234;", "--jamun-soft:#181B22;")
html = html.replace("--kesar:#EAB308;", "--kesar:#F5A623;")
html = html.replace("--kesar-hot:#CA8A04;", "--kesar-hot:#E08A00;")
html = html.replace("--kesar-hover:#FACC15;", "--kesar-hover:#FFC043;")
html = html.replace("--pista:#10B981;", "--pista:#10B981;")
html = html.replace("--pista-dark:#059669;", "--pista-dark:#059669;")
html = html.replace("--malai:#F8FAFC;", "--malai:#FFFFFF;")
html = html.replace("--paper:#F7FAF8;", "--paper:#F4F5F7;")
html = html.replace("--ink:#0A1C16;", "--ink:#0E1015;")
html = html.replace("--ink-80:#16382D;", "--ink-80:#1E222B;")
html = html.replace("--ink-60:rgba(10,28,22,.68);", "--ink-60:rgba(14,16,21,.68);")
html = html.replace("--ink-30:rgba(10,28,22,.28);", "--ink-30:rgba(14,16,21,.28);")
html = html.replace("--line:rgba(10,28,22,.09);", "--line:rgba(14,16,21,.08);")
html = html.replace("--line-dark:rgba(248,250,252,.14);", "--line-dark:rgba(255,255,255,.12);")

# Global color replacements in index.html
html = html.replace("#062C22", "#0E1015")
html = html.replace("#041D16", "#08090C")
html = html.replace("#0C4234", "#181B22")
html = html.replace("#EAB308", "#F5A623")
html = html.replace("#CA8A04", "#E08A00")
html = html.replace("#FACC15", "#FFC043")
html = html.replace("rgba(6, 44, 34", "rgba(14, 16, 21")
html = html.replace("rgba(4, 29, 22", "rgba(8, 9, 12")
html = html.replace("rgba(234, 179, 8", "rgba(245, 166, 35")
html = html.replace("rgba(234,179,8", "rgba(245,166,35")

# Update hero background overlay in index.html
html = html.replace(
    "background: radial-gradient(circle at 50% 35%, rgba(6, 44, 34, 0.4) 0%, rgba(4, 29, 22, 0.68) 65%, rgba(4, 29, 22, 0.92) 100%);",
    "background: radial-gradient(circle at 50% 35%, rgba(14, 16, 21, 0.42) 0%, rgba(8, 9, 12, 0.7) 65%, rgba(8, 9, 12, 0.94) 100%);"
)
html = html.replace(".hero{position:relative;background:#041D16;", ".hero{position:relative;background:#08090C;")

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
        content = content.replace("#062C22", "#0E1015")
        content = content.replace("#041D16", "#08090C")
        content = content.replace("#0C4234", "#181B22")
        content = content.replace("#EAB308", "#F5A623")
        content = content.replace("#CA8A04", "#E08A00")
        content = content.replace("#FACC15", "#FFC043")
        content = content.replace("rgba(6, 44, 34", "rgba(14, 16, 21")
        content = content.replace("rgba(4, 29, 22", "rgba(8, 9, 12")
        content = content.replace("rgba(234, 179, 8", "rgba(245, 166, 35")
        content = content.replace("rgba(234,179,8", "rgba(245,166,35")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated palette in {filename}")

# 4. UPDATE generate_brand_pages.py
with open("generate_brand_pages.py", "r", encoding="utf-8") as f:
    gbp = f.read()

gbp = gbp.replace("#062C22", "#0E1015")
gbp = gbp.replace("#041D16", "#08090C")
gbp = gbp.replace("#0C4234", "#181B22")
gbp = gbp.replace("#EAB308", "#F5A623")
gbp = gbp.replace("#CA8A04", "#E08A00")
gbp = gbp.replace("#FACC15", "#FFC043")
gbp = gbp.replace("rgba(6, 44, 34", "rgba(14, 16, 21")
gbp = gbp.replace("rgba(4, 29, 22", "rgba(8, 9, 12")
gbp = gbp.replace("rgba(234, 179, 8", "rgba(245, 166, 35")
gbp = gbp.replace("rgba(234,179,8", "rgba(245,166,35")

with open("generate_brand_pages.py", "w", encoding="utf-8") as f:
    f.write(gbp)

print("Updated generate_brand_pages.py with Obsidian Black & Electric Amber Gold")
