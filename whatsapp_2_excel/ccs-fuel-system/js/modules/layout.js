/**
 * js/modules/layout.js
 * Renders persistent chrome: sidebar, topbar, autosave indicator.
 * Called once on app init.
 */

'use strict';

(function () {
  // ── Autosave indicator ────────────────────────────────────────────────────
  let _autosaveTimer = null;

  function save() {
    CCS.DB.save();
    _flashSaved();
  }

  function markUnsaved() {
    const el = document.getElementById('autosaveIndicator');
    const txt = document.getElementById('autosaveText');
    if (!el) return;
    clearTimeout(_autosaveTimer);
    el.classList.add('unsaved', 'visible');
    if (txt) txt.textContent = 'Unsaved changes';
    _setFooterAutosave('saving');
  }

  function _flashSaved() {
    const el = document.getElementById('autosaveIndicator');
    const txt = document.getElementById('autosaveText');
    if (!el) return;
    el.classList.remove('unsaved');
    el.classList.add('visible');
    if (txt) txt.textContent = 'Saved';
    clearTimeout(_autosaveTimer);
    _autosaveTimer = setTimeout(() => el.classList.remove('visible'), 2500);
    _setFooterAutosave('saved');
  }

  function _setFooterAutosave(state) {
    const el = document.getElementById('footerAutosave');
    if (!el) return;
    el.textContent = state === 'saved' ? 'Autosave Active' : 'Saving…';
  }

  // ── Clock ─────────────────────────────────────────────────────────────────
  function startClock() {
    function tick() {
      const el = document.getElementById('footerSystemTime');
      if (el) el.textContent = new Date().toLocaleTimeString('en-GB');
    }
    tick();
    setInterval(tick, 1000);
  }

  // ── Region footer ─────────────────────────────────────────────────────────
  function updateFooterRegion() {
    const el = document.getElementById('footerActiveRegion');
    if (el) el.textContent = 'Region: ' + CCS.DB.currentRegion;
  }

  // ── Sidebar HTML ──────────────────────────────────────────────────────────
  const NAV_ITEMS = [
    { section: 'Main' },
    { id: 'dashboard',   label: 'Dashboard',         icon: 'fa-chart-line'    },
    { id: 'orders',      label: 'Orders',             icon: 'fa-file-lines'   },
    { id: 'daily',       label: 'Daily Entry',        icon: 'fa-calendar-day' },
    { id: 'technicians', label: 'Technicians',        icon: 'fa-users'        },
    { id: 'leaderboard', label: 'Leaderboard',        icon: 'fa-trophy'       },
    { section: 'Reports & Tools' },
    { id: 'reports',     label: 'Reports',            icon: 'fa-chart-bar'    },
    { id: 'automation',  label: 'Automation',         icon: 'fa-robot'        },
    { id: 'cycles',      label: 'Cycle Management',   icon: 'fa-rotate'       },
    { section: 'Configuration' },
    { id: 'regions',     label: 'Regions',            icon: 'fa-map'          },
    { id: 'settings',    label: 'Settings',           icon: 'fa-gear'         },
    { id: 'admin',       label: 'Admin',              icon: 'fa-shield-halved', adminOnly: true },
  ];

  function renderSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (!sidebar) return;

    const navHTML = NAV_ITEMS.map(item => {
      if (item.section) {
        return `<div class="sidebar-section-label">${item.section}</div>`;
      }
      return `
        <button class="sidebar-btn" data-page="${item.id}"
          onclick="CCS.Router.go('${item.id}')"
          title="${item.label}"
          ${item.adminOnly ? 'id="sidebarAdminBtn" style="display:none"' : ''}>
          <i class="fa-regular ${item.icon}"></i>
          <span>${item.label}</span>
        </button>`;
    }).join('');

    sidebar.innerHTML = `
      <div class="sidebar-logo">
        <div class="sidebar-logo-mark">C</div>
        <div class="sidebar-logo-text">CCS Fuel System</div>
      </div>
      <nav class="sidebar-nav">${navHTML}</nav>
      <div class="sidebar-footer">
        <button class="sidebar-btn" onclick="CCS.Layout.toggleSidebar()" title="Collapse sidebar">
          <i class="fa-regular fa-sidebar"></i>
          <span>Collapse</span>
        </button>
        <button class="sidebar-btn" id="darkModeBtn" onclick="CCS.Layout.toggleDarkMode()" title="Toggle dark mode">
          <i class="fa-regular fa-moon"></i>
          <span>Dark Mode</span>
        </button>
      </div>`;
  }

  // ── Topbar HTML ───────────────────────────────────────────────────────────
  function renderTopbar() {
    const topbar = document.getElementById('topbar');
    if (!topbar) return;

    topbar.innerHTML = `
      <button class="btn btn-icon btn-ghost" onclick="CCS.Layout.toggleMobileSidebar()" title="Menu" style="display:none" id="mobileMenuBtn">
        <i class="fa-regular fa-bars"></i>
      </button>
      <span class="topbar-title" id="topbarTitle">Dashboard</span>
      <div class="topbar-actions">
        <div class="autosave-indicator" id="autosaveIndicator">
          <div class="autosave-dot" style="animation:autosavePulse 1.5s infinite;"></div>
          <span id="autosaveText">Saved</span>
        </div>

        <!-- Region selector -->
        <div class="region-selector" onclick="CCS.Router.go('regions')" title="Switch region">
          <i class="fa-regular fa-map-pin" style="color:var(--accent-600);"></i>
          <span id="topbarRegion">${CCS.DB.currentRegion}</span>
          <i class="fa-regular fa-chevron-down" style="font-size:0.7rem;color:var(--neutral-400);"></i>
        </div>

        <!-- Notifications -->
        <div class="notif-bell" onclick="CCS.Notifications.toggle()">
          <i class="fa-regular fa-bell" style="font-size:1.1rem;color:var(--neutral-600);"></i>
          <div class="notif-badge" id="notifBadge" style="display:none;">0</div>
          <div class="notif-dropdown" id="notifDropdown">
            <div style="padding:var(--space-3) var(--space-4);border-bottom:1px solid var(--neutral-200);display:flex;align-items:center;justify-content:space-between;">
              <span style="font-weight:600;font-size:var(--text-sm);">Notifications</span>
              <button class="btn btn-ghost btn-sm" onclick="CCS.Notifications.clear();event.stopPropagation()">Clear all</button>
            </div>
            <div id="notifList" style="max-height:320px;overflow-y:auto;"></div>
          </div>
        </div>

        <!-- Keyboard shortcuts -->
        <button class="btn btn-icon btn-ghost" onclick="CCS.Modal.open('shortcutsModal')" title="Keyboard shortcuts (/)">
          <i class="fa-regular fa-keyboard"></i>
        </button>

        <!-- Command palette -->
        <button class="btn btn-icon btn-ghost" onclick="CCS.CommandPalette.open()" title="Command palette (Ctrl+K)">
          <i class="fa-regular fa-magnifying-glass"></i>
        </button>

        <!-- User pill -->
        <div style="position:relative;">
          <div class="auth-user-pill" id="authUserPill" onclick="CCS.Auth.toggleDropdown()">
            <div class="auth-user-avatar-sm" id="authUserAvatarSm">?</div>
            <span style="font-size:var(--text-xs);font-weight:500;" id="authUserPillName">User</span>
            <i class="fa-regular fa-chevron-down" style="font-size:0.65rem;color:var(--neutral-400);"></i>
          </div>
          <div class="auth-user-dropdown" id="authUserDropdown">
            <div style="padding:var(--space-4);border-bottom:1px solid var(--neutral-200);">
              <div style="font-weight:600;font-size:var(--text-sm);" id="authDropdownName"></div>
              <div style="font-size:var(--text-xs);color:var(--neutral-400);" id="authDropdownEmail"></div>
            </div>
            <div id="authAdminMenuItem" style="display:none;">
              <button class="btn btn-ghost w-full" style="justify-content:flex-start;border-radius:0;padding:var(--space-3) var(--space-4);" onclick="CCS.Router.go('admin');CCS.Auth.closeDropdown()">
                <i class="fa-regular fa-shield-halved"></i> Admin Panel
              </button>
            </div>
            <button class="btn btn-ghost w-full" style="justify-content:flex-start;border-radius:0;padding:var(--space-3) var(--space-4);" onclick="CCS.Router.go('settings');CCS.Auth.closeDropdown()">
              <i class="fa-regular fa-gear"></i> Settings
            </button>
            <div style="border-top:1px solid var(--neutral-200);"></div>
            <button class="btn btn-ghost w-full" style="justify-content:flex-start;border-radius:0;padding:var(--space-3) var(--space-4);color:var(--status-danger);" onclick="CCS.Auth.doLogout()">
              <i class="fa-regular fa-arrow-right-from-bracket"></i> Sign Out
            </button>
          </div>
        </div>
      </div>`;
  }

  // ── Dark mode ─────────────────────────────────────────────────────────────
  function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('ccs_dark_mode', isDark ? '1' : '0');
    const btn = document.getElementById('darkModeBtn');
    if (btn) btn.innerHTML = isDark
      ? '<i class="fa-regular fa-sun"></i><span>Light Mode</span>'
      : '<i class="fa-regular fa-moon"></i><span>Dark Mode</span>';
  }

  function applyStoredDarkMode() {
    if (localStorage.getItem('ccs_dark_mode') === '1') {
      document.body.classList.add('dark-mode');
      const btn = document.getElementById('darkModeBtn');
      if (btn) btn.innerHTML = '<i class="fa-regular fa-sun"></i><span>Light Mode</span>';
    }
  }

  // ── Sidebar collapse ──────────────────────────────────────────────────────
  function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (!sidebar) return;
    sidebar.classList.toggle('collapsed');
    localStorage.setItem('ccs_sidebar_collapsed', sidebar.classList.contains('collapsed') ? '1' : '0');
  }

  function toggleMobileSidebar() {
    document.getElementById('sidebar')?.classList.toggle('mobile-open');
  }

  function applySidebarState() {
    if (localStorage.getItem('ccs_sidebar_collapsed') === '1') {
      document.getElementById('sidebar')?.classList.add('collapsed');
    }
    // Show mobile menu btn on small screens
    if (window.innerWidth <= 768) {
      CCS.dom.show('mobileMenuBtn', 'flex');
    }
  }

  // ── Shortcuts modal HTML ──────────────────────────────────────────────────
  function injectShortcutsModal() {
    const shortcuts = [
      ['Ctrl K',  'Open command palette'],
      ['Ctrl S',  'Save (Daily page)'],
      ['ESC',     'Close modal / clear search'],
      ['B',       'Toggle sidebar'],
      ['D',       'Go to Dashboard'],
      ['O',       'Go to Orders'],
      ['L',       'Go to Leaderboard'],
      ['/',       'Show this menu'],
    ];
    const html = `
      <div class="modal-overlay" id="shortcutsModal">
        <div class="modal-container" style="max-width:420px;">
          <div class="modal-header">
            <h3 class="text-xl font-semibold"><i class="fa-regular fa-keyboard" style="color:var(--accent-600);margin-right:8px;"></i>Keyboard Shortcuts</h3>
            <button class="btn btn-icon btn-ghost" onclick="CCS.Modal.close('shortcutsModal')"><i class="fa-regular fa-xmark"></i></button>
          </div>
          <div class="modal-body">
            <div class="shortcut-grid">
              ${shortcuts.map(([key, desc]) => `
                <div class="shortcut-item"><span class="kbd">${key}</span><span>${desc}</span></div>`).join('')}
            </div>
          </div>
        </div>
      </div>`;
    document.getElementById('modals-root').insertAdjacentHTML('beforeend', html);
  }

  // ── Global keyboard shortcuts ─────────────────────────────────────────────
  function initKeyboardShortcuts() {
    document.addEventListener('keydown', e => {
      const tag = document.activeElement?.tagName;
      const typing = ['INPUT','TEXTAREA','SELECT'].includes(tag);

      if ((e.ctrlKey || e.metaKey) && e.key === 'k') { e.preventDefault(); CCS.CommandPalette.open(); }
      if (e.key === 'Escape') CCS.CommandPalette.close();

      if (!typing) {
        if (e.key === 'b') CCS.Layout.toggleSidebar();
        if (e.key === 'd') CCS.Router.go('dashboard');
        if (e.key === 'o') CCS.Router.go('orders');
        if (e.key === 'l') CCS.Router.go('leaderboard');
        if (e.key === '/') { e.preventDefault(); CCS.Modal.open('shortcutsModal'); }
      }
    });
  }

  // ── Init ──────────────────────────────────────────────────────────────────
  function init() {
    renderSidebar();
    renderTopbar();
    injectShortcutsModal();
    applyStoredDarkMode();
    applySidebarState();
    startClock();
    initKeyboardShortcuts();
    updateFooterRegion();
  }

  CCS.Layout = {
    init,
    save,
    markUnsaved,
    updateFooterRegion,
    toggleDarkMode,
    toggleSidebar,
    toggleMobileSidebar,
  };
})();
