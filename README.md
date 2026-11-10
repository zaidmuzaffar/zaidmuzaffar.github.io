# zaid.ops — Portfolio of Zaid Muzaffar

Personal portfolio of a Cloud & DevOps Engineer. The site is designed **like a system**: you enter through a gateway, every section is a service, and the code is split into clear layers — content, styles and behaviour never mix.

Plain **HTML, CSS and JavaScript**. No framework, no build step for the browser, free to host anywhere.

---

## Architecture

```
                ┌──────────────┐
  Visitor ────▶ │  index.html  │  page skeleton (sections, empty slots)
                └──────┬───────┘
                       │ loads
     ┌─────────────────┼──────────────────────────────┐
     ▼                 ▼                              ▼
 CONTENT          STYLES (6 layers)             BEHAVIOUR (modules)
 js/data.js       css/tokens.css     colours,   js/core/app.js      registry + helpers
  profile          fonts, both themes           js/core/render.js   data.js → markup
  sections        css/base.css       reset,     js/core/ui.js       preloader, reveal, scroll
  projects         buttons, motion              js/core/features.js hero, pipeline, filter,
  skills, certs   css/layout.css     nav,                           terminal, GitHub, form,
  timeline         section frame, footer                            analytics
  config          css/components.css cards,     js/core/theme.js    light / dark
                   terminal, palette…           js/core/palette.js  Ctrl + K menu
                  css/sections.css   one block  js/main.js          starts modules in order
                   per section
                  css/case.css       case pages
```

**Rules the code follows**

1. **Content lives only in `js/data.js`.** Projects, skills, certificates, timeline, links and settings. Change the site by editing data, not HTML.
2. **Colours live only in `css/tokens.css`.** Every other file uses variables, which is what makes light/dark mode work.
3. **Every section has the same frame:** `<section id class="wrap section">` → `.section-head` (kicker `NN / name` + title) → content. Headers are generated from `sections` in `data.js`, so the nav, system map, scroll progress and Ctrl + K menu always stay in sync.
4. **Every feature is a module.** It registers with `App.register('name', fn)` and `js/main.js` starts them in a fixed order. A module that finds nothing to do on a page simply returns.

## Page structure

| # | Section | id | What's inside |
|---|---|---|---|
| — | Hero | `top` | Name, typed roles, status dial with portrait |
| 00 | System map | `map` | The site drawn as an architecture diagram — every box links to its section |
| 01 | About | `about` | Intro, live CI/CD pipeline card, quick facts |
| 02 | Experience | `journey` | Internship card with certificate, then the journey timeline |
| 03 | Projects | `projects` | Filterable cards with demos, case studies and PDFs |
| 04 | Stack | `stack` | Skills, certifications (with verify links), languages |
| 05 | Console | `console` | Interactive terminal, GitHub activity, shortcuts |
| 06 | Contact | `contact` | Recommendations (when added), links, contact form |

Between sections, an animated **stage connector** shows data packets moving through a CI/CD stage.

## Features

| Feature | How to use / configure |
|---|---|
| Download CV | Hero button, Contact section, terminal command `cv`, Ctrl + K. File: `docs/Zaid_Muzaffar_CV.pdf` (public version without phone number) |
| Command menu | `Ctrl + K` / `⌘ + K` or the search button. Search sections, projects and actions |
| Light / dark theme | Sun/moon button, terminal command `theme`, or Ctrl + K. The choice is remembered |
| Interactive terminal | `help`, `whoami`, `skills`, `projects`, `certs`, `contact`, `theme`, `clear` |
| GitHub activity | Shows the contribution graph for `config.githubUser` once the site is hosted |
| Contact form | Create a free form at **formspree.io**, paste its ID into `config.formspreeId` |
| Analytics | Create a free site at **goatcounter.com**, paste its code into `config.goatcounter` |
| Recommendations | Add real quotes (with permission) to `recommendations` in `data.js`. Hidden while empty |
| 404 page | `404.html` — GitHub Pages and Firebase show it automatically for broken links |
| Reduced motion | All animation stops if the visitor's system asks for reduced motion |

## Folder structure

```
portfolio/
├── index.html              Home page skeleton
├── 404.html                "Deployment failed" page
├── css/                    tokens → base → layout → components → sections (+ case)
├── js/
│   ├── data.js             ALL content and settings
│   ├── main.js             Starts the modules
│   └── core/               app, render, ui, features, theme, palette
├── projects/               One case study page per project
├── docs/                   Case study PDFs
├── assets/                 Portrait, favicon, project screenshots
└── tools/                  Python scripts that build index.html, 404.html and the case study pages
```

The HTML pages share one head, nav, footer and section connector (`tools/partials.py`). After changing a case study or the page skeleton, run `python3 tools/build_site.py` and `python3 tools/build_cases.py`. Content changes in `js/data.js` need no rebuild.

## Projects and links

| Project | Live / demo | Code | Demo login | Case study PDF |
|---|---|---|---|---|
| Star Pump House | https://starpumphouse.web.app | https://github.com/zaidmuzaffar/star-pump-house | `demo@starpumphouse.com` / `Star123@` | [Full case study](https://github.com/zaidmuzaffar/star-pump-house/blob/main/docs/Star_Pump_House_Full_Case_Study.pdf) |
| Vigil | https://vigil-7fa6b.web.app | — | — (mobile app) | `docs/Vigil_Case_Study.pdf` |
| Skill Go Lab (internship capstone) | — | — | — | `docs/Cloud_DevOps_Internship_Certificate_Zaid_Muzaffar.pdf` (certificate) |
| "Mac" Voice Assistant | — (runs locally) | — | — | `docs/Voice_Assistant_Case_Study.pdf` |
| Linux Automation | — | — | — | `docs/Linux_Automation_Case_Study.pdf` |
| Lawyer–Client Platform (FYP) | — | — | — | `docs/Lawyer_Client_Platform_Case_Study.pdf` |

## Common edits

- **Add a project:** add an object to `projects` in `js/data.js` (title, status, cats, desc, stack, links). It appears in the grid, the filter counts, the terminal and the Ctrl + K menu automatically.
- **Add a skill or certificate:** edit `skills` or `certs` in `js/data.js`.
- **Change colours:** edit `css/tokens.css` (both the dark block and the light block).
- **Change the photo:** replace `assets/zaid.jpg` with a square image (800×800).

## Run locally

```bash
cd portfolio
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy for free

### GitHub Pages (gives `zaidmuzaffar.github.io`)
1. Create a **public** repository named exactly `zaidmuzaffar.github.io`.
2. Put all files from this folder in it and push.
3. Repository → **Settings → Pages** → Deploy from a branch → `main` / `(root)` → Save.
4. After about a minute the site is live at **https://zaidmuzaffar.github.io**.

### Firebase Hosting
```bash
npm install -g firebase-tools
firebase login
firebase init hosting      # public directory: .   single-page app: No
firebase deploy --only hosting
```

## Case study PDFs

Open a case study page in Chrome → Print → Save as PDF with **Background graphics** on. Print styles hide the navigation and keep cards together.

© Zaid Muzaffar
