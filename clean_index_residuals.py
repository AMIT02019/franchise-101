# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace residual default quiz match title & default brand
html = html.replace('<h3 style="font-size:clamp(24px,3vw,34px);color:var(--malai);margin-bottom:6px" id="quizMatchTitle">Chai Katta</h3>', '<h3 style="font-size:clamp(24px,3vw,34px);color:var(--malai);margin-bottom:6px" id="quizMatchTitle">Mr. Sandwich</h3>')
html = html.replace('<h3 style="font-size:32px;color:var(--malai);margin-top:6px" id="modalTitle">Chai Katta</h3>', '<h3 style="font-size:32px;color:var(--malai);margin-top:6px" id="modalTitle">Beyond Temptation</h3>')
html = html.replace("let matchedBrand = 'Chai Katta';", "let matchedBrand = 'Mr. Sandwich';")
html = html.replace("const brand = window.matchedQuizBrand || 'Chai Katta';", "const brand = window.matchedQuizBrand || 'Mr. Sandwich';")

# Replace voice testimonials
html = html.replace('Chai Katta &middot; Kothrud, Pune', 'Beyond Temptation &middot; Baner, Pune')
html = html.replace('Momo Mafia &middot; Indiranagar, Bengaluru', 'Mr. Sandwich &middot; Indiranagar, Bengaluru')
html = html.replace('Biryani Bay &middot; Andheri West, Mumbai', 'South Twist &middot; Kothrud, Pune')

# Replace territory slots in CITY_DATA
city_data_old = """const CITY_DATA = {
  mumbai: {
    name: 'Mumbai (MMR)',
    units: 142,
    density: 'High Footfall Transit & Corporate Parks',
    brands: ['Chai Katta (4 slots)', 'Kulfi Club (3 slots)', 'Momo Mafia (5 slots)', 'Biryani Bay (6 slots)']
  },
  pune: {
    name: 'Pune & PCMC',
    units: 98,
    density: 'Student Campuses & Tech Corridors',
    brands: ['Chai Katta (3 slots)', 'Waffle Theory (3 slots)', 'Frost & Co. (4 slots)', 'Bun Maska Co. (4 slots)']
  },
  delhi: {
    name: 'Delhi NCR (Gurugram/Noida)',
    units: 184,
    density: 'High AOV Markets & Metro Stations',
    brands: ['Momo Mafia (7 slots)', 'Tandoor Tribe (6 slots)', 'Frost & Co. (5 slots)', 'Chai Katta (8 slots)']
  },
  bengaluru: {
    name: 'Bengaluru',
    units: 126,
    density: 'Tech Hubs & Residential High Streets',
    brands: ['Biryani Bay (6 slots)', 'Kulfi Club (4 slots)', 'Chai Katta (3 slots)', 'Dosa Dastarkhan (3 slots)']
  },
  hyderabad: {
    name: 'Hyderabad',
    units: 82,
    density: 'Gachibowli Tech Corridor & Jubilee Hills',
    brands: ['Biryani Bay (5 slots)', 'Frost & Co. (3 slots)', 'Tandoor Tribe (2 slots)']
  },
  ahmedabad: {
    name: 'Ahmedabad',
    units: 64,
    density: 'Commercial Corridors & SG Highway',
    brands: ['Chai Katta (3 slots)', 'Momo Mafia (3 slots)', 'Dosa Dastarkhan (4 slots)']
  },
  indore: {
    name: 'Indore',
    units: 48,
    density: 'Food Streets & 56 Dukan Catchment',
    brands: ['Kulfi Club (4 slots)', 'Biryani Bay (3 slots)', 'Waffle Theory (2 slots)']
  },
  lucknow: {
    name: 'Lucknow',
    units: 52,
    density: 'Hazratganj & Gomti Nagar Commercials',
    brands: ['Chai Katta (3 slots)', 'Kulfi Club (3 slots)', 'Frost & Co. (3 slots)']
  }
};"""

city_data_new = """const CITY_DATA = {
  mumbai: {
    name: 'Mumbai (MMR)',
    units: 142,
    density: 'High Footfall Transit & Corporate Parks',
    brands: ['Beyond Temptation (3 slots)', 'Dunk Burgers (4 slots)', 'Mr. Sandwich (5 slots)', 'South Twist (4 slots)']
  },
  pune: {
    name: 'Pune & PCMC',
    units: 98,
    density: 'Student Campuses & Tech Corridors',
    brands: ['Beyond Temptation (5 slots)', 'South Twist (4 slots)', 'Cafe Choco Craze (4 slots)', 'Dunk Burgers (3 slots)']
  },
  delhi: {
    name: 'Delhi NCR (Gurugram/Noida)',
    units: 184,
    density: 'High AOV Markets & Metro Stations',
    brands: ['Mr. Sandwich (8 slots)', 'Beyond Temptation (4 slots)', 'Dunk Burgers (5 slots)', 'Cafe Choco Craze (3 slots)']
  },
  bengaluru: {
    name: 'Bengaluru',
    units: 126,
    density: 'Tech Hubs & Residential High Streets',
    brands: ['South Twist (6 slots)', 'Mr. Sandwich (5 slots)', 'Beyond Temptation (3 slots)', 'Dunk Burgers (4 slots)']
  },
  hyderabad: {
    name: 'Hyderabad',
    units: 82,
    density: 'Gachibowli Tech Corridor & Jubilee Hills',
    brands: ['South Twist (4 slots)', 'Beyond Temptation (3 slots)', 'Mr. Sandwich (4 slots)', 'Dunk Burgers (3 slots)']
  },
  ahmedabad: {
    name: 'Ahmedabad',
    units: 64,
    density: 'Commercial Corridors & SG Highway',
    brands: ['Beyond Temptation (4 slots)', 'Mr. Sandwich (5 slots)', 'Cafe Choco Craze (3 slots)']
  },
  indore: {
    name: 'Indore',
    units: 48,
    density: 'Food Streets & Commercial Belts',
    brands: ['Mr. Sandwich (4 slots)', 'Beyond Temptation (3 slots)', 'South Twist (3 slots)']
  },
  lucknow: {
    name: 'Lucknow',
    units: 52,
    density: 'Hazratganj & Gomti Nagar Commercials',
    brands: ['Mr. Sandwich (6 slots)', 'Beyond Temptation (3 slots)', 'Dunk Burgers (3 slots)', 'South Twist (2 slots)']
  }
};"""

html = html.replace(city_data_old, city_data_new)

# Update quiz recommendation logic on homepage
html = html.replace("cat: 'Beverages', capex: '₹6–11L', payback: '11–14 mo', desc: 'Chai Katta kiosk model", "cat: 'Sandwiches & Subs', capex: '₹9–17.5L', payback: '8–12 mo', desc: 'Mr. Sandwich European subs and cafe model")
html = html.replace("brandName = 'Chai Katta';", "brandName = 'Mr. Sandwich';")
html = html.replace("brandName = 'Momo Mafia';", "brandName = 'Dunk Burgers';")
html = html.replace("brandName = 'Biryani Bay';", "brandName = 'South Twist';")
html = html.replace("brandName = 'Kulfi Club';", "brandName = 'Beyond Temptation';")
html = html.replace("brandName = 'Tandoor Tribe';", "brandName = 'Cafe Choco Craze';")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Cleaned all legacy residuals from index.html successfully!")
