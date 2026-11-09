/* =========================================================
   UI LAYER · js/core/ui.js
   Page-wide behaviour shared by every page:
   preloader, copy buttons, click ping, reveal on scroll,
   sticky nav, scroll progress, timeline fill, case-study TOC.
   ========================================================= */
(function () {
  'use strict';

  /* Boot preloader */
  App.register('preloader', function (App) {
    var pre = App.$('.preloader');
    document.body.classList.add('loaded');
    if (!pre) return;
    var fill = App.$('.boot-fill', pre), pct = App.$('.boot-pct span', pre), level = 0;
    var done = function () { pre.classList.add('done'); };
    if (App.reduceMotion) return done();
    var t = setInterval(function () {
      level = Math.min(100, level + 4 + Math.random() * 7);
      if (fill) fill.style.width = level + '%';
      if (pct) pct.textContent = Math.round(level);
      if (level >= 100) { clearInterval(t); setTimeout(done, 250); }
    }, 45);
  });

  /* Copy buttons + click ping */
  App.register('interactions', function (App) {
    document.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-copy]');
      if (!btn) return;
      e.preventDefault();
      App.copy(btn.getAttribute('data-copy'));
    });
    if (App.reduceMotion) return;
    document.addEventListener('pointerdown', function (e) {
      if (e.target.closest('.palette')) return;
      for (var i = 0; i < 2; i++) {
        var r = document.createElement('span');
        r.className = 'ripple' + (i ? ' r2' : '');
        r.style.left = e.clientX + 'px';
        r.style.top = e.clientY + 'px';
        document.body.appendChild(r);
        setTimeout(function (el) { el.remove(); }, 1100, r);
      }
    });
  });

  /* Reveal on scroll */
  App.register('reveal', function (App) {
    var els = App.$$('.reveal');
    if (!('IntersectionObserver' in window) || App.reduceMotion) { els.forEach(function (el) { el.classList.add('in'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });
    App.observeReveal = function (el) { io.observe(el); };
  });

  /* Sticky nav, scroll progress, timeline fill, TOC, active nav link */
  App.register('scroll', function (App) {
    var nav = App.$('.nav');
    var fill = App.$('.scroll-pipe-fill');
    var nodes = App.$$('.scroll-pipe-node');
    var targets = nodes.map(function (n) { return document.querySelector(n.getAttribute('href')); });
    var tl = App.$('.timeline'), tlFill = App.$('.timeline-pipe-fill');
    var toc = App.$$('.toc a'), tocT = toc.map(function (a) { return document.querySelector(a.getAttribute('href')); });
    var navLinks = App.$$('#nav-links a'), navT = navLinks.map(function (a) { return document.querySelector(a.getAttribute('href')); });

    function place() {
      var docH = document.documentElement.scrollHeight - window.innerHeight;
      nodes.forEach(function (n, i) {
        var t = targets[i]; if (!t || docH <= 0) return;
        var p = Math.min(1, Math.max(0, (t.offsetTop - 80) / docH));
        n.style.top = (p * 100) + '%'; n.dataset.p = p;
      });
    }
    function current(list) {
      var c = -1;
      list.forEach(function (s, i) { if (s && s.getBoundingClientRect().top < 160) c = i; });
      return c;
    }
    function onScroll() {
      var y = window.scrollY, docH = document.documentElement.scrollHeight - window.innerHeight, p = docH > 0 ? y / docH : 0;
      if (nav) nav.classList.toggle('scrolled', y > 10);
      if (fill) fill.style.height = (p * 100) + '%';
      nodes.forEach(function (n) { n.classList.toggle('on', p + 0.001 >= parseFloat(n.dataset.p || 2)); });
      if (tl && tlFill) {
        var r = tl.getBoundingClientRect();
        tlFill.style.height = (Math.min(1, Math.max(0, (window.innerHeight * 0.7 - r.top) / r.height)) * 100) + '%';
      }
      if (toc.length) { var c = Math.max(0, current(tocT)); toc.forEach(function (a, i) { a.classList.toggle('on', i === c); }); }
      if (navLinks.length) { var k = current(navT); navLinks.forEach(function (a, i) { a.classList.toggle('on', i === k); }); }
    }
    App.refreshScroll = function () { place(); onScroll(); };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', App.refreshScroll);
    window.addEventListener('load', App.refreshScroll);
    App.refreshScroll();

    var yr = App.$('[data-year]'); if (yr) yr.textContent = new Date().getFullYear();
  });
})();
