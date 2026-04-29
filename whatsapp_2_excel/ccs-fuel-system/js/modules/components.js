/**
 * js/modules/components.js
 * Reusable UI builders shared across page modules:
 * skeletons, empty states, KPI cards, confirm dialogs.
 */

'use strict';

(function () {

  // ── Skeleton screens ────────────────────────────────────────────────────
  const SKELETONS = {
    dashboard: () => `<div>
      <div class="skeleton skeleton-card" style="height:160px;margin-bottom:1.5rem;border-radius:var(--radius-2xl);"></div>
      <div class="dashboard-kpi-grid">${Array(4).fill('<div class="skeleton skeleton-card" style="height:110px;"></div>').join('')}</div>
      <div class="grid grid-cols-2 gap-4">${Array(2).fill('<div class="skeleton skeleton-card tall"></div>').join('')}</div>
    </div>`,

    orders: () => `<div>
      <div class="skeleton skeleton-card" style="height:48px;margin-bottom:1.5rem;border-radius:var(--radius-xl);"></div>
      ${Array(4).fill('<div class="skeleton skeleton-card short mb-3"></div>').join('')}
    </div>`,

    daily: () => `<div>
      <div class="skeleton skeleton-card short mb-4"></div>
      ${Array(6).fill('<div class="skeleton skeleton-card short mb-2"></div>').join('')}
    </div>`,

    leaderboard: () => `<div>
      <div class="skeleton-kpi-grid grid-cols-3">${Array(3).fill('<div class="skeleton skeleton-card" style="height:110px;"></div>').join('')}</div>
      ${Array(5).fill('<div class="skeleton skeleton-card short mb-2"></div>').join('')}
    </div>`,

    technicians: () => `<div>
      <div class="skeleton skeleton-card" style="height:48px;margin-bottom:1.5rem;border-radius:var(--radius-xl);"></div>
      <div class="dashboard-kpi-grid">${Array(4).fill('<div class="skeleton skeleton-card" style="height:88px;"></div>').join('')}</div>
      ${Array(8).fill('<div class="skeleton skeleton-card" style="height:44px;margin-bottom:0.5rem;border-radius:var(--radius-md);"></div>').join('')}
    </div>`,

    generic: () => '<div class="skeleton skeleton-card tall"></div>',
  };

  function skeleton(page) {
    return (SKELETONS[page] || SKELETONS.generic)();
  }

  // ── Empty states ────────────────────────────────────────────────────────
  const ILLUSTRATIONS = {
    orders: `<svg viewBox="0 0 120 120" fill="none"><rect x="20" y="15" width="80" height="90" rx="8" fill="var(--neutral-200)"/><rect x="32" y="35" width="56" height="6" rx="3" fill="var(--neutral-300)"/><rect x="32" y="50" width="40" height="6" rx="3" fill="var(--neutral-300)"/><rect x="32" y="65" width="48" height="6" rx="3" fill="var(--neutral-300)"/><circle cx="85" cy="80" r="18" fill="var(--accent-100)"/><path d="M78 80h14M85 73v14" stroke="var(--accent-600)" stroke-width="2.5"/></svg>`,
    daily:  `<svg viewBox="0 0 120 120" fill="none"><rect x="15" y="25" width="90" height="80" rx="8" fill="var(--neutral-200)"/><rect x="15" y="35" width="90" height="12" fill="var(--accent-100)"/><circle cx="38" cy="18" r="7" fill="var(--neutral-300)"/><circle cx="82" cy="18" r="7" fill="var(--neutral-300)"/><rect x="27" y="57" width="16" height="14" rx="3" fill="var(--neutral-300)"/><rect x="52" y="57" width="16" height="14" rx="3" fill="var(--accent-200)"/><rect x="77" y="57" width="16" height="14" rx="3" fill="var(--neutral-300)"/></svg>`,
    leaderboard: `<svg viewBox="0 0 120 120" fill="none"><rect x="20" y="55" width="22" height="50" rx="4" fill="var(--neutral-300)"/><rect x="49" y="30" width="22" height="75" rx="4" fill="var(--accent-200)"/><rect x="78" y="70" width="22" height="35" rx="4" fill="var(--neutral-300)"/><path d="M58 20l2.5 5 5.5.8-4 3.9.9 5.5L58 33l-4.9 2.6.9-5.5-4-3.9 5.5-.8z" fill="#FFD700"/></svg>`,
    tech:   `<svg viewBox="0 0 120 120" fill="none"><circle cx="60" cy="42" r="22" fill="var(--neutral-200)"/><path d="M20 95c0-22 18-36 40-36s40 14 40 36" stroke="var(--neutral-300)" stroke-width="8" stroke-linecap="round" fill="none"/></svg>`,
  };

  const EMPTY_META = {
    orders:      { title: 'No orders yet',             desc: 'Create your first order to start tracking fuel allocation' },
    daily:       { title: 'No entries for this date',  desc: 'Add entries above to start tracking fuel supply' },
    leaderboard: { title: 'No data available',         desc: 'Add allocated supply entries to see the leaderboard' },
    tech:        { title: 'No technicians',            desc: 'Add technicians to this region to get started' },
  };

  function emptyState(type, actionLabel, actionFn) {
    const ill  = ILLUSTRATIONS[type] || ILLUSTRATIONS.daily;
    const meta = EMPTY_META[type]    || EMPTY_META.daily;
    return `
      <div class="empty-state">
        <div class="empty-illustration" style="max-width:120px;margin:0 auto;">${ill}</div>
        <h3 class="text-lg font-semibold mt-4">${meta.title}</h3>
        <p class="text-sm mt-2 mb-4" style="color:var(--neutral-500);">${meta.desc}</p>
        ${actionLabel ? `<button class="btn btn-primary" onclick="${actionFn}"><i class="fa-regular fa-plus"></i> ${actionLabel}</button>` : ''}
      </div>`;
  }

  // ── KPI card builder ────────────────────────────────────────────────────
  function kpiCard({ icon, iconBg, iconColor, value, label, trend, trendDir, targetPct, id }) {
    return `
      <div class="kpi-card">
        <div class="kpi-icon" style="background:${iconBg};color:${iconColor};">
          <i class="fa-regular ${icon}"></i>
        </div>
        <div class="kpi-value" ${id ? `id="${id}"` : ''}>${value}</div>
        <div class="kpi-label">${label}</div>
        ${trend ? `<div class="kpi-trend trend-${trendDir || 'up'}">
          <i class="fa-regular fa-arrow-${trendDir === 'down' ? 'down' : 'up'}"></i> ${trend}
        </div>` : ''}
        ${targetPct != null ? `
          <div class="target-bar-wrap">
            <div class="target-bar-label">
              <span>Target progress</span><span>${targetPct.toFixed(1)}%</span>
            </div>
            <div class="target-bar">
              <div class="target-bar-fill" style="width:${Math.min(targetPct, 100)}%;"></div>
            </div>
          </div>` : ''}
      </div>`;
  }

  // ── Confirm dialog (returns Promise<boolean>) ────────────────────────────
  function confirm(message, opts = {}) {
    return new Promise(resolve => {
      const id = CCS.utils.uid('confirm');
      const html = `
        <div class="modal-overlay active" id="${id}">
          <div class="modal-container" style="max-width:400px;">
            <div class="modal-header">
              <h3 class="text-xl font-semibold">${opts.title || 'Confirm'}</h3>
            </div>
            <div class="modal-body">
              <p style="color:var(--neutral-700);">${message}</p>
              ${opts.input ? `<div class="input-group mt-4">
                <input type="text" class="input-field" id="${id}_input" placeholder=" ">
                <label class="input-label">${opts.inputLabel || 'Type to confirm'}</label>
              </div>` : ''}
            </div>
            <div class="modal-footer">
              <button class="btn btn-secondary" id="${id}_cancel">Cancel</button>
              <button class="btn ${opts.danger ? 'btn-danger' : 'btn-primary'}" id="${id}_ok">${opts.okLabel || 'Confirm'}</button>
            </div>
          </div>
        </div>`;
      document.getElementById('modals-root').insertAdjacentHTML('beforeend', html);

      const overlay = document.getElementById(id);
      const ok      = document.getElementById(id + '_ok');
      const cancel  = document.getElementById(id + '_cancel');

      const done = (result) => { overlay.remove(); resolve(result); };

      ok.addEventListener('click', () => {
        if (opts.input) {
          const val = document.getElementById(id + '_input')?.value.trim();
          done(val);
        } else {
          done(true);
        }
      });
      cancel.addEventListener('click', () => done(false));
    });
  }

  // ── Progress bar HTML ────────────────────────────────────────────────────
  function progressBar(pct, opts = {}) {
    const cls = pct >= 100 ? 'danger' : pct >= 85 ? 'warning' : 'success';
    return `
      <div>
        <div class="progress-bar">
          <div class="progress-fill ${cls}" style="width:${Math.min(pct, 100)}%;"></div>
        </div>
        ${opts.label !== false ? `<div style="font-size:var(--text-xs);color:var(--neutral-500);margin-top:3px;text-align:right;">${pct.toFixed(1)}%</div>` : ''}
      </div>`;
  }

  CCS.Components = { skeleton, emptyState, kpiCard, confirm, progressBar };
})();
