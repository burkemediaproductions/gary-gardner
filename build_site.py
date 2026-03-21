from pathlib import Path

root = Path('/mnt/data/gardner-site')
css = r'''
:root {
  --purple: #852d97;
  --purple-dark: #682173;
  --purple-ink: #5c1f69;
  --blue: #17a9e1;
  --blue-deep: #0d8fc0;
  --ink: #2f2f35;
  --muted: #62646d;
  --bg: #f7f7f9;
  --white: #ffffff;
  --sand: #efe6d6;
  --shadow: 0 14px 36px rgba(18, 24, 40, 0.14);
  --radius: 22px;
  --radius-sm: 14px;
  --container: 1180px;
  --display: "Barlow Condensed", "Arial Narrow", Arial, sans-serif;
  --body: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: var(--body);
  color: var(--ink);
  background: var(--bg);
  line-height: 1.6;
}
a { color: var(--blue-deep); text-decoration-thickness: 2px; text-underline-offset: 3px; }
a:hover { color: var(--purple); }
img { max-width: 100%; display: block; }
iframe { width: 100%; border: 0; }
button, input, textarea { font: inherit; }
.skip-link {
  position: absolute; left: 1rem; top: -3rem;
  background: var(--purple); color: #fff; padding: .8rem 1rem; z-index: 1000;
  border-radius: 999px; text-decoration: none; font-weight: 700;
}
.skip-link:focus { top: 1rem; }
.site-header {
  position: sticky; top: 0; z-index: 90;
  background: rgba(255,255,255,.96); backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0,0,0,.06);
}
.header-inner {
  max-width: var(--container); margin: 0 auto; padding: .9rem 1rem;
  display: flex; align-items: center; justify-content: space-between; gap: 1rem;
}
.brand {
  display: inline-flex; align-items: center; gap: .95rem; text-decoration: none;
  color: var(--ink);
}
.brand-mark {
  width: 70px; height: 70px; border-radius: 50%;
  background: linear-gradient(145deg, var(--blue), var(--purple));
  display: grid; place-items: center; color: #fff; font-weight: 900; font-size: 1.75rem;
  box-shadow: var(--shadow);
}
.brand-text { display: grid; line-height: 1; }
.brand-kicker {
  font-family: var(--display); font-size: 1.05rem; letter-spacing: .04em; color: var(--purple);
  text-transform: uppercase; font-weight: 700;
}
.brand-title {
  font-family: var(--display); text-transform: uppercase; font-weight: 800;
  font-size: clamp(1.9rem, 3vw, 2.7rem); color: var(--blue-deep); letter-spacing: .03em;
}
.brand-sub {
  font-family: var(--display); text-transform: uppercase; font-size: 1.12rem;
  color: var(--purple); font-weight: 800; letter-spacing: .04em;
}
.header-right { display: flex; align-items: center; gap: .75rem; }
.social-links, .footer-social { display: flex; align-items: center; gap: .65rem; }
.social-link {
  width: 2.7rem; height: 2.7rem; border-radius: 50%; display: grid; place-items: center;
  color: var(--blue-deep); background: rgba(23,169,225,.08); text-decoration: none;
  transition: transform .2s ease, background .2s ease, color .2s ease;
}
.social-link:hover, .social-link:focus-visible { transform: translateY(-2px); background: rgba(133,45,151,.12); color: var(--purple); }
.social-link svg { width: 1.3rem; height: 1.3rem; }
.menu-button {
  border: 0; background: var(--purple); color: #fff; width: 3.5rem; height: 3.5rem;
  border-radius: 18px; display: grid; place-items: center; cursor: pointer; box-shadow: var(--shadow);
}
.menu-button svg { width: 1.7rem; height: 1.7rem; }
.primary-nav {
  position: fixed; inset: 0 0 0 auto; width: min(92vw, 420px); background: linear-gradient(180deg, var(--purple), var(--purple-dark));
  color: #fff; transform: translateX(104%); transition: transform .28s ease; z-index: 120;
  padding: 1rem; box-shadow: -10px 0 30px rgba(0,0,0,.25);
}
.primary-nav.open { transform: translateX(0); }
.nav-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.2rem; }
.nav-title {
  font-family: var(--display); text-transform: uppercase; letter-spacing: .05em; font-size: 2rem; margin: 0;
}
.nav-close { background: rgba(255,255,255,.12); color: #fff; border: 0; width: 3rem; height: 3rem; border-radius: 14px; cursor: pointer; }
.nav-list, .nav-sublist { list-style: none; padding: 0; margin: 0; }
.nav-list > li + li { margin-top: .35rem; }
.nav-list a {
  display: block; color: #fff; text-decoration: none; padding: .95rem 1rem; border-radius: 16px;
  font-weight: 700; letter-spacing: .01em; background: rgba(255,255,255,.04);
}
.nav-list a[aria-current="page"], .nav-list a:hover, .nav-list a:focus-visible { background: rgba(255,255,255,.16); }
.nav-group > span {
  display: block; padding: .95rem 1rem .55rem; font-family: var(--display); letter-spacing: .05em; text-transform: uppercase;
  color: rgba(255,255,255,.82); font-size: 1.1rem;
}
.nav-sublist a { margin-left: .7rem; background: transparent; }
.nav-backdrop {
  position: fixed; inset: 0; background: rgba(16, 16, 24, .55); z-index: 110;
  opacity: 0; visibility: hidden; transition: opacity .25s ease;
}
.nav-backdrop.open { opacity: 1; visibility: visible; }
main { display: block; }
.container {
  width: min(100% - 2rem, var(--container)); margin: 0 auto;
}
.hero {
  position: relative; min-height: clamp(440px, 74vh, 780px); color: #fff; overflow: clip;
  display: grid; align-items: end; background: linear-gradient(180deg, rgba(8,12,24,.12), rgba(8,12,24,.72));
}
.hero::before {
  content: ""; position: absolute; inset: 0; background: linear-gradient(135deg, rgba(23,169,225,.35), rgba(133,45,151,.48)); pointer-events: none;
}
.hero--video {
  background:
    radial-gradient(circle at 22% 24%, rgba(255,255,255,.18), transparent 24%),
    linear-gradient(180deg, rgba(8,12,24,.22), rgba(8,12,24,.66)),
    linear-gradient(135deg, #1a7cbf 0%, #7b2f96 55%, #31153f 100%);
}
.hero-media-placeholder,
.inline-image-placeholder {
  position: absolute; inset: 0; display: grid; place-items: center; text-align: center; color: rgba(255,255,255,.92);
}
.hero-media-placeholder .label,
.inline-image-placeholder .label {
  border: 2px solid rgba(255,255,255,.7); border-radius: 999px; padding: .8rem 1.1rem;
  font-family: var(--display); letter-spacing: .06em; text-transform: uppercase; background: rgba(0,0,0,.18);
}
.hero--image {
  background:
    linear-gradient(180deg, rgba(8,12,24,.18), rgba(8,12,24,.58)),
    linear-gradient(120deg, #c8e8f8 0%, #f7f7f9 50%, #e1b86b 100%);
}
.hero--blue { background: linear-gradient(180deg, rgba(6,71,103,.20), rgba(6,71,103,.2)), linear-gradient(135deg, #11a6dd, #0c7ead); }
.hero--cityhall { background: linear-gradient(180deg, rgba(8,12,24,.18), rgba(8,12,24,.52)), linear-gradient(120deg, #eed6a1, #caa866 58%, #9b7a43); }
.hero-content { position: relative; z-index: 1; width: min(100% - 2rem, var(--container)); margin: 0 auto; padding: 8rem 0 4rem; }
.hero-title {
  margin: 0; font-family: var(--display); text-transform: uppercase; line-height: .95; letter-spacing: .03em;
  font-size: clamp(3.1rem, 9vw, 7rem); text-shadow: 0 8px 28px rgba(0,0,0,.28);
}
.hero-subtitle {
  margin: 1rem 0 0; max-width: 48rem; font-size: clamp(1.1rem, 2vw, 1.35rem); color: rgba(255,255,255,.95);
}
.hero-actions { display: flex; flex-wrap: wrap; gap: .9rem; margin-top: 1.35rem; }
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: .7rem;
  min-height: 3.25rem; padding: .85rem 1.2rem; border-radius: 16px; border: 2px solid transparent;
  text-decoration: none; font-weight: 800; cursor: pointer; transition: transform .2s ease, box-shadow .2s ease, background .2s ease;
}
.btn:hover, .btn:focus-visible { transform: translateY(-2px); box-shadow: var(--shadow); }
.btn--primary { background: var(--purple); color: #fff; }
.btn--secondary { background: rgba(255,255,255,.12); color: #fff; border-color: rgba(255,255,255,.3); }
.btn--blue { background: var(--blue-deep); color: #fff; }
.btn svg { width: 1.1rem; height: 1.1rem; }
.section { padding: 4rem 0; position: relative; }
.section--tight { padding: 3rem 0; }
.section--white { background: #fff; }
.section--blue { background: var(--blue); color: #fff; }
.section--purple { background: var(--purple); color: #fff; }
.section-heading {
  font-family: var(--display); text-transform: uppercase; letter-spacing: .04em; line-height: .98;
  font-size: clamp(2.2rem, 5vw, 4.5rem); margin: 0 0 1rem;
}
.section-heading--purple { color: var(--purple); }
.lead {
  font-size: clamp(1.15rem, 2vw, 1.4rem); color: var(--muted); max-width: 60rem;
}
.copy p { font-size: clamp(1.08rem, 1.6vw, 1.34rem); color: var(--muted); margin: 0 0 1.25rem; }
.grid-2 {
  display: grid; gap: 2rem; align-items: center; grid-template-columns: 1.12fr .88fr;
}
.card {
  background: #fff; border-radius: var(--radius); box-shadow: var(--shadow); overflow: hidden;
}
.inline-image-placeholder {
  position: relative; min-height: 340px; border-radius: var(--radius); box-shadow: var(--shadow);
  background: linear-gradient(135deg, rgba(23,169,225,.6), rgba(133,45,151,.75));
}
.inline-image-placeholder.circle { border-radius: 50%; aspect-ratio: 1 / 1; min-height: 0; width: min(100%, 540px); margin: 0 auto; }
.bullets { list-style: none; margin: 1.5rem 0 0; padding: 0; display: grid; gap: 1.15rem; }
.bullets li {
  position: relative; padding-left: 2.2rem; color: var(--muted); font-size: clamp(1.05rem, 1.5vw, 1.28rem);
}
.bullets li::before {
  content: ""; position: absolute; left: 0; top: .52rem; width: .88rem; height: .88rem; background: var(--blue);
  transform: rotate(45deg); border-radius: 2px;
}
.supporters-list { display: grid; gap: 1rem; margin-top: 2rem; }
.supporter { border-left: 6px solid var(--purple); padding-left: 1rem; }
.supporter-name {
  margin: 0; font-family: var(--display); text-transform: uppercase; color: var(--purple); letter-spacing: .03em;
  font-size: clamp(1.5rem, 3vw, 2.25rem);
}
.supporter-role { margin: 0; color: var(--muted); font-size: clamp(1.05rem, 1.6vw, 1.3rem); }
.cta-panel {
  margin-top: 2rem; padding: 1.6rem; background: linear-gradient(135deg, rgba(133,45,151,.08), rgba(23,169,225,.1));
  border-radius: var(--radius); border: 1px solid rgba(0,0,0,.05);
}
.form-card {
  background: #fff; border-radius: var(--radius); box-shadow: var(--shadow); padding: 1.25rem;
}
.form-grid { display: grid; gap: 1rem; grid-template-columns: 1fr 1fr; }
.form-field { display: grid; gap: .45rem; }
.form-field--full { grid-column: 1 / -1; }
label { font-weight: 800; color: var(--ink); }
input, textarea {
  width: 100%; padding: .92rem 1rem; border-radius: 14px; border: 1px solid #d6d9e1; background: #fff;
}
textarea { min-height: 180px; resize: vertical; }
input:focus, textarea:focus, .menu-button:focus-visible, .btn:focus-visible, .nav-close:focus-visible {
  outline: 3px solid rgba(23,169,225,.35); outline-offset: 2px;
}
.contact-list { display: grid; gap: 1rem; margin-top: 1.5rem; }
.contact-item {
  display: flex; align-items: center; gap: .85rem; text-decoration: none; color: var(--blue-deep); font-size: clamp(1rem, 1.5vw, 1.18rem);
}
.contact-item svg { width: 1.5rem; height: 1.5rem; flex: 0 0 auto; }
.video-grid {
  display: grid; gap: 1.25rem; grid-template-columns: repeat(2, minmax(0, 1fr));
}
.video-card, .gallery-card {
  background: rgba(255,255,255,.14); border-radius: var(--radius-sm); overflow: hidden; box-shadow: var(--shadow);
}
.video-card h3, .archive-card h3 {
  margin: 0; padding: 1rem 1rem 0; font-size: 1.2rem; line-height: 1.2;
}
.video-frame { aspect-ratio: 16 / 9; background: rgba(255,255,255,.08); }
.video-copy { padding: 0 1rem 1rem; font-size: .98rem; color: rgba(255,255,255,.92); }
.gallery-grid {
  display: grid; gap: 1rem; grid-template-columns: repeat(3, minmax(0, 1fr)); margin-top: 1.5rem;
}
.gallery-grid img { aspect-ratio: 1 / 1; object-fit: cover; width: 100%; }
.archive-grid { display: grid; gap: 1.3rem; }
.resources-list { list-style: none; padding: 0; margin: 1.4rem 0 0; display: grid; gap: .9rem; }
.resources-list li { padding-left: 2rem; position: relative; }
.resources-list li::before {
  content: ""; position: absolute; left: 0; top: .55rem; width: .9rem; height: .9rem; background: var(--blue); transform: rotate(45deg); border-radius: 2px;
}
.resources-list a { font-size: clamp(1.08rem, 1.6vw, 1.3rem); }
.site-footer {
  background: var(--purple); color: #fff; padding: 2rem 0;
}
.footer-inner {
  width: min(100% - 2rem, var(--container)); margin: 0 auto; display: grid; gap: 1rem;
}
.footer-meta { color: rgba(255,255,255,.94); }
.footer-meta p { margin: .25rem 0; }
.footer-note { font-size: .96rem; }
.footer-links a { color: #fff; }
.mountain-divider,
.slash-divider { position: relative; height: 110px; overflow: hidden; }
.mountain-divider::before,
.mountain-divider::after {
  content: ""; position: absolute; bottom: 0; background: var(--blue);
}
.mountain-divider::before {
  left: -5%; width: 58%; height: 100%; clip-path: polygon(0 100%, 18% 62%, 34% 78%, 50% 34%, 66% 74%, 84% 44%, 100% 100%);
}
.mountain-divider::after {
  right: -4%; width: 55%; height: 86%; clip-path: polygon(0 100%, 15% 56%, 37% 80%, 53% 42%, 68% 76%, 86% 58%, 100% 100%);
  background: #0f98cd;
}
.slash-divider::before {
  content: ""; position: absolute; inset: 0; background: linear-gradient(171deg, var(--blue) 0 47%, #fff 48% 100%);
}
.hero-chevron {
  position: absolute; inset-inline: 0; bottom: 1rem; display: flex; justify-content: center; z-index: 2;
}
.hero-chevron a {
  color: #fff; width: 3rem; height: 3rem; border-radius: 999px; background: rgba(255,255,255,.14);
  display: grid; place-items: center; text-decoration: none;
}
.hero-chevron svg { width: 1.2rem; height: 1.2rem; }
.sr-only {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden;
  clip: rect(0,0,0,0); white-space: nowrap; border: 0;
}
@media (max-width: 960px) {
  .grid-2, .video-grid, .gallery-grid { grid-template-columns: 1fr; }
  .gallery-grid img { aspect-ratio: 4 / 3; }
}
@media (max-width: 760px) {
  .header-inner { align-items: flex-start; }
  .brand-mark { width: 56px; height: 56px; font-size: 1.4rem; }
  .brand-title { font-size: 1.75rem; }
  .brand-sub { font-size: .98rem; }
  .header-right { gap: .45rem; }
  .social-links { gap: .4rem; }
  .social-link { width: 2.35rem; height: 2.35rem; }
  .menu-button { width: 3.15rem; height: 3.15rem; border-radius: 14px; }
  .hero-content { padding-top: 6rem; }
  .hero-actions { flex-direction: column; align-items: stretch; }
  .btn { width: 100%; }
  .form-grid { grid-template-columns: 1fr; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
'''

js = r'''
(() => {
  const menuButton = document.querySelector('[data-menu-button]');
  const nav = document.querySelector('[data-nav]');
  const backdrop = document.querySelector('[data-nav-backdrop]');
  const closeButton = document.querySelector('[data-nav-close]');

  const closeMenu = () => {
    if (!nav) return;
    nav.classList.remove('open');
    backdrop?.classList.remove('open');
    menuButton?.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  };

  const openMenu = () => {
    if (!nav) return;
    nav.classList.add('open');
    backdrop?.classList.add('open');
    menuButton?.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  };

  menuButton?.addEventListener('click', () => {
    const isOpen = nav?.classList.contains('open');
    isOpen ? closeMenu() : openMenu();
  });

  closeButton?.addEventListener('click', closeMenu);
  backdrop?.addEventListener('click', closeMenu);

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeMenu();
  });

  nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
})();
'''

icons = {
    'facebook': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 8.5V6.8c0-.8.4-1.3 1.4-1.3H17V2.2c-.4-.1-1.7-.2-3.2-.2-3.2 0-5.3 1.9-5.3 5.5v2H5v3.8h3.5V22h4V13.3h3.3l.5-3.8h-3.8Z"/></svg>',
    'instagram': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M7.2 2h9.6A5.2 5.2 0 0 1 22 7.2v9.6a5.2 5.2 0 0 1-5.2 5.2H7.2A5.2 5.2 0 0 1 2 16.8V7.2A5.2 5.2 0 0 1 7.2 2Zm0 1.9A3.3 3.3 0 0 0 3.9 7.2v9.6a3.3 3.3 0 0 0 3.3 3.3h9.6a3.3 3.3 0 0 0 3.3-3.3V7.2a3.3 3.3 0 0 0-3.3-3.3H7.2Zm9.9 1.5a1.2 1.2 0 1 1 0 2.3 1.2 1.2 0 0 1 0-2.3ZM12 7a5 5 0 1 1 0 10.1A5 5 0 0 1 12 7Zm0 1.9a3.1 3.1 0 1 0 0 6.2 3.1 3.1 0 0 0 0-6.2Z"/></svg>',
    'email': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M3 5.5A2.5 2.5 0 0 1 5.5 3h13A2.5 2.5 0 0 1 21 5.5v13a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 18.5v-13Zm2.1.4 6.8 5.7 6.9-5.7H5.1Zm13.8 2.4-6.4 5.3a.8.8 0 0 1-1 0L5.1 8.3v10.2c0 .3.2.5.5.5h13c.3 0 .5-.2.5-.5V8.3Z"/></svg>',
    'menu': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 6h16v2.5H4V6Zm0 4.75h16v2.5H4v-2.5ZM4 15.5h16V18H4v-2.5Z"/></svg>',
    'close': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="m6.7 5.3 5.3 5.3 5.3-5.3 1.4 1.4-5.3 5.3 5.3 5.3-1.4 1.4-5.3-5.3-5.3 5.3-1.4-1.4 5.3-5.3-5.3-5.3 1.4-1.4Z"/></svg>',
    'thumb': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M2 10.5h4V21H2v-10.5Zm7 10.5h8.7c1.2 0 2.2-.8 2.5-2l1.5-6.1A2.6 2.6 0 0 0 19.1 10H14V6.4c0-1.2-.7-2.2-1.8-2.7l-.4-.2-4 6.1H9V21Z"/></svg>',
    'id': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Zm0 2v12h16V6H4Zm4 2.1a3.4 3.4 0 1 1 0 6.8 3.4 3.4 0 0 1 0-6.8Zm6.6.9H18v1.8h-3.4V9Zm0 3H18v1.8h-3.4V12Zm-9.1 4.2h5A3.6 3.6 0 0 0 8 15c-1.1 0-2.1.4-2.5 1.2Z"/></svg>',
    'heart': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 21.3 10.6 20C5.2 15 2 12.1 2 8.5A4.5 4.5 0 0 1 6.5 4C8.3 4 10 4.8 11 6.1 12 4.8 13.7 4 15.5 4A4.5 4.5 0 0 1 20 8.5c0 3.6-3.2 6.5-8.6 11.5L12 21.3Z"/></svg>',
    'chevron': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="m12 16.4-7-7 1.4-1.4 5.6 5.6 5.6-5.6L19 9.4l-7 7Z"/></svg>',
    'phone': '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.7 3h3.1l1.3 4.2-2.1 1.9a15 15 0 0 0 5.9 5.9l1.9-2.1L21 14.2v3.1c0 1-.8 1.7-1.7 1.7C10.8 19 5 13.2 5 5.7 5 4.8 5.7 4 6.7 4V3Z"/></svg>'
}

def social_links(root_prefix=''):
    return f'''
    <div class="social-links" aria-label="Social media links">
      <a class="social-link" href="https://www.facebook.com/gardnerfordhs" target="_blank" rel="noreferrer" aria-label="Facebook">{icons['facebook']}</a>
      <a class="social-link" href="https://www.instagram.com/gardnerfordhs/" target="_blank" rel="noreferrer" aria-label="Instagram">{icons['instagram']}</a>
      <a class="social-link" href="mailto:gardnerfordhs@gmail.com" aria-label="Email">{icons['email']}</a>
    </div>
    '''

nav_items = [
    ('Home', '/index.html', 'index'),
    ('Who Is Gary?', '/who-is-gary/index.html', 'who'),
    ('The Issues', '/the-issues/index.html', 'issues'),
    ('Supporters', '/supporters/index.html', 'supporters'),
    ('Contact', '/contact/index.html', 'contact'),
    ('Links & Resources', '/links-resources/index.html', 'links'),
]

media_items = [
    ('2022 Election', '/media/index.html', 'media'),
    ('Media Archive', '/media/media-archive/index.html', 'archive'),
]

def nav_markup(prefix, current):
    links = []
    for label, href, key in nav_items:
        aria = ' aria-current="page"' if key == current else ''
        links.append(f'<li><a href="{prefix}{href}"{aria}>{label}</a></li>')
    media_sub = []
    for label, href, key in media_items:
        aria = ' aria-current="page"' if key == current else ''
        media_sub.append(f'<li><a href="{prefix}{href}"{aria}>{label}</a></li>')
    return f'''
    <div class="nav-backdrop" data-nav-backdrop></div>
    <nav class="primary-nav" data-nav aria-label="Primary navigation">
      <div class="nav-head">
        <h2 class="nav-title">Menu</h2>
        <button class="nav-close" type="button" data-nav-close aria-label="Close menu">{icons['close']}</button>
      </div>
      <ul class="nav-list">
        {''.join(links)}
        <li class="nav-group">
          <span>Media</span>
          <ul class="nav-sublist">{''.join(media_sub)}</ul>
        </li>
      </ul>
    </nav>
    '''


def site_header(prefix, current):
    home_aria = ' aria-current="page"' if current == 'index' else ''
    return f'''
    <a class="skip-link" href="#main-content">Skip to content</a>
    <header class="site-header">
      <div class="header-inner">
        <a class="brand" href="{prefix}/index.html"{home_aria}>
          <span class="brand-mark" aria-hidden="true">G</span>
          <span class="brand-text">
            <span class="brand-kicker">Gary</span>
            <span class="brand-title">Gardner</span>
            <span class="brand-sub">City Council District 1 · Delivering for DHS</span>
          </span>
        </a>
        <div class="header-right">
          {social_links(prefix)}
          <button class="menu-button" type="button" data-menu-button aria-expanded="false" aria-controls="site-navigation" aria-label="Open menu">{icons['menu']}</button>
        </div>
      </div>
    </header>
    {nav_markup(prefix, current)}
    '''


def footer(prefix):
    return f'''
    <footer class="site-footer">
      <div class="footer-inner">
        <div class="footer-social">{social_links(prefix)}</div>
        <div class="footer-meta">
          <p>© 2026 Gary Gardner for Desert Hot Springs City Council 2022. All Rights Reserved.</p>
          <p>No tax dollars were used for the creation of this website and none are used for the maintenance or content creation.</p>
          <p>PO Box 333, DHS 92240.</p>
          <p>FPPC#: 1405627</p>
          <p>EIN: 82-5194248</p>
        </div>
        <div class="footer-links footer-note">
          <a href="https://gardnerfordhs.com/terms-of-service-privacy-policy/" target="_blank" rel="noreferrer">Terms of Service &amp; Privacy Policy</a>
        </div>
      </div>
    </footer>
    '''


def page(title, description, prefix, current, body_classes='', extra_head=''):
    css_path = f'{prefix}/assets/css/styles.css'
    js_path = f'{prefix}/assets/js/site.js'
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#852d97">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:site_name" content="Gary Gardner for Desert Hot Springs City Council District 1">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css_path}">
  {extra_head}
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"PoliticalCandidate","name":"Gary Gardner","email":"gardnerfordhs@gmail.com","telephone":"+1-206-669-0548","address":{{"@type":"PostalAddress","postOfficeBoxNumber":"PO Box 333","addressLocality":"Desert Hot Springs","postalCode":"92240","addressRegion":"CA","addressCountry":"US"}},"sameAs":["https://www.facebook.com/gardnerfordhs","https://www.instagram.com/gardnerfordhs/"]}}</script>
</head>
<body class="{body_classes}">
{site_header(prefix, current)}
'''


def end_page(prefix):
    return f'''{footer(prefix)}
<script src="{prefix}/assets/js/site.js" defer></script>
</body>
</html>
'''

home = page(
    'Gary Gardner for Desert Hot Springs City Council District 1 — Delivering for DHS',
    'Gary Gardner for Desert Hot Springs City Council District 1. Delivering for DHS.',
    '.', 'index'
) + r'''
<main id="main-content">
  <section class="hero hero--video" aria-labelledby="hero-title">
    <div class="hero-media-placeholder" aria-hidden="true"><span class="label">Homepage Video Hero Placeholder</span></div>
    <div class="hero-content">
      <h1 id="hero-title" class="hero-title">Gary Gardner for Desert Hot Springs City Council District 1</h1>
      <p class="hero-subtitle">Councilman Gary Gardner is the real deal for Desert Hot Springs, working to keep our city safe, programs maintained, business friendly and fiscally responsible.</p>
      <div class="hero-actions">
        <a class="btn btn--primary" href="#about-home">''' + icons['thumb'] + r'''<span>Gardner for DHS</span></a>
        <a class="btn btn--secondary" href="./who-is-gary/index.html">''' + icons['id'] + r'''<span>Who is Gary?</span></a>
        <a class="btn btn--secondary" href="./supporters/index.html#endorse">''' + icons['heart'] + r'''<span>Endorse</span></a>
      </div>
    </div>
    <div class="hero-chevron"><a href="#about-home" aria-label="Scroll to content">''' + icons['chevron'] + r'''</a></div>
  </section>

  <section class="section section--white" id="about-home">
    <div class="container grid-2">
      <div class="copy">
        <h2 class="section-heading section-heading--purple">Gardner for DHS</h2>
        <p>It’s been my honor to serve on the city council since 2018. When I was first elected, my primary goal was to keep the city moving forward and to improve the lives of all our residents. I’ve worked tirelessly towards that, and I believe we’ve made great strides towards realizing the potential that this city has — to become a strong, vibrant community that attracts residents and visitors to our wonderful outdoor recreation possibilities, our world-famous hot mineral water spas, and our sense of community.</p>
        <p>We are now the fastest-growing city in the Coachella Valley. That growth will be challenging, but we are well prepared for it.</p>
      </div>
      <div class="inline-image-placeholder circle" role="img" aria-label="Gary Gardner at Fire Station image placeholder"><span class="label">Image Placeholder</span></div>
    </div>
  </section>

  <div class="mountain-divider" aria-hidden="true"></div>

  <section class="section section--blue">
    <div class="container">
      <ul class="bullets">
        <li>Since 2019 we’ve seen our city – for the first time in history – be in a secure financial position, with more than twelve million dollars in reserves for a rainy day.</li>
        <li>Since 2019 we’ve moved into a brand new one-stop-shopping City Hall that was built without affecting our budget by refinancing old bonds and taking those savings to build the new City Hall.</li>
        <li>Since 2019 we’ve developed a culture of “Can-Do” with our city staff, empowering them to find ways to get things done with the full support of the City Council.</li>
        <li>Since 2019 we’ve seen a renaissance in our Hotel and Spa industry, with several new properties – including the stunning Azure Palms Hot Springs opening. We’ll continue to see more of that with an innovative “Spa Revitalization” program that Councilmember Pye and I developed that will encourage further investments in dilapidated and unused spas in our city.</li>
        <li>Since 2019 we’ve improved our parks and our outdoor recreation, opening new trails, including the spectacular Long Canyon Trail into Joshua Tree National Park. All this year you’ll continue to see improvements in our parks across the city.</li>
        <li>Since 2019 we’ve doubled down on our efforts to keep the city clean, with programs of volunteers cleaning vacant lots, and increasing our fines for illegal dumping.</li>
        <li>Since 2019 we’ve expanded our police department, and our crime rate has dropped significantly – Desert Hot Springs' crime rate is now lower than Palm Springs, Cathedral City, and Indio.</li>
        <li>Since 2019 we’ve nearly doubled our cannabis businesses in the city, employing hundreds of Desert Hot Springs residents and generating millions in tax revenue to keep our city healthy.</li>
      </ul>
      <p style="margin-top:1.6rem"><a class="btn btn--primary" href="./who-is-gary/index.html">Learn More About Me</a></p>
    </div>
  </section>
</main>
''' + end_page('.')

who = page(
    'Who Is Gary? — Gary Gardner for Desert Hot Springs City Council District 1',
    'Who is Gary Gardner? Learn more about his background and public service.',
    '..', 'who'
) + r'''
<main id="main-content">
  <section class="hero hero--image" aria-labelledby="who-hero">
    <div class="hero-media-placeholder" aria-hidden="true"><span class="label">Image Hero Placeholder</span></div>
    <div class="hero-content">
      <h1 id="who-hero" class="hero-title">Who Is Gary?</h1>
    </div>
  </section>

  <section class="section section--white">
    <div class="container copy">
      <h2 class="section-heading section-heading--purple">Hello, I'm Gary Gardner.</h2>
      <p>I first “discovered” Desert Hot Springs about 15 years ago as an occasional snowbird from the Pacific Northwest. After I retired in 2015, I could have moved just about anywhere I wanted to live, and I CHOSE Desert Hot Springs – probably for the same reason most of you have. The small-town feel, these expansive views of our gorgeous desert, our award-winning water, the hot spring spas, the charming history, and the friendly people.</p>
      <p>I ran and was elected to the City Council in 2018, and re-elected in 2022, after serving on the Planning Commission and chairing the Human Rights Committee. I love this city and its residents, and I want to make sure we continue along the successful path of balancing responsible growth with prudent fiscal management, and diversifying our economy while making sure our cannabis industry thrives. I’m honored to be chosen by my fellow council members to serve as the Mayor Pro Tem for the city this year.</p>
    </div>
  </section>

  <section class="section section--tight section--white">
    <div class="container">
      <div class="inline-image-placeholder" role="img" aria-label="Gary Gardner in front of Desert Hot Springs City Hall image placeholder"><span class="label">Image Placeholder</span></div>
    </div>
  </section>

  <div class="slash-divider" aria-hidden="true"></div>

  <section class="section section--white">
    <div class="container copy">
      <h2 class="section-heading section-heading--purple">My experiences bring a diverse skill set for public service.</h2>
      <p>I’m also fortunate to be the city representative on some very key regional government bodies as well, working to deliver for DHS. I serve as chairman of the Coachella Valley Mountains Conservancy, the agency that develops trails and outdoor recreation opportunities and educational efforts in the desert. I also serve on the Coachella Valley Conservation Commission, the agency charged with environmental protection and conserving open space here in the valley.</p>
      <p>I’m also chair the board of Visit Greater Palm Springs Convention and Visitors Bureau, making sure that our hotels and spas are included in regional tourism and marketing efforts, and bringing increased tourism and economic activity to Desert Hot Springs. And I also serve on the Coachella Valley Mosquito and Vector Control District board, working to keep mosquitos and other vectors and the diseases they bring under control.</p>
      <p>I’m proud of my service to our community. Since my first term, I’ve always had an open-door policy and enjoy meeting with residents. My personal cell phone number is on my city business card and on the city web page, and I’ve done my best to be a responsive council member when neighbors have brought me their concerns. Thank you for allowing me to continue to deliver for Desert Hot Springs and to make Desert Hot Springs the best place to live in Southern California.</p>
    </div>
  </section>
</main>
''' + end_page('..')

issues = page(
    'The Issues — Gary Gardner for Desert Hot Springs City Council District 1',
    'Councilman Gary Gardner’s priorities for Desert Hot Springs.',
    '..', 'issues'
) + r'''
<main id="main-content">
  <section class="hero hero--image" aria-labelledby="issues-hero">
    <div class="hero-media-placeholder" aria-hidden="true"><span class="label">Image Hero Placeholder</span></div>
    <div class="hero-content"><h1 id="issues-hero" class="hero-title">The Issues</h1></div>
  </section>

  <section class="section section--white">
    <div class="container copy">
      <h2 class="section-heading section-heading--purple">Councilman Gary Gardner's Priorities</h2>
      <p class="lead">Desert Hot Springs is the fastest-growing city in the Coachella Valley, and as such there are a number of critical issues that will come before the city council in the next four years. Here are my priorities going forward:</p>
      <ul class="bullets">
        <li>Making sure public safety grows as the city grows. We’ve already bonded for one new fire station on the east side, and we are expanding our downtown police campus -- both will open in 2022/2023. We need to plan now for additional police officers and another fire station, as well as expanded animal control and code enforcement as the city grows. If I’m re-elected this will continue to be my number-one priority.</li>
        <li>Nearly 40% of our municipal budget comes from cannabis taxes, but that’s too much in one bucket. We need to expand our tourism economy by revitalizing our spas, capitalizing on our access to outdoor recreation, as well as new areas such as canna- tourism. We can increase the amount of taxes those sectors bring in, reducing our reliance on cannabis taxes.</li>
      </ul>
      <p>As the city’s representative, and vice-chair on the Visit Greater Palm Springs Joint Powers Authority, I’ve worked hard to make sure Desert Hot Springs isn’t overlooked in regional marketing and I’ve worked on spa revitalization and outdoor recreation so our tourism industry grows with the city.</p>
      <ul class="bullets">
        <li>Our desert landscape is beautiful – it’s one of the main reasons I came to Desert Hot Springs, and why many of us love it so much. Since I was elected, we’ve made great strides in cleaning up our desert, we increased fines for illegal dumping, and we’ve opened new hiking trails and are developing more trials as well as pushing for a visitor center for the Sand to Snow National Monument. I will continue to work to expand our outdoor recreation opportunities and work to keep our desert clean.</li>
        <li>We must improve traffic flow and reduce accidents and fatalities. New houses and new residents and growing industries bring increased traffic, and new roads take a long time to plan and to find funding for. It’s vital that we start the planning process now. I worked to get funding for message signs alerting drivers when roads are closed due to weather, and I promise to make improving our road network and reducing traffic deaths a high priority.</li>
        <li>We need to continue to work on growing our commercial business sector in Desert Hot Springs so residents can shop and dine in their city and not have to travel so far for basic needs and keep sales tax dollars here. Our population level is such that the city needs to do everything it can to attract new retail and restaurant options. I will work with our economic development team on making sure the city is attractive to new stores and restaurants.</li>
        <li>Desert Hot Springs is woefully short on park space for our residents. In 2022 we updated our parks master plan, and we are making some significant investments in improving our existing parks, but we need more parks, especially on the city’s east side. Finding locations and funding for new parks will be a high priority of mine.</li>
      </ul>
    </div>
  </section>
</main>
''' + end_page('..')

supporters = page(
    'Supporters — Gary Gardner for Desert Hot Springs City Council District 1',
    'Thank you to everyone who supported Gary Gardner’s campaign in 2022.',
    '..', 'supporters'
) + r'''
<main id="main-content">
  <section class="hero hero--purple" style="background:linear-gradient(180deg, rgba(8,12,24,.12), rgba(8,12,24,.12)), linear-gradient(135deg, #8a2b98, #6b1e75); min-height: 340px;" aria-labelledby="supporters-hero">
    <div class="hero-content"><h1 id="supporters-hero" class="hero-title">Supporters</h1></div>
  </section>

  <section class="section section--white">
    <div class="container">
      <h2 class="section-heading section-heading--purple">Thank you to everyone who supported my campaign in 2022</h2>
      <div class="supporters-list">
        <div class="supporter"><h3 class="supporter-name">- Scott Matas</h3><p class="supporter-role">Desert Hot Springs Mayor</p></div>
        <div class="supporter"><h3 class="supporter-name">- Jan Pye</h3><p class="supporter-role">Desert Hot Springs Councilwoman</p></div>
        <div class="supporter"><h3 class="supporter-name">- Desert Hot Springs Police Officers Association</h3></div>
        <div class="supporter"><h3 class="supporter-name">- V. Manuel Perez</h3><p class="supporter-role">Riverside County Supervisor District 4</p></div>
        <div class="supporter"><h3 class="supporter-name">- Lisa Middleton</h3><p class="supporter-role">Palm Springs Mayor</p></div>
        <div class="supporter"><h3 class="supporter-name">- Christy Holestege</h3><p class="supporter-role">Palm Springs Council Member</p></div>
        <div class="supporter"><h3 class="supporter-name">- Russ Martin</h3><p class="supporter-role">Mission Springs Water District Board Chair</p></div>
        <div class="supporter"><h3 class="supporter-name">- Richard Duffle</h3><p class="supporter-role">Chair, Desert Hot Springs Planning Commission</p></div>
        <div class="supporter"><h3 class="supporter-name">- Dirk Voss</h3><p class="supporter-role">Former DHS Planning Commission Chair</p></div>
        <div class="supporter"><h3 class="supporter-name">- James Nindel</h3><p class="supporter-role">Desert Hot Springs Planning Commission Vice Chair</p></div>
        <div class="supporter"><h3 class="supporter-name">- Brian Muse</h3><p class="supporter-role">DHS Public Safety Commissioner</p></div>
        <div class="supporter"><h3 class="supporter-name">- Jan Harnik</h3><p class="supporter-role">Palm Desert Mayor</p></div>
        <div class="supporter"><h3 class="supporter-name">- Dana Reed</h3><p class="supporter-role">Indian Wells Mayor</p></div>
        <div class="supporter"><h3 class="supporter-name">- Greg Sanders</h3><p class="supporter-role">Indian Wells Council Member</p></div>
        <div class="supporter"><h3 class="supporter-name">- Kathleen Fitzpatrick</h3><p class="supporter-role">Mayor Pro Tem, City of La Quinta</p></div>
        <div class="supporter"><h3 class="supporter-name">- John Peña</h3><p class="supporter-role">Councilmember, City of La Quinta</p></div>
        <div class="supporter"><h3 class="supporter-name">- Waymond Furmon</h3><p class="supporter-role">Mayor of Indio</p></div>
        <div class="supporter"><h3 class="supporter-name">- Elaine Holmes</h3><p class="supporter-role">Councilmember, City of Indio</p></div>
        <div class="supporter"><h3 class="supporter-name">- Glenn Miller</h3><p class="supporter-role">Councilmember, City of Indio</p></div>
        <div class="supporter"><h3 class="supporter-name">- Peace Officers Research Association of California (PORAC)</h3></div>
        <div class="supporter"><h3 class="supporter-name">- Desert Valley Builders Association (DVBA)</h3></div>
        <div class="supporter"><h3 class="supporter-name">- Desert Stonewall Democrats</h3></div>
        <div class="supporter"><h3 class="supporter-name">- Planned Parenthood of the Pacific Southwest Action Fund</h3></div>
        <div class="supporter"><h3 class="supporter-name">- Bea Gonzalez</h3><p class="supporter-role">Trustee, College of the Desert</p></div>
        <div class="supporter"><h3 class="supporter-name">- Sam Messler</h3><p class="supporter-role">Past President, Diversity DHS</p></div>
        <div class="supporter"><h3 class="supporter-name">- Mirna Flores</h3></div>
        <div class="supporter"><h3 class="supporter-name">- Michael R. Burke</h3><p class="supporter-role">Owner of BurkeMedia Productions / Former Desert Hot Springs Rotary President</p></div>
        <div class="supporter"><h3 class="supporter-name">- Kelly Brady</h3><p class="supporter-role">Owner of Kamp Kelly Dog Day Care</p></div>
      </div>
      <div id="endorse" class="cta-panel">
        <h2 class="section-heading section-heading--purple" style="font-size:clamp(2rem,4vw,3.8rem)">Do you support the Re-election of Gary Gardner for Desert Hot Springs City Council?</h2>
        <a class="btn btn--blue" href="../contact/index.html">Add your name to this list</a>
      </div>
    </div>
  </section>
</main>
''' + end_page('..')

contact = page(
    'Contact — Gary Gardner for Desert Hot Springs City Council District 1',
    'Contact Gary Gardner for Desert Hot Springs City Council District 1.',
    '..', 'contact'
) + r'''
<main id="main-content">
  <section class="hero hero--purple" style="background:linear-gradient(180deg, rgba(8,12,24,.12), rgba(8,12,24,.12)), linear-gradient(135deg, #8a2b98, #6b1e75); min-height: 340px;" aria-labelledby="contact-hero">
    <div class="hero-content"><h1 id="contact-hero" class="hero-title">Contact</h1></div>
  </section>

  <section class="section section--white">
    <div class="container grid-2">
      <div>
        <p class="lead">Please feel free to reach out, ask questions and share concerns. I’m happy to schedule a meeting with you; please fill out the form below or call my cell phone, <a href="tel:+12066690548">206-669-0548</a>.</p>
        <div class="contact-list" aria-label="Contact methods">
          <a class="contact-item" href="mailto:gardnerfordhs@gmail.com">''' + icons['email'] + r'''<span>gardnerfordhs@gmail.com</span></a>
          <a class="contact-item" href="https://www.facebook.com/gardnerfordhs" target="_blank" rel="noreferrer">''' + icons['facebook'] + r'''<span>gardnerfordhs</span></a>
          <a class="contact-item" href="https://www.instagram.com/gardnerfordhs/" target="_blank" rel="noreferrer">''' + icons['instagram'] + r'''<span>gardnerfordhs</span></a>
          <a class="contact-item" href="tel:+12066690548">''' + icons['phone'] + r'''<span>(206) 669-0548</span></a>
        </div>
      </div>
      <div class="form-card">
        <form name="contact" method="POST" data-netlify="true" data-netlify-recaptcha="true">
          <input type="hidden" name="form-name" value="contact">
          <div class="form-grid">
            <div class="form-field">
              <label for="first-name">Your Name <span aria-hidden="true">*</span></label>
              <input id="first-name" name="first-name" type="text" autocomplete="given-name" required>
            </div>
            <div class="form-field">
              <label for="last-name"><span class="sr-only">Your Name continued</span>Last</label>
              <input id="last-name" name="last-name" type="text" autocomplete="family-name" required>
            </div>
            <div class="form-field form-field--full">
              <label for="email">Your Email Address <span aria-hidden="true">*</span></label>
              <input id="email" name="email" type="email" autocomplete="email" required>
            </div>
            <div class="form-field form-field--full">
              <label for="phone">Your Phone Number</label>
              <input id="phone" name="phone" type="tel" autocomplete="tel">
            </div>
            <div class="form-field form-field--full">
              <label for="message">Your Message</label>
              <textarea id="message" name="message"></textarea>
            </div>
            <div class="form-field form-field--full">
              <label>CAPTCHA</label>
              <div data-netlify-recaptcha="true"></div>
            </div>
            <div class="form-field form-field--full">
              <button class="btn btn--primary" type="submit">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>

  <section class="section section--tight section--white">
    <div class="container">
      <img src="https://gardnerfordhs.com/wp-content/uploads/2022/02/GaryGardner-for-DHS-16-1024x682.jpg" alt="Gary Gardner sitting on his motorcycle in the desert." loading="lazy" style="width:100%; border-radius:22px; box-shadow: var(--shadow); object-fit:cover; max-height:620px;">
    </div>
  </section>
</main>
''' + end_page('..')

media = page(
    'Media — Gary Gardner for Desert Hot Springs City Council District 1',
    'Campaign videos and media for Gary Gardner for Desert Hot Springs City Council District 1.',
    '..', 'media'
) + r'''
<main id="main-content">
  <section class="hero hero--blue" aria-labelledby="media-hero" style="min-height: 340px;">
    <div class="hero-content"><h1 id="media-hero" class="hero-title">Media</h1></div>
  </section>

  <section class="section section--blue">
    <div class="container">
      <div class="video-grid">
        <article class="video-card">
          <h2>Re-elect Gary Gardner for Desert Hot Springs City Council</h2>
          <div class="video-frame"><iframe src="https://www.youtube.com/embed/YwziJa6GeO8" title="Re-elect Gary Gardner for Desert Hot Springs City Council" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>
        </article>
        <article class="video-card">
          <h2>Re-elect Gary Gardner Campaign Kick-Off Party!</h2>
          <div class="video-frame"><iframe src="https://www.youtube.com/embed/WGyOpg9nxKQ" title="Re-elect Gary Gardner Campaign Kick-Off Party" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>
        </article>
        <article class="video-card">
          <h2>Gary Gardner for Desert Hot Springs City Council - The Real Deal</h2>
          <div class="video-frame"><iframe src="https://www.youtube.com/embed/FX0cR43KKG4" title="Gary Gardner for Desert Hot Springs City Council - The Real Deal" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>
        </article>
        <article class="video-card">
          <h2>Gary's Goals - Recap Of My Vision</h2>
          <div class="video-frame"><iframe src="https://www.youtube.com/embed/1cpjaVZToDc" title="Gary's Goals - Recap Of My Vision" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>
        </article>
        <article class="video-card">
          <h2>Who is Gary Gardner?</h2>
          <div class="video-frame"><iframe src="https://www.youtube.com/embed/Wd1tq8pt6fU" title="Who is Gary Gardner?" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>
        </article>
        <article class="video-card">
          <h2>Gary's Goals - Talking Traffic Safety</h2>
          <div class="video-frame"><iframe src="https://www.youtube.com/embed/WvyFGSMfs9E" title="Gary's Goals - Talking Traffic Safety" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>
        </article>
      </div>

      <div class="gallery-grid" aria-label="Media photo gallery">
        <figure class="gallery-card"><img src="https://gardnerfordhs.com/wp-content/uploads/2022/02/GaryGardner-for-DHS-16-1024x682.jpg" alt="Gary Gardner standing with the Coachella Valley behind him." loading="lazy"></figure>
        <figure class="gallery-card"><img src="https://gardnerfordhs.com/wp-content/uploads/2022/02/GaryGardner-for-DHS-15-1024x682.jpg" alt="Gary Gardner leaning on a balcony with mountains in the background." loading="lazy"></figure>
        <figure class="gallery-card"><img src="https://gardnerfordhs.com/wp-content/uploads/2022/02/GaryGardner-for-DHS-11-1024x682.jpg" alt="Gary Gardner beside a sculpture in Desert Hot Springs." loading="lazy"></figure>
        <figure class="gallery-card"><img src="https://gardnerfordhs.com/wp-content/uploads/2022/02/GaryGardner-for-DHS-10-1024x682.jpg" alt="Gary Gardner next to a sculpture closeup." loading="lazy"></figure>
        <figure class="gallery-card"><img src="https://gardnerfordhs.com/wp-content/uploads/2022/02/GaryGardner-for-DHS-8-1024x682.jpg" alt="Gary Gardner at Desert Hot Springs City Hall." loading="lazy"></figure>
        <figure class="gallery-card"><img src="https://gardnerfordhs.com/wp-content/uploads/2022/02/GaryGardner-for-DHS-16-1024x682.jpg" alt="Gary Gardner sitting on his motorcycle in the desert." loading="lazy"></figure>
      </div>
    </div>
  </section>
</main>
''' + end_page('..')

archive = page(
    'Media Archive — Gary Gardner for Desert Hot Springs City Council District 1',
    'Media archive for Gary Gardner for Desert Hot Springs City Council District 1.',
    '../..', 'archive'
) + r'''
<main id="main-content">
  <section class="hero hero--blue" aria-labelledby="archive-hero" style="min-height: 340px;">
    <div class="hero-content"><h1 id="archive-hero" class="hero-title">Media Archive</h1></div>
  </section>

  <section class="section section--blue">
    <div class="container">
      <h2 class="section-heading" style="color:#fff">2018 Election</h2>
      <div class="archive-grid">
        <article class="video-card">
          <h3>A post shared by Gary Gardner (@gardnerfordhs) on Jun 8, 2018 at 10:37am PDT</h3>
          <div class="video-copy"><a href="https://www.instagram.com/gardnerfordhs/" target="_blank" rel="noreferrer" style="color:#fff">View on Instagram</a></div>
        </article>
        <article class="video-card">
          <h3>A post shared by Gary Gardner (@gardnerfordhs) on Jun 8, 2018 at 10:39am PDT</h3>
          <div class="video-copy"><a href="https://www.instagram.com/gardnerfordhs/" target="_blank" rel="noreferrer" style="color:#fff">View on Instagram</a></div>
        </article>
        <article class="video-card">
          <h3>A post shared by Gary Gardner (@gardnerfordhs) on Jun 8, 2018 at 10:43am PDT</h3>
          <div class="video-copy"><a href="https://www.instagram.com/gardnerfordhs/" target="_blank" rel="noreferrer" style="color:#fff">View on Instagram</a></div>
        </article>
      </div>
    </div>
  </section>
</main>
''' + end_page('../..')

links = page(
    'Links & Resources — Gary Gardner for Desert Hot Springs City Council District 1',
    'Links and resources shared on the Gary Gardner campaign website.',
    '..', 'links'
) + r'''
<main id="main-content">
  <section class="hero hero--cityhall" aria-labelledby="links-hero">
    <div class="hero-media-placeholder" aria-hidden="true"><span class="label">Image Hero Placeholder</span></div>
    <div class="hero-content"><h1 id="links-hero" class="hero-title">Links &amp; Resources</h1></div>
  </section>

  <section class="section section--white">
    <div class="container copy">
      <ul class="resources-list">
        <li><a href="https://cityofdhs.org" target="_blank" rel="noreferrer">City of Desert Hot Springs</a></li>
        <li><a href="https://scottmatas.com" target="_blank" rel="noreferrer">Mayor Scott Matas</a></li>
        <li><a href="https://mswd.org" target="_blank" rel="noreferrer">Mission Springs Water District</a></li>
        <li><a href="https://www.psusd.us" target="_blank" rel="noreferrer">Palm Springs Unified School District</a></li>
        <li><a href="https://www.collegeofthedesert.edu" target="_blank" rel="noreferrer">College of the Desert</a></li>
        <li><a href="https://gcvcc.org" target="_blank" rel="noreferrer">Greater Coachella Valley Chamber of Commerce</a></li>
        <li><a href="https://www.visitdeserthotsprings.com" target="_blank" rel="noreferrer">Desert Hot Springs Hoteliers Association</a></li>
        <li><a href="https://dhshistoricalsociety.com" target="_blank" rel="noreferrer">Desert Hot Springs Historical Society</a></li>
        <li><a href="https://dhsrotary.org" target="_blank" rel="noreferrer">Desert Hot Springs Rotary Club</a></li>
        <li><a href="https://www.elks.org" target="_blank" rel="noreferrer">Desert Hot Springs Elks Lodge #2639</a></li>
        <li><a href="https://www.cabotsmuseum.org" target="_blank" rel="noreferrer">Cabot’s Pueblo Museum</a></li>
        <li><a href="https://www.facebook.com/" target="_blank" rel="noreferrer">Desert Hot Springs Neighborhood Group on Facebook</a></li>
        <li><a href="https://www.rivco4.org" target="_blank" rel="noreferrer">Riverside County District 4</a></li>
        <li><a href="https://scanlostanimals.com" target="_blank" rel="noreferrer">Lost/Found Pets After Hours</a></li>
      </ul>
    </div>
  </section>
</main>
''' + end_page('..')

files = {
    root / 'assets/css/styles.css': css,
    root / 'assets/js/site.js': js,
    root / 'index.html': home,
    root / 'who-is-gary/index.html': who,
    root / 'the-issues/index.html': issues,
    root / 'supporters/index.html': supporters,
    root / 'contact/index.html': contact,
    root / 'media/index.html': media,
    root / 'media/media-archive/index.html': archive,
    root / 'links-resources/index.html': links,
    root / 'robots.txt': 'User-agent: *\nAllow: /\n\nSitemap: https://gardnerfordhs.com/sitemap.xml\n',
    root / 'sitemap.xml': '''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://gardnerfordhs.com/</loc></url>\n  <url><loc>https://gardnerfordhs.com/who-is-gary/</loc></url>\n  <url><loc>https://gardnerfordhs.com/the-issues/</loc></url>\n  <url><loc>https://gardnerfordhs.com/supporters/</loc></url>\n  <url><loc>https://gardnerfordhs.com/contact/</loc></url>\n  <url><loc>https://gardnerfordhs.com/media/</loc></url>\n  <url><loc>https://gardnerfordhs.com/media/media-archive/</loc></url>\n  <url><loc>https://gardnerfordhs.com/links-resources/</loc></url>\n</urlset>\n''',
    root / 'netlify.toml': '''[build]\n  publish = "."\n\n[[redirects]]\n  from = "/who-is-gary"\n  to = "/who-is-gary/"\n  status = 301\n\n[[redirects]]\n  from = "/the-issues"\n  to = "/the-issues/"\n  status = 301\n\n[[redirects]]\n  from = "/supporters"\n  to = "/supporters/"\n  status = 301\n\n[[redirects]]\n  from = "/contact"\n  to = "/contact/"\n  status = 301\n\n[[redirects]]\n  from = "/media"\n  to = "/media/"\n  status = 301\n\n[[redirects]]\n  from = "/media/media-archive"\n  to = "/media/media-archive/"\n  status = 301\n\n[[redirects]]\n  from = "/links-resources"\n  to = "/links-resources/"\n  status = 301\n'''
}

for path, content in files.items():
    path.write_text(content, encoding='utf-8')

print('wrote files')
