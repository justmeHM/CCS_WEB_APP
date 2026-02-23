/**
 * nav.js — Navigation & Page Routing
 * Controls which section is visible and keeps nav buttons in sync.
 */

import { renderOrders } from './orders.js';
import { renderUnallocReport, renderBackupStatus } from './reports.js';
import { populateLbRegionFilter, renderLeaderboard } from './leaderboard.js';
import { renderRegionList } from './regions.js';

/** Switch to a named page and trigger any page-specific rendering */
export function setPage(pageName, clickedBtn) {
  // Hide all sections, show target
  document.querySelectorAll('section').forEach(s => s.classList.remove('active'));
  document.getElementById('page-' + pageName).classList.add('active');

  // Update page title in topbar
  document.getElementById('pageTitle').textContent = pageName.toUpperCase();

  // Sync bottom-nav buttons
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  const mobBtn = document.getElementById('nav-' + pageName);
  if (mobBtn) mobBtn.classList.add('active');

  // Sync sidebar buttons (desktop)
  document.querySelectorAll('.snav-btn').forEach(b => b.classList.remove('active'));
  if (clickedBtn && clickedBtn.classList.contains('snav-btn')) {
    clickedBtn.classList.add('active');
  }

  // Page-specific initialisation
  if (pageName === 'orders')      renderOrders();
  if (pageName === 'export')      { renderUnallocReport(); renderBackupStatus(); }
  if (pageName === 'leaderboard') { populateLbRegionFilter(); renderLeaderboard(); }
  if (pageName === 'regions')     renderRegionList();
}

/** Wire up Escape key to close all modals */
export function initEscapeKey() {
  document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    ['editModal', 'overageModal', 'summaryModal', 'techHistModal', 'renameModal', 'cloneModal']
      .forEach(id => document.getElementById(id)?.classList.add('hidden'));
  });
}