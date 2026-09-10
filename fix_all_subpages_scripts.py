# -*- coding: utf-8 -*-
import os, re

STANDARD_SCRIPT = """<script>
const nav = document.getElementById('nav');
const topProgress = document.getElementById('topProgress');
const btnBackToTop = document.getElementById('btnBackToTop');
const navToggle = document.getElementById('navToggle');
const mobileDrawer = document.getElementById('mobileDrawer');

window.addEventListener('scroll', () => {
  const scrolled = window.scrollY;
  const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
  if (topProgress) topProgress.style.width = (maxScroll > 0 ? (scrolled / maxScroll) * 100 : 0) + '%';
  if (btnBackToTop) btnBackToTop.classList.toggle('show', scrolled > 400);
  if (nav) nav.classList.toggle('stuck', scrolled > 20);
});

if (navToggle && mobileDrawer) {
  navToggle.addEventListener('click', () => {
    const isOpen = mobileDrawer.classList.toggle('open');
    navToggle.classList.toggle('open', isOpen);
    navToggle.setAttribute('aria-expanded', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });
}

// Reveal elements on scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.05, rootMargin: '0px 0px 50px' });
document.querySelectorAll('.rv').forEach(el => io.observe(el));

function filterCatalog(category, btn) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  const cards = document.querySelectorAll('.brand-detail-card');
  cards.forEach(card => {
    if (category === 'all' || card.dataset.category === category) {
      card.style.display = 'grid';
      card.classList.add('in');
    } else {
      card.style.display = 'none';
    }
  });
}
</script>"""

# 1. Update franchises.html
with open("franchises.html", "r", encoding="utf-8") as f:
    fr_html = f.read()

fr_html = re.sub(r'<script>[\s\S]*?</script>', STANDARD_SCRIPT, fr_html)
with open("franchises.html", "w", encoding="utf-8") as f:
    f.write(fr_html)
print("Updated franchises.html script with IntersectionObserver & working filter")

# 2. Check and add IntersectionObserver to other pages if missing
other_pages = ["develop-brand.html", "develop-scale.html", "franchise-marketing.html", "find-franchise.html", "book-consultation.html", "about.html"]
for p in other_pages:
    if not os.path.exists(p): continue
    with open(p, "r", encoding="utf-8") as f:
        txt = f.read()
    
    if "IntersectionObserver" not in txt:
        # Add observer to script
        observer_snippet = """
// Reveal elements on scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.05, rootMargin: '0px 0px 50px' });
document.querySelectorAll('.rv').forEach(el => io.observe(el));
"""
        txt = txt.replace("</script>", f"{observer_snippet}\n</script>")
        with open(p, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"Added IntersectionObserver to {p}")
    else:
        print(f"IntersectionObserver already present in {p}")
