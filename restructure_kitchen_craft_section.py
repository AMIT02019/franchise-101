# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# New 2x2 Balanced Split Card Structure
NEW_KITCHEN_SECTION = """<!-- ============ BEHIND THE COUNTER (VIDEO SHOWCASE) ============ -->
<section class="sec on-dark" id="kitchen-craft" style="background:var(--jamun-deep);position:relative;overflow:hidden">
  <div class="wrap">
    <div class="sec-top rv" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:40px">
      <div class="sec-head wide">
        <p class="eyebrow on-dark"><span class="pulse"></span> Standardized Operations</p>
        <h2 style="color:var(--malai)">Behind The Counter: Central Kitchen &amp; Supply SOPs</h2>
        <p class="sec-note on-dark">Every flagship brand on Franchise 101 eliminates skilled-chef dependency with automated premixes, central manufacturing, and fast SOPs.</p>
      </div>
      <a class="btn btn--kesar btn--sm" href="#apply">Visit A Live Outlet &rarr;</a>
    </div>

    <!-- 2x2 Balanced Split-Card Grid -->
    <div class="craft-grid-2x2 rv" style="display:grid;grid-template-columns:repeat(2, 1fr);gap:24px">
      
      <!-- Card 1: Beyond Temptation & Cafe Choco Craze -->
      <div class="craft-card" style="background:rgba(255,243,222,0.05);border:1px solid rgba(255,243,222,0.14);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 18px 40px -15px rgba(0,0,0,0.5);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/chocolate_craft.mp4" type="video/mp4">
          </video>
          <span class="tag gold" style="position:absolute;top:12px;left:12px;z-index:2">Chocolate &amp; Cafe Craft</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--malai)">Proprietary Chocolate Bases</h4>
            <p style="font-size:13px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">Over 85% of Cad-Bee bases &amp; dessert pre-mixes are manufactured centrally in Pune with 0% kitchen waste.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--pista);font-weight:700;margin-bottom:8px">&bull; Beyond Temptation &middot; Cafe Choco Craze</div>
            <a href="beyond-temptation.html" style="font-size:13px;color:var(--kesar);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Card 2: Mr. Sandwich -->
      <div class="craft-card" style="background:rgba(255,243,222,0.05);border:1px solid rgba(255,243,222,0.14);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 18px 40px -15px rgba(0,0,0,0.5);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/baking_craft.mp4" type="video/mp4">
          </video>
          <span class="tag green" style="position:absolute;top:12px;left:12px;z-index:2">Chef-Less Baking</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--malai)">Standardized Bread &amp; Subs</h4>
            <p style="font-size:13px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">European subs, paninis, and dough recipes certified for 0% chef skill dependency and fast 4-min dispatch.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--kesar);font-weight:700;margin-bottom:8px">&bull; Mr. Sandwich &middot; 200+ Outlets</div>
            <a href="mr-sandwich.html" style="font-size:13px;color:var(--kesar);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Card 3: South Twist -->
      <div class="craft-card" style="background:rgba(255,243,222,0.05);border:1px solid rgba(255,243,222,0.14);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 18px 40px -15px rgba(0,0,0,0.5);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/cookie_prep.mp4" type="video/mp4">
          </video>
          <span class="tag" style="position:absolute;top:12px;left:12px;z-index:2">Automated Batter</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--malai)">Thatte Idli Pre-Fermented Batter</h4>
            <p style="font-size:13px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">Pre-fermented Thatte Idli batter and Ghee Podi formulations shipped fresh with zero on-site grinding.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--pista);font-weight:700;margin-bottom:8px">&bull; South Twist &middot; QSR Express</div>
            <a href="south-twist.html" style="font-size:13px;color:var(--kesar);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Card 4: Dunk Burgers -->
      <div class="craft-card" style="background:rgba(255,243,222,0.05);border:1px solid rgba(255,243,222,0.14);border-radius:22px;overflow:hidden;display:grid;grid-template-columns:1.05fr 1fr;box-shadow:0 18px 40px -15px rgba(0,0,0,0.5);transition:all 0.3s ease">
        <div style="position:relative;height:100%;min-height:220px;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/dessert_donuts.mp4" type="video/mp4">
          </video>
          <span class="tag gold" style="position:absolute;top:12px;left:12px;z-index:2">Dip-In &amp; Glaze Station</span>
        </div>
        <div style="padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px">
          <div>
            <h4 style="margin:0 0 6px;font-size:18px;color:var(--malai)">Signature Dip-In &amp; Fast Assembly</h4>
            <p style="font-size:13px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">Warm sauce bath burgers, crispy loaded sides, and dessert items prepared in under 180 seconds.</p>
          </div>
          <div>
            <div style="font-family:var(--font-mono);font-size:11.5px;color:var(--kesar);font-weight:700;margin-bottom:8px">&bull; Dunk Burgers &middot; Zero Royalty</div>
            <a href="dunk-burgers.html" style="font-size:13px;color:var(--kesar);font-weight:700;display:inline-flex;align-items:center;gap:4px">View Brand Model &rarr;</a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>"""

# Replace existing kitchen-craft section
html = re.sub(r'<!-- ============ BEHIND THE COUNTER \(VIDEO SHOWCASE\) ============ -->[\s\S]*?<!-- ============ BRANDS MARKETPLACE ============ -->', f"{NEW_KITCHEN_SECTION}\n\n<!-- ============ BRANDS MARKETPLACE ============ -->", html)

# Add media query for craft-grid-2x2 responsive behavior
CRAFT_CSS = """
@media (max-width: 960px) {
  .craft-grid-2x2 { grid-template-columns: 1fr !important; }
}
@media (max-width: 580px) {
  .craft-card { grid-template-columns: 1fr !important; }
}
"""

if ".craft-grid-2x2" not in html:
    html = html.replace("</style>", f"{CRAFT_CSS}\n</style>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated #kitchen-craft section to a balanced 2x2 split-card layout with direct brand links!")
