# -*- coding: utf-8 -*-
import os, re

# ==============================================================================
# 1. UPDATE about.html WITH THE FULL VISION, 3 VERTICALS & ECOSYSTEM ARCHITECTURE
# ==============================================================================

ABOUT_VISION_SECTION_HTML = """<!-- ============ FRANCHISE 101 VISION & 3 KEY VERTICALS ============ -->
<section class="sec" id="vision-ecosystem" style="background:var(--paper);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    
    <!-- Vision Statement Header -->
    <div class="sec-top rv" style="margin-bottom: clamp(36px, 5vw, 56px)">
      <div class="sec-head wide">
        <p class="eyebrow"><span class="pulse"></span> Our Vision</p>
        <h2 style="font-size:clamp(28px, 3.8vw, 46px);line-height:1.2;color:var(--ink)">
          A One-Stop Franchise &amp; Business Solutions Ecosystem
        </h2>
        <p class="sec-note" style="font-size:clamp(16px, 1.8vw, 19px);line-height:1.65;max-width:44ch;color:var(--ink-80)">
          Franchise 101 aspires to become a one-stop franchise and business solutions ecosystem, serving investors, entrepreneurs and brands across the entire business journey.
        </p>
      </div>
      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-left:4px solid var(--kesar);border-radius:18px;padding:24px 28px;box-shadow:0 10px 30px -10px rgba(14,18,26,0.06);max-width:540px">
        <span style="font-family:var(--font-mono);font-size:11.5px;color:var(--kesar-hot);font-weight:700;text-transform:uppercase;letter-spacing:0.08em;display:block;margin-bottom:6px">Core Ecosystem Purpose</span>
        <p style="font-size:15px;line-height:1.6;color:var(--ink);margin:0">
          Our vision is to bring together the expertise, services and execution capabilities required to help people <strong>discover, build, grow and scale businesses</strong>, while creating meaningful connections between investors and brands.
        </p>
      </div>
    </div>

    <!-- The 3 Key Verticals Grid -->
    <div style="margin-bottom:20px">
      <h3 style="font-size:clamp(22px, 2.5vw, 32px);color:var(--ink);margin-bottom:8px">Our Three Core Verticals</h3>
      <p style="font-size:15px;color:var(--ink-60);max-width:60ch">Every engagement across Franchise 101 is structured around three interconnected operational pillars:</p>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:24px;margin-bottom: clamp(48px, 6vw, 72px)" class="rv">
      
      <!-- Vertical 01 -->
      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:24px;padding:32px 28px;display:flex;flex-direction:column;gap:16px;box-shadow:0 12px 36px -12px rgba(14,18,26,0.07);position:relative;transition:all 0.3s ease">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <span style="font-family:var(--font-mono);font-size:13px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:6px 14px;border-radius:999px">01</span>
          <span style="font-family:var(--font-mono);font-size:12px;font-weight:700;color:var(--pista-dark);background:rgba(16,185,129,0.1);padding:5px 12px;border-radius:8px">Find &middot; Evaluate &middot; Invest</span>
        </div>
        <h4 style="font-size:22px;color:var(--ink);margin:0">Investor &amp; Franchise Consulting</h4>
        <p style="font-size:14.5px;color:var(--ink-60);line-height:1.65;margin:0">
          Helping investors and aspiring entrepreneurs discover, evaluate and select franchise and business opportunities suited to their investment capacity, goals, location, interests and level of involvement.
        </p>
        <div style="margin-top:auto;padding-top:14px;border-top:1px solid var(--line)">
          <a href="franchises.html" style="font-size:13.5px;font-weight:700;color:var(--kesar-hot);display:inline-flex;align-items:center;gap:6px">Explore Curated Brands &rarr;</a>
        </div>
      </div>

      <!-- Vertical 02 -->
      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:24px;padding:32px 28px;display:flex;flex-direction:column;gap:16px;box-shadow:0 12px 36px -12px rgba(14,18,26,0.07);position:relative;transition:all 0.3s ease">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <span style="font-family:var(--font-mono);font-size:13px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:6px 14px;border-radius:999px">02</span>
          <span style="font-family:var(--font-mono);font-size:12px;font-weight:700;color:var(--kesar-hot);background:rgba(255,176,32,0.12);padding:5px 12px;border-radius:8px">Concept &middot; Build &middot; Launch</span>
        </div>
        <h4 style="font-size:22px;color:var(--ink);margin:0">Business &amp; Restaurant Development</h4>
        <p style="font-size:14.5px;color:var(--ink-60);line-height:1.65;margin:0">
          <strong>Concept to Key-in-Hand:</strong> Helping entrepreneurs transform an idea into a fully developed, branded and operational business through an integrated range of services spanning concept development, branding, design, setup, operations, marketing and launch.
        </p>
        <div style="background:rgba(14,18,26,0.03);border-radius:10px;padding:10px 14px;font-size:12.5px;color:var(--ink-80);line-height:1.4">
          <em>Clients can engage us for individual services, a combination of services, or a complete end-to-end turnkey solution.</em>
        </div>
        <div style="margin-top:auto;padding-top:14px;border-top:1px solid var(--line)">
          <a href="develop-brand.html" style="font-size:13.5px;font-weight:700;color:var(--kesar-hot);display:inline-flex;align-items:center;gap:6px">View Concept-to-Launch Services &rarr;</a>
        </div>
      </div>

      <!-- Vertical 03 -->
      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:24px;padding:32px 28px;display:flex;flex-direction:column;gap:16px;box-shadow:0 12px 36px -12px rgba(14,18,26,0.07);position:relative;transition:all 0.3s ease">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <span style="font-family:var(--font-mono);font-size:13px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:6px 14px;border-radius:999px">03</span>
          <span style="font-family:var(--font-mono);font-size:12px;font-weight:700;color:var(--pista-dark);background:rgba(16,185,129,0.1);padding:5px 12px;border-radius:8px">Strengthen &middot; Market &middot; Scale</span>
        </div>
        <h4 style="font-size:22px;color:var(--ink);margin:0">Brand Growth &amp; Franchise Expansion</h4>
        <p style="font-size:14.5px;color:var(--ink-60);line-height:1.65;margin:0">
          Helping existing businesses and brands strengthen their brand, enhance their business, develop their franchise proposition, generate investor demand and expand through franchising, with solutions tailored to their individual requirements.
        </p>
        <div style="margin-top:auto;padding-top:14px;border-top:1px solid var(--line)">
          <a href="develop-scale.html" style="font-size:13.5px;font-weight:700;color:var(--kesar-hot);display:inline-flex;align-items:center;gap:6px">Explore Brand Scaling &rarr;</a>
        </div>
      </div>

    </div>

    <!-- ============ THE LARGER ECOSYSTEM FLOW DIAGRAM ============ -->
    <div style="background:#0E121A;border:1px solid rgba(255,255,255,0.12);border-radius:clamp(24px, 4vw, 36px);padding:clamp(32px, 5vw, 56px);color:var(--malai);box-shadow:0 24px 60px -20px rgba(0,0,0,0.6)" class="rv on-dark">
      <div style="text-align:center;max-width:68ch;margin:0 auto 36px">
        <span class="tag gold" style="margin-bottom:10px">Interactive Architecture</span>
        <h3 style="color:var(--malai);font-size:clamp(24px, 3vw, 36px);margin:0 0 10px">The Larger Franchise 101 Ecosystem</h3>
        <p style="color:rgba(248,250,252,0.8);font-size:15.5px;line-height:1.6;margin:0">
          A synchronized marketplace and execution engine creating continuous, high-trust value between capital and brands.
        </p>
      </div>

      <!-- 3-Tier Flow Diagram -->
      <div style="display:flex;flex-direction:column;gap:18px;max-width:880px;margin:0 auto">
        
        <!-- Top Tier: INVESTORS -->
        <div style="background:rgba(255,255,255,0.06);border:1.5px solid rgba(255,255,255,0.15);border-radius:20px;padding:22px 28px;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap">
          <div>
            <span style="font-family:var(--font-mono);font-size:11px;color:var(--kesar);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;display:block">Tier 1 &middot; Capital Side</span>
            <strong style="font-size:20px;color:#FFFFFF">INVESTORS &amp; ENTREPRENEURS</strong>
          </div>
          <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-family:var(--font-mono);font-size:12.5px;color:rgba(248,250,252,0.9)">
            <span>Discover</span> <span style="color:var(--kesar)">&rarr;</span>
            <span>Evaluate</span> <span style="color:var(--kesar)">&rarr;</span>
            <span>Invest</span> <span style="color:var(--kesar)">&rarr;</span>
            <span>Build</span> <span style="color:var(--kesar)">&rarr;</span>
            <span style="color:var(--pista);font-weight:700">Grow</span>
          </div>
        </div>

        <!-- Middle Hub: FRANCHISE 101 -->
        <div style="display:flex;justify-content:center;align-items:center;gap:12px;margin-block:4px">
          <div style="height:24px;width:2px;background:var(--kesar)"></div>
          <span style="font-family:var(--font-mono);font-size:12px;color:var(--kesar);font-weight:700;letter-spacing:0.1em">&#8597; SYNCHRONIZED THROUGH &#8597;</span>
          <div style="height:24px;width:2px;background:var(--kesar)"></div>
        </div>

        <div style="background:linear-gradient(135deg, rgba(255,176,32,0.18), rgba(16,185,129,0.12));border:2px solid var(--kesar);border-radius:22px;padding:26px 32px;text-align:center;box-shadow:0 0 35px rgba(255,176,32,0.25)">
          <span style="font-family:var(--font-mono);font-size:11px;color:var(--kesar);font-weight:800;letter-spacing:0.12em;text-transform:uppercase;display:block;margin-bottom:4px">Central Execution Engine</span>
          <strong style="font-family:var(--font-editorial);font-size:clamp(22px, 2.5vw, 30px);color:#FFFFFF;letter-spacing:0.02em">FRANCHISE 101 ECOSYSTEM</strong>
          <p style="font-family:var(--font-mono);font-size:13.5px;color:rgba(255,255,255,0.9);margin:8px 0 0;font-weight:600">
            Consulting + Development + Execution + Marketing + Technology
          </p>
        </div>

        <!-- Bottom Tier: BRANDS -->
        <div style="display:flex;justify-content:center;align-items:center;gap:12px;margin-block:4px">
          <div style="height:24px;width:2px;background:var(--pista)"></div>
          <span style="font-family:var(--font-mono);font-size:12px;color:var(--pista);font-weight:700;letter-spacing:0.1em">&#8597; EMPOWERING &#8597;</span>
          <div style="height:24px;width:2px;background:var(--pista)"></div>
        </div>

        <div style="background:rgba(255,255,255,0.06);border:1.5px solid rgba(255,255,255,0.15);border-radius:20px;padding:22px 28px;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap">
          <div>
            <span style="font-family:var(--font-mono);font-size:11px;color:var(--pista);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;display:block">Tier 2 &middot; Brand Supply Side</span>
            <strong style="font-size:20px;color:#FFFFFF">EMERGING &amp; ESTABLISHED BRANDS</strong>
          </div>
          <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-family:var(--font-mono);font-size:12.5px;color:rgba(248,250,252,0.9)">
            <span>Build</span> <span style="color:var(--pista)">&rarr;</span>
            <span>Strengthen</span> <span style="color:var(--pista)">&rarr;</span>
            <span>Franchise</span> <span style="color:var(--pista)">&rarr;</span>
            <span>Acquire Investors</span> <span style="color:var(--pista)">&rarr;</span>
            <span style="color:var(--kesar);font-weight:700">Expand</span>
          </div>
        </div>

        <!-- Future Technology Layer -->
        <div style="background:rgba(14,18,26,0.85);border:1.5px dashed rgba(255,255,255,0.25);border-radius:18px;padding:22px 26px;margin-top:14px;display:flex;gap:18px;align-items:center;flex-wrap:wrap">
          <div style="width:44px;height:44px;border-radius:12px;background:rgba(255,176,32,0.15);border:1px solid var(--kesar);display:grid;place-items:center;font-size:20px;flex-shrink:0">
            💻
          </div>
          <div style="flex:1;min-width:260px">
            <span style="font-family:var(--font-mono);font-size:11px;color:var(--kesar);font-weight:700;text-transform:uppercase;letter-spacing:0.08em">Underlying Foundation &middot; Future Technology Layer</span>
            <h5 style="color:#FFFFFF;font-size:16px;margin:2px 0 4px">Franchise Business Management Platform</h5>
            <p style="color:rgba(248,250,252,0.75);font-size:13.5px;line-height:1.55;margin:0">
              Connecting people, businesses, services, data and processes across the entire franchise lifecycle to simplify operations and power scalable multi-unit expansion.
            </p>
          </div>
        </div>

      </div>
    </div>

  </div>
</section>"""

with open("about.html", "r", encoding="utf-8") as f:
    about_html = f.read()

# Replace or insert into about.html
if "<!-- ============ FRANCHISE 101 VISION & 3 KEY VERTICALS ============ -->" in about_html:
    about_html = re.sub(
        r'<!-- ============ FRANCHISE 101 VISION & 3 KEY VERTICALS ============ -->.*?<!-- ============ MISSION & VISION ============ -->',
        ABOUT_VISION_SECTION_HTML + '\n\n<!-- ============ MISSION & VISION ============ -->',
        about_html,
        flags=re.DOTALL
    )
else:
    # Insert right before OUR STORY or MISSION & VISION
    about_html = about_html.replace(
        '<!-- ============ OUR STORY ============ -->',
        f"{ABOUT_VISION_SECTION_HTML}\n\n<!-- ============ OUR STORY ============ -->"
    )

# Update page hero sub in about.html to reflect the official One Sentence Vision Statement
about_html = about_html.replace(
    '<p class="page-hero-sub rise">We founded Franchise 101 with one conviction: prospective food franchisees deserve audited unit economics, realistic payback models, and zero broker markup before risking their hard-earned capital.</p>',
    '<p class="page-hero-sub rise">Franchise 101 aspires to become a trusted, one-stop ecosystem helping investors, entrepreneurs and brands discover, build, grow and scale businesses from concept development to franchising.</p>'
)

with open("about.html", "w", encoding="utf-8") as f:
    f.write(about_html)

print("Updated about.html with Full Vision, 3 Core Verticals & Ecosystem Architecture")


# ==============================================================================
# 2. UPDATE index.html WITH ECOSYSTEM & 3 VERTICALS
# ==============================================================================

INDEX_ECOSYSTEM_SECTION = """<!-- ============ FRANCHISE 101 ECOSYSTEM & 3 VERTICALS ============ -->
<section class="sec" id="ecosystem" style="background:var(--paper);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-top rv" style="margin-bottom:36px">
      <div class="sec-head wide">
        <p class="eyebrow"><span class="pulse"></span> The One-Stop Ecosystem</p>
        <h2 style="color:var(--ink);font-size:clamp(26px, 3.5vw, 42px)">Discover. Build. Grow. Scale.</h2>
        <p class="sec-note" style="color:var(--ink-80)">
          Franchise 101 is a one-stop franchise and business solutions ecosystem bringing together the expertise, services and execution capabilities required to build and scale food enterprises.
        </p>
      </div>
      <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">
        <a class="btn btn--kesar btn--sm" href="about.html#vision-ecosystem">Read Full Vision &rarr;</a>
        <a class="btn btn--ghost btn--sm" href="book-consultation.html">Schedule Strategy Call</a>
      </div>
    </div>

    <!-- 3 Core Verticals Grid -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(300px, 1fr));gap:22px;margin-bottom:36px" class="rv">
      
      <!-- Card 01 -->
      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:22px;padding:28px 24px;display:flex;flex-direction:column;gap:14px;box-shadow:0 10px 30px -10px rgba(14,18,26,0.06);transition:transform 0.3s ease">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <span style="font-family:var(--font-mono);font-size:12.5px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:5px 12px;border-radius:999px">01</span>
          <span style="font-family:var(--font-mono);font-size:11px;font-weight:700;color:var(--pista-dark);background:rgba(16,185,129,0.1);padding:4px 10px;border-radius:6px">Find &middot; Evaluate &middot; Invest</span>
        </div>
        <h3 style="font-size:20px;color:var(--ink);margin:0">Investor &amp; Franchise Consulting</h3>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Helping investors discover, evaluate and select verified food franchise opportunities matched to their capital, city location, and involvement level.
        </p>
        <div style="margin-top:auto;padding-top:12px;border-top:1px solid var(--line)">
          <a href="franchises.html" style="font-size:13px;font-weight:700;color:var(--kesar-hot);display:inline-flex;align-items:center;gap:4px">View 5 Curated Brands &rarr;</a>
        </div>
      </div>

      <!-- Card 02 -->
      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:22px;padding:28px 24px;display:flex;flex-direction:column;gap:14px;box-shadow:0 10px 30px -10px rgba(14,18,26,0.06);transition:transform 0.3s ease">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <span style="font-family:var(--font-mono);font-size:12.5px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:5px 12px;border-radius:999px">02</span>
          <span style="font-family:var(--font-mono);font-size:11px;font-weight:700;color:var(--kesar-hot);background:rgba(255,176,32,0.12);padding:4px 10px;border-radius:6px">Concept &middot; Build &middot; Launch</span>
        </div>
        <h3 style="font-size:20px;color:var(--ink);margin:0">Business &amp; Restaurant Development</h3>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          <strong>Concept to Key-in-Hand:</strong> Transforming culinary ideas into operational brands across concept creation, kitchen design, menu engineering, SOPs, and turnkey launch.
        </p>
        <div style="margin-top:auto;padding-top:12px;border-top:1px solid var(--line)">
          <a href="develop-brand.html" style="font-size:13px;font-weight:700;color:var(--kesar-hot);display:inline-flex;align-items:center;gap:4px">Concept-to-Launch Services &rarr;</a>
        </div>
      </div>

      <!-- Card 03 -->
      <div style="background:#FFFFFF;border:1.5px solid var(--line);border-radius:22px;padding:28px 24px;display:flex;flex-direction:column;gap:14px;box-shadow:0 10px 30px -10px rgba(14,18,26,0.06);transition:transform 0.3s ease">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <span style="font-family:var(--font-mono);font-size:12.5px;font-weight:800;color:var(--kesar);background:rgba(255,176,32,0.12);padding:5px 12px;border-radius:999px">03</span>
          <span style="font-family:var(--font-mono);font-size:11px;font-weight:700;color:var(--pista-dark);background:rgba(16,185,129,0.1);padding:4px 10px;border-radius:6px">Strengthen &middot; Market &middot; Scale</span>
        </div>
        <h3 style="font-size:20px;color:var(--ink);margin:0">Brand Growth &amp; Franchise Expansion</h3>
        <p style="font-size:14px;color:var(--ink-60);line-height:1.6;margin:0">
          Helping established food businesses strengthen their brand identity, structure their franchise model, generate investor demand, and expand nationwide.
        </p>
        <div style="margin-top:auto;padding-top:12px;border-top:1px solid var(--line)">
          <a href="develop-scale.html" style="font-size:13px;font-weight:700;color:var(--kesar-hot);display:inline-flex;align-items:center;gap:4px">Scale Your Network &rarr;</a>
        </div>
      </div>

    </div>

  </div>
</section>"""

def update_index_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        idx_content = f.read()

    if "<!-- ============ FRANCHISE 101 ECOSYSTEM & 3 VERTICALS ============ -->" in idx_content:
        idx_content = re.sub(
            r'<!-- ============ FRANCHISE 101 ECOSYSTEM & 3 VERTICALS ============ -->.*?<!-- ============ BRAND MATRIX',
            INDEX_ECOSYSTEM_SECTION + '\n\n<!-- ============ BRAND MATRIX',
            idx_content,
            flags=re.DOTALL
        )
    else:
        # Insert before BRAND MATRIX or after Hero
        idx_content = idx_content.replace(
            '<!-- ============ BRAND MATRIX',
            f"{INDEX_ECOSYSTEM_SECTION}\n\n<!-- ============ BRAND MATRIX"
        )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print(f"Updated {filepath} with Ecosystem & 3 Verticals")

update_index_file("index.html")
update_index_file("franq-franchise-website.html")
