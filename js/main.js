/* =========================================================
   ENTRY POINT · js/main.js
   Starts every module in order. Load order in HTML:
   data.js → core/app.js → core/*.js → main.js
   ========================================================= */
App.start([
  'view',         // laptop / mobile view on phones
  'theme',        // light / dark
  'render',       // data.js → markup (home page only)
  'preloader',    // boot screen
  'interactions', // copy buttons, click ping
  'lightbox',     // image preview
  'reveal',       // animate in on scroll
  'scroll',       // nav, progress, timeline, TOC
  'hero',         // typed role, status dial
  'pipeline',     // CI/CD card
  'filter',       // project filter
  'terminal',     // interactive terminal
  'activity',     // GitHub graph
  'contact',      // contact form
  'palette',      // Ctrl + K
  'analytics'     // GoatCounter (only if configured)
]);
