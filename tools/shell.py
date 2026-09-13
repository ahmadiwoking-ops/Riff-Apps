"""Shared HTML shell for every Riff Apps page.

Run `python3 tools/build.py` from the project root after editing to
regenerate all pages with a consistent header and footer.
"""

SITE = "https://riff-apps.com"
EMAIL = "Contact@Riff-Apps.com"

NAV = [
    ("/", "Home"),
    ("/services", "Services"),
    ("/work", "Work"),
    ("/governance", "Governance"),
]

LEGAL = [
    ("privacy-policy", "Privacy policy", "How we collect, use and protect personal data."),
    ("terms-of-service", "Terms of service", "The agreement covering this site and our services."),
    ("cookie-policy", "Cookie policy", "What we store on your device, and why."),
    ("gdpr", "GDPR", "Your rights under UK and EU data protection law."),
    ("ai-transparency", "AI transparency", "Where AI is used, and how decisions are governed."),
    ("acceptable-use", "Acceptable use", "What our products and services may not be used for."),
    ("law-enforcement", "Law enforcement", "How authorities request data from us."),
    ("refund-policy", "Refund policy", "Cancellations, refunds and billing disputes."),
]


def head(title, description, path, css_depth=0, extra_head="", body_class=""):
    root = "../" if css_depth else "./"
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE}{path}">
<meta name="theme-color" content="#0A1C3E">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Riff Apps">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/assets/img/riff-apps-logo.png">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="{root}assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="{root}assets/fonts/outfit-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/css/fonts.css">
<link rel="stylesheet" href="{root}assets/css/site.css">
{extra_head}</head>
<body{f' class="{body_class}"' if body_class else ''}>
<a class="skip" href="#main">Skip to content</a>
"""


def header(current, css_depth=0):
    root = "../" if css_depth else "./"
    links = ""
    for href, label in NAV:
        aria = ' aria-current="page"' if href == current else ""
        links += f'    <a href="{href}"{aria}>{label}</a>\n'
    return f"""<header class="topbar">
  <div class="shell topbar-inner">
    <a class="brand" href="/">
      <img src="{root}assets/img/riff-mark.png" alt="" width="40" height="34">
      <span><b>Riff</b> Apps</span>
    </a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
    <nav class="nav" id="primary-nav" aria-label="Primary">
{links}      <a class="btn" href="/contact">Start a project</a>
    </nav>
  </div>
</header>
<main id="main">
"""


def footer(css_depth=0, scripts=""):
    root = "../" if css_depth else "./"
    legal_links = "\n".join(
        f'          <li><a href="/legal/{slug}">{label}</a></li>' for slug, label, _ in LEGAL
    )
    return f"""</main>
<hr class="rule">
<footer class="footer">
  <div class="shell">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="footer-brand" href="/">
          <img src="{root}assets/img/riff-mark.png" alt="" width="38" height="32">
          <span><b>Riff</b> Apps</span>
        </a>
        <p>A UK studio building AI-powered web and mobile applications, with data protection and AI governance built in from the first sprint.</p>
      </div>

      <div>
        <h2>Company</h2>
        <ul>
          <li><a href="/services">Services</a></li>
          <li><a href="/work">Work</a></li>
          <li><a href="/governance">Governance</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </div>

      <div>
        <h2>Products</h2>
        <ul>
          <li><a href="https://riff-app.co.uk" rel="noopener">Riff</a></li>
          <li><a href="https://teachwise-ai.com" rel="noopener">TeachWise AI</a></li>
          <li><a href="/work#project-controls">Project controls</a></li>
          <li><a href="/contact">Partner with us</a></li>
        </ul>
      </div>

      <div>
        <h2>Legal</h2>
        <ul>
{legal_links}
        </ul>
      </div>
    </div>

    <div class="footer-base">
      <p>&copy; <span data-year>2026</span> Riff Apps. All rights reserved.</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p class="footer-tagline">Ideas &middot; Build &middot; Connect</p>
    </div>
  </div>
</footer>
<script src="{root}assets/js/site.js" defer></script>
{scripts}</body>
</html>
"""


def page(title, description, path, body, current="", css_depth=0, scripts="", extra_head=""):
    return (
        head(title, description, path, css_depth, extra_head)
        + header(current, css_depth)
        + body
        + footer(css_depth, scripts)
    )
