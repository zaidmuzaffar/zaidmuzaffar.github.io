"""Builds Zaid Muzaffar's CV as HTML and renders it to PDF.
Two versions: full (with phone, for applications) and web (no phone, for the public portfolio).
The phone number is not stored in this public repo: set CV_PHONE to build the full version, e.g.
    CV_PHONE='+92 ...' python3 tools/build_cv.py
Without it only the web version is built."""
import os
from playwright.sync_api import sync_playwright

PHONE = os.environ.get('CV_PHONE', '').strip()

def contact(with_phone):
    items = []
    if with_phone:
        items.append(PHONE)
    items += [
        '<a href="mailto:zaidmuzaffar81@gmail.com">zaidmuzaffar81@gmail.com</a>',
        'Islamabad, Pakistan',
    ]
    links = [
        '<a href="https://zaidmuzaffar.github.io">zaidmuzaffar.github.io</a>',
        '<a href="https://github.com/zaidmuzaffar">github.com/zaidmuzaffar</a>',
        '<a href="https://www.linkedin.com/in/zaid-muzaffar-57329237a/">linkedin.com/in/zaid-muzaffar</a>',
    ]
    return ' &nbsp;|&nbsp; '.join(items) + '<br>' + ' &nbsp;|&nbsp; '.join(links)


def html(with_phone):
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Zaid Muzaffar — CV</title>
<style>
@page {{ size: A4; margin: 14mm 15mm 13mm; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: 'Inter', 'Carlito', sans-serif; font-size: 9.4pt; line-height: 1.4; color: #1d2733; }}
a {{ color: #0B6E8F; text-decoration: none; }}
header {{ text-align: center; padding-bottom: 8px; border-bottom: 2px solid #0B6E8F; }}
h1 {{ margin: 0; font-size: 22pt; letter-spacing: 1px; color: #0E2A3B; font-weight: 800; }}
.title {{ margin: 2px 0 6px; font-size: 11pt; color: #0B6E8F; font-weight: 600; }}
.contact {{ font-size: 8.8pt; color: #3a4754; line-height: 1.6; }}
h2 {{ margin: 11px 0 5px; padding-bottom: 3px; font-size: 10.2pt; letter-spacing: 1.6px; text-transform: uppercase; color: #0E2A3B; border-bottom: 1px solid #c9d6de; font-weight: 800; break-after: avoid; }}
p {{ margin: 0 0 4px; }}
.item {{ margin-bottom: 8px; break-inside: avoid; }}
.row {{ display: flex; justify-content: space-between; align-items: baseline; gap: 12px; }}
.row b {{ font-size: 10pt; color: #0E2A3B; }}
.date {{ font-size: 8.8pt; color: #5b6b78; white-space: nowrap; }}
.sub {{ font-size: 9pt; color: #0B6E8F; font-weight: 600; margin-bottom: 2px; }}
ul {{ margin: 2px 0 0; padding-left: 15px; }}
li {{ margin-bottom: 1.5px; }}
.tech {{ font-size: 8.9pt; color: #3a4754; margin-top: 2px; }}
.tech b {{ color: #1d2733; }}
.skills {{ display: grid; grid-template-columns: 150px 1fr; gap: 3px 10px; }}
.skills b {{ color: #0E2A3B; }}
</style></head><body>

<header>
  <h1>ZAID MUZAFFAR</h1>
  <div class="title">Cloud &amp; DevOps Engineer &nbsp;·&nbsp; BS Computer Science</div>
  <div class="contact">{contact(with_phone)}</div>
</header>

<h2>Profile</h2>
<p>Computer Science graduate focused on cloud engineering and DevOps. Completed a 160-hour Cloud &amp; DevOps internship with an overall rating of Excellent, and now building ShopOps: a production-style platform that takes a web service from laptop to Kubernetes with CI security scanning, Terraform on AWS, Helm, GitOps with Argo CD and Prometheus/Grafana monitoring, at zero cost. Also built and deployed a live Firebase web application that my family's hardware business uses every day. Looking for a Cloud / DevOps role to automate deployment pipelines and run reliable, scalable infrastructure.</p>

<h2>Experience</h2>
<div class="item">
  <div class="row"><b>Cloud &amp; DevOps Intern</b><span class="date">Completed 15 Oct 2026 &nbsp;·&nbsp; 4 weeks, 160 hours</span></div>
  <div class="sub">Skill Set Go EduTech &nbsp;·&nbsp; Virtual internship &nbsp;·&nbsp; Overall performance: Excellent &nbsp;·&nbsp; <a href="https://zaidmuzaffar.github.io/docs/Cloud_DevOps_Internship_Certificate_Zaid_Muzaffar.pdf">Certificate</a> &nbsp;·&nbsp; <a href="https://github.com/zaidmuzaffar/SkillSetGo-Cloud-Devops-Internship">Lab repo</a></div>
  <ul>
    <li>Containerised an Nginx web application with <b>Docker</b> and <b>Docker Compose</b> (web + Redis services).</li>
    <li>Wrote a <b>GitHub Actions</b> workflow that builds the Docker image automatically on every push and pull request.</li>
    <li>Deployed the application to <b>Kubernetes</b> (Minikube) with a Deployment and NodePort Service using kubectl; added ConfigMaps and Secrets.</li>
    <li>Learned the <b>Terraform</b> workflow (init, plan, apply) and documented the deployment architecture.</li>
    <li>Linux system administration and shell scripting; tracked work in Zenhub. Completed 16+ practical tasks, 3 mini projects and 2 major projects.</li>
  </ul>
</div>

<h2>Skills</h2>
<div class="skills">
  <b>CI/CD &amp; Automation</b><span>GitHub Actions · CI/CD pipelines · Trivy image scanning · GitHub OIDC · Git &amp; GitHub · Bash / shell scripting · Zenhub · Agile / Scrum</span>
  <b>Containers &amp; Kubernetes</b><span>Docker (multi-stage, non-root) · Docker Compose · Kubernetes (k3d/k3s, Minikube, kubectl) · Helm · Argo CD (GitOps) · HPA autoscaling</span>
  <b>IaC &amp; Cloud</b><span>Terraform (S3 remote state with locking) · AWS (IAM, VPC, EC2, S3, Route 53, Budgets) · Firebase (Hosting, Firestore, Authentication, App Check)</span>
  <b>Observability</b><span>Prometheus · Grafana · PromQL alert rules · RED metrics · structured JSON logs</span>
  <b>Systems</b><span>Linux administration · process management · networking (subnets, routing, DNS) · SSH · environment configuration</span>
  <b>Web &amp; Data</b><span>JavaScript · HTML/CSS · React.js · Node.js · Express · REST APIs · PostgreSQL · MongoDB · MySQL · Cloud Firestore</span>
  <b>AI &amp; Mobile</b><span>Google Gemini API (function calling) · Ollama · TensorFlow Lite · Python · Flutter (Dart)</span>
</div>

<h2>Projects</h2>
<div class="item">
  <div class="row"><b>ShopOps Platform – Production DevOps Pipeline (7 of 8 phases done)</b><span class="date">Nov 2026 – Present</span></div>
  <ul>
    <li>Taking a Node.js and PostgreSQL inventory service from laptop to production in eight phases, planned like company work (ticket PLAT-101) on a zero-cost budget.</li>
    <li><b>CI:</b> GitHub Actions runs the tests, builds multi-stage non-root images and blocks fixable HIGH/CRITICAL vulnerabilities with Trivy; images are pushed to GHCR only from main.</li>
    <li><b>Terraform on AWS:</b> two-zone VPC without a NAT gateway, tiered security groups, S3 remote state with locking, budget alerts, and GitHub OIDC instead of stored keys.</li>
    <li><b>Kubernetes:</b> Helm chart with probes, resource limits, autoscaling (2–5 pods) and disruption budgets, deployed by Argo CD with automatic sync and self-healing.</li>
    <li><b>Monitoring and hardening:</b> Prometheus metrics, a Grafana dashboard and alerts; daily backups with a restore test, Sealed Secrets, TLS via cert-manager, k6 load tests (50 req/s, 0 errors, p95 8 ms).</li>
  </ul>
  <div class="tech"><b>Tech:</b> Node.js, PostgreSQL, Docker, GitHub Actions, Trivy, Terraform, AWS, Kubernetes (k3d), Helm, Argo CD, Prometheus, Grafana, cert-manager, k6 &nbsp;·&nbsp; <a href="https://github.com/zaidmuzaffar/shopops-platform">Code</a> · <a href="https://zaidmuzaffar.github.io/projects/shopops-platform.html">Case study</a></div>
</div>
<div class="item">
  <div class="row"><b>Star Pump House – Shop Management System (Live)</b><span class="date">Sep 2026 – Oct 2026</span></div>
  <ul>
    <li>Designed, built and deployed a web app that my family's pump and hardware shop uses every day in place of paper registers: stock, sales, customer credit, suppliers, wholesale accounts, cash closing and profit reports across 23 screens.</li>
    <li>Cloud Firestore with per-user security rules, owner and salesman roles enforced on the server, and Firebase App Check.</li>
    <li>AI assistant using Google Gemini function calling (17 read-only tools) that answers from the shop's records in English or Urdu.</li>
    <li>57 releases shipped from real user feedback with the Firebase CLI; runs at zero cost on Firebase's free tier.</li>
  </ul>
  <div class="tech"><b>Tech:</b> JavaScript, Firebase (Auth, Firestore, Hosting, App Check), Gemini AI, Git &nbsp;·&nbsp; <a href="https://starpumphouse.web.app">Live demo</a> · <a href="https://github.com/zaidmuzaffar/star-pump-house">Code</a> · Demo login: demo@starpumphouse.com / Star123@</div>
</div>
<div class="item">
  <div class="row"><b>Automated Linux System Administration &amp; Shell Scripts</b><span class="date"></span></div>
  <p>Modular Bash scripts automating user access management, environment setup, process monitoring, log parsing and system health checks; versioned and documented in Git.</p>
  <div class="tech"><b>Tech:</b> Linux, Bash, Git</div>
</div>
<div class="item">
  <div class="row"><b>Lawyer–Client Matching Web Platform – Final Year Project</b><span class="date">Sep 2024 – Jul 2025</span></div>
  <ul>
    <li>Web platform matching clients with lawyers by expertise and search criteria, built end to end.</li>
    <li>Designed MongoDB schemas and REST API endpoints for data exchange and payment processing; managed environment variables, CORS policies and server deployment.</li>
  </ul>
  <div class="tech"><b>Tech:</b> React.js, Node.js, Express, MongoDB, REST APIs</div>
</div>
<div class="item">
  <div class="row"><b>Vigil – Fall Detection &amp; Live Location Safety App (in progress)</b><span class="date">Oct 2026 – Present</span></div>
  <p>Flutter app with an on-device 1D-CNN fall-detection model (TensorFlow Lite) that alerts trusted circles with live location, a loud alarm and strong vibration; Firebase backend with security rules.</p>
  <div class="tech"><b>Tech:</b> Flutter (Dart), TensorFlow Lite, Python, Google Colab, Firebase</div>
</div>
<div class="item">
  <div class="row"><b>Voice AI Assistant for macOS (in progress)</b><span class="date">Oct 2026 – Present</span></div>
  <p>Always-on voice assistant that replies in Urdu or English and controls apps, WhatsApp and the system; Gemini Live online with a local Ollama model as offline fallback; spoken confirmation before destructive actions.</p>
  <div class="tech"><b>Tech:</b> Python, Gemini Live API, Ollama (Qwen 2.5 14B), macOS automation</div>
</div>

<h2>Education</h2>
<div class="item">
  <div class="row"><b>Bachelor of Science in Computer Science</b><span class="date">Sep 2021 – Jan 2026</span></div>
  <div class="sub">COMSATS University Islamabad, Abbottabad Campus</div>
  <p><b>Relevant courses:</b> Operating Systems, Computer Networks, Database Systems, Data Structures &amp; Algorithms, Software Engineering, Web Technologies, Parallel &amp; Distributed Computing, Artificial Intelligence, Machine Learning.</p>
</div>

<h2>Certifications</h2>
<ul>
  <li><a href="https://zaidmuzaffar.github.io/docs/Cloud_DevOps_Internship_Certificate_Zaid_Muzaffar.pdf"><b>Cloud &amp; DevOps Internship — Certificate of Completion</b></a>, Skill Set Go EduTech (Oct 2026, ID SSG/REG/B1/0457)</li>
  <li><b>IBM DevOps and Software Engineering (Coursera):</b> <a href="https://www.coursera.org/account/accomplishments/verify/ID5UOQ95D0QG">Introduction to DevOps</a> · <a href="https://www.coursera.org/account/accomplishments/verify/BLP5F4L1Z822">Introduction to Cloud Computing</a> · <a href="https://www.coursera.org/account/accomplishments/verify/RV1DV08NWGEQ">Agile Development and Scrum</a> · <a href="https://www.coursera.org/account/accomplishments/verify/320E4Z1HD7JE">Introduction to Software Engineering</a> · <a href="https://coursera.org/verify/EG8VQBHHNTO5">Getting Started with Git and GitHub</a></li>
  <li>Linux Administration &amp; DevOps Practical Hands-on Training (self-paced)</li>
</ul>

<h2>Languages &amp; Volunteering</h2>
<p><b>Languages:</b> English (C1, proficient) · Urdu (native) · Pashto (native)</p>
<p><b>Volunteering, COMSATS University:</b> Tech Club member organising coding competitions and workshops; peer tutor for Programming Fundamentals (C++); volunteer at the University IT Help Desk.</p>

</body></html>'''


if __name__ == '__main__':
    out = {}
    versions = [('Zaid_Muzaffar_CV_web.pdf', False)]
    if PHONE:
        versions.insert(0, ('Zaid_Muzaffar_CV.pdf', True))
    else:
        print('CV_PHONE not set: building only the web version')
    for name, ph in versions:
        path = os.path.abspath(name)   # Chrome needs an absolute file:// URL
        open(path.replace('.pdf', '.html'), 'w').write(html(ph))
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
            pg = b.new_page()
            pg.goto('file://' + path.replace('.pdf', '.html'))
            pg.pdf(path=path, format='A4', print_background=True, prefer_css_page_size=True)
            b.close()
        print('built', path)
