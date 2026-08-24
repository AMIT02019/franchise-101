# -*- coding: utf-8 -*-
import os, re

# Executive Professional Color System:
# Deep Sapphire Slate (#0A0F1D / #0F172A), Prestige Executive Gold (#C59B27 / #D4AF37), Clean White (#FFFFFF), Crisp Slate Paper (#F8FAFC)

# 1. UPDATE styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace CSS variables
css = css.replace("--jamun: #0E1015;", "--jamun: #0F172A;")
css = css.replace("--jamun-deep: #08090C;", "--jamun-deep: #0A0F1D;")
css = css.replace("--jamun-soft: #181B22;", "--jamun-soft: #1E293B;")
css = css.replace("--kesar: #F5A623;", "--kesar: #C59B27;")
css = css.replace("--kesar-hot: #E08A00;", "--kesar-hot: #B3861B;")
css = css.replace("--kesar-hover: #FFC043;", "--kesar-hover: #D4AF37;")
css = css.replace("--pista: #10B981;", "--pista: #059669;")
css = css.replace("--pista-dark: #059669;", "--pista-dark: #047857;")
css = css.replace("--malai: #FFFFFF;", "--malai: #FFFFFF;")
css = css.replace("--paper: #F4F5F7;", "--paper: #F8FAFC;")
css = css.replace("--paper-card: #FFFFFF;", "--paper-card: #FFFFFF;")
css = css.replace("--ink: #0E1015;", "--ink: #0F172A;")
css = css.replace("--ink-80: #1E222B;", "--ink-80: #334155;")
css = css.replace("--ink-60: rgba(14, 16, 21, 0.68);", "--ink-60: rgba(15, 23, 42, 0.7);")
css = css.replace("--ink-30: rgba(14, 16, 21, 0.28);", "--ink-30: rgba(15, 23, 42, 0.3);")
css = css.replace("--line: rgba(14, 16, 21, 0.08);", "--line: #E2E8F0;")
css = css.replace("--line-dark: rgba(255, 255, 255, 0.12);", "--line-dark: rgba(255, 255, 255, 0.12);")
css = css.replace("--line-gold: rgba(245, 166, 35, 0.35);", "--line-gold: rgba(197, 155, 39, 0.35);")

# Global replacements of color hexes in styles.css
css = css.replace("#0E1015", "#0F172A")
css = css.replace("#08090C", "#0A0F1D")
css = css.replace("#181B22", "#1E293B")
css = css.replace("#F5A623", "#C59B27")
css = css.replace("#E08A00", "#B3861B")
css = css.replace("#FFC043", "#D4AF37")
css = css.replace("rgba(14, 16, 21", "rgba(15, 23, 42")
css = css.replace("rgba(8, 9, 12", "rgba(10, 15, 29")
css = css.replace("rgba(245, 166, 35", "rgba(197, 155, 39")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated styles.css with Executive Professional Palette")

# 2. UPDATE index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace :root tokens in index.html
html = html.replace("--jamun:#0E1015;", "--jamun:#0F172A;")
html = html.replace("--jamun-deep:#08090C;", "--jamun-deep:#0A0F1D;")
html = html.replace("--jamun-soft:#181B22;", "--jamun-soft:#1E293B;")
html = html.replace("--kesar:#F5A623;", "--kesar:#C59B27;")
html = html.replace("--kesar-hot:#E08A00;", "--kesar-hot:#B3861B;")
html = html.replace("--kesar-hover:#FFC043;", "--kesar-hover:#D4AF37;")
html = html.replace("--pista:#10B981;", "--pista:#059669;")
html = html.replace("--pista-dark:#059669;", "--pista-dark:#047857;")
html = html.replace("--malai:#FFFFFF;", "--malai:#FFFFFF;")
html = html.replace("--paper:#F4F5F7;", "--paper:#F8FAFC;")
html = html.replace("--ink:#0E1015;", "--ink:#0F172A;")
html = html.replace("--ink-80:#1E222B;", "--ink-80:#334155;")
html = html.replace("--ink-60:rgba(14,16,21,.68);", "--ink-60:rgba(15,23,42,.7);")
html = html.replace("--ink-30:rgba(14,16,21,.28);", "--ink-30:rgba(15,23,42,.3);")
html = html.replace("--line:rgba(14,16,21,.08);", "--line:#E2E8F0;")
html = html.replace("--line-dark:rgba(255,255,255,.12);", "--line-dark:rgba(255,255,255,.12);")

# Global replacements in index.html
html = html.replace("#0E1015", "#0F172A")
html = html.replace("#08090C", "#0A0F1D")
html = html.replace("#181B22", "#1E293B")
html = html.replace("#F5A623", "#C59B27")
html = html.replace("#E08A00", "#B3861B")
html = html.replace("#FFC043", "#D4AF37")
html = html.replace("rgba(14, 16, 21", "rgba(15, 23, 42")
html = html.replace("rgba(8, 9, 12", "rgba(10, 15, 29")
html = html.replace("rgba(245, 166, 35", "rgba(197, 155, 39")
html = html.replace("rgba(245,166,35", "rgba(197,155,39")

# Update hero background overlay in index.html
html = html.replace(
    "background: radial-gradient(circle at 50% 35%, rgba(14, 16, 21, 0.42) 0%, rgba(8, 9, 12, 0.7) 65%, rgba(8, 9, 12, 0.94) 100%);",
    "background: radial-gradient(circle at 50% 35%, rgba(15, 23, 42, 0.45) 0%, rgba(10, 15, 29, 0.72) 65%, rgba(10, 15, 29, 0.95) 100%);"
)
html = html.replace(".hero{position:relative;background:#08090C;", ".hero{position:relative;background:#0A0F1D;")

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
        content = content.replace("#0E1015", "#0F172A")
        content = content.replace("#08090C", "#0A0F1D")
        content = content.replace("#181B22", "#1E293B")
        content = content.replace("#F5A623", "#C59B27")
        content = content.replace("#E08A00", "#B3861B")
        content = content.replace("#FFC043", "#D4AF37")
        content = content.replace("rgba(14, 16, 21", "rgba(15, 23, 42")
        content = content.replace("rgba(8, 9, 12", "rgba(10, 15, 29")
        content = content.replace("rgba(245, 166, 35", "rgba(197, 155, 39")
        content = content.replace("rgba(245,166,35", "rgba(197,155,39")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated palette in {filename}")

# 4. UPDATE generate_brand_pages.py
with open("generate_brand_pages.py", "r", encoding="utf-8") as f:
    gbp = f.read()

gbp = gbp.replace("#0E1015", "#0F172A")
gbp = gbp.replace("#08090C", "#0A0F1D")
gbp = gbp.replace("#181B22", "#1E293B")
gbp = gbp.replace("#F5A623", "#C59B27")
gbp = gbp.replace("#E08A00", "#B3861B")
gbp = gbp.replace("#FFC043", "#D4AF37")
gbp = gbp.replace("rgba(14, 16, 21", "rgba(15, 23, 42")
gbp = gbp.replace("rgba(8, 9, 12", "rgba(10, 15, 29")
gbp = gbp.replace("rgba(245, 166, 35", "rgba(197, 155, 39")
gbp = gbp.replace("rgba(245,166,35", "rgba(197,155,39")

with open("generate_brand_pages.py", "w", encoding="utf-8") as f:
    f.write(gbp)

print("Updated generate_brand_pages.py with Executive Professional Palette")
