# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add CSS for Hero Donut Background Video
HERO_CSS_BLOCK = """/* ============ HERO BACKGROUND VIDEO ============ */
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
  opacity: 0.78;
  display: block;
  filter: brightness(0.85) contrast(1.1);
  transition: opacity 1s ease;
}
.hero-video-overlay {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: radial-gradient(circle at 50% 30%, rgba(37, 16, 60, 0.45) 0%, rgba(24, 8, 37, 0.72) 65%, rgba(24, 8, 37, 0.92) 100%);
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

html = html.replace("""/* ============ HERO ============ */
.hero{
  position:relative;background:var(--jamun);color:var(--malai);
  padding:clamp(110px,14vh,152px) 0 0;overflow:clip;
  border-radius:0 0 clamp(24px,4vw,44px) clamp(24px,4vw,44px);
}
.hero::before{
  content:"";position:absolute;inset:0;
  background:radial-gradient(58% 46% at 50% 2%,rgba(255,176,32,.24),transparent 68%);
  pointer-events:none;
}""", HERO_CSS_BLOCK)

# 2. Add text-shadow for crisp legibility over donut video
html = html.replace(
    ".hero h1{color:var(--malai);max-width:14ch;}",
    ".hero h1{color:var(--malai);max-width:14ch;text-shadow:0 4px 24px rgba(0,0,0,0.85), 0 2px 8px rgba(0,0,0,0.95);}"
)
html = html.replace(
    ".hero-sub{max-width:54ch;color:rgba(255,243,222,.94);font-size:clamp(16px,1.6vw,19px)}",
    ".hero-sub{max-width:54ch;color:rgba(255,243,222,.95);font-size:clamp(16px,1.6vw,19px);text-shadow:0 2px 14px rgba(0,0,0,0.9);}"
)

# 3. Add Donut Video markup inside <header class="hero on-dark" id="top">
OLD_HERO_HEADER = '<header class="hero on-dark" id="top">\n  <div class="wrap hero-grid">'
NEW_HERO_HEADER = """<header class="hero on-dark" id="top">
  <!-- Background Donut Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" id="heroBgVideo" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" webkit-playsinline="true" preload="auto" disablepictureinpicture="true" disableremoteplayback="true" poster="assets/brands/beyond_temptation_food.png">
      <source src="assets/videos/dessert_donuts.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>

  <div class="wrap hero-grid">"""

html = html.replace(OLD_HERO_HEADER, NEW_HERO_HEADER)

# 4. Add Autoplay Script
AUTOPLAY_JS = """
// ============ GUARANTEED AUTOPLAY KICKOFF ============
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

    playVid();
    document.addEventListener('DOMContentLoaded', playVid);
    window.addEventListener('load', playVid);
    window.addEventListener('pageshow', playVid);

    ['touchstart', 'scroll', 'mousemove', 'click', 'keydown'].forEach(function(evt) {
      window.addEventListener(evt, playVid, { once: true, passive: true });
    });
  }
})();
"""

if "// ============ GUARANTEED AUTOPLAY KICKOFF ============" not in html:
    html = html.replace("</script>\n</body>", f"{AUTOPLAY_JS}\n</script>\n</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Applied donut background video to hero section in index.html & franq-franchise-website.html")
