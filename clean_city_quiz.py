# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Testimonials
html = html.replace('Shalini M.</strong><small>Kulfi Club &middot; Bandra, Mumbai</small>', 'Shalini M.</strong><small>Beyond Temptation &middot; Bandra, Mumbai</small>')
html = html.replace('Aditya K.</strong><small>Biryani Bay &middot; Andheri West, Mumbai</small>', 'Aditya K.</strong><small>South Twist &middot; Kothrud, Pune</small>')

# 2. Update CITY_SLOTS
CITY_SLOTS_REPLACEMENT = """/* ============ CITY AVAILABILITY CHECKER ============ */
const CITY_SLOTS = {
  mumbai: {
    name: 'Mumbai & MMR',
    slots: '18 Brand Slots Available',
    desc: 'High-demand catchments open in Thane, Navi Mumbai, Andheri East, and Powai. Average kiosk footfall 1,400+ daily.',
    brands: ['Beyond Temptation (4 slots)', 'Dunk Burgers (3 slots)', 'Mr. Sandwich (5 slots)', 'South Twist (6 slots)']
  },
  pune: {
    name: 'Pune & PCMC',
    slots: '14 Brand Slots Available',
    desc: 'Prime student and tech park zones available in Kothrud, Baner, Viman Nagar, and Hinjawadi Phase 1.',
    brands: ['Beyond Temptation (5 slots)', 'South Twist (4 slots)', 'Cafe Choco Craze (3 slots)', 'Dunk Burgers (2 slots)']
  },
  bangalore: {
    name: 'Bengaluru',
    slots: '22 Brand Slots Available',
    desc: 'Dense tech cluster opportunities in HSR Layout, Koramangala, Whitefield, and Electronic City.',
    brands: ['South Twist (8 slots)', 'Mr. Sandwich (6 slots)', 'Beyond Temptation (4 slots)', 'Dunk Burgers (4 slots)']
  },
  delhi: {
    name: 'Delhi NCR (Gurugram, Noida)',
    slots: '26 Brand Slots Available',
    desc: 'Rapid QSR footfall corridors in Cyber Hub, Sector 62 Noida, South Ext, and Rajouri Garden.',
    brands: ['Mr. Sandwich (8 slots)', 'Beyond Temptation (6 slots)', 'Dunk Burgers (7 slots)', 'Cafe Choco Craze (5 slots)']
  },
  hyderabad: {
    name: 'Hyderabad & Secunderabad',
    slots: '16 Brand Slots Available',
    desc: 'Bustling evening trade in Madhapur, Gachibowli, Kukatpally, and Jubilee Hills.',
    brands: ['South Twist (6 slots)', 'Beyond Temptation (4 slots)', 'Mr. Sandwich (3 slots)', 'Dunk Burgers (3 slots)']
  },
  ahmedabad: {
    name: 'Ahmedabad & Surat',
    slots: '12 Brand Slots Available',
    desc: 'High-margin dessert and vegetarian fast-casual slots in SG Highway, Bodakdev, and Vesu.',
    brands: ['Beyond Temptation (5 slots)', 'Mr. Sandwich (4 slots)', 'Cafe Choco Craze (3 slots)']
  },
  chennai: {
    name: 'Chennai',
    slots: '10 Brand Slots Available',
    desc: 'Key transit & college hubs in OMR, Anna Nagar, T. Nagar, and Velachery.',
    brands: ['South Twist (5 slots)', 'Mr. Sandwich (3 slots)', 'Beyond Temptation (2 slots)']
  },
  kolkata: {
    name: 'Kolkata',
    slots: '11 Brand Slots Available',
    desc: 'Strong evening street food demand in Salt Lake Sector V, Park Street, and Newtown.',
    brands: ['Mr. Sandwich (4 slots)', 'Dunk Burgers (4 slots)', 'Beyond Temptation (3 slots)']
  },
  jaipur: {
    name: 'Jaipur & Rajasthan',
    slots: '9 Brand Slots Available',
    desc: 'Tourist and student catchments in Malviya Nagar, Vaishali Nagar, and MI Road.',
    brands: ['Beyond Temptation (3 slots)', 'Mr. Sandwich (4 slots)', 'Cafe Choco Craze (2 slots)']
  },
  lucknow: {
    name: 'Lucknow & Kanpur',
    slots: '8 Brand Slots Available',
    desc: 'Gomti Nagar, Hazratganj, and Alambagh commercial high-street spaces.',
    brands: ['Mr. Sandwich (4 slots)', 'Beyond Temptation (2 slots)', 'South Twist (2 slots)']
  }
};"""

html = re.sub(r'/\* ============ CITY AVAILABILITY CHECKER ============ \*/[\s\S]*?const CITY_SLOTS = \{[\s\S]*?\};\n', f'{CITY_SLOTS_REPLACEMENT}\n', html)

# 3. Update Quiz matching logic in index.html
QUIZ_MATCH_LOGIC = """  // Compute matched brand based on budget & category
  let matchedBrand = 'Mr. Sandwich';
  let matchCat = 'Sandwiches & Subs';
  let matchCapex = '₹9–17.5L';
  let matchPayback = '8–12 mo';
  let matchModel = 'FOFO';
  let matchDesc = "India's Largest Brand in the Sandwich Segment. 200+ Outlets across 100+ Cities. European gourmet subs, paninis & coffees with 39%–42% net margin and 8-12 month payback.";
  let matchImg = 'assets/brands/mr-sandwich.png';

  if (quizState.category === 'dessert') {
    matchedBrand = 'Beyond Temptation';
    matchCat = 'Dessert & Cafe';
    matchCapex = '₹13–20L';
    matchPayback = '12–16 mo';
    matchModel = 'FOFO / FOCO';
    matchDesc = '90+ Outlets across 8 states since 2009. Own factory in Pune supplies >85% of menu items. Famous for Cad-Bee chocolate thick shakes, BT Special Cold Coffee & Mastani.';
    matchImg = 'assets/brands/beyond-temptation.png';
  } else if (quizState.category === 'qsr' || quizState.category === 'burgers') {
    matchedBrand = 'Dunk Burgers';
    matchCat = 'Burgers & QSR';
    matchCapex = '₹15–25L';
    matchPayback = '12–15 mo';
    matchModel = 'Zero Royalty';
    matchDesc = "India's First Dip-In Burger Brand with 16+ years of manufacturing foundation. Signature sauce-bath burgers, crispy wings, loaded fries, Cad-B shakes & zero royalty.";
    matchImg = 'assets/brands/dunk-burgers.png';
  } else if (quizState.category === 'cloud' || quizState.category === 'southindian') {
    matchedBrand = 'South Twist';
    matchCat = 'South Indian QSR';
    matchCapex = '₹10–20L';
    matchPayback = '10–14 mo';
    matchModel = 'FOFO';
    matchDesc = 'Fastest growing authentic South Indian franchise. Ghee Podi Thatte Idlis, crispy Benne Dosas, Appe & Filter Coffee with chef-less automated batter pre-mixes.';
    matchImg = 'assets/brands/south_twist_food.png';
  } else if (quizState.category === 'cafe' || quizState.category === 'chocolate') {
    matchedBrand = 'Cafe Choco Craze';
    matchCat = 'Chocolate Cafe';
    matchCapex = '₹8–20L';
    matchPayback = '9–14 mo';
    matchModel = 'FOFO';
    matchDesc = 'Iconic Pune chocolate cafe chain with 80+ outlets. Renowned for Chocolick B (signature Cad-B chocolate thick shake), pizzas, and high repeat footfall.';
    matchImg = 'assets/brands/cafe-choco-craze.png';
  }

  if (quizState.budget === '60plus' || quizState.model === 'foco') {
    matchCapex = '₹40L – 1 Cr';
    matchPayback = '14–18 mo';
    matchModel = 'Master Territory';
    matchDesc += ' [Eligible for Master Franchise: Exclusive territory rights, 40-50% franchise fee sharing & raw material revenue share.]';
  }"""

html = re.sub(r'  // Compute matched brand based on budget & category[\s\S]*?document\.getElementById\(\'quizMatchTitle\'\)', f'{QUIZ_MATCH_LOGIC}\n\n  document.getElementById(\'quizMatchTitle\')', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html city slots and quiz logic to 100% 5 official brands!")
