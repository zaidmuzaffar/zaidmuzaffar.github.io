"""Builds index.html and 404.html from the shared partials.
Lists (projects, skills, timeline…) are filled at runtime from js/data.js."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partials import head, nav, footer, scripts, divider

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

INDEX = head('Zaid Muzaffar — Cloud & DevOps Engineer',
             'Zaid Muzaffar — Cloud & DevOps Engineer. CI/CD, containers, AWS and real shipped products: case studies, demos and contact.') + '''
<body data-base="">

<!-- Boot screen: a deploy runs before the page opens -->
<div class="preloader" aria-hidden="true">
  <div class="boot">
    <div class="boot-line">$ git push origin main</div>
    <div class="boot-line">› build &nbsp;<span class="ok">✓</span> &nbsp;› test &nbsp;<span class="ok">✓</span> &nbsp;› deploy</div>
    <div class="boot-bar"><div class="boot-fill"></div></div>
    <div class="boot-pct">DEPLOYING <span>0</span>%</div>
  </div>
</div>

<!-- Scroll progress: one node per section (built from data.js) -->
<nav class="scroll-pipe" aria-label="Section progress"><div class="scroll-pipe-fill"></div><div id="scroll-nodes"></div></nav>
<div class="toast" role="status" aria-live="polite"></div>

''' + nav() + '''

<main id="top">

  <!-- ============ HERO ============ -->
  <section class="wrap hero" aria-label="Introduction">
    <div class="hero-text">
      <div class="label reveal"><span class="dot"></span>SYSTEM ONLINE · ISLAMABAD, PAKISTAN</div>
      <h1 class="reveal d1">Zaid<br><span class="accent">Muzaffar</span><span class="caret">_</span></h1>
      <div class="hero-role reveal d2">&gt; <span class="typed"></span><span class="caret">|</span></div>
      <p class="hero-lead reveal d2">I automate the path from code to production — CI/CD pipelines, containers and cloud infrastructure — and I ship real products along the way: a live business system, an on-device AI safety app and a bilingual voice assistant.</p>
      <div class="hero-actions reveal d3">
        <a href="#projects" class="btn btn-primary">View my projects <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        <a href="https://www.linkedin.com/in/zaid-muzaffar-57329237a/" class="btn btn-ghost">LinkedIn</a>
        <a href="https://github.com/zaidmuzaffar" class="btn btn-ghost">GitHub</a>
      </div>
    </div>
    <aside class="card status-card reveal d4" aria-label="Current role">
      <div class="status-top"><span>SYSTEM STATUS</span><span class="live">● 200 OK</span></div>
      <div class="gauge">
        <svg viewBox="0 0 220 210" aria-hidden="true">
          <path class="g-track" d="M45 175 A92 92 0 1 1 175 175" fill="none" stroke-width="12" stroke-linecap="round"/>
          <path class="g-arc cyan" d="M45 175 A92 92 0 1 1 175 175" fill="none" stroke-width="12" stroke-linecap="round"/>
          <path class="g-arc amber" d="M45 175 A92 92 0 1 1 175 175" fill="none" stroke-width="12" stroke-linecap="round"/>
          <circle class="g-ring" cx="110" cy="110" r="76" fill="none" stroke-width="1.5" stroke-dasharray="3 9" opacity=".7"/>
          <g class="g-needle"><circle class="a" cx="110" cy="18" r="9"/><circle class="b" cx="110" cy="18" r="4"/></g>
        </svg>
        <img src="assets/zaid.jpg" alt="Portrait of Zaid Muzaffar" width="400" height="400">
      </div>
      <div class="status-role">Cloud &amp; DevOps Engineer</div>
      <div class="mini-grid">
        <div class="mini"><small>DEGREE</small><b>BS CS · 2026</b></div>
        <div class="mini"><small>FOCUS</small><b>Cloud Solution Architecture</b></div>
      </div>
    </aside>
  </section>

  <div class="marquee" aria-hidden="true">
    <div class="marquee-track">
      <span>CI/CD</span><i>◆</i><span>DOCKER</span><i>◆</i><span>KUBERNETES</span><i>◆</i><span>AWS</span><i>◆</i><span>IAM</span><i>◆</i><span>VPC</span><i>◆</i><span>S3</span><i>◆</i><span>TERRAFORM</span><i>◆</i><span>LINUX</span><i>◆</i><span>GITHUB ACTIONS</span><i>◆</i><span>FIREBASE</span><i>◆</i><span>FLUTTER</span><i>◆</i>
      <span>CI/CD</span><i>◆</i><span>DOCKER</span><i>◆</i><span>KUBERNETES</span><i>◆</i><span>AWS</span><i>◆</i><span>IAM</span><i>◆</i><span>VPC</span><i>◆</i><span>S3</span><i>◆</i><span>TERRAFORM</span><i>◆</i><span>LINUX</span><i>◆</i><span>GITHUB ACTIONS</span><i>◆</i><span>FIREBASE</span><i>◆</i><span>FLUTTER</span><i>◆</i>
    </div>
  </div>

  <!-- ============ 00 · SYSTEM MAP ============ -->
  <section id="map" class="wrap section" style="padding-top:72px">
    <div class="section-head reveal" data-head data-sub="This portfolio is laid out like a system: you come in through the gateway and every section is a service. Click any box to jump to it."></div>
    <div class="card sysmap reveal" id="sysmap"></div>
  </section>

  ''' + divider('01 · about', 'commit', 'push ✓') + '''

  <!-- ============ 01 · ABOUT ============ -->
  <section id="about" class="wrap section">
    <div class="section-head reveal" data-head></div>
    <div class="about-grid">
      <div class="card about-main reveal">
        <p class="big">I like systems that run themselves: code goes in, tests run, containers build, infrastructure updates, and a working release comes out the other end — every time.</p>
        <p>I studied Computer Science at COMSATS University Islamabad, Abbottabad Campus (2021–2026). Along the way I built and shipped real software end to end — a production web app used every day, a Flutter safety app with an on-device neural network, and a voice assistant that controls macOS — handling everything from the database to deployment myself.</p>
        <p>Today I work as a <strong>Cloud &amp; DevOps Engineer</strong>: CI/CD pipelines, Docker and Kubernetes, AWS networking and security (IAM, VPC, S3), and infrastructure as code. My goal is simple — make shipping software boring, fast and safe.</p>
      </div>
      <div class="card pipeline-card reveal d2" aria-label="Example CI/CD pipeline">
        <div class="pc-head"><span class="mono">PIPELINE #128 · main</span><span class="pc-badge">running</span></div>
        <ol class="pc-stages">
          <li class="pc-stage"><span class="pc-icon"></span><b>Checkout</b><small>git clone</small></li>
          <li class="pc-stage"><span class="pc-icon"></span><b>Build</b><small>docker build</small></li>
          <li class="pc-stage"><span class="pc-icon"></span><b>Test</b><small>unit + lint</small></li>
          <li class="pc-stage"><span class="pc-icon"></span><b>Push</b><small>registry</small></li>
          <li class="pc-stage"><span class="pc-icon"></span><b>Deploy</b><small>kubectl apply</small></li>
        </ol>
        <p class="pc-foot">Automate everything. Ship small. Monitor always.</p>
      </div>
      <div class="facts reveal" id="facts"></div>
    </div>
  </section>

  ''' + divider('02 · journey', 'checkout ✓', 'build ✓') + '''

  <!-- ============ 02 · JOURNEY ============ -->
  <section id="journey" class="wrap section">
    <div class="section-head reveal" data-head></div>
    <div class="timeline">
      <div class="timeline-pipe" aria-hidden="true"><div class="timeline-pipe-fill"></div></div>
      <ol id="timeline-list"></ol>
    </div>
  </section>

  ''' + divider('03 · projects', 'test ✓', 'release ✓') + '''

  <!-- ============ 03 · PROJECTS ============ -->
  <section id="projects" class="wrap section">
    <div class="section-head reveal">
      <div data-head></div>
      <div class="filters" id="filters" role="group" aria-label="Filter projects"></div>
    </div>
    <div class="projects" id="project-grid"></div>
  </section>

  ''' + divider('04 · stack', 'image ✓', 'push ✓') + '''

  <!-- ============ 04 · STACK ============ -->
  <section id="stack" class="wrap section">
    <div class="section-head reveal" data-head></div>
    <div class="stack-grid" id="skills"></div>
    <h3 class="sub-head reveal">Certifications <span class="mono" style="font-size:12px;color:var(--muted);font-weight:400" id="certs-issuer"></span></h3>
    <div class="cert-list reveal" id="certs"></div>
    <h3 class="sub-head reveal">Languages</h3>
    <div class="langs reveal" id="langs"></div>
  </section>

  ''' + divider('05 · console', 'monitor ✓', 'logs ✓') + '''

  <!-- ============ 05 · CONSOLE ============ -->
  <section id="console" class="wrap section">
    <div class="section-head reveal" data-head data-sub="Ask the terminal anything about me, or check my latest activity on GitHub."></div>
    <div class="console-grid">
      <div class="card terminal reveal">
        <div class="term-bar"><span></span><span></span><span></span><b>zaid@ops: ~</b></div>
        <div class="term-out" id="term-out" aria-live="polite"></div>
        <form class="term-in" id="term-form" autocomplete="off">
          <label for="term-input">zaid@ops:~$</label>
          <input id="term-input" type="text" spellcheck="false" placeholder="type help and press Enter">
        </form>
        <div class="term-hints">
          <button type="button" data-cmd="whoami">whoami</button><button type="button" data-cmd="skills">skills</button><button type="button" data-cmd="projects">projects</button><button type="button" data-cmd="certs">certs</button><button type="button" data-cmd="contact">contact</button><button type="button" data-cmd="clear">clear</button>
        </div>
      </div>
      <div class="side-stack">
        <div class="card activity reveal d1">
          <div class="activity-head"><span class="mono">GITHUB ACTIVITY · @zaidmuzaffar</span><a class="plink" href="https://github.com/zaidmuzaffar">Profile ↗</a></div>
          <div id="activity-graph"></div>
        </div>
        <div class="card activity reveal d2">
          <div class="activity-head"><span class="mono">SHORTCUTS</span></div>
          <p style="margin:0;color:var(--text-2);font-size:15px">Press <span class="kbd">Ctrl</span> + <span class="kbd">K</span> (or <span class="kbd">⌘</span> + <span class="kbd">K</span>) anywhere to jump to a section, open a case study, copy my email or switch the theme.</p>
          <button type="button" class="plink" data-palette style="align-self:flex-start">Open command menu</button>
        </div>
      </div>
    </div>
  </section>

  ''' + divider('06 · contact', 'ready ✓', 'live ✓') + '''

  <!-- ============ 06 · CONTACT ============ -->
  <section id="contact" class="wrap section" style="padding-bottom:0">
    <div class="section-head reveal" data-head></div>

    <div id="recs-block" hidden>
      <div class="recs" id="recs"></div>
    </div>

    <div class="connect reveal">
      <svg class="connect-deco" viewBox="0 0 260 260" aria-hidden="true"><circle cx="130" cy="130" r="110" fill="none" stroke-width="2"/><g class="deco-hand"><path d="M130 40 V130 H210" fill="none" stroke-width="10" stroke-linecap="round"/></g></svg>
      <div class="connect-left">
        <span class="mono" style="font-size:13px;letter-spacing:1.5px">$ ssh zaid@ops</span>
        <h2>Let's build &amp;<br>ship together.</h2>
        <div class="connect-links">
          <button type="button" class="connect-link" id="copy-email" data-copy=""><span id="contact-email"></span><span aria-hidden="true">copy</span></button>
          <a class="connect-link" href="https://www.linkedin.com/in/zaid-muzaffar-57329237a/">LinkedIn <span aria-hidden="true">↗</span></a>
          <a class="connect-link" href="https://github.com/zaidmuzaffar">GitHub · zaidmuzaffar <span aria-hidden="true">↗</span></a>
        </div>
      </div>
      <div class="connect-form">
        <form class="form" id="contact-form">
          <div class="form-row">
            <div class="field"><label for="cf-name">NAME</label><input id="cf-name" name="name" type="text" required autocomplete="name"></div>
            <div class="field"><label for="cf-email">EMAIL</label><input id="cf-email" name="email" type="email" required autocomplete="email"></div>
          </div>
          <div class="field"><label for="cf-msg">MESSAGE</label><textarea id="cf-msg" name="message" required></textarea></div>
          <button type="submit" class="btn">Send message <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
          <div class="form-status" id="form-status" role="status" aria-live="polite"></div>
        </form>
      </div>
    </div>
  </section>

</main>

''' + footer() + '\n' + scripts() + '''
</body>
</html>
'''

NOT_FOUND = head('404 — Deployment failed · Zaid Muzaffar', 'This page does not exist.') + '''
<body data-base="">
<div class="toast" role="status" aria-live="polite"></div>
''' + nav(links_html='', cta_href='index.html#contact') + '''
<main class="wrap" style="min-height:70vh;display:flex;align-items:center;padding-top:40px;padding-bottom:40px">
  <div class="card terminal" style="width:100%;max-width:760px;margin:0 auto">
    <div class="term-bar"><span></span><span></span><span></span><b>zaid@ops: ~/404</b></div>
    <div class="term-out" style="height:auto;padding-bottom:22px"><div class="cmd">curl -I this-page</div><div>HTTP/1.1 <span class="hl">404 Not Found</span></div><div class="cmd">kubectl get page</div><div>Error from server (NotFound): this page was never deployed.</div><div class="cmd">git log --oneline -1</div><div><span class="ok">●</span> rolled back to a page that exists ↓</div></div>
    <div class="term-hints" style="padding-top:6px">
      <a class="plink main" href="index.html">← Back to home</a>
      <a class="plink" href="index.html#projects">Projects</a>
      <a class="plink" href="index.html#contact">Contact</a>
      <button type="button" class="plink" data-palette>Search (Ctrl K)</button>
    </div>
  </div>
</main>
''' + footer() + '\n' + scripts() + '''
</body>
</html>
'''

if __name__ == '__main__':
    with open(os.path.join(SITE, 'index.html'), 'w') as f:
        f.write(INDEX)
    with open(os.path.join(SITE, '404.html'), 'w') as f:
        f.write(NOT_FOUND)
    print('built index.html, 404.html')
