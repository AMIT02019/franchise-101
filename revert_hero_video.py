# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove Hero Video CSS and restore original .hero and .hero::before styles
HERO_CSS_TO_REMOVE = """/* ============ HERO BACKGROUND VIDEO ============ */
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
  opacity: 0.55 !important;
  display: block !important;
  filter: brightness(0.7) contrast(1.15) saturate(1.1);
}
.hero-video-overlay {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: radial-gradient(circle at 50% 30%, rgba(37, 16, 60, 0.6) 0%, rgba(24, 8, 37, 0.85) 65%, rgba(24, 8, 37, 0.96) 100%);
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

ORIGINAL_HERO_CSS = """/* ============ HERO ============ */
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

html = html.replace(HERO_CSS_TO_REMOVE, ORIGINAL_HERO_CSS)

# 2. Remove the Video Tag from HTML
HERO_MARKUP_WITH_VIDEO = """<!-- ============ HERO ============ -->
<header class="hero on-dark" id="top">
  <!-- Background Ambient Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" id="heroBgVideo" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" webkit-playsinline="true" preload="auto" disablepictureinpicture="true" disableremoteplayback="true" poster="assets/brands/beyond_temptation_food.png">
      <source src="assets/videos/chocolate_craft.mp4" type="video/mp4">
      <source src="assets/videos/baking_craft.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>

  <div class="wrap hero-grid">"""

CLEAN_HERO_MARKUP = """<!-- ============ HERO ============ -->
<header class="hero on-dark" id="top">
  <div class="wrap hero-grid">"""

html = html.replace(HERO_MARKUP_WITH_VIDEO, CLEAN_HERO_MARKUP)

# 3. Remove Background Video Autoplay script from bottom
AUTOPLAY_SCRIPT = """// ============ GUARANTEED AUTOPLAY KICKOFF ============
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

html = html.replace(AUTOPLAY_SCRIPT, "")

# 4. Clean text shadows
html = html.replace("text-shadow:0 4px 24px rgba(0,0,0,0.8), 0 2px 10px rgba(0,0,0,0.9)", "")
html = html.replace(";text-shadow:0 2px 16px rgba(0,0,0,0.85)", "")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Reverted hero video changes: clean original Royal Jamun aesthetic restored!")
