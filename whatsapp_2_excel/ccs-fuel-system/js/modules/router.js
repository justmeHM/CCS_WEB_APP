/**
 * js/modules/router.js
 * Lightweight SPA router.
 *
 * Each page is a module in js/pages/*.js that exports a
 * `render(container)` function attached to CCS.Pages.
 *
 * Usage:
 *   CCS.Router.go('dashboard')    // navigate with transition
 *   CCS.Router.current            // read current page id
 */

'use strict';

(function () {
  let _current = null;

  // Map page id → { label, icon, module key on CCS.Pages }
  const PAGE_MAP = {
    dashboard:   { label: 'Dashboard',            icon: 'fa-chart-line',       module: 'Dashboard'   },
    orders:      { label: 'Orders',               icon: 'fa-file-lines',       module: 'Orders'      },
    daily:       { label: 'Daily Entry',          icon: 'fa-calendar-day',     module: 'Daily'       },
    technicians: { label: 'Technicians',          icon: 'fa-users',            module: 'Technicians' },
    leaderboard: { label: 'Leaderboard',          icon: 'fa-trophy',           module: 'Leaderboard' },
    reports:     { label: 'Reports',              icon: 'fa-chart-bar',        module: 'Reports'     },
    automation:  { label: 'Automation',           icon: 'fa-robot',            module: 'Automation'  },
    cycles:      { label: 'Cycle Management',     icon: 'fa-rotate',           module: 'Cycles'      },
    regions:     { label: 'Region Management',    icon: 'fa-map',              module: 'Regions'     },
    admin:       { label: 'Admin',                icon: 'fa-shield-halved',    module: 'Admin'       },
    settings:    { label: 'Settings',             icon: 'fa-gear',             module: 'Settings'    },
  };

  function getContainer() { return document.getElementById('pageContent'); }

  function updateSidebar(pageId) {
    document.querySelectorAll('.sidebar-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.page === pageId);
    });
  }

  function updateBreadcrumb(pageId) {
    const meta = PAGE_MAP[pageId];
    if (!meta) return;
    const bar = document.getElementById('breadcrumbBar');
    if (!bar) return;
    bar.innerHTML = `
      <i class="fa-regular fa-house" style="color:var(--neutral-400);"></i>
      <i class="fa-regular fa-chevron-right" style="font-size:0.6rem;color:var(--neutral-300);"></i>
      <span style="color:var(--accent-600);font-weight:500;">${meta.label}</span>
      <span style="margin-left:auto;font-size:0.7rem;color:var(--neutral-400);">
        <i class="fa-regular fa-map-pin"></i> ${CCS.DB.currentRegion}
      </span>`;
  }

  function updateTopbar(pageId) {
    const meta = PAGE_MAP[pageId];
    if (!meta) return;
    const el = document.getElementById('topbarTitle');
    if (el) el.textContent = meta.label;
  }

  async function go(pageId, options = {}) {
    const meta = PAGE_MAP[pageId];
    if (!meta) { console.warn(`[Router] Unknown page: ${pageId}`); return; }

    const pageModule = CCS.Pages?.[meta.module];
    if (!pageModule?.render) { console.warn(`[Router] Page module not loaded: ${meta.module}`); return; }

    const container = getContainer();
    if (!container) return;

    // Exit animation on old content
    if (_current && !options.skipTransition) {
      container.classList.add('page-exiting');
      await new Promise(r => setTimeout(r, 180));
      container.classList.remove('page-exiting');
    }

    _current = pageId;
    container.innerHTML = pageModule.skeleton?.() || '';
    container.classList.add('page-entering');

    // Let skeletons paint before heavy render
    await new Promise(r => requestAnimationFrame(r));

    try {
      await pageModule.render(container);
    } catch (e) {
      console.error(`[Router] Error rendering ${pageId}:`, e);
      container.innerHTML = `<div class="card" style="text-align:center;padding:3rem;color:var(--status-danger);">
        <i class="fa-regular fa-circle-xmark" style="font-size:2rem;margin-bottom:1rem;display:block;"></i>
        <h3>Page failed to load</h3>
        <p style="color:var(--neutral-500);margin-top:.5rem;font-size:.85rem;">${e.message}</p>
      </div>`;
    }

    container.classList.remove('page-entering');
    updateSidebar(pageId);
    updateBreadcrumb(pageId);
    updateTopbar(pageId);
    CCS.Notifications?.refresh();
  }

  CCS.Router = {
    go,
    get current() { return _current; },
    get pages()   { return PAGE_MAP; },
  };
})();
