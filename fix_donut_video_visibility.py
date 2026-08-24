# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Video CSS with the rock-solid production standard
OLD_VIDEO_CSS = """/* ============ HERO BACKGROUND VIDEO ============ */
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
}"""

NEW_VIDEO_CSS = """/* ============ HERO BACKGROUND VIDEO ============ */
.hero-video-wrap {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}
.hero-bg-video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  transform: translate(-50%, -50%);
  object-fit: cover;
  opacity: 0.88 !important;
  display: block !important;
  filter: brightness(0.9) contrast(1.1);
  transition: opacity 0.5s ease;
}
.hero-video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  background: radial-gradient(circle at 50% 35%, rgba(37, 16, 60, 0.38) 0%, rgba(24, 8, 37, 0.65) 65%, rgba(24, 8, 37, 0.9) 100%);
  pointer-events: none;
}

/* ============ HERO ============ */
.hero{
  position:relative;background:#180825;color:var(--malai);
  padding:clamp(110px,14vh,152px) 0 0;overflow:hidden;
  border-radius:0 0 clamp(24px,4vw,44px) clamp(24px,4vw,44px);
}"""

html = html.replace(OLD_VIDEO_CSS, NEW_VIDEO_CSS)

# 2. Update Video Tag with multiple fallback sources and forced attributes
OLD_VID_TAG = """  <!-- Background Donut Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" id="heroBgVideo" autoplay="autoplay" muted="muted" loop="loop" playsinline="playsinline" webkit-playsinline="true" preload="auto" disablepictureinpicture="true" disableremoteplayback="true" poster="assets/brands/beyond_temptation_food.png">
      <source src="assets/videos/dessert_donuts.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>"""

NEW_VID_TAG = """  <!-- Background Donut Video Layer -->
  <div class="hero-video-wrap" aria-hidden="true">
    <video class="hero-bg-video" id="heroBgVideo" autoplay muted loop playsinline webkit-playsinline="true" preload="auto" poster="assets/brands/beyond_temptation_food.png">
      <source src="assets/videos/dessert_donuts.mp4" type="video/mp4">
      <source src="7021017_Donuts_Doughnuts_1280x720.mp4" type="video/mp4">
    </video>
    <div class="hero-video-overlay"></div>
  </div>"""

html = html.replace(OLD_VID_TAG, NEW_VID_TAG)

# 3. Update Autoplay Script to ensure immediate playback and unpause
OLD_AUTOPLAY = """// ============ GUARANTEED AUTOPLAY KICKOFF ============
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
})();"""

NEW_AUTOPLAY = """// ============ GUARANTEED AUTOPLAY KICKOFF ============
(function() {
  const bgVid = document.getElementById('heroBgVideo');
  if (bgVid) {
    bgVid.muted = true;
    bgVid.defaultMuted = true;
    bgVid.volume = 0;
    bgVid.setAttribute('muted', '');
    bgVid.setAttribute('playsinline', '');
    bgVid.setAttribute('autoplay', '');
    
    const tryPlay = function() {
      const p = bgVid.play();
      if (p !== undefined) {
        p.catch(function() {
          // Retry on user interaction
        });
      }
    };

    tryPlay();
    document.addEventListener('DOMContentLoaded', tryPlay);
    window.addEventListener('load', tryPlay);
    window.addEventListener('pageshow', tryPlay);

    ['touchstart', 'scroll', 'mousemove', 'click', 'keydown', 'wheel'].forEach(function(evt) {
      window.addEventListener(evt, tryPlay, { once: true, passive: true });
    });
  }
})();"""

html = html.replace(OLD_AUTOPLAY, NEW_AUTOPLAY)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("franq-franchise-website.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Applied rock-solid positioning, overflow fix, and fallback sources for donut hero video!")
