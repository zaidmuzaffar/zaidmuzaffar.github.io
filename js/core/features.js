/* =========================================================
   FEATURES · js/core/features.js
   Home-page features, one module each:
   hero (typed role + status dial), pipeline card, project filter,
   terminal, GitHub activity, contact form, analytics.
   ========================================================= */
(function () {
  'use strict';

  /* Hero: typed role line + status dial */
  App.register('hero', function (App) {
    var g = App.$('.gauge');
    if (g) setTimeout(function () { g.classList.add('on'); }, App.reduceMotion ? 0 : 1300);
    var typed = App.$('.typed');
    if (!typed) return;
    var roles = App.data.profile.roles;
    if (App.reduceMotion) { typed.textContent = roles[0]; return; }
    var ri = 0, ci = 0, del = false;
    (function tick() {
      var w = roles[ri];
      ci += del ? -1 : 1;
      typed.textContent = w.slice(0, ci);
      var wait = del ? 35 : 70;
      if (!del && ci === w.length) { del = true; wait = 1600; }
      else if (del && ci === 0) { del = false; ri = (ri + 1) % roles.length; wait = 300; }
      setTimeout(tick, wait);
    })();
  });

  /* CI/CD pipeline card: stages run in a loop */
  App.register('pipeline', function (App) {
    var stages = App.$$('.pc-stage'), badge = App.$('.pc-badge');
    if (!stages.length) return;
    var step = 0;
    var paint = function () {
      stages.forEach(function (s, i) { s.classList.toggle('done', i < step); s.classList.toggle('run', i === step); });
      var ok = step >= stages.length;
      if (badge) { badge.textContent = ok ? 'passed' : 'running'; badge.classList.toggle('passed', ok); }
    };
    if (App.reduceMotion) { step = stages.length; return paint(); }
    paint();
    setInterval(function () { step = step > stages.length ? 0 : step + 1; paint(); }, 1100);
  });

  /* Project filter */
  App.register('filter', function (App) {
    var btns = App.$$('#filters button'), cards = App.$$('.project');
    btns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var cat = btn.getAttribute('data-filter'), n = 0;
        btns.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        cards.forEach(function (c) {
          var show = cat === 'all' || c.getAttribute('data-cat').split(' ').indexOf(cat) !== -1;
          c.hidden = !show;
          if (show) { n++; var num = App.$('.project-num', c); if (num) num.textContent = (n < 10 ? '0' : '') + n + ' /'; c.classList.add('in'); }
        });
        setTimeout(App.refreshScroll, 50);
      });
    });
  });

  /* Interactive terminal — answers come from js/data.js */
  App.register('terminal', function (App) {
    var out = App.$('#term-out'), form = App.$('#term-form'), input = App.$('#term-input');
    if (!out || !form) return;
    var D = App.data, e = App.esc, pad = function (s, n) { s = String(s); while (s.length < n) s += ' '; return s; };
    var cmds = {
      help: function () {
        return 'Available commands:\n' + [['whoami', 'who I am'], ['skills', 'my stack'], ['projects', 'things I have built'], ['certs', 'certifications'], ['contact', 'how to reach me'], ['cv', 'download my CV'], ['theme', 'switch light / dark'], ['clear', 'clear the screen']]
          .map(function (c) { return '  <span class="hl">' + pad(c[0], 10) + '</span>' + c[1]; }).join('\n');
      },
      whoami: function () { return e(D.profile.name + ' — ' + D.profile.role + '.\n' + D.facts[1].v + ', ' + D.facts[2].v + '.\nBased in ' + D.profile.location + '.\nI automate the path from code to production.'); },
      skills: function () { return D.skills.map(function (g) { return '<span class="hl">' + e(pad(g.group.toLowerCase(), 22)) + '</span>' + e(g.items.join(' · ')); }).join('\n'); },
      projects: function () {
        return D.projects.map(function (p) {
          var cs = p.links.filter(function (l) { return /case study/i.test(l.label); })[0];
          return '<span class="ok">●</span> ' + e(pad(p.title.split(' — ')[0], 34)) + e(pad(p.statusText.toLowerCase(), 12)) + (cs ? '<a href="' + e(cs.href) + '">case study</a>' : '');
        }).join('\n');
      },
      certs: function () { return e(D.certsIssuer) + ':\n' + D.certs.map(function (c) { return '  ' + e(c.name); }).join('\n'); },
      contact: function () { return 'email     ' + e(D.profile.email) + '\nlinkedin  <a href="' + e(D.profile.linkedin) + '">linkedin.com/in/zaid-muzaffar</a>\ngithub    <a href="' + e(D.profile.github) + '">github.com/' + e(D.config.githubUser) + '</a>'; },
      cv: function () { return 'CV ready → <a href="' + e(D.profile.cv) + '" download>Zaid_Muzaffar_CV.pdf</a>'; },
      resume: function () { return cmds.cv(); },
      theme: function () { if (App.toggleTheme) App.toggleTheme(); return 'theme switched to <span class="hl">' + document.documentElement.getAttribute('data-theme') + '</span>'; },
      ls: function () { return 'about.md  journey.log  projects/  stack.yml  certs/  contact.txt'; },
      sudo: function () { return 'Nice try. Permission denied 🙂'; },
      date: function () { return e(new Date().toString()); }
    };
    var run = function (raw) {
      var c = raw.trim().toLowerCase(); if (!c) return;
      if (c === 'clear') { out.innerHTML = ''; return; }
      var line = document.createElement('div'); line.className = 'cmd'; line.textContent = raw.trim(); out.appendChild(line);
      var key = c.split(' ')[0], res = document.createElement('div');
      res.innerHTML = cmds[key] ? cmds[key]() : 'command not found: ' + e(key) + ' — try <span class="hl">help</span>';
      out.appendChild(res); out.scrollTop = out.scrollHeight; if (App.markExternal) App.markExternal();
    };
    App.runCommand = run;
    out.innerHTML = 'Welcome to zaid.ops — type <span class="hl">help</span> or tap a command below.';
    run('help');
    form.addEventListener('submit', function (ev) { ev.preventDefault(); run(input.value); input.value = ''; });
    App.$$('[data-cmd]').forEach(function (b) { b.addEventListener('click', function () { run(b.getAttribute('data-cmd')); }); });
  });

  /* GitHub activity graph
     1st choice: contribution data (github-contributions-api.jogruber.de) drawn in the site's own colours.
     2nd choice: ready-made image from ghchart.  Last resort: a link to the profile. */
  App.register('activity', function (App) {
    var box = App.$('#activity-graph'); if (!box) return;
    var user = App.data.config.githubUser, e = App.esc, done = false;
    var link = '<a class="plink" href="https://github.com/' + e(user) + '" target="_blank" rel="noopener noreferrer">Open my GitHub profile ↗</a>';
    var showLink = function () {
      if (done) return; done = true;
      box.innerHTML = '<div class="activity-fallback"><span>The contribution graph couldn\'t load right now (it also won\'t show inside a preview).</span>' + link + '</div>';
    };
    var tryImage = function () {
      if (done) return;
      var img = new Image();
      img.alt = 'GitHub contribution graph for ' + user;
      img.onload = function () { if (done) return; done = true; box.innerHTML = ''; box.appendChild(img); };
      img.onerror = showLink;
      img.src = 'https://ghchart.rshah.org/0A8FB0/' + encodeURIComponent(user);
      setTimeout(function () { if (!done) showLink(); }, 8000);
    };
    var draw = function (data) {
      var days = (data && data.contributions) || [];
      if (!days.length) throw new Error('no data');
      var total = days.reduce(function (n, d) { return n + (d.count || 0); }, 0);
      var first = new Date(days[0].date + 'T00:00:00').getDay();      // pad so columns start on Sunday
      var cells = '';
      for (var i = 0; i < first; i++) cells += '<i class="pad"></i>';
      days.forEach(function (d) {
        cells += '<i class="l' + (d.level || 0) + '" title="' + e(d.count + ' contribution' + (d.count === 1 ? '' : 's') + ' on ' + d.date) + '"></i>';
      });
      done = true;
      box.innerHTML = '<div class="contrib-total"><b>' + total + '</b> contributions in the last year</div>' +
        '<div class="contrib-scroll"><div class="contrib" role="img" aria-label="' + total + ' GitHub contributions in the last year">' + cells + '</div></div>' +
        '<div class="contrib-legend"><span>Less</span><i class="l0"></i><i class="l1"></i><i class="l2"></i><i class="l3"></i><i class="l4"></i><span>More</span></div>';
      var sc = App.$('.contrib-scroll', box); if (sc) sc.scrollLeft = sc.scrollWidth;   // show the most recent weeks first
    };
    box.innerHTML = '<div class="activity-fallback"><span>Loading activity…</span></div>';
    if (!window.fetch) return tryImage();
    var timer = setTimeout(function () { if (!done) tryImage(); }, 6000);
    fetch('https://github-contributions-api.jogruber.de/v4/' + encodeURIComponent(user) + '?y=last')
      .then(function (r) { if (!r.ok) throw new Error('http ' + r.status); return r.json(); })
      .then(function (data) { if (done) return; clearTimeout(timer); draw(data); })
      .catch(function () { clearTimeout(timer); tryImage(); });
  });

  /* Contact form → Formspree (set formspreeId in js/data.js) */
  App.register('contact', function (App) {
    var form = App.$('#contact-form'); if (!form) return;
    var status = App.$('#form-status'), id = App.data.config.formspreeId, email = App.data.profile.email;
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!form.reportValidity()) return;
      if (!id) { status.textContent = 'The form isn\'t connected yet — please email ' + email + ' directly.'; return; }
      var btn = App.$('button[type=submit]', form);
      btn.disabled = true; status.textContent = 'Sending…';
      fetch('https://formspree.io/f/' + encodeURIComponent(id), { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) })
        .then(function (r) {
          if (!r.ok) throw new Error('send failed');
          form.reset(); status.textContent = 'Thanks! Your message was sent — I\'ll reply soon.';
        })
        .catch(function () { status.textContent = 'Couldn\'t send right now — please email ' + email + ' directly.'; })
        .then(function () { btn.disabled = false; });
    });
  });

  /* Privacy-friendly analytics (GoatCounter) — only loads when a code is set in js/data.js */
  App.register('analytics', function (App) {
    var code = App.data.config.goatcounter;
    if (!code) return;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://gc.zgo.at/count.js';
    s.setAttribute('data-goatcounter', 'https://' + code + '.goatcounter.com/count');
    document.body.appendChild(s);
  });
})();
