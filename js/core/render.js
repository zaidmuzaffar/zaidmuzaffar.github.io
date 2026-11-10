/* =========================================================
   RENDER LAYER · js/core/render.js
   Turns js/data.js into page markup. Only runs on the home page
   (each target element is optional).
   ========================================================= */
(function () {
  'use strict';
  App.register('render', function (App) {
    var D = App.data, e = App.esc, $ = App.$;
    var put = function (sel, html) { var el = $(sel); if (el) el.innerHTML = html; return el; };

    /* Nav links, scroll-progress nodes */
    var navSections = D.sections.filter(function (s) { return s.id !== 'map' && s.id !== 'contact'; });
    put('#nav-links', navSections.map(function (s) {
      return '<a href="#' + s.id + '">' + s.num + ' ' + e(s.name) + '</a>';
    }).join(''));
    put('#scroll-nodes', '<a class="scroll-pipe-node" href="#top"><span>top</span></a>' + D.sections.map(function (s) {
      return '<a class="scroll-pipe-node" href="#' + s.id + '"><span>' + s.num + ' ' + e(s.name) + '</span></a>';
    }).join(''));

    /* Section headers: every section gets the same kicker + title */
    D.sections.forEach(function (s) {
      var head = $('#' + s.id + ' [data-head]');
      if (!head) return;
      var sub = head.getAttribute('data-sub');
      head.innerHTML = '<h2 class="section-title"><span class="section-kicker">' + s.num + ' / ' + e(s.name) + '</span>' + e(s.title) + '</h2>' +
        (sub ? '<p class="section-sub">' + e(sub) + '</p>' : '');
    });

    /* 00 · System map */
    var counts = {
      about: D.facts.length + ' facts',
      journey: (D.experience || []).length + ' internship · ' + D.timeline.length + ' milestones',
      projects: D.projects.length + ' builds',
      stack: D.skills.reduce(function (n, g) { return n + g.items.length; }, 0) + ' tools',
      console: 'interactive',
      contact: 'open'
    };
    var services = D.sections.filter(function (s) { return s.id !== 'map'; });
    put('#sysmap',
      '<div class="sm-col"><div class="sm-node"><span class="sm-tag">CLIENT</span><b>You</b><small>browser · phone</small></div></div>' +
      '<div class="sm-link"></div>' +
      '<div class="sm-node sm-gateway"><span class="sm-tag">GATEWAY</span><b>zaid<span style="color:var(--accent)">.ops</span></b><small>this portfolio</small></div>' +
      '<div class="sm-link"></div>' +
      '<div class="sm-services">' + services.map(function (s) {
        return '<a class="sm-node" href="#' + s.id + '"><span class="sm-led" aria-hidden="true"></span><span class="sm-tag">' + s.num + ' · SERVICE</span><b>' + e(s.service) + '</b><small>' + e(counts[s.id] || s.desc) + '</small></a>';
      }).join('') + '</div>' +
      '<div class="sm-link"></div>' +
      '<div class="sm-col">' + D.external.map(function (x) {
        return '<a class="sm-node" href="' + e(x.href) + '"><span class="sm-tag">EXTERNAL</span><b>' + e(x.name) + ' ↗</b><small>' + e(x.meta) + '</small></a>';
      }).join('') + '</div>' +
      '<div class="sm-legend"><span><i></i>service healthy</span><span>click any box to jump there</span><span>press <span class="kbd">Ctrl</span> + <span class="kbd">K</span> to search everything</span></div>'
    );

    /* 01 · About facts */
    put('#facts', D.facts.map(function (f) {
      return '<div class="card fact"><small>' + e(f.k) + '</small><b>' + e(f.v) + '</b></div>';
    }).join(''));

    /* 02 · Experience */
    put('#experience', (D.experience || []).map(function (x) {
      return '<article class="card xp reveal">' +
        '<div class="xp-main">' +
          '<div class="xp-top"><span class="status live">COMPLETED</span><span class="mono xp-type">' + e(x.type) + '</span></div>' +
          '<h3 class="xp-role">' + e(x.role) + '</h3>' +
          '<div class="xp-org">' + e(x.org) + ' <span>· ' + e(x.period) + '</span></div>' +
          '<p class="xp-sum">' + e(x.summary) + '</p>' +
          '<ul class="xp-list">' + x.highlights.map(function (h) { return '<li>' + e(h) + '</li>'; }).join('') + '</ul>' +
          '<div class="chips">' + x.tools.map(function (t) { return '<span class="chip">' + e(t) + '</span>'; }).join('') + '</div>' +
        '</div>' +
        '<aside class="xp-side">' +
          '<div class="xp-stats">' + x.stats.map(function (st) { return '<div><b>' + e(st.n) + '</b><small>' + e(st.k) + '</small></div>'; }).join('') + '</div>' +
          '<a class="xp-cert" href="' + e(x.certificate) + '"><img src="' + e(x.certificateImage) + '" alt="Certificate of completion: ' + e(x.role) + ', ' + e(x.org) + '" loading="lazy"><span>View certificate (PDF) ↓</span></a>' +
          '<small class="mono xp-id">' + e(x.id) + '</small>' +
        '</aside></article>';
    }).join(''));

    /* 02 · Journey timeline */
    put('#timeline-list', D.timeline.map(function (t) {
      return '<li class="tl-item reveal' + (t.now ? ' now' : '') + '"><span class="tl-when">' + (t.now ? '<span class="dot"></span>' : '') + e(t.when) + '</span>' +
        '<div class="tl-what"><strong>' + e(t.title) + '</strong><span>' + e(t.text) + '</span></div></li>';
    }).join(''));

    /* 03 · Projects */
    put('#filters', D.filters.map(function (f, i) {
      var n = f.id === 'all' ? D.projects.length : D.projects.filter(function (p) { return p.cats.indexOf(f.id) !== -1; }).length;
      return '<button type="button" data-filter="' + f.id + '" aria-pressed="' + (i === 0) + '">' + e(f.label) + '<span>' + n + '</span></button>';
    }).join(''));
    put('#project-grid', D.projects.map(function (p, i) {
      var demo = p.demo ? '<div class="demo-box">' +
        '<div class="row"><span class="k">email</span><span class="v">' + e(p.demo.email) + '</span><button class="copy-btn" type="button" data-copy="' + e(p.demo.email) + '" aria-label="Copy demo email">copy</button></div>' +
        '<div class="row"><span class="k">password</span><span class="v">' + e(p.demo.password) + '</span><button class="copy-btn" type="button" data-copy="' + e(p.demo.password) + '" aria-label="Copy demo password">copy</button></div></div>' : '';
      var links = p.links.length ? '<div class="project-links">' + p.links.map(function (l) {
        return '<a class="plink' + (l.main ? ' main' : '') + '" href="' + e(l.href) + '">' + e(l.label) + '</a>';
      }).join('') + '</div>' : '';
      return '<article class="card project reveal d' + (i % 3) + '" data-cat="' + p.cats.join(' ') + '">' +
        '<div class="project-top"><span class="project-num">' + (i < 9 ? '0' : '') + (i + 1) + ' /</span><span class="status ' + p.status + '">' + e(p.statusText) + '</span></div>' +
        '<div class="project-body"><h3>' + e(p.title) + '</h3><p>' + e(p.desc) + '</p><span class="project-stack">' + e(p.stack) + '</span></div>' +
        demo + links + '</article>';
    }).join(''));

    /* 04 · Stack */
    put('#skills', D.skills.map(function (g, i) {
      return '<div class="card stack-card reveal d' + (i % 4) + '"><span class="mono">' + e(g.group) + '</span><div class="chips">' +
        g.items.map(function (it) { return '<span class="chip">' + e(it) + '</span>'; }).join('') + '</div></div>';
    }).join(''));
    put('#certs-issuer', e(D.certsIssuer));
    put('#certs', D.certs.map(function (c) {
      return '<a class="cert" href="' + e(c.href) + '">' + e(c.name) + ' <small>' + e(c.tag || 'verify ↗') + '</small></a>';
    }).join(''));
    put('#langs', D.languages.map(function (l) {
      return '<div class="lang"><b>' + e(l.name) + '</b><span>' + e(l.level) + '</span></div>';
    }).join(''));

    /* Recommendations: hidden until real ones are added in data.js */
    var recBlock = $('#recs-block');
    if (recBlock) {
      if (D.recommendations && D.recommendations.length) {
        recBlock.hidden = false;
        put('#recs', D.recommendations.map(function (r) {
          return '<figure class="card rec reveal"><blockquote>“' + e(r.quote) + '”</blockquote><figcaption><b>' + e(r.name) + '</b>' + e(r.role || '') + '</figcaption></figure>';
        }).join(''));
      } else {
        recBlock.hidden = true;
      }
    }

    /* Contact */
    put('#contact-email', e(D.profile.email));
    var cb = $('#copy-email'); if (cb) cb.setAttribute('data-copy', D.profile.email);
  });
})();
