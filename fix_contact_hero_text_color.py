# -*- coding: utf-8 -*-

def fix_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Add explicit styling for .contact-hero h1, .contact-hero h2, .contact-hero p, .badge-trust
    old_block = """.contact-hero {
  position: relative;
  background: radial-gradient(circle at 50% 20%, rgba(14, 18, 26, 0.6) 0%, #080B10 100%), #080B10;
  padding: clamp(90px, 12vw, 140px) 0 clamp(40px, 6vw, 70px);
  color: var(--malai);
  overflow: hidden;
  border-bottom: 1px solid var(--line-dark);
}"""

    new_block = """.contact-hero {
  position: relative;
  background: radial-gradient(circle at 50% 20%, rgba(14, 18, 26, 0.6) 0%, #080B10 100%), #080B10;
  padding: clamp(90px, 12vw, 140px) 0 clamp(40px, 6vw, 70px);
  color: #FFFFFF !important;
  overflow: hidden;
  border-bottom: 1px solid var(--line-dark);
}
.contact-hero h1 {
  color: #FFFFFF !important;
  font-family: var(--font-editorial), var(--font-display), serif;
  font-weight: 700;
  letter-spacing: -0.025em;
  line-height: 1.15;
  text-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
}
.contact-hero .page-hero-sub {
  color: rgba(248, 250, 252, 0.88) !important;
  font-size: clamp(16px, 1.8vw, 18.5px);
  line-height: 1.65;
}
.contact-hero .badge-trust {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.18);
  color: #FFFFFF !important;
}"""

    if old_block in content:
        content = content.replace(old_block, new_block)
    else:
        # Also inject at top of style
        content = content.replace('<style>', '<style>\n' + new_block)

    # In HTML header itself, ensure inline color style is safe
    content = content.replace(
        '<h1 class="rise" style="font-size:clamp(34px,4.5vw,56px);max-width:20ch;margin-block:16px 14px">Get In Touch With Senior Franchise Advisors.</h1>',
        '<h1 class="rise" style="font-size:clamp(34px,4.5vw,56px);max-width:20ch;margin-block:16px 14px;color:#FFFFFF!important">Get In Touch With Senior Franchise Advisors.</h1>'
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed hero text color in {filename}")

fix_file("contact.html")
fix_file("book-consultation.html")
