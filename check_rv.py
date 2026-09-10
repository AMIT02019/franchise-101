# -*- coding: utf-8 -*-
import os, re

files = [
    'index.html',
    'about.html',
    'franchises.html',
    'develop-brand.html',
    'develop-scale.html',
    'franchise-marketing.html',
    'find-franchise.html',
    'book-consultation.html'
]

print("=== CHECKING SCROLL REVEAL (.rv) ACROSS ALL PAGES ===\n")

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    rv_count = c.count('class="') + c.count("class='")
    has_rv_elements = 'class="' in c and ' rv' in c
    has_io = 'IntersectionObserver' in c
    
    print(f"FILE: {f}")
    print(f"  - Has .rv elements: {has_rv_elements}")
    print(f"  - Has IntersectionObserver: {has_io}")
    if has_rv_elements and not has_io:
        print(f"  ⚠️ CRITICAL BUG: Elements will be hidden with opacity 0!")
    print("-" * 50)
