/**
 * app.js — Application Entry Point
 * Imports all modules and exposes a single global `App` object
 * that inline HTML event handlers (onclick="App.X()") can call.
 * This avoids polluting the global scope with individual functions.
 */

import { populateRegions, changeRegion, addRegion, deleteRegion, renderRegionList,
         addTechnician, deleteTech, renderTechList,
         openRenameRegion, openRenameTech, closeRenameModal, confirmRename } from './modules/regions.js';

import { createOrder, allocateFuel, clearOrderFilter, renderOrders,
         toggleOrderCard, toggleEditOrderDate, cancelOrderDateEdit, saveOrderDate, deleteOrder,
         toggleAllocEdit, cancelAllocEdit, saveAllocEdit,
         openOverageComment, closeOverageModal, saveOverageComment,
         openCloneModal, closeCloneModal, confirmClone,
         populateAllocOrder, populateAllocTech } from './modules/orders.js';

import { toggleAccordion, loadDailyLog, renderDailyHistory,
         addDailyEntry, techSelected, orderDropdownChanged,
         saveDaily, openEditModal, closeEditModal, saveEditEntry,
         deleteDailyEntry, openDailySummary, loadSummaryForDateRange, closeSummaryModal } from './modules/daily.js';

import { renderLeaderboard, populateLbRegionFilter, openTechHistory, closeTechHistModal } from './modules/leaderboard.js';

import { exportOrders, backupData, restoreData, renderBackupStatus, renderUnallocReport } from './modules/reports.js';

import { setPage, initEscapeKey } from './modules/nav.js';

/* ── Expose all functions via a single App namespace ─────────── */
window.App = {
  // Navigation
  setPage,

  // Regions & technicians
  populateRegions, changeRegion, addRegion, deleteRegion, renderRegionList,
  addTechnician, deleteTech, renderTechList,
  openRenameRegion, openRenameTech, closeRenameModal, confirmRename,

  // Orders
  createOrder, allocateFuel, clearOrderFilter, renderOrders,
  toggleOrderCard, toggleEditOrderDate, cancelOrderDateEdit, saveOrderDate, deleteOrder,
  toggleAllocEdit, cancelAllocEdit, saveAllocEdit,
  openOverageComment, closeOverageModal, saveOverageComment,
  openCloneModal, closeCloneModal, confirmClone,

  // Daily log
  toggleAccordion, loadDailyLog, renderDailyHistory,
  addDailyEntry, techSelected, orderDropdownChanged,
  saveDaily, openEditModal, closeEditModal, saveEditEntry,
  deleteDailyEntry, openDailySummary, loadSummaryForDateRange, closeSummaryModal,

  // Leaderboard
  renderLeaderboard, populateLbRegionFilter, openTechHistory, closeTechHistModal,

  // Reports
  exportOrders, backupData, restoreData, renderBackupStatus, renderUnallocReport,
};

/* ── Bootstrap ────────────────────────────────────────────────── */
populateRegions();
setPage('daily', null);
document.getElementById('dailyDate').value = new Date().toISOString().slice(0, 10);
loadDailyLog();
renderDailyHistory();
renderBackupStatus();
initEscapeKey();