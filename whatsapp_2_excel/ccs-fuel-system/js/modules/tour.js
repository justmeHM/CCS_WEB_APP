/**
 * js/modules/tour.js
 * Guided onboarding tour with spotlight highlighting.
 */

'use strict';

(function () {
  const STEPS = [
    { target: '#sidebar',       title: 'Navigation',       desc: 'Use the sidebar to move between pages — Dashboard, Orders, Daily Entry, and more.' },
    { target: '[data-page="orders"]',  title: 'Orders',    desc: 'Create fuel orders and allocate litres to technicians per order.' },
    { target: '[data-page="daily"]',   title: 'Daily Entry',desc: 'Record each day\'s fuel supply per technician from this page.' },
    { target: '[data-page="leaderboard"]', title: 'Leaderboard', desc: 'Track technician performance ranked by fuel supplied.' },
    { target: '[data-page="automation"]',  title: 'Automation',  desc: 'Paste WhatsApp reports to auto-fill daily entries in seconds.' },
    { target: '#topbarRegion',  title: 'Regions',          desc: 'Switch between regions at any time from this selector.' },
  ];

  let _step = 0;

  function _spot(el) {
    const sp = document.getElementById('tourSpotlight');
    if (!sp || !el) return;
    const rect = el.getBoundingClientRect();
    const pad  = 8;
    Object.assign(sp.style, {
      top:    (rect.top    - pad + window.scrollY) + 'px',
      left:   (rect.left   - pad) + 'px',
      width:  (rect.width  + pad * 2) + 'px',
      height: (rect.height + pad * 2) + 'px',
    });
  }

  function _tooltip(el, step) {
    const tt = document.getElementById('tourTooltip');
    if (!tt || !el) return;

    document.getElementById('tourStepIndicator').textContent = `Step ${_step + 1} of ${STEPS.length}`;
    document.getElementById('tourTitle').textContent = step.title;
    document.getElementById('tourDesc').textContent  = step.desc;

    const rect = el.getBoundingClientRect();
    const left = Math.min(rect.right + 16, window.innerWidth - 380);
    const top  = Math.max(rect.top, 80);
    Object.assign(tt.style, { top: top + 'px', left: left + 'px', display: 'block' });

    document.getElementById('tourPrevBtn').style.visibility = _step === 0 ? 'hidden' : 'visible';
    document.getElementById('tourNextBtn').textContent = _step === STEPS.length - 1 ? 'Finish' : 'Next →';
  }

  function _render() {
    const step = STEPS[_step];
    const el   = document.querySelector(step.target);
    if (!el) { _step < STEPS.length - 1 ? next() : end(); return; }
    _spot(el);
    _tooltip(el, step);
  }

  function start() {
    if (localStorage.getItem('ccs_tour_done')) return;
    _step = 0;
    document.getElementById('tourBackdrop').style.display = 'block';
    document.getElementById('tourTooltip').style.display  = 'block';
    _render();
  }

  function next() {
    _step++;
    if (_step >= STEPS.length) { end(); return; }
    _render();
  }

  function prev() {
    if (_step > 0) { _step--; _render(); }
  }

  function end() {
    document.getElementById('tourBackdrop').style.display = 'none';
    document.getElementById('tourTooltip').style.display  = 'none';
    localStorage.setItem('ccs_tour_done', '1');
  }

  CCS.Tour = { start, next, prev, end };
})();
