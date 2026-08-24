# -*- coding: utf-8 -*-
import os, json, shutil

# 1. CREATE contact.html from book-consultation.html
with open("book-consultation.html", "r", encoding="utf-8") as f:
    content = f.read()

# Enhance title and meta for contact.html
content = content.replace(
    "<title>Book a Consultation & Contact Us — Franchise 101</title>",
    "<title>Contact Us & Book Consultation — Franchise 101</title>"
)

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Created contact.html successfully")

# 2. UPDATE vercel.json for seamless /contact and /book-consultation routing
vercel_config = {
    "version": 2,
    "cleanUrls": True,
    "rewrites": [
        { "source": "/contact", "destination": "/contact.html" },
        { "source": "/contact.html", "destination": "/contact.html" },
        { "source": "/book-consultation", "destination": "/book-consultation.html" },
        { "source": "/book-consultation.html", "destination": "/book-consultation.html" }
    ]
}

with open("vercel.json", "w", encoding="utf-8") as f:
    json.dump(vercel_config, f, indent=2)

print("Updated vercel.json with clean rewrites")

# 3. UPDATE all navigation bars to link to contact.html
all_pages = [
    "index.html", "franq-franchise-website.html", "about.html", "franchises.html",
    "find-franchise.html", "develop-brand.html", "develop-scale.html", "franchise-marketing.html",
    "beyond-temptation.html", "dunk-burgers.html", "mr-sandwich.html", "south-twist.html",
    "cafe-choco-craze.html", "book-consultation.html", "contact.html"
]

for filename in all_pages:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            html = f.read()
        
        # Replace <a href="book-consultation.html">Contact</a> with <a href="contact.html">Contact</a>
        html = html.replace('<a href="book-consultation.html">Contact</a>', '<a href="contact.html">Contact</a>')
        html = html.replace('<a href="/book-consultation.html">Contact</a>', '<a href="contact.html">Contact</a>')
        html = html.replace('<a href="/book-consultation">Contact</a>', '<a href="contact.html">Contact</a>')
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Verified and updated contact links in {filename}")
