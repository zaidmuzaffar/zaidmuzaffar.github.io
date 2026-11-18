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
# 0. SHOPOPS PLATFORM
# =====================================================================
REPO = 'https://github.com/zaidmuzaffar/shopops-platform'
SHOPOPS = dict(
    file='shopops-platform.html',
    title='ShopOps Platform',
    kicker='CASE STUDY 01 · CLOUD &amp; DEVOPS · IN BUILD · 6/8',
    h1='ShopOps Platform<br><span style="color:var(--accent)">From laptop to production, the DevOps way</span>',
    lead='A small inventory service taken through the whole path a real team uses to ship software: containers, a CI pipeline with security scanning, infrastructure as code, Kubernetes, GitOps and monitoring. Planned as company ticket PLAT-101 and built phase by phase on a zero-cost budget. Six of the eight phases are done.',
    meta=[('ROLE', 'Sole engineer: app, containers, pipeline, infrastructure'), ('TICKET', 'PLAT-101 · 8 phases'),
          ('DONE', 'Phase 0 → 6: app, Docker, CI, Terraform, Kubernetes, GitOps, monitoring'),
          ('NEXT', 'TLS · backups · k6 load tests · runbook'), ('BUDGET', '$0 — free tools and free tiers only')],
    links=[btn(REPO, 'Source code ↗', True), btn(REPO + '/actions', 'Pipeline runs ↗'),
           btn(REPO + '/tree/main/k8s/helm/shopops', 'Helm chart ↗'), btn(REPO + '/tree/main/infra', 'Terraform ↗')],
    next=('star-pump-house.html', 'Star Pump House — Shop Management System'),
    sections=[
        ('brief', 'The brief', '''
<p>I wrote the project the way a platform team receives work: a ticket with a goal, constraints and a definition of done.</p>
<div class="callout brass"><span class="mono">PLAT-101</span><p>Take the shop inventory service from "runs on my laptop" to a reproducible, tested, scanned and observable deployment. Every change goes through a pull request and a pipeline. Secrets never enter Git. <strong>Total cost: zero</strong> — local clusters and free tiers only, with a short, budget-capped cloud deploy at the end that is torn down with <code>terraform destroy</code>.</p></div>
<p>The application is deliberately small — a REST API for products with a web front end — so the attention goes to how it is built, shipped and run.</p>'''),
        ('architecture', 'Architecture', flow([
            ('Browser', 'localhost:8081'),
            ('Ingress · Traefik', 'The only way in'),
            ('web · Nginx', '3 pods · static UI, proxies /api'),
            ('api · Node.js', '2–5 pods · scales on CPU'),
            ('PostgreSQL 16', 'StatefulSet + volume'),
        ]) + '''
<p>The stack runs on a local Kubernetes cluster: k3d, with one server and one agent node inside Docker. Only the ingress is reachable from outside; the API and the database are internal services that find each other by name. Prometheus collects the API's metrics every 30 seconds and Grafana turns them into the dashboard shown in Phase 6.</p>
<h3>How a change reaches the cluster</h3>''' + flow([
            ('Pull request', 'Code, chart or config'),
            ('CI checks', 'Tests · build · Trivy · Terraform plan'),
            ('Merge', 'Only after the checks pass'),
            ('Argo CD', 'Syncs the Helm chart from main'),
            ('Cluster', 'Matches Git'),
        ]) + '''
<p>Nobody runs <code>kubectl apply</code> or <code>helm upgrade</code> by hand. In this local setup the images are built on my machine and loaded into the cluster; the production values point at the images the pipeline publishes to GHCR.</p>'''),
        ('phases', 'Roadmap', table(
            ['Phase', 'What it delivers', 'Status'],
            [['0 · Application', 'Node.js API with 12-factor config, liveness and readiness endpoints, graceful SIGTERM shutdown, JSON logs, automated tests', '✅ Done'],
             ['1 · Containers', 'Multi-stage Dockerfiles, non-root users, read-only filesystem, Compose stack with healthchecks and an isolated database', '✅ Done'],
             ['2 · CI pipeline', 'GitHub Actions: test → build → Trivy scan → push to GHCR, least-privilege permissions', '✅ Done'],
             ['3 · Infrastructure as code', 'Terraform on AWS: budget alerts, a two-zone VPC, tiered security groups, remote state with locking, GitHub OIDC with no stored keys', '✅ Done'],
             ['4 · Kubernetes', 'k3d cluster, Helm chart with dev and prod values, probes, resource limits, autoscaling, disruption budgets', '✅ Done'],
             ['5 · GitOps', 'Argo CD deploys the chart from Git with automatic sync, pruning and self-healing', '✅ Done'],
             ['6 · Observability', 'Prometheus metrics from the API, a Grafana dashboard and three alert rules', '✅ Done'],
             ['7 · Hardening', 'TLS, secret management, database backups, k6 load tests', 'Next'],
             ['8 · Operations', 'Runbook, game day, postmortem and final documentation', 'Planned']])),
        ('containers', 'Phase 1 — Containers', features([
            ('Multi-stage build', 'Separate stages install dependencies, run the tests and build a small runtime image that holds only what the app needs.'),
            ('Layer caching', 'Dependency files are copied before the source, so <code>npm ci</code> only re-runs when dependencies change.'),
            ('Non-root', 'The API runs as the <code>node</code> user and the web server as an unprivileged Nginx user — checked with <code>whoami</code>.'),
            ('Locked-down runtime', 'Read-only filesystem, <code>no-new-privileges</code>, a tmpfs for <code>/tmp</code> and an init process for clean signal handling.'),
            ('Healthchecks', 'The API waits for Postgres to be <em>healthy</em>, not just started, and the web waits for the API.'),
            ('Secrets out of Git', 'The database password lives in a git-ignored <code>.env</code>; Compose refuses to start without it.'),
        ])),
        ('pipeline', 'Phase 2 — CI pipeline', flow([
            ('Pull request', 'Every change'),
            ('Test', 'npm ci · node --test'),
            ('Build', 'api + web in parallel, cached'),
            ('Trivy scan', 'Fail on fixable HIGH / CRITICAL'),
            ('GHCR', 'Push on main only'),
        ]) + '''
<ul><li><strong>Least privilege:</strong> the workflow can only read the repository; the build job alone gets permission to write packages.</li>
<li><strong>No pushes from pull requests:</strong> images are published only from <code>main</code>, so untrusted code can never reach the registry.</li>
<li><strong>Pinned scanner:</strong> Trivy is pinned to versions known to be safe after the March 2026 supply-chain attack on its GitHub Action, when release tags were overwritten with credential-stealing code.</li></ul>'''),
        ('terraform', 'Phase 3 — Infrastructure as code', '''
<p>The AWS side is written in Terraform and reviewed as a plan before anything is applied. This phase builds only what costs nothing to keep: no servers, no NAT gateway, no load balancer, no managed Kubernetes. Those wait for one short, budget-capped week at the end.</p>''' + features([
            ('Budget alerts', 'Email at $1 and $5 of real spend, and when the forecast passes the monthly limit. They count spend <em>before</em> credits: with credits applied the bill reads $0 and the alerts would never fire.'),
            ('Network without a NAT gateway', 'A VPC across two availability zones with public and private subnets. The private subnets have no route to the internet, so no NAT gateway is needed; one would cost over $30 a month even when idle.'),
            ('Tiered security groups', 'Internet → web on 80/443, web → API on 3000, API → database on 5432, and nothing else. Each rule points at the security group in front of it, not at IP ranges.'),
            ('Remote state with locking', "State lives in an S3 bucket that is versioned, encrypted, closed to the public and protected by <code>prevent_destroy</code>. S3's native lock file stops two runs from changing it at once."),
            ('No stored AWS keys', "GitHub Actions gets short-lived credentials through OIDC. The role trusts only this repository's <code>main</code> branch and its pull requests, can read the account, and can write only the state bucket."),
            ('Plan on every pull request', 'The pipeline runs <code>terraform fmt</code>, <code>validate</code> and <code>plan</code>, so an infrastructure change is reviewed like code. Locally I only apply saved plans.'),
        ])),
        ('kubernetes', 'Phase 4 — Kubernetes', '''
<p>The three services moved from Compose to a local Kubernetes cluster: first as plain manifests with Kustomize, then as a Helm chart. I tested the basics by hand: deleted pods and watched Kubernetes replace them, and ran a load test to watch the autoscaler react.</p>''' + features([
            ('Local cluster, zero cost', 'k3d runs a real k3s cluster in Docker. Images are loaded with <code>k3d image import</code>, so no registry is needed.'),
            ('Health probes', 'Liveness restarts an API pod that hangs; readiness keeps a pod out of traffic until it can serve. Both use the endpoints built in Phase 0.'),
            ('Limits and locked-down pods', 'Every container declares the CPU and memory it needs and may use. API and web run as non-root with every Linux capability dropped; the API also has a read-only filesystem.'),
            ('Database with a volume', 'PostgreSQL runs as a StatefulSet on a persistent volume, with its password in a Secret created outside Git. The existing products were moved over with <code>pg_dump</code>.'),
            ('Autoscaling', 'The API runs 2 to 5 pods, targeting 60% CPU. Under the load test it scaled to 5, then back to 2 when the load stopped. Disruption budgets keep at least one API and one web pod up during maintenance.'),
            ('Helm chart', 'One chart, two values files. Development uses local images and small limits; production uses the GHCR images, 3–10 API pods and a 10 GB volume. Upgrades and rollbacks are one command each.'),
        ])),
        ('gitops', 'Phase 5 — GitOps', '''
<p>Argo CD runs inside the cluster and watches the Helm chart on the <code>main</code> branch. From this phase on, Git is the single source of truth: the cluster changes only when a pull request is merged.</p>
<ul><li><strong>Automatic sync:</strong> a merged change reaches the cluster within about three minutes, the interval at which Argo CD checks Git.</li>
<li><strong>Prune:</strong> a resource deleted from Git is deleted from the cluster too, so nothing is left running by accident.</li>
<li><strong>Self-heal:</strong> a change made directly with <code>kubectl</code> is reverted to what Git says.</li>
<li><strong>First change through GitOps:</strong> scaling the web tier to three pods was a one-line pull request; after the merge Argo CD rolled it out without a single manual command.</li>
<li><strong>Rollback:</strong> reverting the commit is the rollback, through the same reviewed path as any other change.</li></ul>'''),
        ('monitoring', 'Phase 6 — Monitoring', '''
<p>The API now reports its own health in numbers. I wrote the <code>/metrics</code> endpoint by hand in the Prometheus text format, in under a hundred lines and with no new dependency. The monitoring stack (Prometheus and Grafana, from the kube-prometheus-stack chart) collects it every 30 seconds.</p>''' + features([
            ('RED metrics', 'Rate, errors and duration: requests counted by method, route and status, plus a latency histogram. Memory, CPU and the running version of every pod come with them.'),
            ('Few, fixed labels', 'Product IDs are grouped under <code>/api/products/:id</code> and health checks are not counted, so the number of time series stays the same however many products exist.'),
            ('Monitoring as code', 'The scrape target, the alert rules and the dashboard ship inside the Helm chart, so Argo CD deploys them with the app. Nothing is set up by clicking in a UI.'),
            ('Three alerts', 'API unreachable for 2 minutes · more than 5% of requests failing for 5 minutes · p95 latency above 500 ms for 10 minutes.'),
            ('Tested', 'Five new tests check the output format, the counting and the route grouping. With the earlier ones that makes eleven, and they now also run inside the image build.'),
            ('Light enough for a laptop', 'Prometheus keeps two days of data and Alertmanager is off until there is a notification channel, so the whole stack runs next to the app.'),
        ]) + '''
<figure class="shot"><img src="../assets/shopops/grafana-dashboard.jpg" alt="Grafana dashboard for the ShopOps API with request rate, error rate, p95 latency, running version, requests by route and status code, latency percentiles and the number of API pods" loading="lazy"><figcaption>Grafana: the API dashboard during a test. 0% errors, p95 under 5 ms, and the autoscaler adding a third pod during a burst at 14:03.</figcaption></figure>
<figure class="shot"><img src="../assets/shopops/alert-rules.jpg" alt="Grafana alert list showing the three ShopOps alert rules, all in the Normal state" loading="lazy"><figcaption>The three alert rules, loaded from the Helm chart, all Normal.</figcaption></figure>
<h3>What the dashboard taught me</h3>
<p>During that burst the requests graph peaked below 3 per second, yet the autoscaler still added a pod. A two-minute <code>rate()</code> spreads a short burst across the whole window, while the autoscaler checks CPU every 15 seconds. Latency told the same story: at 14:10 the median stayed near 2.5 ms while p99 jumped to 21 ms. Averages hide exactly the moments you need to see.</p>'''),
        ('incidents', 'What went wrong, and how I fixed it', '''
<h3>The scanner blocked my first pull request</h3>
<p>Both image builds failed on the first pipeline run: Trivy found <strong>high-severity vulnerabilities in zlib</strong> inside the base images, with fixed versions already available. I upgraded OS packages during the build, moved Nginx to the maintained stable image and removed <code>npm</code> and <code>corepack</code> from the API runtime image, which the running app never uses. The next run passed. The problem was caught before merge, not in production.</p>
<h3>The pipeline was locked out of AWS</h3>
<p>Once the OIDC role existed, the Terraform job failed with <code>AccessDenied</code>. The trust policy looked right, so instead of guessing I opened CloudTrail and read what AWS had actually received. GitHub identified the repository by its <strong>immutable owner and repository IDs</strong> (<code>repo:owner@id/name@id</code>), not the plain name my policy expected. After I matched that format the job passed. A bonus: a deleted and recreated repository with the same name cannot use the role.</p>
<h3>Tests that never ran</h3>
<p>Since Phase 1 the Dockerfile had a test stage, and I believed a failing test would stop the image build. In Phase 6 I found it never ran: BuildKit only builds the stages the final image depends on, and nothing depended on the test stage, so it was silently skipped. Now the runtime stage copies one file from the test stage, which forces the tests to run. The first real run failed straight away on a test that needs the web folder, which is not part of the API image; that test is skipped inside the build and still runs in CI.</p>
<h3>A database restart hidden in the chart</h3>
<p>While bumping the chart version I noticed that every pod template carried the chart's version labels. A new label means a new pod template, and a new template means new pods, so every release would have restarted PostgreSQL for no reason. The database and web pods now carry only stable labels.</p>
<h3>My load generator ran out of ports</h3>
<p>To test the autoscaler I fired requests in a tight loop from a busybox pod. After a while every request failed with <em>Cannot assign requested address</em>: a closed connection keeps its local port reserved for a while, and the loop used them up faster than they came back. A short pause between requests fixed it; a proper load-testing tool, k6, is part of Phase 7.</p>'''),
        ('decisions', 'Key decisions', table(
            ['Decision', 'Why'],
            [['Plain <code>node:http</code>, one dependency (<code>pg</code>)', 'A small dependency tree is less to patch and less for a scanner to flag.'],
             ['Metrics written by hand, not with a client library', 'The Prometheus text format is simple. Writing it kept the dependency count at one and taught me what each number means.'],
             ['Readiness separate from liveness', '"The process is up" and "it can serve traffic" are different questions, and Kubernetes acts on each one differently.'],
             ['Only the ingress is exposed', 'The API and the database are internal services; the database is never reachable from outside.'],
             ['Fail the pipeline only on fixable vulnerabilities', 'Blocks real, actionable risk without failing on issues nobody can fix yet.'],
             ['GitHub OIDC instead of stored AWS keys', 'Short-lived credentials; nothing long-lived to leak from the repository.'],
             ['No NAT gateway', "The private subnets don't need the internet yet, and a NAT gateway is billed for every hour it exists."],
             ['Local Kubernetes (k3d) instead of EKS', 'Same skills, zero cost; the cloud is used briefly at the end, behind budget alerts.'],
             ['The cluster changes only through Git (Argo CD)', 'Every change is reviewed, recorded in history and reversible with a revert.'],
             ['Dashboards and alerts inside the Helm chart', 'They are versioned and reviewed like code, and deployed together with the app they watch.']])),
        ('learned', 'What I have learned so far', '''
<ul><li>"Started" is not "ready" — healthchecks and readiness are what make a system start reliably.</li>
<li>A container image is only as secure as its base layers; scanning has to run on every change.</li>
<li>Check that the safety net works: a test stage that silently never runs is worse than none.</li>
<li>When access is denied, read the audit log before changing policies. CloudTrail showed exactly what AWS received.</li>
<li>Averages hide the moments that matter; look at short windows and at p95 and p99, not only the median.</li>
<li>In Kubernetes, labels on a pod template are part of the release: change them and the pods restart.</li>
<li>"Free" is a design constraint, not an excuse. It shaped the network, the cluster and the order of the work.</li></ul>'''),
        ('docs', 'Documentation', '''
<h3>Run it with Docker Compose</h3>
<ol><li>Clone <code>github.com/zaidmuzaffar/shopops-platform</code> and install Docker.</li>
<li>Create the secret file: <code>echo "POSTGRES_PASSWORD=yourpassword" &gt; .env</code> (letters and numbers only).</li>
<li>Start the stack: <code>docker compose up -d --build</code>, then <code>docker compose ps</code> until all three services are healthy.</li>
<li>Open <code>http://localhost:8080</code>.</li></ol>
<h3>Run it on Kubernetes</h3>
<ol><li>Create a local cluster: <code>k3d cluster create shopops --agents 1 -p "8081:80@loadbalancer"</code>.</li>
<li>Build the images and load them into the cluster: <code>docker build -t shopops-api:0.5.0 app/api</code>, <code>docker build -t shopops-web:local app/web</code>, then <code>k3d image import shopops-api:0.5.0 shopops-web:local -c shopops</code>.</li>
<li>Create the namespace and the database secret: <code>kubectl create namespace shopops</code>, then <code>kubectl -n shopops create secret generic shopops-db --from-literal=POSTGRES_PASSWORD=yourpassword</code>.</li>
<li>Install kube-prometheus-stack as Helm release <code>monitoring</code> in the <code>monitoring</code> namespace; the chart's alert rules and dashboard need it. To skip monitoring, set <code>monitoring.enabled=false</code>.</li>
<li>Install Argo CD and apply <code>argocd/shopops-app.yaml</code>; Argo CD then deploys the chart from <code>main</code>. Without Argo CD: <code>helm install shopops k8s/helm/shopops -n shopops</code>.</li>
<li>Open <code>http://localhost:8081</code>.</li></ol>
<h3>Repository layout</h3>
<p><code>app/api</code> — Node.js service, tests and Dockerfile. <code>app/web</code> — UI, Nginx config and Dockerfile. <code>compose.yaml</code> — the local stack. <code>.github/workflows</code> — the CI pipeline. <code>infra/</code> — Terraform for AWS. <code>k8s/base</code> — plain Kubernetes manifests (Kustomize). <code>k8s/helm/shopops</code> — the Helm chart, with the alert rules and the Grafana dashboard. <code>argocd/</code> — the Argo CD application. <code>docs/</code> — phase notes; the runbook and postmortem arrive in Phase 8.</p>'''),
    ],
)

# =====================================================================
# 1. STAR PUMP HOUSE
# =====================================================================
SPH = dict(
    file='star-pump-house.html',
    title='Star Pump House',
    kicker='CASE STUDY 02 · LIVE IN DAILY USE',
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
    kicker='CASE STUDY 03 · IN ACTIVE DEVELOPMENT',
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
    kicker='CASE STUDY 04 · IN ACTIVE DEVELOPMENT',
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
    kicker='CASE STUDY 05 · CLOUD & DEVOPS',
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
    kicker='CASE STUDY 06 · FINAL YEAR PROJECT',
    h1='Lawyer–Client<br><span style="color:var(--accent)">Matching Platform</span>',
    lead='My final year project at COMSATS: a web platform that helps clients find the right lawyer by expertise and search criteria, built end to end from database to interface.',
    meta=[('CONTEXT', 'Final Year Project, COMSATS Abbottabad'), ('STACK', 'React · Node.js · Express · MongoDB'), ('YEAR', '2025–2026'), ('STATUS', 'Complete')],
    links=[btn('../docs/Lawyer_Client_Platform_Case_Study.pdf', 'Case study PDF ↓', True), btn('https://github.com/zaidmuzaffar', 'GitHub profile ↗')],
    next=('shopops-platform.html', 'ShopOps Platform — Production DevOps Pipeline'),
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

for p in (SHOPOPS, SPH, VIGIL, VOICE, LINUX, LAWYER):
    page(p)
print('ok', os.listdir(OUT))
