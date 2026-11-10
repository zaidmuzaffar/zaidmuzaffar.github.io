"""Shared page pieces (head, nav, footer, scripts, section connector).
Every HTML page in the site is built from these, so they all share one structure."""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

# Applies the saved theme before first paint (no flash of the wrong theme).
THEME_BOOT = ("<script>try{var t=localStorage.getItem('zaid-theme');if(t)document.documentElement.setAttribute('data-theme',t);}catch(e){}</script>")

# Phones open in "laptop view" (a 1100px-wide layout) unless the visitor picked "mobile view".
LAPTOP_WIDTH = 1100
VIEW_BOOT = ("<script>(function(){var small=Math.min(screen.width,screen.height)<900,v=null;"
             "try{v=localStorage.getItem('zaid-view');}catch(e){}"
             "if(small)document.documentElement.classList.add('small-device');"
             "if(small&&v!=='mobile'){document.getElementById('vp').setAttribute('content','width=%d');"
             "document.documentElement.classList.add('laptop-view');}})();</script>" % LAPTOP_WIDTH)

CSS_LAYERS = ['tokens', 'base', 'layout', 'components', 'sections']
JS_FILES = ['data.js', 'core/app.js', 'core/theme.js', 'core/render.js', 'core/ui.js', 'core/features.js', 'core/palette.js', 'main.js']


def head(title, desc, base='', extra_css=()):
    css = '\n'.join(f'<link rel="stylesheet" href="{base}css/{c}.css">' for c in list(CSS_LAYERS) + list(extra_css))
    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" id="vp" content="width=device-width, initial-scale=1">
{VIEW_BOOT}
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#07131A">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml">
{THEME_BOOT}
{FONTS}
{css}
</head>'''


LOGO = ('<svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><circle class="logo-ring" cx="17" cy="17" r="15" fill="none" stroke-width="2"/>'
        '<g class="logo-hand"><path d="M17 6 L17 17 L26 21" fill="none" stroke-width="2.5" stroke-linecap="round"/></g></svg>')


def nav(base='', links_html='<nav class="nav-links" id="nav-links" aria-label="Sections"></nav>', cta_href='#contact'):
    return f'''<header class="nav">
  <div class="wrap nav-inner">
    <a href="{base}index.html#top" class="logo" aria-label="zaid.ops home">{LOGO}<span class="logo-text">zaid<em>.ops</em></span></a>
    <div style="display:flex;align-items:center;flex-wrap:wrap;gap:4px">
      {links_html}
      <div class="nav-tools">
        <button type="button" class="icon-btn" data-palette aria-label="Search the site (Ctrl + K)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg><span class="kbd-hint">Ctrl K</span></button>
        <button type="button" class="icon-btn view-btn" data-view-toggle hidden></button>
        <button type="button" class="icon-btn" data-theme-toggle aria-label="Switch theme"></button>
        <a href="{cta_href}" class="nav-cta">ssh zaid →</a>
      </div>
    </div>
  </div>
</header>'''


def footer(base=''):
    return f'''<footer class="wrap footer">
  <span>© <span data-year>2026</span> Zaid Muzaffar</span>
  <span><a href="{base}index.html#map">system map</a> · <a href="https://github.com/zaidmuzaffar">github</a> · build: passing · status: 200 OK</span>
</footer>'''


def scripts(base=''):
    return '\n'.join(f'<script src="{base}js/{f}"></script>' for f in JS_FILES)


PATH = "M0 70 H520 C570 70 570 34 620 34 H820 C870 34 870 70 920 70 H1440"
_glow_id = [0]


def divider(label, left='build ✓', right='deploy ✓'):
    _glow_id[0] += 1
    gid = f'sdglow{_glow_id[0]}'
    pw = max(136, len(label) * 8.6 + 36)   # pill grows with the label
    pk = ''.join(
        f'<rect class="packet" x="-7" y="-3.5" width="14" height="7" rx="3.5">'
        f'<animateMotion dur="4.5s" begin="{b}s" repeatCount="indefinite" rotate="auto" path="{PATH}"/></rect>'
        for b in (0, 1.5, 3))
    return f'''<div class="stage-divider" aria-hidden="true">
  <svg viewBox="0 0 1440 110" preserveAspectRatio="xMidYMid slice">
    <defs><filter id="{gid}" x="-20%" y="-200%" width="140%" height="500%"><feGaussianBlur stdDeviation="4"/></filter></defs>
    <path class="sd-base" d="{PATH}" fill="none" stroke-width="2"/>
    <path class="comet sd-glow" d="{PATH}" pathLength="1000" fill="none" stroke-width="6" stroke-linecap="round" filter="url(#{gid})" opacity=".55"/>
    <path class="comet sd-core" d="{PATH}" pathLength="1000" fill="none" stroke-width="2" stroke-linecap="round"/>
    {pk}
    <g class="sd-node"><circle cx="400" cy="70" r="6" stroke-width="2"/><text x="400" y="98" text-anchor="middle">{left}</text></g>
    <g class="sd-node"><circle cx="1040" cy="70" r="6" stroke-width="2"/><text x="1040" y="98" text-anchor="middle">{right}</text></g>
    <rect class="sd-pulse" x="{720 - pw / 2:.0f}" y="20" width="{pw:.0f}" height="28" rx="14" stroke-width="1.5"/>
    <rect class="sd-pill" x="{720 - pw / 2:.0f}" y="20" width="{pw:.0f}" height="28" rx="14" stroke-width="1.5"/>
    <text class="sd-label" x="720" y="38.5" text-anchor="middle">{label}</text>
  </svg>
</div>'''
