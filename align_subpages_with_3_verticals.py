# -*- coding: utf-8 -*-
import os, re

# 1. Update develop-brand.html (Vertical 02: Business & Restaurant Development - Concept to Key-in-Hand)
with open("develop-brand.html", "r", encoding="utf-8") as f:
    dev_brand = f.read()

dev_brand = dev_brand.replace(
    '<p class="eyebrow on-dark">Food Concept Incubator</p>',
    '<p class="eyebrow on-dark"><span class="pulse"></span> Vertical 02 &middot; Concept &middot; Build &middot; Launch</p>'
)
dev_brand = dev_brand.replace(
    '<h1 class="rise">Turn your recipe into a franchise-ready brand.</h1>',
    '<h1 class="rise">Business &amp; Restaurant Development &mdash; Concept to Key-in-Hand.</h1>'
)
dev_brand = dev_brand.replace(
    '<p class="page-hero-sub rise">We take single-outlet restaurant founders and cloud kitchen operators and build turnkey franchise systems: recipe standardization, supplier agreements, kitchen CAD layouts, and legal documentation in 6 weeks.</p>',
    '<p class="page-hero-sub rise">Helping entrepreneurs transform an idea into a fully developed, branded and operational business through an integrated range of services spanning concept development, branding, design, setup, operations, marketing and launch. Clients can engage us for individual services, a combination of services, or a complete end-to-end solution.</p>'
)

with open("develop-brand.html", "w", encoding="utf-8") as f:
    f.write(dev_brand)
print("Aligned develop-brand.html with Vertical 02")

# 2. Update develop-scale.html (Vertical 03: Brand Growth & Franchise Expansion)
with open("develop-scale.html", "r", encoding="utf-8") as f:
    dev_scale = f.read()

dev_scale = dev_scale.replace(
    '<p class="eyebrow on-dark">Expansion Acceleration Desk</p>',
    '<p class="eyebrow on-dark"><span class="pulse"></span> Vertical 03 &middot; Strengthen &middot; Market &middot; Scale</p>'
)
dev_scale = dev_scale.replace(
    '<h1 class="rise">Scale your food brand from 5 to 50 outlets nationwide.</h1>',
    '<h1 class="rise">Brand Growth &amp; Franchise Expansion Network.</h1>'
)
dev_scale = dev_scale.replace(
    '<p class="page-hero-sub rise">We help verified regional food brands expand across Tier 1, 2, and 3 cities with qualified multi-unit investor placement, master franchise agreements, and centralized supply chain auditing.</p>',
    '<p class="page-hero-sub rise">Helping existing businesses and brands strengthen their brand, enhance their business, develop their franchise proposition, generate investor demand and expand through franchising, with solutions tailored to their individual requirements.</p>'
)

with open("develop-scale.html", "w", encoding="utf-8") as f:
    f.write(dev_scale)
print("Aligned develop-scale.html with Vertical 03")

# 3. Update franchise-marketing.html (Vertical 03: Brand Growth & Franchise Expansion)
with open("franchise-marketing.html", "r", encoding="utf-8") as f:
    f_mkt = f.read()

f_mkt = f_mkt.replace(
    '<p class="eyebrow on-dark">Investor Demand Generation</p>',
    '<p class="eyebrow on-dark"><span class="pulse"></span> Vertical 03 &middot; Strengthen &middot; Market &middot; Scale</p>'
)

with open("franchise-marketing.html", "w", encoding="utf-8") as f:
    f.write(f_mkt)
print("Aligned franchise-marketing.html with Vertical 03")

# 4. Update find-franchise.html & franchises.html (Vertical 01: Investor & Franchise Consulting)
with open("find-franchise.html", "r", encoding="utf-8") as f:
    find_f = f.read()

find_f = find_f.replace(
    '<p class="eyebrow on-dark">Intelligent Franchise Matcher</p>',
    '<p class="eyebrow on-dark"><span class="pulse"></span> Vertical 01 &middot; Find &middot; Evaluate &middot; Invest</p>'
)
find_f = find_f.replace(
    '<p class="page-hero-sub rise">Answer 5 quick questions about your capital availability, preferred food format, and target location. Our algorithm matches you with vetted brands that fit your exact profile.</p>',
    '<p class="page-hero-sub rise">Investor &amp; Franchise Consulting: Helping investors and aspiring entrepreneurs discover, evaluate and select franchise and business opportunities suited to their investment capacity, goals, location, interests and level of involvement.</p>'
)

with open("find-franchise.html", "w", encoding="utf-8") as f:
    f.write(find_f)
print("Aligned find-franchise.html with Vertical 01")
