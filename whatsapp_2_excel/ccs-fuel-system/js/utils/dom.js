/**
 * js/utils/dom.js
 * Lightweight DOM helpers to reduce boilerplate.
 * Depends on: helpers.js (CCS namespace must exist)
 */

'use strict';

CCS.dom = {
  /** querySelector shorthand */
  qs(selector, root = document) { return root.querySelector(selector); },

  /** querySelectorAll → Array */
  qsa(selector, root = document) { return [...root.querySelectorAll(selector)]; },

  /** getElementById shorthand */
  id(id) { return document.getElementById(id); },

  /** Create an element with optional props & children */
  el(tag, props = {}, ...children) {
    const elem = document.createElement(tag);
    Object.entries(props).forEach(([k, v]) => {
      if (k === 'class')       elem.className = v;
      else if (k === 'style')  Object.assign(elem.style, v);
      else if (k.startsWith('on')) elem.addEventListener(k.slice(2).toLowerCase(), v);
      else                     elem.setAttribute(k, v);
    });
    children.forEach(child => {
      if (typeof child === 'string') elem.appendChild(document.createTextNode(child));
      else if (child) elem.appendChild(child);
    });
    return elem;
  },

  /** Set innerHTML safely (no script injection) */
  html(elem, markup) {
    if (typeof elem === 'string') elem = document.getElementById(elem);
    if (elem) elem.innerHTML = markup;
  },

  /** Show / hide with display property */
  show(elem, display = '') {
    if (typeof elem === 'string') elem = document.getElementById(elem);
    if (elem) elem.style.display = display;
  },
  hide(elem) {
    if (typeof elem === 'string') elem = document.getElementById(elem);
    if (elem) elem.style.display = 'none';
  },

  /** Toggle a class */
  toggle(elem, cls, force) {
    if (typeof elem === 'string') elem = document.getElementById(elem);
    if (elem) elem.classList.toggle(cls, force);
  },

  /** Animated counter (spring easing) */
  animateCounter(el, target, suffix = '', duration = 800) {
    if (!el) return;
    const start = parseFloat(el.textContent.replace(/[^0-9.-]/g, '')) || 0;
    const startTime = performance.now();
    if (el._animFrame) cancelAnimationFrame(el._animFrame);

    const easeOutCubic = t => 1 - Math.pow(1 - t, 3);
    const easeOutElastic = t => Math.sin(-13 * (t + 1) * Math.PI / 2) * Math.pow(2, -10 * t) + 1;

    const tick = now => {
      const progress = Math.min((now - startTime) / duration, 1);
      const eased = progress < 0.8
        ? easeOutCubic(progress / 0.8) * 0.8
        : 0.8 + easeOutElastic((progress - 0.8) / 0.2) * 0.2;
      const current = start + (target - start) * eased;
      el.textContent = (Number.isInteger(target) ? Math.round(current).toLocaleString() : current.toFixed(1)) + suffix;
      if (progress < 1) { el._animFrame = requestAnimationFrame(tick); }
      else { el.textContent = (Number.isInteger(target) ? target.toLocaleString() : target.toFixed(1)) + suffix; }
    };

    el._animFrame = requestAnimationFrame(tick);
  },

  /** Render a tech avatar HTML string */
  techAvatar(name, extra = '') {
    const c = CCS.utils.colorIndex(name);
    return `<div class="tech-avatar" data-color="${c}" ${extra}>${name.charAt(0).toUpperCase()}</div>`;
  },
};
