# -*- coding: utf-8 -*-
import os, shutil, re

# 1. Create assets/videos and copy files with clean names
os.makedirs("assets/videos", exist_ok=True)

video_map = {
    "2235515_Man_Baking_1280x720.mp4": "assets/videos/baking_craft.mp4",
    "6037351_Chef_Cake_1280x720.mp4": "assets/videos/chocolate_craft.mp4",
    "7021015_Making_Cookies_Chocolate_Chip_Cookies_1280x720.mp4": "assets/videos/cookie_prep.mp4",
    "7021017_Donuts_Doughnuts_1280x720.mp4": "assets/videos/dessert_donuts.mp4"
}

for src, dst in video_map.items():
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {src} -> {dst}")

# 2. UPDATE INDEX.HTML HERO BACKGROUND VIDEO TO USE LOCAL ASSETS
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update hero background video to local high-speed file
LOCAL_HERO_VIDEO = """  <!-- Background Ambient Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" id="heroBgVideo" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" webkit-playsinline="true" preload="auto" disablepictureinpicture="true" disableremoteplayback="true" poster="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1600&auto=format&fit=crop&q=80">
      <source src="assets/videos/chocolate_craft.mp4" type="video/mp4">
      <source src="assets/videos/baking_craft.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>"""

html = re.sub(r'<!-- Background Ambient Video Layer -->[\s\S]*?</div>\s*</div>', LOCAL_HERO_VIDEO.strip(), html)

# 3. ADD "BEHIND THE COUNTER: STANDARDIZED CULINARY OPERATIONS" VIDEO SHOWCASE SECTION TO INDEX.HTML
VIDEO_GALLERY_SECTION = """<!-- ============ BEHIND THE COUNTER (VIDEO SHOWCASE) ============ -->
<section class="sec on-dark" id="kitchen-craft" style="background:var(--jamun-deep);position:relative;overflow:hidden">
  <div class="wrap">
    <div class="sec-top rv" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:36px">
      <div class="sec-head wide">
        <p class="eyebrow on-dark"><span class="pulse"></span> Kitchen Operations &amp; Craft</p>
        <h2 style="color:var(--malai)">Behind The Counter: Standardized Culinary Operations</h2>
        <p class="sec-note on-dark">Every flagship brand on Franchise 101 runs on chef-less pre-mixes, proprietary central recipes, and strict quality SOPs.</p>
      </div>
      <a class="btn btn--kesar btn--sm" href="#apply">Visit A Live Outlet &rarr;</a>
    </div>

    <!-- 4-Video Interactive Grid -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(270px, 1fr));gap:22px" class="rv">
      
      <!-- Video 1: Master Chocolate & Dessert Formulations -->
      <div class="video-card" style="background:rgba(255,243,222,0.06);border:1px solid rgba(255,243,222,0.16);border-radius:20px;overflow:hidden;box-shadow:0 15px 35px -10px rgba(0,0,0,0.5)">
        <div style="position:relative;width:100%;aspect-ratio:16/10;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/chocolate_craft.mp4" type="video/mp4">
          </video>
          <span class="tag gold" style="position:absolute;top:12px;left:12px;z-index:2">Chocolate &amp; Cafe Craft</span>
        </div>
        <div style="padding:20px;display:flex;flex-direction:column;gap:8px">
          <h4 style="margin:0;font-size:18px;color:var(--malai)">Proprietary Chocolate Blends</h4>
          <p style="font-size:13.5px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">Supplying &gt;85% of Cad-Bee bases &amp; dessert premixes from centralized Pune manufacturing units.</p>
          <div style="margin-top:8px;font-family:var(--font-mono);font-size:12px;color:var(--pista);font-weight:700">Brands: Beyond Temptation &middot; Cafe Choco Craze</div>
        </div>
      </div>

      <!-- Video 2: Artisanal Baking & Kitchen Craft -->
      <div class="video-card" style="background:rgba(255,243,222,0.06);border:1px solid rgba(255,243,222,0.16);border-radius:20px;overflow:hidden;box-shadow:0 15px 35px -10px rgba(0,0,0,0.5)">
        <div style="position:relative;width:100%;aspect-ratio:16/10;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/baking_craft.mp4" type="video/mp4">
          </video>
          <span class="tag green" style="position:absolute;top:12px;left:12px;z-index:2">Chef-Less Baking SOPs</span>
        </div>
        <div style="padding:20px;display:flex;flex-direction:column;gap:8px">
          <h4 style="margin:0;font-size:18px;color:var(--malai)">Standardized Bread &amp; Sub Prep</h4>
          <p style="font-size:13.5px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">European gourmet breads, paninis, and dough crusts certified for 0% kitchen skill dependency.</p>
          <div style="margin-top:8px;font-family:var(--font-mono);font-size:12px;color:var(--kesar);font-weight:700">Brands: Mr. Sandwich &middot; 200+ Outlets</div>
        </div>
      </div>

      <!-- Video 3: High-Velocity Dough & Patty Preparation -->
      <div class="video-card" style="background:rgba(255,243,222,0.06);border:1px solid rgba(255,243,222,0.16);border-radius:20px;overflow:hidden;box-shadow:0 15px 35px -10px rgba(0,0,0,0.5)">
        <div style="position:relative;width:100%;aspect-ratio:16/10;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/cookie_prep.mp4" type="video/mp4">
          </video>
          <span class="tag" style="position:absolute;top:12px;left:12px;z-index:2">Automated Batter &amp; Pre-mix</span>
        </div>
        <div style="padding:20px;display:flex;flex-direction:column;gap:8px">
          <h4 style="margin:0;font-size:18px;color:var(--malai)">South Indian Automated Batter</h4>
          <p style="font-size:13.5px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">Pre-fermented Thatte Idli batter and Ghee Podi formulations shipped fresh with zero on-site soaking.</p>
          <div style="margin-top:8px;font-family:var(--font-mono);font-size:12px;color:var(--pista);font-weight:700">Brand: South Twist &middot; QSR Express</div>
        </div>
      </div>

      <!-- Video 4: Fresh Glazing & QSR Speed -->
      <div class="video-card" style="background:rgba(255,243,222,0.06);border:1px solid rgba(255,243,222,0.16);border-radius:20px;overflow:hidden;box-shadow:0 15px 35px -10px rgba(0,0,0,0.5)">
        <div style="position:relative;width:100%;aspect-ratio:16/10;background:#000;overflow:hidden">
          <video autoplay muted loop playsinline preload="metadata" style="width:100%;height:100%;object-fit:cover">
            <source src="assets/videos/dessert_donuts.mp4" type="video/mp4">
          </video>
          <span class="tag gold" style="position:absolute;top:12px;left:12px;z-index:2">Dip-In &amp; Glaze Station</span>
        </div>
        <div style="padding:20px;display:flex;flex-direction:column;gap:8px">
          <h4 style="margin:0;font-size:18px;color:var(--malai)">Signature Dip-In &amp; Fast Assembly</h4>
          <p style="font-size:13.5px;color:rgba(255,243,222,0.75);line-height:1.5;margin:0">Warm sauce bath burgers, crispy loaded fries, and sweet treats prepared in under 180 seconds.</p>
          <div style="margin-top:8px;font-family:var(--font-mono);font-size:12px;color:var(--kesar);font-weight:700">Brand: Dunk Burgers &middot; Zero Royalty</div>
        </div>
      </div>

    </div>
  </div>
</section>"""

if 'id="kitchen-craft"' not in html:
    # Insert right after the brands marketplace or after #how
    html = html.replace('<!-- ============ BRANDS MARKETPLACE ============ -->', f"{VIDEO_GALLERY_SECTION}\n\n<!-- ============ BRANDS MARKETPLACE ============ -->")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Integrated local video gallery and hero background in index.html and franq-franchise-website.html")
