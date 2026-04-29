/**
 * js/utils/formatters.js
 * Pure formatting helpers for dates, numbers, and strings.
 */

'use strict';

CCS.fmt = {
  /** Format litres with L suffix */
  litres(n, decimals = 1) {
    if (n == null || isNaN(n)) return '—';
    return Number.isInteger(n) ? `${n.toLocaleString()}L` : `${parseFloat(n).toFixed(decimals)}L`;
  },

  /** Format a date string (YYYY-MM-DD) to a readable label */
  date(isoDate, opts = {}) {
    if (!isoDate) return '—';
    return new Date(isoDate + 'T00:00:00').toLocaleDateString('en-GB', {
      day: '2-digit', month: 'short', year: 'numeric', ...opts,
    });
  },

  /** Format a percentage */
  pct(value, total) {
    if (!total) return '0%';
    return `${Math.min(100, (value / total) * 100).toFixed(1)}%`;
  },

  /** Convert bytes to human-readable size */
  bytes(b) {
    if (b < 1024) return `${b} B`;
    if (b < 1048576) return `${(b / 1024).toFixed(1)} KB`;
    return `${(b / 1048576).toFixed(1)} MB`;
  },

  /** Truncate a string to maxLen characters */
  truncate(str, maxLen = 40) {
    if (!str) return '';
    return str.length > maxLen ? str.slice(0, maxLen) + '…' : str;
  },

  /** Capitalise first letter */
  capitalise(str = '') {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
  },

  /** Format a number with thousand separators */
  number(n, decimals = 0) {
    if (n == null || isNaN(n)) return '—';
    return parseFloat(n).toLocaleString(undefined, {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals,
    });
  },
};
