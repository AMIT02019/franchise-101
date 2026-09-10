# -*- coding: utf-8 -*-
import os, re

print("Starting complete website synchronization with Google Doc content...")

# ==============================================================================
# SCRIPT TO APPLY COMPLETE GOOGLE DOC SPECIFICATION ACROSS ALL PAGES
# ==============================================================================

# Standard Navigation Snippet
NAV_LINKS_HTML = """    <a href="index.html">Home</a>
    <a href="franchises.html">Explore Franchises</a>
    <a href="develop-brand.html">Build Your Brand</a>
    <a href="develop-scale.html">Franchise &amp; Scale</a>
    <a href="franchise-marketing.html">Franchise Marketing</a>
    <a href="about.html">About Us</a>
    <a href="contact.html">Book a Consultation</a>"""

MOBILE_NAV_LINKS_HTML = """      <a href="index.html" class="mobile-nav-link">Home</a>
      <a href="franchises.html" class="mobile-nav-link">Explore Franchises</a>
      <a href="develop-brand.html" class="mobile-nav-link">Build Your Brand</a>
      <a href="develop-scale.html" class="mobile-nav-link">Franchise &amp; Scale</a>
      <a href="franchise-marketing.html" class="mobile-nav-link">Franchise Marketing</a>
      <a href="about.html" class="mobile-nav-link">About Us</a>
      <a href="contact.html" class="mobile-nav-link">Book a Consultation</a>"""

FOOTER_DISCLAIMER_HTML = """    <div style="border-top:1px solid rgba(255,255,255,0.1);padding-top:20px;margin-top:24px">
      <p style="font-size:13px;color:rgba(248,250,252,0.65);line-height:1.6;margin:0 0 12px">
        <strong>Franchise 101 Growth Partners LLP</strong> provides franchise consulting, business-development and related services. Franchise and business investments involve risk. Franchise 101 does not guarantee returns, profitability or business success. Brand-specific commercial and financial information may be supplied by the respective franchisor and should be independently verified before investment.
      </p>
      <div style="display:flex;gap:18px;flex-wrap:wrap;font-size:12.5px">
        <a href="privacy-policy.html" style="color:rgba(248,250,252,0.75)">Privacy Policy</a>
        <a href="terms.html" style="color:rgba(248,250,252,0.75)">Terms &amp; Conditions</a>
        <a href="disclaimer.html" style="color:rgba(248,250,252,0.75)">Franchise &amp; ROI Disclaimer</a>
      </div>
    </div>"""

# ------------------------------------------------------------------------------
# 1. UPDATE index.html & franq-franchise-website.html
# ------------------------------------------------------------------------------

def update_homepage(filename):
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    # Hero copy
    html = re.sub(
        r'<p class="page-hero-sub rise">.*?</p>',
        '<p class="page-hero-sub rise">Franchise 101 is a trusted franchise and business solutions ecosystem helping investors discover the right opportunities, entrepreneurs build businesses from concept to launch, and brands franchise and scale.</p>',
        html,
        flags=re.DOTALL
    )

    # Hero subtitle in .hero-sub
    html = re.sub(
        r'<p class="hero-sub">.*?</p>',
        '<p class="hero-sub">Franchise 101 is a trusted franchise and business solutions ecosystem helping investors discover the right opportunities, entrepreneurs build businesses from concept to launch, and brands franchise and scale.</p>',
        html,
        flags=re.DOTALL
    )

    # Why Franchise 101 Section Update (Section 1.3 in Google Doc)
    WHY_SECTION_HTML = """<!-- ============ WHY FRANCHISE 101 ============ -->
<section class="sec" id="why-franchise101" style="background:#FFFFFF;border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-top rv" style="margin-bottom:36px">
      <div class="sec-head wide">
        <p class="eyebrow"><span class="pulse"></span> Why Franchise 101</p>
        <h2 style="color:var(--ink);font-size:clamp(26px, 3.6vw, 44px)">
          Experience Behind Every Opportunity. Guidance Behind Every Decision.
        </h2>
        <p class="sec-note" style="color:var(--ink-80);font-size:16.5px;line-height:1.65">
          Franchise decisions involve significant capital, time and commitment. Franchise 101 combines industry experience, practical business-building expertise and an investor-first approach to help entrepreneurs navigate these decisions with greater clarity and confidence.
        </p>
      </div>
    </div>

    <!-- 6 Key Differentiators Grid -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:20px;margin-bottom:32px" class="rv">
      
      <div style="background:var(--paper);border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px">
        <strong style="font-family:var(--font-display);font-size:28px;color:var(--kesar-hot)">15+ Years</strong>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Combined Industry Experience</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Our partners bring over 15 years of combined experience across franchising, restaurant development, business consulting, design and execution.
        </p>
      </div>

      <div style="background:var(--paper);border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px">
        <strong style="font-family:var(--font-display);font-size:28px;color:var(--pista-dark)">End-to-End</strong>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Process Knowledge</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Our experience extends beyond franchise sales&mdash;from concept development and operations to outlet development, franchise expansion and investor acquisition.
        </p>
      </div>

      <div style="background:var(--paper);border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px">
        <strong style="font-family:var(--font-display);font-size:28px;color:var(--kesar-hot)">10+ Brands</strong>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Scaling Brand Portfolios</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Extensive experience working with more than 10 brands through different critical stages of expansion and regional market entry.
        </p>
      </div>

      <div style="background:var(--paper);border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px">
        <strong style="font-family:var(--font-display);font-size:28px;color:var(--pista-dark)">100+ Outlets</strong>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Franchisees Facilitated</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Our team brings first-hand experience in facilitating more than 100 franchise units and operators through our associated F&amp;B ventures.
        </p>
      </div>

      <div style="background:var(--paper);border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px">
        <strong style="font-family:var(--font-display);font-size:28px;color:var(--kesar-hot)">8+ States</strong>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Multi-State Presence</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Demonstrated track record establishing and expanding commercial business presence across more than 8 Indian states.
        </p>
      </div>

      <div style="background:var(--paper);border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px">
        <strong style="font-family:var(--font-display);font-size:28px;color:var(--pista-dark)">50+ Concepts</strong>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Restaurant Concepts Supported</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          More than 50 restaurant concepts supported across concept development, menu engineering, kitchen operations and turnkey business setup.
        </p>
      </div>

    </div>

    <!-- Trust Statement Callout -->
    <div style="background:#0E121A;border:1px solid rgba(255,255,255,0.12);border-radius:20px;padding:26px 32px;color:var(--malai);display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap" class="on-dark rv">
      <div style="max-width:62ch">
        <span style="font-family:var(--font-mono);font-size:11px;color:var(--kesar);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;display:block;margin-bottom:4px">Our Core Commitment</span>
        <p style="font-size:15px;line-height:1.65;color:rgba(248,250,252,0.9);margin:0">
          Our objective is not simply to facilitate a franchise transaction. We aim to understand the investor first, evaluate the opportunity carefully and help create a more informed path towards business ownership.
        </p>
      </div>
      <a class="btn btn--kesar btn--sm" href="contact.html">Book an Advisory Session &rarr;</a>
    </div>

  </div>
</section>"""

    # How It Works 6-Step Journey Update (Section 1.4 in Google Doc)
    HOW_IT_WORKS_HTML = """<!-- ============ HOW IT WORKS (YOUR JOURNEY) ============ -->
<section class="sec" id="how-it-works" style="background:var(--paper);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-top rv" style="margin-bottom:36px">
      <div class="sec-head wide">
        <p class="eyebrow"><span class="pulse"></span> How It Works</p>
        <h2 style="color:var(--ink);font-size:clamp(26px, 3.5vw, 42px)">Your Journey with Franchise 101</h2>
        <p class="sec-note" style="color:var(--ink-80)">
          A structured, 6-stage pathway designed to move investors from exploration to a successful, operational launch.
        </p>
      </div>
      <div style="font-family:var(--font-mono);font-size:12px;color:var(--kesar-hot);font-weight:700;background:#FFFFFF;border:1px solid var(--line);padding:8px 16px;border-radius:999px">
        Discover &rarr; Consult &rarr; Match &rarr; Evaluate &rarr; Finalise &rarr; Launch
      </div>
    </div>

    <!-- 6 Stages Grid -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:20px" class="rv">
      
      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px;box-shadow:0 8px 24px -8px rgba(14,18,26,0.05)">
        <span style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:4px 10px;border-radius:6px;width:fit-content">01</span>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Tell Us What You're Looking For</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Submit an enquiry and share your investment range, preferred location, business interests, timeline and level of involvement.
        </p>
      </div>

      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px;box-shadow:0 8px 24px -8px rgba(14,18,26,0.05)">
        <span style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:4px 10px;border-radius:6px;width:fit-content">02</span>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Consultation &amp; Requirement Study</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Our team understands your requirements, objectives and preferences before recommending opportunities from our curated brand pool.
        </p>
      </div>

      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px;box-shadow:0 8px 24px -8px rgba(14,18,26,0.05)">
        <span style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:4px 10px;border-radius:6px;width:fit-content">03</span>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Opportunity Matching</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          We shortlist relevant franchise opportunities based on factors such as investment, location, category, business model and investor suitability.
        </p>
      </div>

      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px;box-shadow:0 8px 24px -8px rgba(14,18,26,0.05)">
        <span style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:4px 10px;border-radius:6px;width:fit-content">04</span>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Brand Introduction &amp; Evaluation</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          We facilitate discussions between you and shortlisted brands, help you understand the opportunity and support the evaluation process before you make your decision.
        </p>
      </div>

      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px;box-shadow:0 8px 24px -8px rgba(14,18,26,0.05)">
        <span style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:4px 10px;border-radius:6px;width:fit-content">05</span>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Franchise Finalisation</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Once an opportunity is selected, we assist in coordinating the next commercial and legal agreement stages between the investor and the brand.
        </p>
      </div>

      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:20px;padding:26px;display:flex;flex-direction:column;gap:10px;box-shadow:0 8px 24px -8px rgba(14,18,26,0.05)">
        <span style="font-family:var(--font-mono);font-size:12px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:4px 10px;border-radius:6px;width:fit-content">06</span>
        <h4 style="font-size:17px;color:var(--ink);margin:0">Setup &amp; Launch Support</h4>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Depending on requirements, Franchise 101 supports location assistance, outlet development, kitchen CAD, interiors, business setup and launch coordination through our wider ecosystem.
        </p>
      </div>

    </div>
  </div>
</section>"""

    # Official FAQ Section (Section 1.7 in Google Doc)
    FAQ_SECTION_HTML = """<!-- ============ OFFICIAL FAQ ============ -->
<section class="sec" id="faq" style="background:#FFFFFF;border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-top rv" style="margin-bottom:32px">
      <div class="sec-head wide">
        <p class="eyebrow"><span class="pulse"></span> Frequently Asked Questions</p>
        <h2 style="color:var(--ink);font-size:clamp(26px, 3.5vw, 42px)">Clear Answers. Objective Insights.</h2>
        <p class="sec-note" style="color:var(--ink-80)">
          Everything you need to know about navigating the Franchise 101 ecosystem.
        </p>
      </div>
    </div>

    <div style="max-width:880px;margin:0 auto;display:flex;flex-direction:column;gap:14px" class="rv">
      
      <details style="background:var(--paper);border:1.5px solid var(--line);border-radius:16px;padding:18px 22px;cursor:pointer" open>
        <summary style="font-family:var(--font-display);font-size:17px;font-weight:700;color:var(--ink);outline:none">What does Franchise 101 do?</summary>
        <p style="font-size:14.5px;color:var(--ink-80);line-height:1.65;margin:12px 0 0">
          Franchise 101 is a franchise and business solutions ecosystem that helps investors discover and evaluate franchise opportunities, entrepreneurs develop businesses from concept to launch, and existing brands strengthen, franchise and scale.
        </p>
      </details>

      <details style="background:var(--paper);border:1.5px solid var(--line);border-radius:16px;padding:18px 22px;cursor:pointer">
        <summary style="font-family:var(--font-display);font-size:17px;font-weight:700;color:var(--ink);outline:none">How does Franchise 101 help me find a franchise?</summary>
        <p style="font-size:14.5px;color:var(--ink-80);line-height:1.65;margin:12px 0 0">
          We begin by understanding your investment capacity, preferred location, business interests, timeline and desired level of involvement. Based on these requirements, our team identifies relevant opportunities from our brand network and assists you through consultation, brand introductions and the evaluation process.
        </p>
      </details>

      <details style="background:var(--paper);border:1.5px solid var(--line);border-radius:16px;padding:18px 22px;cursor:pointer">
        <summary style="font-family:var(--font-display);font-size:17px;font-weight:700;color:var(--ink);outline:none">Does Franchise 101 guarantee returns from a franchise?</summary>
        <p style="font-size:14.5px;color:var(--ink-80);line-height:1.65;margin:12px 0 0">
          No. Every business involves risk, and actual performance depends on multiple factors including location, operations, management, market conditions and brand performance. Franchise 101 assists with evaluation and decision-making but does not guarantee returns, profits or business success.
        </p>
      </details>

      <details style="background:var(--paper);border:1.5px solid var(--line);border-radius:16px;padding:18px 22px;cursor:pointer">
        <summary style="font-family:var(--font-display);font-size:17px;font-weight:700;color:var(--ink);outline:none">Do I have to choose only from brands listed on your website?</summary>
        <p style="font-size:14.5px;color:var(--ink-80);line-height:1.65;margin:12px 0 0">
          Our featured opportunities represent brands currently available through our network. During consultation, our team will focus on understanding your requirements and discussing suitable available options.
        </p>
      </details>

      <details style="background:var(--paper);border:1.5px solid var(--line);border-radius:16px;padding:18px 22px;cursor:pointer">
        <summary style="font-family:var(--font-display);font-size:17px;font-weight:700;color:var(--ink);outline:none">Can Franchise 101 help with setting up the outlet?</summary>
        <p style="font-size:14.5px;color:var(--ink-80);line-height:1.65;margin:12px 0 0">
          Yes. Depending on the requirement, our wider business-development ecosystem can support areas such as outlet planning, design, fit-out, kitchen planning, operational development, branding, marketing and launch coordination.
        </p>
      </details>

      <details style="background:var(--paper);border:1.5px solid var(--line);border-radius:16px;padding:18px 22px;cursor:pointer">
        <summary style="font-family:var(--font-display);font-size:17px;font-weight:700;color:var(--ink);outline:none">Can you help me create my own brand instead of buying a franchise?</summary>
        <p style="font-size:14.5px;color:var(--ink-80);line-height:1.65;margin:12px 0 0">
          Yes. Franchise 101's Business &amp; Restaurant Development services are designed for entrepreneurs who want to develop their own concept. We can support individual requirements or provide an integrated concept-to-launch solution.
        </p>
      </details>

      <details style="background:var(--paper);border:1.5px solid var(--line);border-radius:16px;padding:18px 22px;cursor:pointer">
        <summary style="font-family:var(--font-display);font-size:17px;font-weight:700;color:var(--ink);outline:none">I already own a business. Can Franchise 101 help me franchise it?</summary>
        <p style="font-size:14.5px;color:var(--ink-80);line-height:1.65;margin:12px 0 0">
          Yes. We work with existing businesses looking to strengthen their proposition, prepare for franchising, generate investor interest and expand into new markets.
        </p>
      </details>

      <details style="background:var(--paper);border:1.5px solid var(--line);border-radius:16px;padding:18px 22px;cursor:pointer">
        <summary style="font-family:var(--font-display);font-size:17px;font-weight:700;color:var(--ink);outline:none">Is the consultation paid?</summary>
        <p style="font-size:14.5px;color:var(--ink-80);line-height:1.65;margin:12px 0 0">
          No. Our team offers the first consultation free of charge for prospective investors and business founders.
        </p>
      </details>

    </div>
  </div>
</section>"""

    # Final CTA Section (Section 1.8 in Google Doc)
    FINAL_CTA_HTML = """<!-- ============ FINAL CTA (YOUR NEXT BUSINESS STARTS HERE) ============ -->
<section class="sec on-dark" style="background:#0E121A;border-top:1px solid rgba(255,255,255,0.12);padding:clamp(60px, 8vw, 100px) 0">
  <div class="wrap">
    <div style="max-width:68ch;margin:0 auto;text-align:center" class="rv">
      <span class="tag gold" style="margin-bottom:12px">Get In Touch</span>
      <h2 style="color:var(--malai);font-size:clamp(30px, 4.2vw, 52px);margin:0 0 16px;line-height:1.15">
        Your Next Business Starts Here.
      </h2>
      <p style="color:rgba(248,250,252,0.85);font-size:clamp(16px, 1.8vw, 19px);line-height:1.65;margin:0 auto 28px">
        Whether you're looking for the right franchise, planning to build your own concept or exploring the next stage of growth for your brand, start the conversation with Franchise 101.
      </p>
      <div style="display:flex;gap:14px;justify-content:center;align-items:center;flex-wrap:wrap">
        <a class="btn btn--kesar" href="contact.html">Book a Consultation <span class="arw">&rarr;</span></a>
        <a class="btn btn--ghost" href="https://wa.me/912240008899?text=Hi%20Franchise%20101,%20I%20would%20like%20to%20speak%20with%20an%20advisor." target="_blank">WhatsApp Us 💬</a>
      </div>
    </div>
  </div>
</section>"""

    # Replace / Insert sections into index.html
    # 1. Why section replacement
    if '<section class="sec" id="why-franchise101"' in html:
        html = re.sub(r'<section class="sec" id="why-franchise101".*?</section>', WHY_SECTION_HTML, html, flags=re.DOTALL)
    else:
        html = html.replace('<!-- ============ CITY AVAILABILITY CHECKER ============ -->', f"{WHY_SECTION_HTML}\n\n<!-- ============ CITY AVAILABILITY CHECKER ============ -->")

    # 2. How it works replacement
    if '<section class="sec" id="how-it-works"' in html:
        html = re.sub(r'<section class="sec" id="how-it-works".*?</section>', HOW_IT_WORKS_HTML, html, flags=re.DOTALL)
    else:
        html = html.replace('<!-- ============ CITY AVAILABILITY CHECKER ============ -->', f"{HOW_IT_WORKS_HTML}\n\n<!-- ============ CITY AVAILABILITY CHECKER ============ -->")

    # 3. FAQ section replacement
    if '<section class="sec" id="faq"' in html:
        html = re.sub(r'<section class="sec" id="faq".*?</section>', FAQ_SECTION_HTML, html, flags=re.DOTALL)
    else:
        html = html.replace('<!-- ============ FOOTER ============ -->', f"{FAQ_SECTION_HTML}\n\n{FINAL_CTA_HTML}\n\n<!-- ============ FOOTER ============ -->")

    # 4. Final CTA replacement
    if '<!-- ============ FINAL CTA' in html:
        html = re.sub(r'<!-- ============ FINAL CTA.*?<!-- ============ FOOTER', f"{FINAL_CTA_HTML}\n\n<!-- ============ FOOTER", html, flags=re.DOTALL)

    # 5. Update Footer Disclaimer
    if '<div style="border-top:1px solid rgba(255,255,255,0.1)' not in html:
        html = html.replace('</footer>', f"{FOOTER_DISCLAIMER_HTML}\n</footer>")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {filename} with Google Doc sections!")

update_homepage("index.html")
update_homepage("franq-franchise-website.html")
