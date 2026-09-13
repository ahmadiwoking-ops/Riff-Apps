/* Riff Apps — hero tile field.
   A grid of app tiles that ripples in waves, responds to the pointer and
   occasionally sheds a tile to the left, mirroring the logo mark. */

(function () {
  var canvas = document.getElementById('hero-canvas');
  if (!canvas || !canvas.getContext) return;

  var ctx = canvas.getContext('2d');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');

  var SPECTRUM = [
    [0, 180, 240],   // cyan
    [10, 120, 240],  // blue
    [26, 47, 210],   // indigo
    [122, 43, 232],  // violet
    [181, 22, 200]   // magenta
  ];

  var COLS = 11;
  var tiles = [];
  var strays = [];
  var w = 0, h = 0, cell = 0, pad = 0, dpr = 1;
  var pointer = { x: -999, y: -999, active: false };
  var t = 0, raf = null, visible = true;

  function mix(p) {
    p = Math.max(0, Math.min(0.9999, p));
    var s = p * (SPECTRUM.length - 1);
    var i = Math.floor(s), f = s - i;
    var a = SPECTRUM[i], b = SPECTRUM[Math.min(i + 1, SPECTRUM.length - 1)];
    return [
      Math.round(a[0] + (b[0] - a[0]) * f),
      Math.round(a[1] + (b[1] - a[1]) * f),
      Math.round(a[2] + (b[2] - a[2]) * f)
    ];
  }

  function roundRect(x, y, size, r) {
    ctx.beginPath();
    if (ctx.roundRect) { ctx.roundRect(x, y, size, size, r); return; }
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + size, y, x + size, y + size, r);
    ctx.arcTo(x + size, y + size, x, y + size, r);
    ctx.arcTo(x, y + size, x, y, r);
    ctx.arcTo(x, y, x + size, y, r);
    ctx.closePath();
  }

  function build() {
    var rect = canvas.getBoundingClientRect();
    if (!rect.width) return;
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = rect.width; h = rect.height;
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    var gap = w / COLS * 0.22;
    cell = (w - gap * (COLS + 1)) / COLS;
    pad = gap;

    tiles = [];
    var cx = (COLS - 1) / 2;
    for (var r = 0; r < COLS; r++) {
      for (var c = 0; c < COLS; c++) {
        var dx = c - cx, dy = r - cx;
        var dist = Math.sqrt(dx * dx + dy * dy);
        // Clear a hole in the middle so the logo mark sits in open space,
        // and fade the field out towards the corners.
        var clearing = Math.min(1, Math.max(0, (dist - 2.1) / 1.6));
        var edge = Math.min(1, Math.max(0, (6.4 - dist) / 2.2));
        var base = clearing * edge;
        if (base < 0.02) continue;
        tiles.push({
          c: c, r: r,
          x: pad + c * (cell + pad),
          y: pad + r * (cell + pad),
          base: base,
          hue: (c / (COLS - 1)) * 0.72 + (r / (COLS - 1)) * 0.28,
          phase: dist * 0.55 + Math.random() * 0.4,
          lift: 0
        });
      }
    }
  }

  function shed() {
    if (strays.length > 5 || !tiles.length) return;
    var seed = tiles[Math.floor(Math.random() * tiles.length)];
    strays.push({
      x: seed.x, y: seed.y,
      vx: -(0.35 + Math.random() * 0.45),
      vy: (Math.random() - 0.6) * 0.18,
      size: cell * (0.5 + Math.random() * 0.4),
      hue: seed.hue,
      life: 1
    });
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    var i, tile, col;

    for (i = 0; i < tiles.length; i++) {
      tile = tiles[i];

      // Travelling diagonal wave.
      var wave = Math.sin(t * 0.9 - tile.phase * 1.15);
      var energy = 0.5 + 0.5 * wave;

      // Pointer proximity lift.
      var target = 0;
      if (pointer.active) {
        var px = pointer.x - (tile.x + cell / 2);
        var py = pointer.y - (tile.y + cell / 2);
        var pd = Math.sqrt(px * px + py * py);
        target = Math.max(0, 1 - pd / (cell * 3.4));
      }
      tile.lift += (target - tile.lift) * 0.12;

      var amp = tile.base * (0.30 + energy * 0.62 + tile.lift * 0.55);
      var size = cell * (0.68 + energy * 0.14 + tile.lift * 0.2);
      var off = (cell - size) / 2 - tile.lift * 3;

      col = mix(tile.hue * 0.85 + energy * 0.12);
      // Lift the peaks towards white so the wave reads as light moving
      // across the field rather than a flat block of colour.
      var lum = energy * 0.28 + tile.lift * 0.35;
      var r0 = Math.round(col[0] + (255 - col[0]) * lum);
      var g0 = Math.round(col[1] + (255 - col[1]) * lum);
      var b0 = Math.round(col[2] + (255 - col[2]) * lum);

      ctx.globalAlpha = Math.min(1, amp);
      ctx.fillStyle = 'rgb(' + r0 + ',' + g0 + ',' + b0 + ')';
      ctx.shadowColor = 'rgba(' + col[0] + ',' + col[1] + ',' + col[2] + ',0.9)';
      ctx.shadowBlur = (energy * 10 + tile.lift * 18) * tile.base;
      roundRect(tile.x + off, tile.y + off, size, size * 0.26);
      ctx.fill();
      ctx.shadowBlur = 0;

      if (tile.lift > 0.15) {
        ctx.globalAlpha = tile.lift * 0.5;
        ctx.strokeStyle = 'rgba(234,240,252,0.9)';
        ctx.lineWidth = 1;
        ctx.stroke();
      }
    }

    for (i = strays.length - 1; i >= 0; i--) {
      var s = strays[i];
      s.x += s.vx; s.y += s.vy; s.life -= 0.006;
      if (s.life <= 0 || s.x < -s.size) { strays.splice(i, 1); continue; }
      col = mix(s.hue);
      ctx.globalAlpha = Math.max(0, s.life) * 0.85;
      ctx.fillStyle = 'rgb(' + col[0] + ',' + col[1] + ',' + col[2] + ')';
      roundRect(s.x, s.y, s.size, s.size * 0.26);
      ctx.fill();
    }

    ctx.globalAlpha = 1;
  }

  function loop() {
    t += 0.016;
    if (Math.random() < 0.014) shed();
    draw();
    raf = requestAnimationFrame(loop);
  }

  function start() {
    if (raf || reduced.matches || !visible) return;
    raf = requestAnimationFrame(loop);
  }
  function stop() {
    if (raf) { cancelAnimationFrame(raf); raf = null; }
  }

  function staticFrame() {
    t = 1.6;
    pointer.active = false;
    draw();
  }

  canvas.addEventListener('pointermove', function (e) {
    var rect = canvas.getBoundingClientRect();
    pointer.x = e.clientX - rect.left;
    pointer.y = e.clientY - rect.top;
    pointer.active = true;
    if (reduced.matches) draw();
  });
  canvas.addEventListener('pointerleave', function () {
    pointer.active = false;
    if (reduced.matches) staticFrame();
  });

  var resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      build();
      if (reduced.matches) staticFrame();
    }, 150);
  });

  document.addEventListener('visibilitychange', function () {
    if (document.hidden) stop(); else start();
  });

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
      if (visible) start(); else stop();
    }, { threshold: 0.05 }).observe(canvas);
  }

  function init() {
    build();
    if (reduced.matches) staticFrame(); else start();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else { init(); }

  if (reduced.addEventListener) {
    reduced.addEventListener('change', function () {
      stop();
      if (reduced.matches) staticFrame(); else start();
    });
  }
})();
