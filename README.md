# Riff Apps — riff-apps.com

A static website for Riff Apps. No build step, no framework, no runtime
dependencies. Fifteen HTML pages, one stylesheet, two small scripts and
self-hosted fonts.

---

## Deploying to Vercel

The site is plain static files, so Vercel needs no build command.

### Option A — drag and drop (fastest)

1. Go to your Vercel dashboard and choose **Add New → Project**.
2. Select **Deploy a template or upload**, then drop in this folder (or the
   `.zip`, unzipped first).
3. Framework Preset: **Other**. Build Command: leave empty. Output Directory:
   leave empty (the root is the output).
4. Deploy.

### Option B — from Git (recommended for ongoing work)

```bash
cd riff-apps
git init
git add .
git commit -m "Riff Apps website"
git remote add origin git@github.com:YOUR-ACCOUNT/riff-apps.git
git push -u origin main
```

Then in Vercel: **Add New → Project → Import Git Repository**, pick the repo,
set Framework Preset to **Other**, and deploy. Every push to `main` redeploys.

### Option C — Vercel CLI

```bash
npm i -g vercel
cd riff-apps
vercel          # preview deployment
vercel --prod   # production deployment
```

### Connecting the domain

In the Vercel project: **Settings → Domains → Add**, enter `riff-apps.com`,
and add `www.riff-apps.com` as a redirect to the apex. Vercel will show the
DNS records to set at your registrar — usually an `A` record for the apex and
a `CNAME` for `www`. HTTPS is issued automatically.

### Local preview

`file://` won't work because links use clean URLs (`/services`, not
`/services.html`). Use either:

```bash
vercel dev          # matches production exactly, including vercel.json
# or
npx serve .         # quick preview
```

---

## What's in `vercel.json`

| Setting | Why |
|---|---|
| `cleanUrls: true` | `/services` serves `services.html`; `.html` URLs redirect to the clean form |
| `trailingSlash: false` | One canonical URL per page, no duplicate-content split |
| Security headers | HSTS, `nosniff`, `X-Frame-Options: DENY`, a strict `Referrer-Policy`, and a `Permissions-Policy` that turns off camera, mic, geolocation and ad-topics APIs |
| Content Security Policy | `default-src 'self'` — nothing loads from anywhere but your own domain |
| Cache-Control | Fonts cached for a year (immutable), images a week, CSS/JS a day |
| Redirects | `/privacy`, `/terms`, `/cookies`, `/projects`, `/about` → their real pages |

If you later add analytics or an embedded widget, the CSP will block it until
you add that origin to the relevant directive. That's deliberate — it's a
prompt to make a conscious decision, not an obstacle.

---

## Before you go live

**1. Fill in the company details.** The legal pages contain two visible
placeholders:

```
[company number]
[registered office address]
```

They appear in `legal/privacy-policy.html`, `legal/terms-of-service.html`,
`legal/gdpr.html` and `legal/law-enforcement.html`. To change them everywhere
at once, edit `ENTITY` near the top of `tools/build_legal.py` and re-run the
build (see below).

**2. Have the policies reviewed.** They're written specifically to match what
this site and your products actually do, rather than generic boilerplate — but
they are not legal advice. Get a solicitor across them before launch,
particularly the liability caps in the terms, the consumer cancellation
section in the refund policy, and the sub-processor lists in the privacy
policy and GDPR statement (the named providers are a starting assumption and
need checking against what you actually use).

**3. Expand the TeachWise AI copy.** Its site is client-rendered, so the
description was written from its public positioning only. It's the thinnest
section on the site. `work.html` and `index.html` both carry it.

**4. Check the "typical reply within two working days" promise** on
`contact.html` is one you want to make.

---

## The contact form

The site is static, so there is no server to receive a form post. The form in
`contact.html` validates the fields and then opens the visitor's own email
client with a pre-filled message to `Contact@Riff-Apps.com`. Nothing is
stored or transmitted by the site itself.

That's honest and zero-maintenance, but it does lose people who use webmail
without a registered mail handler. Two upgrade paths when you want one:

**Formspree or similar** — change the `<form>` to
`action="https://formspree.io/f/YOUR-ID" method="POST"`, delete the submit
handler in `assets/js/site.js`, and add `https://formspree.io` to
`form-action` in the CSP in `vercel.json`.

**A Vercel function** — create `api/contact.js`, send with Resend or
Postmark using an environment variable for the key, and point the form's
`fetch` at `/api/contact`. `connect-src 'self'` in the CSP already allows
this, no change needed.

---

## Editing the site

### Content

Every page is readable HTML. For a one-off wording change, edit the `.html`
file directly and redeploy.

### Anything affecting the header, footer or nav

Those are generated, so editing one page by hand would leave the other
fourteen out of sync. Instead edit the generators and rebuild:

```bash
python3 tools/build_pages.py    # home, services, work, governance, contact, 404
python3 tools/build_legal.py    # the eight policies + legal index
```

- `tools/shell.py` — the shared `<head>`, header, nav and footer. Change the
  nav items in `NAV`, the legal list in `LEGAL`, or the company details in
  `ENTITY` (that one lives in `build_legal.py`).
- `tools/build_pages.py` — body content for the main pages.
- `tools/build_legal.py` — body content for the policies, and `UPDATED`, the
  "last updated" date shown on each one.

**Bump `UPDATED` whenever you change a policy's substance.** It's the date
visitors and regulators rely on.

The `tools/` folder is not served — it contains no HTML at a routable path —
but you can delete it from the deployed copy if you'd rather keep it out of
the bundle entirely. Keep it in Git either way.

### Adding a new page

1. Add a section to `tools/build_pages.py` following an existing one.
2. Add the route to `sitemap.xml`.
3. Add it to `NAV` in `tools/shell.py` if it belongs in the header.
4. Rebuild.

---

## Design reference

Colours are sampled from the logo artwork and defined once as custom
properties at the top of `assets/css/site.css`:

| Token | Hex | Use |
|---|---|---|
| `--navy` | `#0A1C3E` | Page ground, taken from the logo's ink |
| `--navy-deep` | `#061128` | Alternate darker band |
| `--paper` | `#F5F7FC` | Light bands and all legal pages |
| `--cyan` | `#00B4F0` | Spectrum start, links on dark |
| `--blue` | `#0A78F0` | |
| `--indigo` | `#1A2FD2` | |
| `--violet` | `#7A2BE8` | |
| `--magenta` | `#B516C8` | Spectrum end |
| `--amber` / `--green` | `#F59B3C` / `#4CC45C` | The warm and green app tiles in the mark; used sparingly for status |

The `--spectrum` gradient is used as a structural rule marking section
boundaries, and on primary buttons. It is deliberately not used as background
decoration.

Type is Outfit (display and UI) and IBM Plex Sans (body). Headings pair weight
700 against weight 200 to echo the "Riff Apps" wordmark.

### The hero animation

`assets/js/hero.js` draws a grid of app tiles on a canvas. A diagonal wave
travels through them, tiles lift and brighten under the pointer, and one
occasionally detaches and drifts left before fading — the trailing squares in
the logo. The centre is left clear so the mark sits in open space.

It stops when scrolled out of view or when the tab is hidden, and renders a
single static frame if the visitor has `prefers-reduced-motion` set. Tuning
constants are near the top: `COLS` for grid density, and the multipliers in
`draw()` for brightness and wave speed.

---

## Accessibility

Built to WCAG 2.2 AA, which the Governance page commits to publicly — so it
should stay true:

- Skip link, landmarks, and a visible focus ring on every interactive element
- The mobile menu is a real button with `aria-expanded`, closes on Escape
- Form fields have real labels; status messages use `role="status"`
- The canvas has a text alternative and respects reduced motion
- Colour is never the only carrier of meaning
- Layout holds at 200% zoom and down to 320px wide

If you add components, keep to that bar — a broken claim on the Governance
page is worse than no claim.

---

## Files

```
index.html              Home, with the animated hero
services.html           What you do and how you charge
work.html               Riff, TeachWise AI, energy project controls
governance.html         AI commitments, data protection, security, accessibility
contact.html            Enquiry form
404.html                Not found
legal/                  index + 8 policies
assets/css/site.css     All styling, tokens at the top
assets/css/fonts.css    @font-face for the self-hosted fonts
assets/js/site.js       Nav, footer year, contact form
assets/js/hero.js       Hero canvas animation
assets/fonts/           Outfit + IBM Plex Sans, latin woff2 (196 KB total)
assets/img/             Logo, cropped mark, favicons
tools/                  Page generators (not served)
vercel.json             Routing, headers, caching, redirects
sitemap.xml             Update when you add pages
robots.txt              Allows everything, points at the sitemap
site.webmanifest        Icons and theme colour
```

Fonts are self-hosted from the `@fontsource` packages rather than loaded from
Google Fonts. That's a deliberate choice: it means loading a page makes no
third-party request, no visitor IP is shared with anyone, and the cookie
policy can honestly say the site needs no consent banner. If you swap the
fonts, keep them self-hosted or that claim stops being true.

Contact: Contact@Riff-Apps.com
