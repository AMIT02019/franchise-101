# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def inspect_page(page_name):
    with open(page_name, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    print(f"\n==================== {page_name} ====================")
    for i, s in enumerate(soup.find_all(["section", "header"])):
        sid = s.get("id", "no-id")
        scls = s.get("class", [])
        style = s.get("style", "")
        wrap = s.find("div", class_="wrap")
        h = s.find(["h1", "h2", "h3"])
        htxt = h.get_text(strip=True)[:45] if h else "None"
        htxt = htxt.encode('ascii', 'ignore').decode('ascii')
        
        # Check direct child of section
        children = [c for c in s.children if c.name]
        c_names = [f"<{c.name} class='{' '.join(c.get('class', []))}'>" for c in children]
        
        print(f"[{i}] id='{sid}' class='{' '.join(scls)}'")
        print(f"    Heading: {htxt}")
        print(f"    Children: {c_names}")
        if style:
            print(f"    Style: {style}")

for p in ["index.html", "franchises.html", "develop-brand.html", "develop-scale.html", "about.html", "contact.html", "find-franchise.html"]:
    inspect_page(p)
