/* =========================================================
   THEME · js/core/theme.js
   Light / dark switch. The saved choice is applied by a tiny
   inline script in <head> before paint, so there is no flash.
   ========================================================= */
(function () {
  'use strict';
  /* Laptop / mobile view switch — only offered on phones and small tablets */
  App.register('view', function (App) {
    var root = document.documentElement;
    if (!root.classList.contains('small-device')) return;
    var laptop = root.classList.contains('laptop-view');
    App.$$('[data-view-toggle]').forEach(function (b) {
      b.hidden = false;
      b.setAttribute('aria-label', laptop ? 'Switch to mobile view' : 'Switch to laptop view');
      b.innerHTML = laptop
        ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/></svg><span>Mobile view</span>'
        : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/></svg><span>Laptop view</span>';
      b.addEventListener('click', function () {
        App.store.set('zaid-view', laptop ? 'mobile' : 'laptop');
        window.location.reload();
      });
    });
    App.toggleView = function () { var b = App.$('[data-view-toggle]'); if (b) b.click(); };
  });

  App.register('theme', function (App) {
    var root = document.documentElement;
    var btns = App.$$('[data-theme-toggle]');
    var paint = function () {
      var light = root.getAttribute('data-theme') === 'light';
      btns.forEach(function (b) {
        b.setAttribute('aria-label', light ? 'Switch to dark theme' : 'Switch to light theme');
        b.innerHTML = light
          ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
          : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
      });
    };
    App.toggleTheme = function () {
      var next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      root.setAttribute('data-theme', next);
      App.store.set('zaid-theme', next);
      paint();
    };
    btns.forEach(function (b) { b.addEventListener('click', App.toggleTheme); });
    paint();
  });
})();
