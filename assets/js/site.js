/* Riff Apps — shared behaviour */

(function () {
  /* Mobile navigation ---------------------------------------------------- */
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('primary-nav');

  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.getAttribute('data-open') === 'true';
      nav.setAttribute('data-open', String(!open));
      btn.setAttribute('aria-expanded', String(!open));
      btn.setAttribute('aria-label', open ? 'Open menu' : 'Close menu');
    });

    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.setAttribute('data-open', 'false');
        btn.setAttribute('aria-expanded', 'false');
      }
    });

    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.getAttribute('data-open') === 'true') {
        nav.setAttribute('data-open', 'false');
        btn.setAttribute('aria-expanded', 'false');
        btn.focus();
      }
    });
  }

  /* Current year in the footer ------------------------------------------- */
  var year = document.querySelectorAll('[data-year]');
  for (var i = 0; i < year.length; i++) {
    year[i].textContent = String(new Date().getFullYear());
  }

  /* Contact form ---------------------------------------------------------
     The site ships as a static build with no server, so the form composes a
     pre-filled message in the visitor's own mail client. Nothing is stored or
     transmitted by Riff Apps until they press send. See README.md for wiring
     this to a serverless handler instead. */
  var form = document.getElementById('contact-form');
  if (form) {
    var status = document.getElementById('form-status');

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var data = new FormData(form);
      var name = (data.get('name') || '').toString().trim();
      var org = (data.get('organisation') || '').toString().trim();
      var email = (data.get('email') || '').toString().trim();
      var topic = (data.get('topic') || '').toString().trim();
      var message = (data.get('message') || '').toString().trim();

      if (!name || !email || !message) {
        if (status) status.textContent = 'Add your name, email and a short message before sending.';
        return;
      }

      var subject = topic ? topic + ' enquiry from ' + name : 'Enquiry from ' + name;
      var body = [
        'Name: ' + name,
        'Organisation: ' + (org || 'Not given'),
        'Email: ' + email,
        'Topic: ' + (topic || 'General'),
        '',
        message,
        '',
        '— Sent from riff-apps.com'
      ].join('\n');

      window.location.href = 'mailto:Contact@Riff-Apps.com'
        + '?subject=' + encodeURIComponent(subject)
        + '&body=' + encodeURIComponent(body);

      if (status) {
        status.textContent = 'Your mail app is opening with this message ready to send. '
          + 'If nothing happens, email Contact@Riff-Apps.com directly.';
      }
    });
  }
})();
