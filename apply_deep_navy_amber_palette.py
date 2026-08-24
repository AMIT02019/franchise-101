# -*- coding: utf-8 -*-
import os, re

# 1. UPDATE styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace CSS variables
css = css.replace("--jamun: #25103C;", "--jamun: #0F172A;")
css = css.replace("--jamun-deep: #180825;", "--jamun-deep: #080D1A;")
css = css.replace("--jamun-soft: #3B1C5C;", "--jamun-soft: #1E293B;")
css = css.replace("--kesar: #FFB020;", "--kesar: #F59E0B;")
css = css.replace("--kesar-hot: #FFB020;", "--kesar-hot: #D97706;")
css = css.replace("--kesar-hover: #FFBA36;", "--kesar-hover: #FBBF24;")
css = css.replace("--pista: #A9E86B;", "--pista: #10B981;")
css = css.replace("--pista-dark: #327515;", "--pista-dark: #047857;")
css = css.replace("--malai: #FFF3DE;", "--malai: #F8FAFC;")
css = css.replace("--malai-cream: #FAF0DC;", "--malai-cream: #F1F5F9;")
css = css.replace("--paper: #FAF8F3;", "--paper: #F8FAFC;")
css = css.replace("--paper: #FAF7F2;", "--paper: #F8FAFC;")
css = css.replace("--ink: #1A1420;", "--ink: #0F172A;")
css = css.replace("--ink-80: #382F42;", "--ink-80: #1E293B;")
css = css.replace("--ink-60: rgba(26, 20, 32, 0.64);", "--ink-60: rgba(15, 23, 42, 0.68);")
css = css.replace("--ink-30: rgba(26, 20, 32, 0.28);", "--ink-30: rgba(15, 23, 42, 0.28);")
css = css.replace("--line: rgba(26, 20, 32, 0.1);", "--line: rgba(15, 23, 42, 0.09);")
css = css.replace("--line-dark: rgba(255, 243, 222, 0.16);", "--line-dark: rgba(248, 250, 252, 0.14);")
css = css.replace("--line-gold: rgba(255, 176, 32, 0.35);", "--line-gold: rgba(245, 158, 11, 0.35);")

# Global replacements of hardcoded colors in CSS
css = css.replace("#25103C", "#0F172A")
css = css.replace("#180825", "#080D1A")
css = css.replace("#381958", "#1E293B")
css = css.replace("#3B1C5C", "#1E293B")
css = css.replace("#FFB020", "#F59E0B")
css = css.replace("#A9E86B", "#10B981")
css = css.replace("#FFF3DE", "#F8FAFC")
css = css.replace("rgba(37, 16, 60", "rgba(15, 23, 42")
css = css.replace("rgba(24, 8, 37", "rgba(8, 13, 26")
css = css.replace("rgba(255, 176, 32", "rgba(245, 158, 11")
css = css.replace("rgba(169, 232, 107", "rgba(16, 185, 129")
css = css.replace("rgba(255, 243, 222", "rgba(248, 250, 252")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated styles.css with Deep Navy & Warm Amber Gold")

# 2. UPDATE index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace :root tokens in index.html
html = html.replace("--jamun:#25103C;", "--jamun:#0F172A;")
html = html.replace("--jamun-deep:#180825;", "--jamun-deep:#080D1A;")
html = html.replace("--jamun-soft:#3B1C5C;", "--jamun-soft:#1E293B;")
html = html.replace("--kesar:#FFB020;", "--kesar:#F59E0B;")
html = html.replace("--kesar-hot:#FFB020;", "--kesar-hot:#D97706;")
html = html.replace("--kesar-hover:#FFBA36;", "--kesar-hover:#FBBF24;")
html = html.replace("--pista:#A9E86B;", "--pista:#10B981;")
html = html.replace("--pista-dark:#327515;", "--pista-dark:#047857;")
html = html.replace("--malai:#FFF3DE;", "--malai:#F8FAFC;")
html = html.replace("--paper:#FAF8F3;", "--paper:#F8FAFC;")
html = html.replace("--ink:#1A1420;", "--ink:#0F172A;")
html = html.replace("--ink-80:#382F42;", "--ink-80:#1E293B;")
html = html.replace("--ink-60:rgba(26,20,32,.64);", "--ink-60:rgba(15,23,42,.68);")
html = html.replace("--ink-30:rgba(26,20,32,.28);", "--ink-30:rgba(15,23,42,.28);")
html = html.replace("--line:rgba(26,20,32,.1);", "--line:rgba(15,23,42,.09);")
html = html.replace("--line-dark:rgba(255,243,222,.16);", "--line-dark:rgba(248,250,252,.14);")

# Global color string replacements in index.html
html = html.replace("#25103C", "#0F172A")
html = html.replace("#180825", "#080D1A")
html = html.replace("#381958", "#1E293B")
html = html.replace("#3B1C5C", "#1E293B")
html = html.replace("#FFB020", "#F59E0B")
html = html.replace("#A9E86B", "#10B981")
html = html.replace("#FFF3DE", "#F8FAFC")
html = html.replace("rgba(37, 16, 60", "rgba(15, 23, 42")
html = html.replace("rgba(24, 8, 37", "rgba(8, 13, 26")
html = html.replace("rgba(255, 176, 32", "rgba(245, 158, 11")
html = html.replace("rgba(255,176,32", "rgba(245,158,11")
html = html.replace("rgba(169, 232, 107", "rgba(16, 185, 129")
html = html.replace("rgba(169,232,107", "rgba(16,185,129")
html = html.replace("rgba(255, 243, 222", "rgba(248, 250, 252")
html = html.replace("rgba(255,243,222", "rgba(248,250,252")

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
        content = content.replace("#25103C", "#0F172A")
        content = content.replace("#180825", "#080D1A")
        content = content.replace("#381958", "#1E293B")
        content = content.replace("#3B1C5C", "#1E293B")
        content = content.replace("#FFB020", "#F59E0B")
        content = content.replace("#A9E86B", "#10B981")
        content = content.replace("#FFF3DE", "#F8FAFC")
        content = content.replace("rgba(37, 16, 60", "rgba(15, 23, 42")
        content = content.replace("rgba(24, 8, 37", "rgba(8, 13, 26")
        content = content.replace("rgba(255, 176, 32", "rgba(245, 158, 11")
        content = content.replace("rgba(255,176,32", "rgba(245,158,11")
        content = content.replace("rgba(169, 232, 107", "rgba(16, 185, 129")
        content = content.replace("rgba(169,232,107", "rgba(16,185,129")
        content = content.replace("rgba(255, 243, 222", "rgba(248, 250, 252")
        content = content.replace("rgba(255,243,222", "rgba(248,250,252")
        content = content.replace("#1e0e30", "#080D1A")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated palette in {filename}")

# 4. UPDATE generate_brand_pages.py
with open("generate_brand_pages.py", "r", encoding="utf-8") as f:
    gbp = f.read()

gbp = gbp.replace("#25103C", "#0F172A")
gbp = gbp.replace("#180825", "#080D1A")
gbp = gbp.replace("#381958", "#1E293B")
gbp = gbp.replace("#FFB020", "#F59E0B")
gbp = gbp.replace("#A9E86B", "#10B981")
gbp = gbp.replace("#FFF3DE", "#F8FAFC")
gbp = gbp.replace("rgba(255, 243, 222", "rgba(248, 250, 252")
gbp = gbp.replace("rgba(255,243,222", "rgba(248,250,252")
gbp = gbp.replace("rgba(255, 176, 32", "rgba(245, 158, 11")
gbp = gbp.replace("rgba(255,176,32", "rgba(245,158,11")

with open("generate_brand_pages.py", "w", encoding="utf-8") as f:
    f.write(gbp)

print("Updated generate_brand_pages.py with Deep Navy & Warm Amber Gold")
