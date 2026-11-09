/* =========================================================
   APP CORE · js/core/app.js
   Tiny shared toolkit + module registry.
   Every feature file calls App.register(name, init);
   js/main.js starts them in a fixed order.
   ========================================================= */
(function () {
  'use strict';
  var modules = {};
  var App = window.App = {
    reduceMotion: !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches),
    data: window.SITE || {},

    register: function (name, init) { modules[name] = init; },
    start: function (order) {
      order.forEach(function (name) {
        if (!modules[name]) return;
        try { modules[name](App); } catch (err) { if (window.console) console.error('[' + name + ']', err); }
      });
    },

    $: function (sel, root) { return (root || document).querySelector(sel); },
    $$: function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); },
    esc: function (t) { return String(t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); },

    toast: function (msg) {
      var el = App.$('.toast');
      if (!el) return;
      el.textContent = msg;
      el.classList.add('show');
      clearTimeout(App._toastTimer);
      App._toastTimer = setTimeout(function () { el.classList.remove('show'); }, 1800);
    },
    copy: function (text) {
      try {
        navigator.clipboard.writeText(text).then(function () { App.toast('Copied: ' + text); }, function () { App.toast(text); });
      } catch (err) { App.toast(text); }
    },
    store: {
      get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
      set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) { /* storage unavailable */ } }
    }
  };
})();
