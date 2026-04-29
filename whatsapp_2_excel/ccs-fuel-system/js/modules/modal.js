/**
 * js/modules/modal.js
 * Modal lifecycle: open/close with focus trap and ARIA.
 */

'use strict';

(function () {
  const trapHandlers = new Map();

  function open(modalId) {
    const overlay = document.getElementById(modalId);
    if (!overlay) return;
    overlay.classList.add('active');
    overlay._triggerEl = document.activeElement;
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');

    const heading = overlay.querySelector('h2,h3,h4,[id$="Title"],[id$="title"]');
    if (heading) {
      if (!heading.id) heading.id = modalId + '_label';
      overlay.setAttribute('aria-labelledby', heading.id);
    }

    requestAnimationFrame(() => {
      const focusable = getFocusable(overlay);
      if (focusable.length) focusable[0].focus();

      const trap = e => {
        if (e.key !== 'Tab') return;
        const els = getFocusable(overlay);
        if (!els.length) return;
        if (e.shiftKey) {
          if (document.activeElement === els[0]) { e.preventDefault(); els[els.length - 1].focus(); }
        } else {
          if (document.activeElement === els[els.length - 1]) { e.preventDefault(); els[0].focus(); }
        }
      };
      document.addEventListener('keydown', trap);
      trapHandlers.set(modalId, trap);
    });
  }

  function close(modalId) {
    const overlay = document.getElementById(modalId);
    if (!overlay) return;
    overlay.classList.remove('active');
    const trap = trapHandlers.get(modalId);
    if (trap) { document.removeEventListener('keydown', trap); trapHandlers.delete(modalId); }
    overlay._triggerEl?.focus?.();
  }

  function getFocusable(root) {
    return [...root.querySelectorAll(
      'button:not([disabled]),input:not([disabled]),select:not([disabled]),textarea:not([disabled]),[tabindex]:not([tabindex="-1"])'
    )];
  }

  // Close on backdrop click
  document.addEventListener('click', e => {
    if (e.target.classList.contains('modal-overlay') && e.target.classList.contains('active')) {
      close(e.target.id);
    }
  });

  // Close on ESC
  document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    const active = document.querySelector('.modal-overlay.active');
    if (active) close(active.id);
  });

  CCS.Modal = { open, close };
})();
