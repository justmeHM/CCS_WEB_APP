/**
 * js/modules/command-palette.js
 * Ctrl+K command palette — searches pages, actions, technicians.
 */

'use strict';

(function () {
  let _activeIdx = -1;
  let _items = [];

  function buildItems(query = '') {
    const q = query.toLowerCase().trim();
    const results = [];

    // Pages
    Object.entries(CCS.Router.pages).forEach(([id, meta]) => {
      if (!q || meta.label.toLowerCase().includes(q) || id.includes(q)) {
        results.push({ group: 'Pages', icon: meta.icon, label: meta.label, action: () => CCS.Router.go(id) });
      }
    });

    // Technicians
    CCS.DB.technicians().forEach(t => {
      if (!q || t.toLowerCase().includes(q)) {
        results.push({ group: 'Technicians', icon: 'fa-user', label: t, action: () => CCS.Router.go('technicians') });
      }
    });

    // Orders
    Object.keys(CCS.DB.orders()).forEach(orderNo => {
      if (!q || orderNo.toLowerCase().includes(q)) {
        results.push({ group: 'Orders', icon: 'fa-file-lines', label: `Order ${orderNo}`, action: () => CCS.Router.go('orders') });
      }
    });

    return results;
  }

  function renderItems(query) {
    _items = buildItems(query);
    _activeIdx = _items.length ? 0 : -1;

    const body = document.getElementById('cmdBody');
    if (!body) return;

    if (!_items.length) {
      body.innerHTML = '<div class="p-6 text-center text-sm" style="color:var(--neutral-400);">No results found</div>';
      return;
    }

    let html = '';
    let lastGroup = null;
    _items.forEach((item, i) => {
      if (item.group !== lastGroup) {
        html += `<div class="cmd-group-label">${item.group}</div>`;
        lastGroup = item.group;
      }
      html += `
        <div class="cmd-item${i === _activeIdx ? ' active' : ''}" data-idx="${i}" onclick="CCS.CommandPalette._pick(${i})">
          <div class="cmd-item-icon"><i class="fa-regular ${item.icon}"></i></div>
          <span>${item.label}</span>
        </div>`;
    });
    body.innerHTML = html;
  }

  function open() {
    const overlay = document.getElementById('cmdOverlay');
    if (!overlay) return;
    overlay.classList.add('active');
    const input = document.getElementById('cmdInput');
    if (input) { input.value = ''; input.focus(); }
    renderItems('');
  }

  function close() {
    document.getElementById('cmdOverlay')?.classList.remove('active');
  }

  function pick(idx) {
    const item = _items[idx];
    if (!item) return;
    item.action();
    close();
  }

  function navigate(dir) {
    if (!_items.length) return;
    _activeIdx = (_activeIdx + dir + _items.length) % _items.length;
    document.querySelectorAll('#cmdBody .cmd-item').forEach((el, i) => {
      el.classList.toggle('active', i === _activeIdx);
      if (i === _activeIdx) el.scrollIntoView({ block: 'nearest' });
    });
  }

  // Input handler
  document.addEventListener('input', e => {
    if (e.target.id === 'cmdInput') renderItems(e.target.value);
  });

  document.addEventListener('keydown', e => {
    const overlay = document.getElementById('cmdOverlay');
    if (!overlay?.classList.contains('active')) return;
    if (e.key === 'ArrowDown') { e.preventDefault(); navigate(1); }
    if (e.key === 'ArrowUp')   { e.preventDefault(); navigate(-1); }
    if (e.key === 'Enter')     { e.preventDefault(); pick(_activeIdx); }
    if (e.key === 'Escape')    close();
  });

  // Close on backdrop click
  document.addEventListener('click', e => {
    if (e.target.id === 'cmdOverlay') close();
  });

  CCS.CommandPalette = { open, close, _pick: pick };
})();
