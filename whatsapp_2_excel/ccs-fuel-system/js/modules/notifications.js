/**
 * js/modules/notifications.js
 * Builds and renders the notification panel.
 * Scans DB for: unassigned orders, nearly-full orders,
 * overages, and inactive technicians.
 */

'use strict';

(function () {
  let _data = [];

  function build() {
    _data = [];
    const threeDaysAgo = new Date(Date.now() - 3 * 86400000).toISOString().slice(0, 10);

    Object.entries(CCS.DB.data.regions).forEach(([rName, r]) => {
      // Unassigned orders missing a comment
      Object.keys(r.orders).forEach(orderNo => {
        const order = r.orders[orderNo];
        if (!Object.keys(order.allocations || {}).length) {
          if (!r.unassignedComments?.[orderNo]) {
            _data.push({
              type: 'info', icon: '📝', bg: 'var(--status-info-bg)',
              title: 'Unassigned Order Needs Comment',
              desc: `${orderNo} · ${rName}`,
              action: () => CCS.Router.go('orders'),
            });
          }
        }
      });

      // Nearly-full and overage orders
      Object.values(r.orders).forEach(o => {
        const pct = o.totalLiters > 0 ? (o.suppliedTotal / o.totalLiters) * 100 : 0;
        if (pct >= 90 && pct < 100) {
          _data.push({
            type: 'warn', icon: '⚠️', bg: 'var(--status-warning-bg)',
            title: `Order ${o.orderNo} nearly full`,
            desc: `${pct.toFixed(0)}% used · ${(o.totalLiters - o.suppliedTotal).toFixed(1)}L remaining · ${rName}`,
            action: () => CCS.Router.go('orders'),
          });
        }

        Object.entries(o.allocations || {}).forEach(([tech, alloc]) => {
          const supplied = Object.values(r.dailyLog).flat()
            .filter(e => e.orderNo === o.orderNo && e.technician === tech)
            .reduce((s, e) => s + e.supplied, 0);
          if (supplied > alloc) {
            _data.push({
              type: 'error', icon: '🔴', bg: 'var(--status-danger-bg)',
              title: `Overage: ${tech} on ${o.orderNo}`,
              desc: `${(supplied - alloc).toFixed(1)}L over allocation · ${rName}`,
              action: () => CCS.Router.go('orders'),
            });
          }
        });
      });

      // Inactive technicians (3+ days)
      r.technicians.forEach(t => {
        const hasActivity = Object.values(r.dailyLog).flat().some(e => e.technician === t);
        if (!hasActivity) return;
        const recentActivity = Object.entries(r.dailyLog)
          .filter(([date]) => date >= threeDaysAgo)
          .some(([, entries]) => entries.some(e => e.technician === t));
        if (!recentActivity) {
          _data.push({
            type: 'info', icon: '👤', bg: 'var(--status-info-bg)',
            title: `${t} inactive 3+ days`,
            desc: `No supply entries recently · ${rName}`,
            action: null,
          });
        }
      });
    });

    return _data;
  }

  function render() {
    build();
    const badge = document.getElementById('notifBadge');
    const list  = document.getElementById('notifList');
    if (!badge || !list) return;

    if (!_data.length) {
      badge.style.display = 'none';
      list.innerHTML = '<div class="p-6 text-center" style="color:var(--neutral-400);"><i class="fa-regular fa-bell-slash" style="font-size:1.5rem;display:block;margin-bottom:.5rem;"></i>No notifications</div>';
      return;
    }

    badge.style.display = 'flex';
    badge.textContent = _data.length;
    list.innerHTML = _data.map((n, i) => `
      <div class="notif-item" onclick="_notifClick(${i})">
        <div class="notif-icon" style="background:${n.bg};">${n.icon}</div>
        <div class="notif-text">
          <div class="notif-title">${n.title}</div>
          <div class="notif-desc">${n.desc}</div>
        </div>
      </div>`).join('');
  }

  // Global click handler referenced inline above
  window._notifClick = i => {
    _data[i]?.action?.();
    close();
  };

  function toggle() {
    const dd = document.getElementById('notifDropdown');
    if (!dd) return;
    dd.classList.toggle('open');
    if (dd.classList.contains('open')) render();
  }

  function close() {
    document.getElementById('notifDropdown')?.classList.remove('open');
  }

  function clear() {
    _data = [];
    const badge = document.getElementById('notifBadge');
    const list  = document.getElementById('notifList');
    if (badge) badge.style.display = 'none';
    if (list)  list.innerHTML = '<div class="p-6 text-center" style="color:var(--neutral-400);">No notifications</div>';
    close();
  }

  CCS.Notifications = { build, render, refresh: render, toggle, close, clear };
})();
