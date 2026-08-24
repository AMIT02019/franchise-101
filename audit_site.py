# -*- coding: utf-8 -*-
import os, re

files = [
    'index.html',
    'about.html',
    'franchises.html',
    'beyond-temptation.html',
    'dunk-burgers.html',
    'mr-sandwich.html',
    'south-twist.html',
    'cafe-choco-craze.html',
    'develop-brand.html',
    'develop-scale.html',
    'franchise-marketing.html',
    'find-franchise.html',
    'book-consultation.html'
]

print("=== COMPLETE 13-PAGE AUDIT & ANALYSIS REPORT ===\n")

for f in files:
    if not os.path.exists(f):
        print(f"[MISSING] {f}")
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1) if title_match else 'NO TITLE'
    
    desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
    desc = desc_match.group(1) if desc_match else 'NO DESCRIPTION'
    
    brands = ['Beyond Temptation', 'Dunk Burgers', 'Mr. Sandwich', 'South Twist', 'Cafe Choco Craze']
    brand_counts = {b: content.count(b) for b in brands}
    
    legacy = ['Chai Katta', 'Kulfi Club', 'Momo Mafia', 'Biryani Bay', 'Waffle Theory', 'Tandoor Tribe']
    legacy_found = [l for l in legacy if l in content]
    
    nav_links = re.findall(r'href=["\']([^#"\']+\.html)["\']', content)
    missing_links = [l for l in set(nav_links) if not os.path.exists(l)]
    
    has_drawer = 'id="mobileDrawer"' in content
    has_nav = 'id="nav"' in content
    has_footer = '<footer' in content
    has_io = 'IntersectionObserver' in content
    
    print(f"PAGE: [{f}]")
    print(f"  - Title: {title}")
    print(f"  - Size: {len(content):,} chars")
    print(f"  - Nav / Drawer / Footer / Scroll Reveal: {'[OK] 100% Complete' if (has_drawer and has_nav and has_footer and has_io) else '[ERR] Check components'}")
    print(f"  - Internal Links: {missing_links if missing_links else '[OK] 100% Valid (No 404s)'}")
    print("-" * 60)
