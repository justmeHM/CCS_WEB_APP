/**
 * js/utils/helpers.js
 * Pure utility functions – no DOM, no side effects.
 * Safe to import first; has no dependencies.
 */

'use strict';

// Global namespace – all modules attach to this object
window.CCS = window.CCS || {};

CCS.utils = {
  /**
   * Generate a hash-based color index (0-7) from a string.
   * Used for consistent technician avatar colours.
   */
  colorIndex(str) {
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = str.charCodeAt(i) + ((hash << 5) - hash);
    }
    return Math.abs(hash) % 8;
  },

  /**
   * Deep clone a value using the structured-clone API (falls back to JSON).
   */
  clone(value) {
    try { return structuredClone(value); } catch { return JSON.parse(JSON.stringify(value)); }
  },

  /**
   * Debounce a function call.
   */
  debounce(fn, ms = 300) {
    let timer;
    return (...args) => { clearTimeout(timer); timer = setTimeout(() => fn(...args), ms); };
  },

  /**
   * Generate a unique ID string.
   */
  uid(prefix = 'id') {
    return `${prefix}_${Date.now()}_${Math.random().toString(36).slice(2, 7)}`;
  },

  /**
   * Simple SHA-256 hash via Web Crypto API. Returns hex string.
   */
  async sha256(text) {
    const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
    return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
  },

  /**
   * Clamp a number between min and max.
   */
  clamp(value, min, max) { return Math.min(Math.max(value, min), max); },

  /**
   * Group an array of objects by a key.
   */
  groupBy(arr, key) {
    return arr.reduce((acc, item) => {
      const k = typeof key === 'function' ? key(item) : item[key];
      (acc[k] = acc[k] || []).push(item);
      return acc;
    }, {});
  },

  /**
   * Sort an array of objects by a key, ascending or descending.
   */
  sortBy(arr, key, dir = 'asc') {
    return [...arr].sort((a, b) => {
      const va = typeof key === 'function' ? key(a) : a[key];
      const vb = typeof key === 'function' ? key(b) : b[key];
      if (va < vb) return dir === 'asc' ? -1 : 1;
      if (va > vb) return dir === 'asc' ?  1 : -1;
      return 0;
    });
  },
};
