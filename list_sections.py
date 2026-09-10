# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

print("=== ALL SECTIONS IN INDEX.HTML ===\n")
sections = soup.find_all(["section", "header"])
for i, s in enumerate(sections):
    sec_id = s.get("id", "NO_ID")
    sec_cls = " ".join(s.get("class", []))
    h2 = s.find(["h1", "h2", "h3"])
    h2_text = h2.get_text(strip=True) if h2 else "NO HEADING"
    h2_text = h2_text.encode('ascii', 'ignore').decode('ascii')
    eyebrow = s.find(class_=re.compile(r"eyebrow", re.I))
    eyebrow_text = eyebrow.get_text(strip=True) if eyebrow else ""
    eyebrow_text = eyebrow_text.encode('ascii', 'ignore').decode('ascii')
    print(f"{i+1}. [#{sec_id}] (class: {sec_cls})")
    print(f"   Eyebrow: {eyebrow_text}")
    print(f"   Heading: {h2_text}")
    print("-" * 50)
