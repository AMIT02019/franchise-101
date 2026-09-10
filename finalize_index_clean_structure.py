# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# Remove unwanted sections from soup:
# 1. Remove #kitchen-craft
kc = soup.find(id="kitchen-craft")
if kc:
    kc.decompose()

# 2. Remove any section with eyebrow 'Franchisees' or 'Since 2019'
for sec in soup.find_all("section"):
    eyebrow = sec.find(class_=re.compile(r"eyebrow", re.I))
    if eyebrow:
        txt = eyebrow.get_text(strip=True).lower()
        if "franchisees" in txt or "since 2019" in txt or "before you apply" in txt:
            sec.decompose()

# 3. Remove #city-sec, #quiz, #budget, #brand-services, #about, #apply if any exist
for unwanted_id in ["city-sec", "quiz", "budget", "brand-services", "about", "apply", "how"]:
    el = soup.find(id=unwanted_id)
    if el:
        el.decompose()

# Write back to index.html and franq-franchise-website.html
cleaned_html = str(soup)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(cleaned_html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(cleaned_html)

print("BeautifulSoup clean completed!")
