/**
 * ui.js — Shared UI Utilities
 * Covers: order counter / summary strip updates.
 * Small helpers used across multiple modules.
 */

import { DB } from './db.js';

/** Update the order counter badge, summary strip pills, and stat tiles */
export function updateOrderCounter() {
  const orders  = Object.values(DB.regions[DB.currentRegion].orders);
  const open    = orders.filter(o => o.status === 'OPEN').length;

  const totalOrdered  = orders.reduce((s, o) => s + o.totalLiters,   0);
  const totalSupplied = orders.reduce((s, o) => s + o.suppliedTotal,  0);
  const totalBalance  = totalOrdered - totalSupplied;

  // Order counter badge (region row)
  const el = document.getElementById('orderCounter');
  if (el) el.textContent = `${orders.length} orders · ${open} open`;

  // Summary strip pills
  _setText('totalOrdered',  totalOrdered);
  _setText('totalSupplied', totalSupplied);
  _setText('totalBalance',  totalBalance);

  // Daily page stat tiles
  _setText('stOrdered',  totalOrdered  + 'L');
  _setText('stSupplied', totalSupplied + 'L');
  const stB = document.getElementById('stBalance');
  if (stB) { stB.textContent = totalBalance + 'L'; stB.style.color = totalBalance < 0 ? 'var(--red)' : '#dc2626'; }

  // Orders page stat tiles
  _setText('ordStOrdered',  totalOrdered  + 'L');
  _setText('ordStSupplied', totalSupplied + 'L');
  _setText('ordStBalance',  totalBalance  + 'L');

  // Orders count badge
  const ocb = document.getElementById('ordersCountBadge');
  if (ocb) ocb.textContent = `${orders.length} total · ${open} open`;
}

function _setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}