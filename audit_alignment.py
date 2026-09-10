# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

pages = ['index.html', 'franchises.html', 'develop-brand.html', 'develop-scale.html', 'franchise-marketing.html', 'about.html', 'contact.html', 'find-franchise.html']

for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    print(f"\n==================== {page} ====================")
    sections = soup.find_all(['section', 'header', 'footer'])
    for i, sec in enumerate(sections):
        tag = sec.name
        sec_id = sec.get('id', '')
        classes = " ".join(sec.get('class', []))
        direct_divs = sec.find_all('div', recursive=False)
        div_classes = [d.get('class', []) for d in direct_divs]
        has_wrap = any('wrap' in c for c in div_classes)
        print(f"[{i}] <{tag} id='{sec_id}' class='{classes}'>")
        print(f"    Has direct .wrap: {has_wrap} (Classes of direct child divs: {div_classes})")
