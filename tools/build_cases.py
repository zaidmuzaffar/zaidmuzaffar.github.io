"""Builds the case-study pages for the portfolio from one shared template."""
import os, re, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partials import divider

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'projects')

from partials import head as _head, nav as _nav, footer as _footer, scripts as _scripts

def HEAD_FOR(title, desc):
    return (_head(title + ' — Case study · Zaid Muzaffar', desc, base='../', extra_css=['case']) +
            '\n<body data-base="../">\n<div class="toast" role="status" aria-live="polite"></div>\n' +
            _nav(base='../', links_html='<nav class="nav-links"><a href="../index.html#projects" style="display:inline-block">all projects</a></nav>', cta_href='../index.html#contact') +
            '\n<main>\n')

FOOT = '</main>\n' + _footer('../') + '\n' + _scripts('../') + '\n</body>\n</html>\n'

ARROW = '<div class="flow-arrow" aria-hidden="true"><svg viewBox="0 0 36 14"><path class="flow" d="M0 7 H30" stroke="currentColor" stroke-width="3" fill="none"/><path d="M26 2 L33 7 L26 12" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg></div>'


def flow(nodes):
    parts = []
    for i, (b, s) in enumerate(nodes):
        if i:
            parts.append(ARROW)
        parts.append(f'<div class="flow-node"><b>{b}</b><span>{s}</span></div>')
    return '<div class="flow-diagram">' + ''.join(parts) + '</div>'


def features(items):
    return '<div class="feature-grid">' + ''.join(
        f'<div class="feature"><b>{b}</b><span>{s}</span></div>' for b, s in items) + '</div>'


def table(head, rows):
    h = ''.join(f'<th>{c}</th>' for c in head)
    r = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<div class="table-box"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def page(p):
    sections = p['sections']
    toc = ''.join(f'<a href="#{sid}">{i+1:02d} {name.lower()}</a>' for i, (sid, name, _) in enumerate(sections))
    body = ''.join(
        f'<section id="{sid}" class="reveal"><h2><span class="num">{i+1:02d} / {name.lower()}</span>{name}</h2>{content}</section>'
        for i, (sid, name, content) in enumerate(sections))
    meta = ''.join(f'<div><small>{k}</small><b>{v}</b></div>' for k, v in p['meta'])
    links = ''.join(p['links'])
    demo = p.get('demo', '')
    nxt = p['next']
    out = HEAD_FOR(html.escape(p['title']), html.escape(p['lead'])) + f'''
<section class="wrap case-hero">
  <a class="back" href="../index.html#projects">← all projects</a>
  <span class="label"><span class="dot"></span>{p['kicker']}</span>
  <h1 class="reveal">{p['h1']}</h1>
  <p class="lead reveal d1">{p['lead']}</p>
  <div class="meta reveal d2">{meta}</div>
  {demo}
  <div class="case-links reveal d3">{links}</div>
</section>
''' + divider('case study','plan ✓','ship ✓') + f'''
<div class="wrap case-body">
  <nav class="toc" aria-label="On this page">{toc}</nav>
  <div class="case-content">
    {body}
    <a class="next-case" href="{nxt[0]}"><span><small>next case study</small><b>{nxt[1]}</b></span><span aria-hidden="true" style="font-size:28px;color:var(--accent)">→</span></a>
  </div>
</div>
''' + FOOT
    with open(os.path.join(OUT, p['file']), 'w') as f:
        f.write(out)


def btn(href, text, main=False):
    return f'<a class="btn {"btn-primary" if main else "btn-ghost"}" href="{href}">{text}</a>'


# =====================================================================
# 1. STAR PUMP HOUSE
# =====================================================================
SPH = dict(
    file='star-pump-house.html',
    title='Star Pump House',
    kicker='CASE STUDY 01 · LIVE IN DAILY USE',
    h1='Star Pump House<br><span style="color:var(--accent)">Shop Management System</span>',
    lead='A full-stack web app that replaced paper registers in our family\'s pump and hardware shop: stock, sales, credit, suppliers, wholesale accounts, cash closing, profit — and an AI assistant that speaks Roman Urdu.',
    meta=[('ROLE', 'Sole developer: design, build, deploy, maintain'), ('USERS', 'My brother (owner) + salesman'),
          ('STACK', 'JavaScript · Firebase · Gemini'), ('STATUS', 'Live · 57 releases'), ('HOSTING COST', 'Free (Firebase Spark plan)')],
    demo='''<div class="demo-box reveal d2" style="max-width:520px">
    <div class="row"><span class="k">email</span><span class="v">demo@starpumphouse.com</span><button class="copy-btn" type="button" data-copy="demo@starpumphouse.com" aria-label="Copy demo email">copy</button></div>
    <div class="row"><span class="k">password</span><span class="v">Star123@</span><button class="copy-btn" type="button" data-copy="Star123@" aria-label="Copy demo password">copy</button></div>
    <span class="demo-note">The demo account holds made-up products, customers and sales. It is completely separate from the real shop's data.</span>
  </div>''',
    links=[btn('https://starpumphouse.web.app', 'Open live demo ↗', True), btn('https://github.com/zaidmuzaffar/star-pump-house', 'Source code ↗'), btn('https://github.com/zaidmuzaffar/star-pump-house/blob/main/docs/Star_Pump_House_Full_Case_Study.pdf', 'Case study PDF ↗')],
    next=('vigil.html', 'Vigil — Fall Detection & Live Location'),
    sections=[
        ('problem', 'The problem', '''
<p>Star Pump House sells water pumps, wire, safety cable and hardware, and also supplies other shops wholesale on credit. Everything lived in notebooks: stock, daily sales, customer credit (<em>udhaar</em>), supplier bills and the accounts of the shops we supply.</p>
<p>That caused the same questions every day, with no quick answer:</p>
<ul><li>What is running low, and what is already on its way from a supplier?</li>
<li>Who owes us money, how much, and since when?</li>
<li>How much cash <em>should</em> be in the drawer tonight?</li>
<li>What did we actually earn this month after costs and expenses?</li></ul>
<div class="callout brass"><span class="mono">CONSTRAINTS</span><p>It had to cost nothing to run, work on a laptop and a phone at the counter, be simple enough for someone who isn't a developer, and keep each account's data private. I was a beginner at coding when I started.</p></div>'''),
        ('role', 'My role', '''
<p>I did everything end to end: gathered requirements from the counter, designed the screens, built and tested every page, set up security and deployment, and kept shipping improvements based on real feedback. My brother runs the shop and is the main user, which made every rough edge visible fast.</p>'''),
        ('solution', 'What I built', features([
            ('Stock by category', 'Pumps, wire, safety cable and other items, each with its own fields. Wire and cable are tracked in feet; bundle counts drop automatically as footage is sold.'),
            ('Sell flow', 'Multi-product bills, cash or credit, partial payments with a remaining-balance tracker, and a guard that blocks selling above the listed price.'),
            ('Credit (udhaar)', 'A pending-payments page grouped by bill, with bulk "mark received", and received records kept visible with a green badge.'),
            ('Suppliers & wholesale', 'Purchases, supplier balances and separate accounts for the shops we supply.'),
            ('Cash closing', 'A daily count of the drawer that knows exactly how much should be there.'),
            ('Profit & charts', 'Profit after costs and expenses; daily, weekly, monthly and overall charts with averages, highs and change.'),
            ('Salesman login', 'A separate role that can sell but cannot see the accounts — enforced by Firestore security rules, not just hidden in the UI.'),
            ('Receipts', 'PDF receipts and customer statements generated in the browser, shareable on WhatsApp.'),
            ('Ask AI', 'An assistant that answers questions from the shop\'s own records in English or Roman Urdu and opens pre-filled forms that the owner confirms before saving.'),
        ]) + '<p>Plus dark mode, a phone layout with a "laptop view" toggle, voice input, backup &amp; restore and a morning summary report.</p>'),
        ('architecture', 'Architecture', flow([
            ('Browser', 'Plain HTML, CSS and JavaScript modules — no build step'),
            ('Firebase Auth', 'Email/password; session-only login'),
            ('Cloud Firestore', 'All data under <code>users/{uid}/…</code>'),
            ('Firebase Hosting', 'Static files on a free global CDN'),
        ]) + '''
<p>The AI assistant uses <strong>Gemini through Firebase AI Logic</strong> with function calling: the model can look up records and propose an action (a sale, a payment received, a new product), but it only ever <strong>opens a pre-filled form</strong>. A person presses Save.</p>
<p>Abuse protection uses <strong>App Check with reCAPTCHA Enterprise</strong>, and the browser API key is restricted to the app's own domains.</p>'''),
        ('decisions', 'Key decisions', table(
            ['Decision', 'Why'],
            [['Firebase instead of MongoDB + Node.js', 'No server to run or pay for; Auth, database and hosting in one free plan — right for a one-person project.'],
             ['Multi-tenant data under <code>users/{uid}</code>', 'Every signed-up account sees only its own data; this is also what lets the public demo sit safely next to the real shop.'],
             ['Roles in security rules', 'A salesman account is limited on the server, so hiding a button is never the only protection.'],
             ['AI proposes, human saves', 'Money records must be correct; the model fills forms but never writes on its own.'],
             ['Session-only login', 'A shared counter laptop should not stay signed in after the browser closes.'],
             ['Client-side PDFs', 'Receipts work without a server and cost nothing.']])),
        ('challenges', 'Challenges', '''
<h3>Selling by the foot</h3><p>Wire is bought in bundles but sold by length. I modelled price-per-foot and footage, and made the bundle count fall automatically as feet are sold, so stock always matches the shelf.</p>
<h3>One bill, many products, partial payment</h3><p>A customer may buy three items, pay part now and the rest later. The remaining balance is split proportionally across the items, kept in sync between Sales and Pending Payments, and the rows are grouped back into one bill by their shared timestamp.</p>
<h3>Free-tier limits</h3><p>Firestore's free plan allows a fixed number of reads per day. I learned how page loads translate into reads, watched usage in the console, and planned date-limited loading for when the sales history grows.</p>
<h3>Security as a beginner</h3><p>I learned that a Firebase API key is meant to be public, and that real protection comes from security rules, App Check and domain restrictions — and set up all three.</p>'''),
        ('process', 'How I shipped it', '''
<p>I built it in small, numbered releases — <strong>57 so far</strong>. Each one changed only what was needed and was tested in a headless browser against a stubbed Firebase with seeded fake data before it reached the shop. Feedback from the counter decided the next release: a slow page, a confusing message or a missing field became the next update.</p>'''),
        ('results', 'Results', '''
<ul><li>The shop uses it every day in place of paper registers.</li>
<li>Stock, credit and profit questions are now answered in seconds instead of by flipping through notebooks.</li>
<li>It runs on Firebase's free plan, so hosting costs nothing.</li>
<li>A public demo with fake data lets anyone try every screen without touching real records.</li></ul>'''),
        ('learned', 'What I learned', '''
<ul><li>Designing data models around how a business actually works (feet vs units, partial payments, wholesale).</li>
<li>Thinking about security on the server side: rules, roles, App Check.</li>
<li>Shipping in small increments with testing, and treating user feedback as the roadmap.</li>
<li>Using an LLM safely in a money-handling app: tools, not autonomy.</li></ul>'''),
        ('screens', 'Screenshots', '''
<p>All screenshots use the demo account's made-up data.</p>
<figure class="shot"><img src="../assets/sph/dashboard.jpg" alt="Dashboard with morning report, KPIs and sales chart" loading="lazy"><figcaption>Dashboard — morning report, KPIs and the sales chart</figcaption></figure>
<figure class="shot"><img src="../assets/sph/sales.jpg" alt="Sales summary with one row per customer bill" loading="lazy"><figcaption>Sales Summary — one row per bill, with receipt PDF and WhatsApp sharing</figcaption></figure>
<div class="shot-pair">
<figure class="shot"><img src="../assets/sph/ai.jpg" alt="Ask AI assistant answering in Roman Urdu" loading="lazy"><figcaption>Ask AI — answers from the shop's records and opens a pre-filled form</figcaption></figure>
<figure class="shot"><img src="../assets/sph/phone.jpg" alt="Phone layout" loading="lazy"><figcaption>Phone layout</figcaption></figure>
</div>'''),
        ('documents', 'Documents', '''
<p>The full write-ups live in the project's GitHub repository.</p>
<div class="doc-list">
<a class="doc" href="https://github.com/zaidmuzaffar/star-pump-house/blob/main/docs/Star_Pump_House_Full_Case_Study.pdf"><span class="doc-ic">PDF</span><span><b>Full case study</b><small>18 pages · problem, design, build, results</small></span></a>
<a class="doc" href="https://github.com/zaidmuzaffar/star-pump-house/blob/main/docs/Star_Pump_House_Project_Overview.pdf"><span class="doc-ic">PDF</span><span><b>Project overview</b><small>Features, architecture and tech stack</small></span></a>
<a class="doc" href="https://github.com/zaidmuzaffar/star-pump-house/blob/main/docs/Star_Pump_House_UI_Screenshots.pdf"><span class="doc-ic">PDF</span><span><b>UI screenshots</b><small>Every screen: desktop, dark mode and phone</small></span></a>
<a class="doc" href="https://github.com/zaidmuzaffar/star-pump-house#readme"><span class="doc-ic">MD</span><span><b>Technical documentation (README)</b><small>Data model, setup, deploying, security, AI assistant</small></span></a>
</div>'''),
        ('docs', 'Documentation', '''
<h3>Repository structure</h3>
<p><code>src/</code> holds the web app (HTML pages, CSS, JavaScript modules, Firebase config). <code>docs/</code> holds the full case study, UI screenshots and project overview as PDFs.</p>
<h3>Run it locally</h3>
<ol><li>Clone <code>github.com/zaidmuzaffar/star-pump-house</code>.</li>
<li>Create a Firebase project; enable Email/Password Auth and Firestore; paste your web config into the Firebase config file.</li>
<li>Install the CLI: <code>npm install -g firebase-tools</code>, then <code>firebase login</code>.</li>
<li>Serve locally with <code>firebase serve</code>, or deploy with <code>firebase deploy</code>.</li></ol>
<h3>Data model</h3>
<p>Each account's collections — products, sales, upcoming products, suppliers, shops, expenses and more — live under <code>users/{uid}</code>, which keeps accounts isolated and makes per-user security rules simple.</p>'''),
    ],
)

# =====================================================================
# 2. VIGIL
# =====================================================================
VIGIL = dict(
    file='vigil.html',
    title='Vigil',
    kicker='CASE STUDY 02 · IN ACTIVE DEVELOPMENT',
    h1='Vigil<br><span style="color:var(--accent)">Fall detection &amp; live location</span>',
    lead='A free safety app for iPhone and Android. A small neural network on the phone watches for falls; if you don\'t answer "Are you okay?", the people in your circle get a full-screen alert with your live location.',
    meta=[('ROLE', 'Sole developer: app, ML model, backend'), ('PLATFORMS', 'Android & iOS (Flutter)'),
          ('ML', '1D CNN · SisFall · TensorFlow Lite'), ('BACKEND', 'Firebase Auth · Firestore · Hosting'), ('STATUS', 'Working app · model fine-tuning')],
    links=[btn('https://vigil-7fa6b.web.app', 'Project site ↗', True), btn('../docs/Vigil_Case_Study.pdf', 'Case study PDF ↓')],
    next=('voice-assistant.html', '"Mac" — Voice AI Assistant'),
    sections=[
        ('problem', 'The problem', '''
<p>When someone falls and can't get up — an elderly parent, a person working alone, anyone — the minutes before help arrives matter. Most fall-detection solutions rely on a dedicated watch or a paid service. I wanted something that works with <strong>only the phone people already carry</strong>, costs nothing, and alerts the specific people who would actually come.</p>'''),
        ('solution', 'What it does', features([
            ('On-device fall detection', 'A neural network runs on the phone itself — no audio or motion data leaves the device for detection.'),
            ('"Are you okay?" countdown', 'After a suspected fall, a countdown gives the person a chance to cancel a false alarm.'),
            ('Full-screen circle alerts', 'If there\'s no answer, everyone in the circle gets a full-screen alert with a loud alarm and strong vibration.'),
            ('SOS button', 'Trigger the same alert manually at any time.'),
            ('Live location & ETA', 'Helpers tap "on my way"; the person in trouble and the circle see them approach on a map with an ETA.'),
            ('Invite-link circles', 'Start alone, then add family by sharing a link. Circles work like groups, with admins and permissions.'),
            ('Privacy controls', 'Per-person choices about who sees location and who receives alerts.'),
            ('Movement recorder', 'A built-in recorder to capture real phone movement for fine-tuning the model.'),
        ])),
        ('ml', 'The ML model', flow([
            ('SisFall dataset', 'Accelerometer recordings of falls and daily activities'),
            ('Preprocess', 'Resampled to 50 Hz, cut into windows'),
            ('1D CNN', 'Trained in Google Colab'),
            ('Evaluate', 'Subject-independent split'),
            ('TensorFlow Lite', 'Shipped inside the app'),
        ]) + '''
<p>The model is evaluated <strong>subject-independently</strong>: people in the test set are never seen in training, which is closer to how it behaves for a new user.</p>
<p>In the app, inference is wrapped in simple logic that keeps the battery and false alarms down: the model only runs after an <strong>impact above 1.6 g</strong>, checks every <strong>0.5 s</strong>, and has a <strong>60-second cooldown</strong> after an alert.</p>
<div class="callout brass"><span class="mono">HONEST STATUS</span><p>Lab datasets are recorded with sensors strapped to the body, but a phone sits in a pocket, a hand or a bag. In real use the first model raised false alarms during normal movement, so I built the recorder and a fine-tuning notebook that mixes SisFall with my own phone recordings at a low learning rate. Final evaluation numbers will be published here once the real-device data is complete.</p></div>'''),
        ('architecture', 'Architecture', flow([
            ('Flutter app', 'Sensors, model, alerts, maps'),
            ('Firebase Auth', 'Google, email or anonymous sign-in'),
            ('Cloud Firestore', 'Circles, members, alerts, locations — guarded by security rules'),
            ('Firebase Hosting', 'Invite links: <code>/join/CODE</code> opens the app'),
        ]) + '''<p>Invite links are real web URLs. On Android they open the app directly through verified app links; on iPhone (without a paid Apple account) a small page offers an "Open in Vigil" button that hands the code to the app.</p>'''),
        ('challenges', 'Challenges', '''
<h3>False alarms from everyday movement</h3><p>Sitting down hard or dropping the phone can look like a fall. The answer was better data from real phone placements (pocket, hand, bag, table), a fine-tuning pipeline, and the countdown so a person can cancel.</p>
<h3>An alarm that must be heard</h3><p>An alert is useless if it follows the media volume. I configured the audio session so the alarm stays loud with strong vibration even when the phone volume is turned down.</p>
<h3>Alerts while the app is in the background</h3><p>iOS limits background work. Getting alerts to arrive reliably when the app isn't open required notification and background handling specific to each platform.</p>
<h3>Maps for everyone</h3><p>The default map tiles repeated the world and showed local-language labels. I switched to tiles with English labels, limited zoom to one world, and added a satellite toggle.</p>'''),
        ('learned', 'What I learned', '''
<ul><li>The gap between a model that scores well on a dataset and one that works in a pocket — and how to close it with data.</li>
<li>Building a real-time multi-user app on Firestore with security rules that protect location data.</li>
<li>Mobile platform realities: background limits, deep links, audio sessions, permissions.</li></ul>'''),
        ('docs', 'Documentation', '''
<h3>Project layout</h3>
<p><code>app/</code> is the Flutter app only. <code>ml/</code> holds the Colab notebooks (<code>vigil_fall_detection.ipynb</code>, <code>vigil_finetune.ipynb</code>) and the exported <code>vigil_fall_model.tflite</code> with its config. <code>web/</code> is the Firebase Hosting site for invite links. <code>docs/</code> holds the architecture notes and security rules.</p>
<h3>Run the app</h3>
<ol><li>Install Flutter and the FlutterFire CLI.</li>
<li><code>flutterfire configure</code> with your own Firebase project (config files are not committed).</li>
<li><code>flutter run</code> on an Android emulator or a connected iPhone.</li></ol>
<h3>Retrain the model</h3>
<p>Open <code>vigil_finetune.ipynb</code> in Colab with a T4 GPU, point it at your recordings, run all cells, and copy the new <code>.tflite</code> and config into <code>app/assets/models/</code>. No code changes are needed.</p>'''),
    ],
)

# =====================================================================
# 3. VOICE ASSISTANT
# =====================================================================
VOICE = dict(
    file='voice-assistant.html',
    title='"Mac" Voice AI Assistant',
    kicker='CASE STUDY 03 · IN ACTIVE DEVELOPMENT',
    h1='"Mac"<br><span style="color:var(--accent)">A voice assistant that does things</span>',
    lead='An always-on assistant for my MacBook that wakes on its name, talks back in natural Urdu or English, and actually controls the laptop — with spoken confirmation before anything destructive.',
    meta=[('ROLE', 'Sole developer'), ('PLATFORM', 'macOS (Apple Silicon)'), ('BRAIN', 'Gemini Live · Ollama fallback'),
          ('LANGUAGES', 'Urdu & English'), ('STATUS', 'Working daily build')],
    links=[btn('../docs/Voice_Assistant_Case_Study.pdf', 'Case study PDF ↓', True)],
    next=('linux-automation.html', 'Linux System Administration Automation'),
    sections=[
        ('goal', 'The goal', '''
<p>Voice assistants rarely understand Pakistani Urdu, and they mostly answer questions rather than <em>doing</em> things. I wanted an assistant that feels like talking to a person — fast, natural turn-taking, replies in the language I spoke — and can carry out real tasks on my laptop for free.</p>'''),
        ('features', 'What it does', features([
            ('Wake word', 'Always listening in the background for its name, "Mac" — it answers "جی زید؟" and is ready.'),
            ('Natural conversation', 'Follow-up questions without repeating the wake word, with memory of recent context.'),
            ('Two languages', 'Replies in Urdu when spoken to in Urdu, English when spoken to in English.'),
            ('Laptop control', 'Opens apps, plays YouTube videos, checks the weather, takes screenshots, changes volume.'),
            ('WhatsApp', 'Sends messages to contacts by name, then reports back "ہو گیا".'),
            ('Safe by design', 'Restart, shutdown and deleting files need a spoken "jee" before anything happens.'),
        ])),
        ('evolution', 'Architecture — three versions', '''
<h3>v1 · Fully local</h3>''' + flow([('Speech-to-text', 'Local transcription'), ('Ollama · Qwen 2.5', 'Local LLM on the M2 Pro'), ('Text-to-speech', 'Spoken reply')]) + '''
<p>Free and private, but the 7B model produced broken, repetitive Urdu.</p>
<h3>v2 · Cloud first, local fallback</h3>''' + flow([('Speech-to-text', 'Transcribe'), ('Gemini API', 'Fallback chain of models'), ('Ollama 14B', 'Used when offline'), ('Text-to-speech', 'Human-like voice')]) + '''
<p>Much better Urdu, but three stages in a row (transcribe → think → speak) were too slow for natural conversation.</p>
<h3>v3 · Real-time native audio</h3>''' + flow([('Microphone', 'Streamed audio'), ('Gemini Live API', 'Listens and speaks natively'), ('Tool calls', 'macOS actions'), ('Speaker', 'Near-instant reply')]) + '''
<p>Gemini Live hears and speaks audio directly, removing two of the three stages. The local Qwen 2.5 14B model stays as the offline fallback.</p>'''),
        ('challenges', 'Challenges', '''
<h3>Urdu quality</h3><p>The small local model repeated itself. Moving to the 14B model and tuning generation (a repeat penalty and a token cap) fixed the loops.</p>
<h3>Overloaded models and timeouts</h3><p>Free-tier models sometimes returned "high demand" errors. I built an ordered fallback chain. Setting the API timeout too low made the server reject requests, so the server timeout stays at 10 s while a shorter app-level timeout — a background thread and a queue — moves on to the next model.</p>
<h3>Hearing itself</h3><p>The assistant could mishear its own speech, or background noise in a busy shop, as the wake word. I tightened when it listens and how it confirms it was addressed.</p>
<h3>macOS permissions</h3><p>Controlling apps needs Accessibility, Automation, Screen Recording and Full Disk Access. I learned what each permission unlocks and how to tell a permission problem from an API problem.</p>
<h3>Finding the right contact</h3><p>Spoken names don't match contact names exactly; matching had to be forgiving without ever messaging the wrong person.</p>'''),
        ('learned', 'What I learned', '''
<ul><li>Latency is a product feature: architecture choices decide whether a conversation feels human.</li>
<li>Designing failover between cloud and local models.</li>
<li>Giving an AI real power over a computer safely — confirmations for anything destructive.</li></ul>'''),
        ('docs', 'Documentation', '''
<h3>Requirements</h3>
<p>macOS on Apple Silicon, Python 3.11, Homebrew, ffmpeg, and Ollama with <code>qwen2.5:14b</code> pulled for offline use. A free Gemini API key for online mode.</p>
<h3>Setup</h3>
<ol><li><code>ollama pull qwen2.5:14b</code></li>
<li>Create a virtual environment and install the Python requirements.</li>
<li>Add the Gemini key to the environment.</li>
<li>Grant the terminal Accessibility, Automation, Screen Recording and Full Disk Access in System Settings.</li>
<li>Run the assistant; it starts in the background and waits for "Mac".</li></ol>'''),
    ],
)

# =====================================================================
# 4. LINUX AUTOMATION
# =====================================================================
LINUX = dict(
    file='linux-automation.html',
    title='Linux System Administration Automation',
    kicker='CASE STUDY 04 · CLOUD & DEVOPS',
    h1='Linux sysadmin<br><span style="color:var(--accent)">automation with Bash</span>',
    lead='A set of modular Bash scripts that turn repetitive server chores — user access, environment setup, process monitoring, log parsing and health checks — into single, repeatable commands.',
    meta=[('ROLE', 'Sole developer'), ('STACK', 'Linux · Bash · Git'), ('FOCUS', 'Operations automation'), ('STATUS', 'Complete')],
    links=[btn('../docs/Linux_Automation_Case_Study.pdf', 'Case study PDF ↓', True), btn('https://github.com/zaidmuzaffar', 'GitHub profile ↗')],
    next=('lawyer-client.html', 'Lawyer–Client Matching Platform'),
    sections=[
        ('why', 'Why I built it', '''
<p>Doing the same server tasks by hand is slow and error-prone: a missed step when creating a user, a forgotten environment variable, a log nobody reads until something breaks. The DevOps idea I wanted to practice is simple — <strong>if you do it twice, script it</strong>.</p>'''),
        ('scripts', 'What the scripts do', features([
            ('User access management', 'Create, modify and remove users and their permissions consistently.'),
            ('Environment setup', 'Set up environment variables and configuration the same way every time.'),
            ('Process monitoring', 'Check that important processes are running and report the ones that aren\'t.'),
            ('Log parsing', 'Scan logs automatically and pull out the lines that matter.'),
            ('Health checks', 'Routine checks of system health to streamline maintenance.'),
            ('Version control', 'Scripts and configuration documentation managed in Git and GitHub.'),
        ])),
        ('design', 'Design', '''
<p>Each script does one job and can be run on its own or combined with the others. Keeping them modular made them easier to test, reuse and document — the same principle behind larger automation and infrastructure-as-code tools.</p>
<p>The foundation came from my Operating Systems course, where I worked in Ubuntu from the command line throughout: files and directories, processes, threads, concurrency and scheduling.</p>'''),
        ('learned', 'What I learned', '''
<ul><li>Writing Bash that is safe to run more than once.</li>
<li>Thinking in terms of repeatable operations instead of one-off commands.</li>
<li>Documenting operational work so someone else can run it.</li></ul>
<p>This is the base I'm building on for DevOps: next come CI/CD pipelines, containers and infrastructure as code.</p>'''),
    ],
)

# =====================================================================
# 5. LAWYER-CLIENT (FYP)
# =====================================================================
LAWYER = dict(
    file='lawyer-client.html',
    title='Lawyer–Client Matching Platform',
    kicker='CASE STUDY 05 · FINAL YEAR PROJECT',
    h1='Lawyer–Client<br><span style="color:var(--accent)">Matching Platform</span>',
    lead='My final year project at COMSATS: a web platform that helps clients find the right lawyer by expertise and search criteria, built end to end from database to interface.',
    meta=[('CONTEXT', 'Final Year Project, COMSATS Abbottabad'), ('STACK', 'React · Node.js · Express · MongoDB'), ('YEAR', '2025–2026'), ('STATUS', 'Complete')],
    links=[btn('../docs/Lawyer_Client_Platform_Case_Study.pdf', 'Case study PDF ↓', True), btn('https://github.com/zaidmuzaffar', 'GitHub profile ↗')],
    next=('star-pump-house.html', 'Star Pump House — Shop Management System'),
    sections=[
        ('problem', 'The problem', '''
<p>Finding a lawyer usually depends on word of mouth. A client with a specific legal issue has no easy way to compare lawyers by what they actually practice. The platform brings both sides together and matches them on expertise and search parameters.</p>'''),
        ('built', 'What I built', features([
            ('Matching & search', 'Clients find lawyers by area of expertise and other search criteria.'),
            ('REST API', 'Express endpoints for secure data exchange between the React front end and the database.'),
            ('Data model', 'MongoDB schemas for clients, lawyers and their interactions.'),
            ('Payments', 'API endpoints for payment processing.'),
        ])),
        ('architecture', 'Architecture', flow([
            ('React', 'Single-page front end'),
            ('Node.js + Express', 'REST API'),
            ('MongoDB', 'Document database'),
        ]) + '''<p>I set up production-like environments: environment variables for secrets and configuration, CORS policies between front end and API, and server deployment configuration.</p>'''),
        ('learned', 'What I learned', '''
<ul><li>Designing a full MERN application from the schema up.</li>
<li>Building and securing REST APIs.</li>
<li>Configuration management across environments — an early taste of the DevOps side of software.</li></ul>'''),
    ],
)

for p in (SPH, VIGIL, VOICE, LINUX, LAWYER):
    page(p)
print('ok', os.listdir(OUT))
