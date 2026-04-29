/**
 * js/modules/toast.js
 * Queued toast notification system.
 * Max 3 visible at once; queue processes sequentially.
 */

'use strict';

(function () {
  const MAX_VISIBLE = 3;
  const ICONS = {
    success: 'fa-circle-check',
    error:   'fa-circle-xmark',
    warning: 'fa-triangle-exclamation',
    info:    'fa-circle-info',
  };

  const queue = [];
  let processing = false;

  function container() {
    return document.getElementById('toastContainer');
  }

  function remove(toast) {
    if (!toast || toast.classList.contains('removing')) return;
    clearTimeout(toast._timer);
    toast.classList.add('removing');
    setTimeout(() => toast.remove(), 260);
  }

  function process() {
    if (!queue.length) { processing = false; return; }
    processing = true;

    const { message, type, duration } = queue.shift();
    const el = container();
    if (!el) return;

    // Remove oldest if already at max
    const existing = el.querySelectorAll('.toast:not(.removing)');
    if (existing.length >= MAX_VISIBLE) remove(existing[0]);

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `
      <i class="fa-regular ${ICONS[type] || ICONS.info} toast-icon"></i>
      <span class="toast-msg">${message}</span>
      <button class="toast-close" onclick="this.closest('.toast') && CCS.Toast._remove(this.closest('.toast'))">
        <i class="fa-regular fa-xmark"></i>
      </button>
      <div class="toast-progress" style="animation-duration:${duration}ms;"></div>`;

    el.appendChild(toast);
    toast._timer = setTimeout(() => { remove(toast); setTimeout(process, 300); }, duration);
  }

  CCS.Toast = {
    show(message, type = 'success', duration = 3500) {
      queue.push({ message, type, duration });
      if (!processing) process();
    },
    _remove: remove,
  };
})();
