# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Hero Video CSS in index.html
OLD_HERO_CSS = """/* ============ HERO BACKGROUND VIDEO ============ */
.hero-video-wrap {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}
.hero-bg-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.78;
  filter: brightness(0.85) contrast(1.1) saturate(1.2);
  transition: opacity 1.2s ease;
}
.hero-video-overlay {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 30%, rgba(37, 16, 60, 0.35) 0%, rgba(24, 8, 37, 0.6) 60%, rgba(24, 8, 37, 0.85) 100%);
}
.hero-video-overlay::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(24, 8, 37, 0.2) 0%, transparent 35%, rgba(24, 8, 37, 0.88) 100%);
}

/* ============ HERO ============ */
.hero{
  position:relative;background:var(--jamun);color:var(--malai);
  padding:clamp(110px,14vh,152px) 0 0;overflow:clip;
  border-radius:0 0 clamp(24px,4vw,44px) clamp(24px,4vw,44px);
}
.hero::before{
  content:"";position:absolute;inset:0;
  background:radial-gradient(58% 46% at 50% 2%,rgba(255,176,32,.24),transparent 68%);
  pointer-events:none;
}"""

NEW_HERO_CSS = """/* ============ HERO BACKGROUND VIDEO ============ */
.hero-video-wrap {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
  z-index: 1;
}
.hero-bg-video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 1 !important;
  display: block !important;
  filter: brightness(0.88) contrast(1.08) saturate(1.15);
}
.hero-video-overlay {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: rgba(24, 8, 37, 0.48);
  pointer-events: none;
}

/* ============ HERO ============ */
.hero{
  position:relative;background:#180825;color:var(--malai);
  padding:clamp(110px,14vh,152px) 0 0;overflow:clip;
  border-radius:0 0 clamp(24px,4vw,44px) clamp(24px,4vw,44px);
}
.hero::before{
  display: none !important;
}"""

html = html.replace(OLD_HERO_CSS, NEW_HERO_CSS)

# 2. Make sure .hero-grid has z-index: 10
html = html.replace(
    ".hero-grid{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px}",
    ".hero-grid{position:relative;z-index:10;display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px}"
)

# 3. Update Video Tag in HTML to put fastest loading video first with cross-browser attributes
OLD_VID_TAG = """  <!-- Background Ambient Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" id="heroBgVideo" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" webkit-playsinline="true" preload="auto" disablepictureinpicture="true" disableremoteplayback="true" poster="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1600&auto=format&fit=crop&q=80">
      <source src="assets/videos/chocolate_craft.mp4" type="video/mp4">
      <source src="assets/videos/baking_craft.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>"""

NEW_VID_TAG = """  <!-- Background Ambient Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" id="heroBgVideo" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" webkit-playsinline="true" preload="auto" disablepictureinpicture="true" disableremoteplayback="true" poster="assets/brands/beyond_temptation_food.png">
      <source src="assets/videos/dessert_donuts.mp4" type="video/mp4">
      <source src="assets/videos/chocolate_craft.mp4" type="video/mp4">
      <source src="assets/videos/baking_craft.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>"""

html = html.replace(OLD_VID_TAG, NEW_VID_TAG)

# 4. Update Guaranteed Autoplay script to force inline playback
OLD_AUTOPLAY = """// ============ GUARANTEED AUTOPLAY KICKOFF ============
(function() {
  const bgVid = document.getElementById('heroBgVideo');
  if (bgVid) {
    bgVid.muted = true;
    bgVid.defaultMuted = true;
    
    const playVid = function() {
      const p = bgVid.play();
      if (p !== undefined) {
        p.catch(function() {
          // Autoplay policy prevented, will play on user scroll or touch
        });
      }
    };

    // Try immediately on DOM load
    playVid();
    
    // Also try on window load
    window.addEventListener('load', playVid);

    // Fallback trigger on first user gesture
    ['touchstart', 'scroll', 'mousemove', 'click'].forEach(function(evt) {
      window.addEventListener(evt, playVid, { once: true, passive: true });
    });
  }
})();"""

NEW_AUTOPLAY = """// ============ GUARANTEED AUTOPLAY KICKOFF ============
(function() {
  const bgVid = document.getElementById('heroBgVideo');
  if (bgVid) {
    bgVid.muted = true;
    bgVid.defaultMuted = true;
    bgVid.volume = 0;
    
    const playVid = function() {
      if (bgVid.paused) {
        bgVid.play().catch(function() {});
      }
    };

    // Try immediately
    playVid();
    document.addEventListener('DOMContentLoaded', playVid);
    window.addEventListener('load', playVid);
    window.addEventListener('pageshow', playVid);

    // Trigger on any interaction
    ['touchstart', 'scroll', 'mousemove', 'click', 'keydown'].forEach(function(evt) {
      window.addEventListener(evt, playVid, { once: true, passive: true });
    });
  }
})();"""

html = html.replace(OLD_AUTOPLAY, NEW_AUTOPLAY)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Applied 100% visible video styling and forced autoplay in index.html & franq-franchise-website.html")
