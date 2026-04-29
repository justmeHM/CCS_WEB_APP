/**
 * js/pages/dashboard.js
 * Dashboard page — KPI cards, hero banner, charts, recent activity.
 */

'use strict';

CCS.Pages = CCS.Pages || {};

CCS.Pages.Dashboard = {
  skeleton: () => CCS.Components.skeleton('dashboard'),

  async render(container) {
    const region = CCS.DB.region();
    const orders = Object.values(region?.orders || {});
    const log    = region?.dailyLog || {};
    const target = region?.monthlyTarget;

    // ── Compute KPIs ──────────────────────────────────────────────────────
    const totalAllocated = orders.reduce((s, o) => s + (o.totalLiters || 0), 0);
    const totalSupplied  = orders.reduce((s, o) => s + (o.suppliedTotal || 0), 0);
    const openOrders     = orders.filter(o => (o.status || 'open') === 'open').length;
    const allEntries     = Object.values(log).flat();
    const techSet        = new Set(allEntries.map(e => e.technician));
    const totalBalance   = totalAllocated - totalSupplied;
    const targetPct      = target ? (totalSupplied / target) * 100 : null;

    // Today's supply
    const today      = new Date().toISOString().slice(0, 10);
    const todayTotal = (log[today] || []).reduce((s, e) => s + (e.supplied || 0), 0);

    // Weekly trend (last 7 days)
    const weekDays = [];
    for (let i = 6; i >= 0; i--) {
      const d = new Date(Date.now() - i * 86400000).toISOString().slice(0, 10);
      weekDays.push({ date: d, total: (log[d] || []).reduce((s, e) => s + (e.supplied || 0), 0) });
    }

    // Technician performance (top 5)
    const techSupply = {};
    allEntries.forEach(e => { techSupply[e.technician] = (techSupply[e.technician] || 0) + (e.supplied || 0); });
    const topTechs = Object.entries(techSupply).sort((a, b) => b[1] - a[1]).slice(0, 5);
    const maxSupply = topTechs[0]?.[1] || 1;

    // Recent activity (last 5 entries across all dates)
    const recentEntries = Object.entries(log)
      .sort((a, b) => b[0].localeCompare(a[0]))
      .flatMap(([date, entries]) => entries.map(e => ({ ...e, date })))
      .slice(0, 5);

    container.innerHTML = `
      <!-- Hero -->
      <div class="dashboard-hero">
        <div class="hero-content">
          <div class="flex items-center gap-3 mb-4">
            <div style="background:rgba(255,255,255,0.15);border-radius:var(--radius-lg);padding:10px 14px;font-size:1.25rem;">⛽</div>
            <div>
              <h1 style="font-size:var(--text-2xl);font-weight:800;color:white;letter-spacing:-0.03em;">
                ${CCS.DB.currentRegion}
              </h1>
              <p style="color:rgba(255,255,255,0.65);font-size:var(--text-sm);">
                Cycle: ${CCS.DB.currentCycleName} · Started ${CCS.fmt.date(CCS.DB.currentCycleStartDate)}
              </p>
            </div>
          </div>
          <div style="display:flex;gap:var(--space-8);flex-wrap:wrap;">
            <div>
              <div style="font-size:var(--text-3xl);font-weight:800;color:white;" id="heroSupplied">0</div>
              <div style="color:rgba(255,255,255,0.6);font-size:var(--text-xs);text-transform:uppercase;letter-spacing:.05em;">Litres Supplied</div>
            </div>
            <div>
              <div style="font-size:var(--text-3xl);font-weight:800;color:white;" id="heroAllocated">0</div>
              <div style="color:rgba(255,255,255,0.6);font-size:var(--text-xs);text-transform:uppercase;letter-spacing:.05em;">Litres Allocated</div>
            </div>
            ${target ? `<div>
              <div style="font-size:var(--text-3xl);font-weight:800;color:white;" id="heroTarget">0%</div>
              <div style="color:rgba(255,255,255,0.6);font-size:var(--text-xs);text-transform:uppercase;letter-spacing:.05em;">Monthly Target</div>
            </div>` : ''}
          </div>
          ${target ? `<div style="margin-top:var(--space-4);">
            <div style="background:rgba(255,255,255,0.15);border-radius:var(--radius-full);height:6px;overflow:hidden;">
              <div style="height:100%;background:white;border-radius:var(--radius-full);width:${Math.min(targetPct, 100)}%;transition:width 1s var(--ease-spring);"></div>
            </div>
            <div style="display:flex;justify-content:space-between;margin-top:6px;">
              <span style="color:rgba(255,255,255,0.55);font-size:.7rem;">${CCS.fmt.litres(totalSupplied)} of ${CCS.fmt.litres(target)}</span>
              <span style="color:rgba(255,255,255,0.55);font-size:.7rem;">${CCS.fmt.pct(totalSupplied, target)} achieved</span>
            </div>
          </div>` : ''}
        </div>
      </div>

      <!-- KPI Grid -->
      <div class="dashboard-kpi-grid" style="margin-bottom:var(--space-6);">
        ${CCS.Components.kpiCard({ icon: 'fa-droplet', iconBg: '#faeaec', iconColor: 'var(--accent-600)', value: '0L', label: 'Total Allocated', id: 'kpiAllocated' })}
        ${CCS.Components.kpiCard({ icon: 'fa-truck', iconBg: '#e8f3ef', iconColor: '#2e6b4e', value: '0L', label: 'Total Supplied', id: 'kpiSupplied' })}
        ${CCS.Components.kpiCard({ icon: 'fa-file-lines', iconBg: '#f0f7fc', iconColor: 'var(--status-info)', value: openOrders, label: 'Open Orders', id: 'kpiOrders' })}
        ${CCS.Components.kpiCard({ icon: 'fa-users', iconBg: '#f0ebfc', iconColor: '#6b3a9b', value: techSet.size, label: 'Active Techs', id: 'kpiTechs' })}
        ${CCS.Components.kpiCard({ icon: 'fa-calendar-day', iconBg: '#fcf5eb', iconColor: 'var(--status-warning)', value: '0L', label: "Today's Supply", id: 'kpiToday' })}
      </div>

      <!-- Charts row -->
      <div class="grid grid-cols-2 gap-4 mb-5">
        <!-- Weekly trend chart -->
        <div class="card">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:var(--space-4);">
            <h3 class="text-lg font-semibold">7-Day Supply Trend</h3>
            <button class="btn btn-secondary btn-sm" onclick="CCS.Excel.exportDailyLog()">
              <i class="fa-regular fa-download"></i> Export
            </button>
          </div>
          <canvas id="weeklyChart" height="180"></canvas>
        </div>

        <!-- Top technicians -->
        <div class="card">
          <h3 class="text-lg font-semibold mb-4">Top Technicians</h3>
          ${topTechs.length ? topTechs.map(([name, total], i) => `
            <div class="flex items-center gap-3 mb-3">
              <span style="font-weight:700;color:var(--neutral-400);font-size:.7rem;width:20px;text-align:right;">#${i + 1}</span>
              ${CCS.dom.techAvatar(name)}
              <div style="flex:1;min-width:0;">
                <div class="text-sm font-medium" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${name}</div>
                <div style="height:4px;background:var(--neutral-200);border-radius:var(--radius-full);margin-top:4px;overflow:hidden;">
                  <div style="height:100%;background:linear-gradient(90deg,var(--accent-600),var(--accent-400));
                       border-radius:var(--radius-full);width:${(total / maxSupply) * 100}%;"></div>
                </div>
              </div>
              <span class="font-mono text-sm font-semibold">${CCS.fmt.litres(total)}</span>
            </div>`).join('') : CCS.Components.emptyState('tech')}
        </div>
      </div>

      <!-- Bottom row: recent activity + orders summary -->
      <div class="grid grid-cols-2 gap-4">
        <!-- Recent activity -->
        <div class="card">
          <h3 class="text-lg font-semibold mb-4">Recent Activity</h3>
          ${recentEntries.length ? `
            <div class="table-container">
              <table class="table">
                <thead><tr><th>Date</th><th>Technician</th><th>Order</th><th>Supplied</th></tr></thead>
                <tbody>
                  ${recentEntries.map(e => `
                    <tr>
                      <td class="text-sm">${CCS.fmt.date(e.date)}</td>
                      <td>
                        <div class="flex items-center gap-2">
                          ${CCS.dom.techAvatar(e.technician, 'style="width:24px;height:24px;font-size:.65rem;"')}
                          <span class="text-sm">${e.technician}</span>
                        </div>
                      </td>
                      <td><span class="badge badge-info">${e.orderNo}</span></td>
                      <td class="font-mono font-semibold text-sm">${CCS.fmt.litres(e.supplied)}</td>
                    </tr>`).join('')}
                </tbody>
              </table>
            </div>` : CCS.Components.emptyState('daily')}
          <div class="mt-4 text-center">
            <button class="btn btn-ghost btn-sm" onclick="CCS.Router.go('daily')">View all entries <i class="fa-regular fa-arrow-right"></i></button>
          </div>
        </div>

        <!-- Orders summary -->
        <div class="card">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold">Orders Overview</h3>
            <button class="btn btn-primary btn-sm" onclick="CCS.Router.go('orders')">
              View all <i class="fa-regular fa-arrow-right"></i>
            </button>
          </div>
          ${orders.length ? orders.slice(0, 6).map(o => {
            const pct = o.totalLiters > 0 ? ((o.suppliedTotal || 0) / o.totalLiters) * 100 : 0;
            return `
              <div class="mb-3">
                <div class="flex items-center justify-between mb-1">
                  <span class="text-sm font-medium">${o.orderNo}</span>
                  <span class="text-xs" style="color:var(--neutral-500);">${CCS.fmt.litres(o.suppliedTotal || 0)} / ${CCS.fmt.litres(o.totalLiters)}</span>
                </div>
                ${CCS.Components.progressBar(pct, { label: false })}
              </div>`;
          }).join('') : CCS.Components.emptyState('orders', 'Create Order', "CCS.Router.go('orders')")}
        </div>
      </div>`;

    // ── Animate counters ──────────────────────────────────────────────────
    requestAnimationFrame(() => {
      CCS.dom.animateCounter(document.getElementById('heroSupplied'),   totalSupplied,  'L');
      CCS.dom.animateCounter(document.getElementById('heroAllocated'),  totalAllocated, 'L');
      if (targetPct != null) CCS.dom.animateCounter(document.getElementById('heroTarget'), targetPct, '%');
      CCS.dom.animateCounter(document.getElementById('kpiAllocated'), totalAllocated, 'L');
      CCS.dom.animateCounter(document.getElementById('kpiSupplied'),  totalSupplied,  'L');
      CCS.dom.animateCounter(document.getElementById('kpiToday'),     todayTotal,     'L');
    });

    // ── Weekly chart ──────────────────────────────────────────────────────
    this._renderWeeklyChart(weekDays);
  },

  _renderWeeklyChart(weekDays) {
    const canvas = document.getElementById('weeklyChart');
    if (!canvas || !window.Chart) return;

    if (canvas._chartInst) canvas._chartInst.destroy();
    canvas._chartInst = new Chart(canvas, {
      type: 'bar',
      data: {
        labels: weekDays.map(d => new Date(d.date + 'T00:00:00').toLocaleDateString('en-GB', { weekday: 'short', day: '2-digit' })),
        datasets: [{
          label: 'Litres Supplied',
          data: weekDays.map(d => d.total),
          backgroundColor: weekDays.map(d => d.date === new Date().toISOString().slice(0, 10) ? 'rgba(196,30,58,0.9)' : 'rgba(196,30,58,0.35)'),
          borderRadius: 6,
        }],
      },
      options: {
        responsive: true,
        plugins: { legend: { display: false } },
        scales: {
          y: { ticks: { callback: v => v + 'L' }, grid: { color: 'rgba(0,0,0,0.04)' } },
          x: { grid: { display: false } },
        },
      },
    });
  },
};
