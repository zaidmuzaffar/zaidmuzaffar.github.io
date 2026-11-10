/* =========================================================
   COMMAND PALETTE · js/core/palette.js
   Ctrl + K (⌘ + K on Mac) or the search button opens it.
   Arrow keys move, Enter runs, Esc closes.
   Commands are built from js/data.js, so new sections and
   projects appear automatically.
   ========================================================= */
(function () {
  'use strict';
  App.register('palette', function (App) {
    var D = App.data;
    var base = document.body.getAttribute('data-base') || '';   // '' on home, '../' on case pages
    var home = base + 'index.html';
    var go = function (href) { return function () { window.location.href = href; }; };
    var open = function (href) { return function () { window.location.href = href; }; };

    var items = [];
    D.sections.forEach(function (s) {
      items.push({ group: 'GO TO', label: s.num + ' · ' + s.title, hint: s.desc, run: go(base ? home + '#' + s.id : '#' + s.id) });
    });
    D.projects.forEach(function (p) {
      p.links.forEach(function (l) {
        if (!/case study|live demo/i.test(l.label)) return;
        var href = /^https?:/.test(l.href) ? l.href : base + l.href;
        items.push({ group: 'PROJECTS', label: p.title.split(' — ')[0] + ' — ' + l.label.replace(/[→↗]/g, '').trim().toLowerCase(), hint: p.statusText.toLowerCase(), run: open(href) });
      });
    });
    items.push(
      { group: 'ACTIONS', label: 'Download CV (PDF)', hint: 'résumé', run: open(base + D.profile.cv) },
      { group: 'ACTIONS', label: 'Copy email address', hint: D.profile.email, run: function () { App.copy(D.profile.email); } },
      { group: 'ACTIONS', label: 'Switch light / dark theme', hint: 'theme', run: function () { App.toggleTheme && App.toggleTheme(); } },
      { group: 'ACTIONS', label: 'Open GitHub', hint: 'github.com/' + D.config.githubUser, run: open(D.profile.github) },
      { group: 'ACTIONS', label: 'Open LinkedIn', hint: 'linkedin', run: open(D.profile.linkedin) }
    );

    var wrap = document.createElement('div');
    wrap.className = 'palette'; wrap.hidden = true;
    wrap.setAttribute('role', 'dialog'); wrap.setAttribute('aria-modal', 'true'); wrap.setAttribute('aria-label', 'Search the site');
    wrap.innerHTML = '<div class="palette-box"><div class="palette-search">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>' +
      '<input type="text" placeholder="Search sections, projects, actions…" aria-label="Search" autocomplete="off"><kbd>esc</kbd></div>' +
      '<ul class="palette-list" role="listbox"></ul></div>';
    document.body.appendChild(wrap);
    var input = App.$('input', wrap), list = App.$('.palette-list', wrap), shown = [], sel = 0, lastFocus = null;

    function draw() {
      var q = input.value.trim().toLowerCase();
      shown = items.filter(function (it) { return !q || (it.label + ' ' + it.hint + ' ' + it.group).toLowerCase().indexOf(q) !== -1; });
      if (sel >= shown.length) sel = 0;
      if (!shown.length) { list.innerHTML = '<li class="palette-empty">No results for “' + App.esc(q) + '”</li>'; return; }
      var html = '', g = '';
      shown.forEach(function (it, i) {
        if (it.group !== g) { g = it.group; html += '<li class="palette-group" role="presentation">' + g + '</li>'; }
        html += '<li class="palette-item' + (i === sel ? ' on' : '') + '" role="option" aria-selected="' + (i === sel) + '" data-i="' + i + '"><span>' + App.esc(it.label) + '</span><small>' + App.esc(it.hint) + '</small></li>';
      });
      list.innerHTML = html;
      var on = App.$('.palette-item.on', list); if (on) on.scrollIntoView({ block: 'nearest' });
    }
    function show() { lastFocus = document.activeElement; wrap.hidden = false; input.value = ''; sel = 0; draw(); input.focus(); }
    function hide() { wrap.hidden = true; if (lastFocus && lastFocus.focus) lastFocus.focus(); }
    function exec(i) { var it = shown[i]; if (!it) return; hide(); it.run(); }
    App.openPalette = show;

    input.addEventListener('input', function () { sel = 0; draw(); });
    list.addEventListener('click', function (e) { var li = e.target.closest('.palette-item'); if (li) exec(+li.getAttribute('data-i')); });
    wrap.addEventListener('click', function (e) { if (e.target === wrap) hide(); });
    document.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); wrap.hidden ? show() : hide(); return; }
      if (wrap.hidden) return;
      if (e.key === 'Escape') { e.preventDefault(); hide(); }
      else if (e.key === 'ArrowDown') { e.preventDefault(); sel = (sel + 1) % shown.length; draw(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); sel = (sel - 1 + shown.length) % shown.length; draw(); }
      else if (e.key === 'Enter') { e.preventDefault(); exec(sel); }
    });
    App.$$('[data-palette]').forEach(function (b) { b.addEventListener('click', show); });
  });
})();
