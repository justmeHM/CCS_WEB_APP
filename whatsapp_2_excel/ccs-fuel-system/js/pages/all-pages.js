/**
 * js/pages/technicians.js
 */
'use strict';
CCS.Pages = CCS.Pages || {};

CCS.Pages.Technicians = {
  skeleton: () => CCS.Components.skeleton('technicians'),
  async render(container) {
    const region = CCS.DB.region();
    const techs  = region?.technicians || [];
    const plates = region?.technicianPlates || {};
    const targets = region?.techMonthlyTargets || {};

    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-title"><h1>Technicians</h1><p>Manage field technicians for ${CCS.DB.currentRegion}</p></div>
        <button class="btn btn-primary" onclick="CCS.Pages.Technicians.openAdd()">
          <i class="fa-regular fa-user-plus"></i> Add Technician
        </button>
      </div>

      <!-- Summary KPIs -->
      <div class="dashboard-kpi-grid mb-5">
        ${CCS.Components.kpiCard({ icon:'fa-users', iconBg:'#f0ebfc', iconColor:'#6b3a9b', value: techs.length, label:'Total Technicians' })}
        ${CCS.Components.kpiCard({ icon:'fa-truck', iconBg:'#faeaec', iconColor:'var(--accent-600)', value: Object.keys(plates).length, label:'Vehicles Registered' })}
        ${CCS.Components.kpiCard({ icon:'fa-target', iconBg:'#e8f3ef', iconColor:'#2e6b4e', value: Object.keys(targets).length, label:'Targets Set' })}
      </div>

      <!-- Search -->
      <div class="flex gap-3 mb-4">
        <input type="text" class="input-field" placeholder="Search technicians…" style="max-width:280px;"
               oninput="CCS.Pages.Technicians.filter(this.value)">
      </div>

      <!-- Technicians table -->
      <div class="card">
        ${techs.length ? `
          <div class="table-container">
            <table class="table">
              <thead><tr><th>Technician</th><th>Vehicle Plate</th><th>Monthly Target</th><th>Total Supplied</th><th>Actions</th></tr></thead>
              <tbody id="techTableBody">
                ${techs.map(t => this._techRow(t, plates[t] || '', targets[t] || '', region)).join('')}
              </tbody>
            </table>
          </div>` : CCS.Components.emptyState('tech', 'Add Technician', 'CCS.Pages.Technicians.openAdd()')}
      </div>

      <!-- Add/Edit modal -->
      <div class="modal-overlay" id="techModal">
        <div class="modal-container" style="max-width:480px;">
          <div class="modal-header">
            <h3 class="text-xl font-semibold" id="techModalTitle">Add Technician</h3>
            <button class="btn btn-icon btn-ghost" onclick="CCS.Modal.close('techModal')"><i class="fa-regular fa-xmark"></i></button>
          </div>
          <div class="modal-body">
            <div class="input-group">
              <div class="input-wrapper">
                <input type="text" class="input-field" id="techNameInput" placeholder=" ">
                <label class="input-label">Full Name *</label>
              </div>
            </div>
            <div class="input-group">
              <div class="input-wrapper">
                <input type="text" class="input-field" id="techPlateInput" placeholder=" ">
                <label class="input-label">Vehicle Plate</label>
              </div>
            </div>
            <div class="input-group">
              <div class="input-wrapper">
                <input type="number" class="input-field" id="techTargetInput" placeholder=" " min="0">
                <label class="input-label">Monthly Target (L)</label>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary" onclick="CCS.Modal.close('techModal')">Cancel</button>
            <button class="btn btn-primary" onclick="CCS.Pages.Technicians.save()">Save</button>
          </div>
        </div>
      </div>`;
  },

  _techRow(name, plate, target, region) {
    const supplied = Object.values(region.dailyLog || {}).flat()
      .filter(e => e.technician === name).reduce((s, e) => s + (e.supplied || 0), 0);
    const pct = target ? (supplied / target) * 100 : null;
    return `<tr>
      <td><div class="flex items-center gap-3">${CCS.dom.techAvatar(name)}<span class="font-medium">${name}</span></div></td>
      <td><span class="font-mono text-sm">${plate || '—'}</span></td>
      <td>${target ? CCS.fmt.litres(target) : '<span style="color:var(--neutral-400);">Not set</span>'}</td>
      <td>
        <div class="font-mono font-semibold">${CCS.fmt.litres(supplied)}</div>
        ${pct != null ? CCS.Components.progressBar(pct, { label: false }) : ''}
      </td>
      <td>
        <div class="flex gap-1">
          <button class="btn btn-icon btn-ghost" onclick="CCS.Pages.Technicians.openEdit('${name}')" title="Edit"><i class="fa-regular fa-pen"></i></button>
          <button class="btn btn-icon btn-ghost" onclick="CCS.Pages.Technicians.remove('${name}')" title="Remove"><i class="fa-regular fa-trash" style="color:var(--status-danger);"></i></button>
        </div>
      </td>
    </tr>`;
  },

  _editing: null,
  openAdd() {
    this._editing = null;
    document.getElementById('techModalTitle').textContent = 'Add Technician';
    ['techNameInput','techPlateInput','techTargetInput'].forEach(id => { const el = document.getElementById(id); if (el) el.value = ''; });
    CCS.Modal.open('techModal');
  },
  openEdit(name) {
    this._editing = name;
    const region = CCS.DB.region();
    document.getElementById('techModalTitle').textContent = 'Edit Technician';
    document.getElementById('techNameInput').value   = name;
    document.getElementById('techPlateInput').value  = region.technicianPlates?.[name] || '';
    document.getElementById('techTargetInput').value = region.techMonthlyTargets?.[name] || '';
    CCS.Modal.open('techModal');
  },
  save() {
    const name   = document.getElementById('techNameInput')?.value.trim();
    const plate  = document.getElementById('techPlateInput')?.value.trim();
    const target = parseFloat(document.getElementById('techTargetInput')?.value) || 0;
    if (!name) return CCS.Toast.show('Name required', 'warning');

    const region = CCS.DB.region();
    if (!region.technicians) region.technicians = [];
    if (!region.technicianPlates)   region.technicianPlates = {};
    if (!region.techMonthlyTargets) region.techMonthlyTargets = {};

    if (this._editing) {
      const idx = region.technicians.indexOf(this._editing);
      if (idx >= 0) region.technicians[idx] = name;
      if (this._editing !== name) {
        region.technicianPlates[name]   = region.technicianPlates[this._editing];
        region.techMonthlyTargets[name] = region.techMonthlyTargets[this._editing];
        delete region.technicianPlates[this._editing];
        delete region.techMonthlyTargets[this._editing];
      }
    } else {
      if (region.technicians.includes(name)) return CCS.Toast.show('Technician already exists', 'warning');
      region.technicians.push(name);
    }

    if (plate)  region.technicianPlates[name]   = plate;
    if (target) region.techMonthlyTargets[name] = target;

    CCS.Layout.save();
    CCS.Modal.close('techModal');
    CCS.Toast.show(this._editing ? 'Technician updated' : 'Technician added', 'success');
    CCS.Router.go('technicians');
  },
  async remove(name) {
    const ok = await CCS.Components.confirm(`Remove <strong>${name}</strong> from this region?`, { danger: true, okLabel: 'Remove' });
    if (!ok) return;
    const region = CCS.DB.region();
    region.technicians = region.technicians.filter(t => t !== name);
    delete region.technicianPlates?.[name];
    delete region.techMonthlyTargets?.[name];
    CCS.Layout.save();
    CCS.Toast.show('Technician removed', 'success');
    CCS.Router.go('technicians');
  },
  filter(q) {
    const query = q.toLowerCase();
    const tbody = document.getElementById('techTableBody');
    if (!tbody) return;
    tbody.querySelectorAll('tr').forEach(row => {
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(query) ? '' : 'none';
    });
  },
};


/**
 * js/pages/leaderboard.js
 */
CCS.Pages.Leaderboard = {
  skeleton: () => CCS.Components.skeleton('leaderboard'),
  async render(container) {
    const region = CCS.DB.region();
    const log    = region?.dailyLog || {};
    const orders = region?.orders   || {};

    // Aggregate per technician
    const tech = {};
    Object.values(log).flat().forEach(e => {
      if (!tech[e.technician]) tech[e.technician] = { allocated: 0, supplied: 0, entries: 0, orders: new Set() };
      tech[e.technician].allocated += e.allocated || 0;
      tech[e.technician].supplied  += e.supplied  || 0;
      tech[e.technician].entries++;
      tech[e.technician].orders.add(e.orderNo);
    });

    const ranked = Object.entries(tech).sort((a, b) => b[1].supplied - a[1].supplied);
    const max = ranked[0]?.[1].supplied || 1;
    const totalSupplied = ranked.reduce((s, [,v]) => s + v.supplied, 0);

    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-title"><h1>Leaderboard</h1><p>Technician performance ranking for ${CCS.DB.currentRegion}</p></div>
        <button class="btn btn-secondary" onclick="CCS.Excel.exportLeaderboard()">
          <i class="fa-regular fa-file-excel"></i> Export
        </button>
      </div>

      <!-- Summary KPIs -->
      <div class="dashboard-kpi-grid mb-6">
        ${CCS.Components.kpiCard({ icon:'fa-users', iconBg:'#f0ebfc', iconColor:'#6b3a9b', value: ranked.length, label:'Active Technicians' })}
        ${CCS.Components.kpiCard({ icon:'fa-droplet', iconBg:'#faeaec', iconColor:'var(--accent-600)', value: CCS.fmt.litres(totalSupplied), label:'Total Supplied' })}
        ${CCS.Components.kpiCard({ icon:'fa-trophy', iconBg:'#fcf5eb', iconColor:'var(--status-warning)', value: ranked[0]?.[0] || '—', label:'Top Performer' })}
      </div>

      <!-- Ranked list -->
      <div id="lbList">
        ${ranked.length ? ranked.map(([name, s], i) => {
          const pct      = (s.supplied / max) * 100;
          const rankCls  = i === 0 ? 'rank-1' : i === 1 ? 'rank-2' : i === 2 ? 'rank-3' : '';
          const rankIcon = i === 0 ? '🥇' : i === 1 ? '🥈' : i === 2 ? '🥉' : `#${i+1}`;
          const target   = region.techMonthlyTargets?.[name];
          const tPct     = target ? (s.supplied / target) * 100 : null;
          return `
            <div class="leaderboard-card">
              <div class="rank-badge ${rankCls}">${rankIcon}</div>
              ${CCS.dom.techAvatar(name, 'style="width:44px;height:44px;"')}
              <div style="flex:1;min-width:0;">
                <div class="font-semibold">${name}</div>
                <div class="text-xs mt-1" style="color:var(--neutral-500);">
                  ${s.entries} entries · ${s.orders.size} orders
                </div>
                <div class="lb-bar-container mt-2">
                  <div class="lb-bar-fill" style="width:${pct}%;"></div>
                </div>
                ${tPct != null ? `<div class="text-xs mt-1" style="color:var(--neutral-400);">Target: ${tPct.toFixed(1)}% of ${CCS.fmt.litres(target)}</div>` : ''}
              </div>
              <div style="text-align:right;">
                <div class="font-mono font-bold text-lg">${CCS.fmt.litres(s.supplied)}</div>
                <div class="text-xs" style="color:var(--neutral-400);">supplied</div>
                <div class="text-xs font-mono mt-1">${CCS.fmt.litres(s.allocated)} alloc</div>
              </div>
            </div>`;
        }).join('') : CCS.Components.emptyState('leaderboard')}
      </div>`;
  },
};


/**
 * js/pages/reports.js
 */
CCS.Pages.Reports = {
  async render(container) {
    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-title"><h1>Reports</h1><p>Analytics and export for ${CCS.DB.currentRegion}</p></div>
        <button class="btn btn-secondary" onclick="CCS.Excel.exportAllRegions()">
          <i class="fa-regular fa-file-excel"></i> Export All Regions
        </button>
      </div>

      <div class="grid grid-cols-2 gap-4">
        ${[
          { title:'Daily Log Export',    icon:'fa-calendar', desc:'Export complete daily supply log as multi-sheet workbook.', action:"CCS.Excel.exportDailyLog()", btn:'Export Daily Log' },
          { title:'Orders Report',       icon:'fa-file-lines', desc:'Export all orders with allocations and balances.', action:"CCS.Excel.exportOrders()", btn:'Export Orders' },
          { title:'Leaderboard Report',  icon:'fa-trophy', desc:'Export ranked technician performance.', action:"CCS.Excel.exportLeaderboard()", btn:'Export Leaderboard' },
          { title:'All Regions Report',  icon:'fa-map', desc:'Export data across all regions in one workbook.', action:"CCS.Excel.exportAllRegions()", btn:'Export All Regions' },
        ].map(r => `
          <div class="card">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
              <div style="width:40px;height:40px;border-radius:var(--radius-lg);background:var(--accent-100);color:var(--accent-600);display:flex;align-items:center;justify-content:center;">
                <i class="fa-regular ${r.icon}"></i>
              </div>
              <h3 class="text-lg font-semibold">${r.title}</h3>
            </div>
            <p class="text-sm mb-4" style="color:var(--neutral-500);">${r.desc}</p>
            <button class="btn btn-primary btn-sm" onclick="${r.action}">
              <i class="fa-regular fa-download"></i> ${r.btn}
            </button>
          </div>`).join('')}
      </div>

      <!-- Chart section -->
      <div class="card mt-5">
        <h3 class="text-lg font-semibold mb-4">Monthly Supply Overview</h3>
        <canvas id="monthlyChart" height="200"></canvas>
      </div>`;

    this._renderMonthlyChart();
  },

  _renderMonthlyChart() {
    const canvas = document.getElementById('monthlyChart');
    if (!canvas || !window.Chart) return;

    const log = CCS.DB.region()?.dailyLog || {};
    const byMonth = {};
    Object.entries(log).forEach(([date, entries]) => {
      const m = date.slice(0, 7);
      byMonth[m] = (byMonth[m] || 0) + entries.reduce((s, e) => s + (e.supplied || 0), 0);
    });

    const months = Object.keys(byMonth).sort().slice(-12);
    if (canvas._chartInst) canvas._chartInst.destroy();
    canvas._chartInst = new Chart(canvas, {
      type: 'line',
      data: {
        labels: months.map(m => { const [y,mo] = m.split('-'); return new Date(+y,+mo-1).toLocaleString('en-GB',{month:'short',year:'2-digit'}); }),
        datasets: [{ label:'Litres Supplied', data: months.map(m => byMonth[m] || 0), borderColor:'rgba(196,30,58,0.9)', backgroundColor:'rgba(196,30,58,0.08)', fill:true, tension:0.4, pointRadius:4 }],
      },
      options: { responsive:true, plugins:{legend:{display:false}}, scales:{y:{ticks:{callback:v=>v+'L'}}} },
    });
  },
};


/**
 * js/pages/automation.js — WhatsApp parser
 */
CCS.Pages.Automation = {
  async render(container) {
    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-title">
          <h1>Automation</h1>
          <p>Paste WhatsApp field reports to auto-fill daily entries</p>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-5">
        <!-- Input -->
        <div class="card">
          <h3 class="text-lg font-semibold mb-3">Paste WhatsApp Message</h3>
          <p class="text-sm mb-4" style="color:var(--neutral-500);">
            Format: <code style="background:var(--neutral-100);padding:2px 6px;border-radius:4px;">Name: ORDER123 - 500L supplied</code>
          </p>
          <textarea id="whatsappInput" rows="12" class="input-field" placeholder="Paste WhatsApp chat export here…" style="font-family:var(--font-mono);font-size:.8rem;"></textarea>
          <div class="flex gap-2 mt-3">
            <input type="date" class="input-field" id="automationDate" value="${new Date().toISOString().slice(0,10)}" style="width:auto;">
            <button class="btn btn-primary" onclick="CCS.Pages.Automation.parse()">
              <i class="fa-regular fa-wand-magic-sparkles"></i> Parse & Preview
            </button>
            <button class="btn btn-ghost" onclick="document.getElementById('whatsappInput').value=''">Clear</button>
          </div>
        </div>

        <!-- Preview -->
        <div class="card">
          <h3 class="text-lg font-semibold mb-3">Parsed Entries <span id="parsedCount" style="color:var(--neutral-400);font-weight:400;"></span></h3>
          <div id="parsedPreview" style="min-height:200px;">
            <div class="empty-state"><p>Paste a message and click Parse to preview entries.</p></div>
          </div>
          <button class="btn btn-primary mt-4 w-full" id="importBtn" style="display:none;" onclick="CCS.Pages.Automation.importEntries()">
            <i class="fa-regular fa-file-import"></i> Import All Entries
          </button>
        </div>
      </div>`;
  },

  _parsed: [],

  parse() {
    const text = document.getElementById('whatsappInput')?.value || '';
    const techs = CCS.DB.technicians();
    this._parsed = [];

    // Pattern: name: ORDER - 500L / name ORDER 500
    const lines = text.split('\n');
    lines.forEach(line => {
      // Flexible regex: find technician name, order ref, litres
      const orderMatch   = line.match(/[A-Z]{2,4}\d{4,}/i);
      const litresMatch  = line.match(/(\d+(?:\.\d+)?)\s*[Ll]/);
      const techMatch    = techs.find(t => line.toLowerCase().includes(t.toLowerCase()));

      if (techMatch && orderMatch && litresMatch) {
        this._parsed.push({
          technician: techMatch,
          orderNo:    orderMatch[0].toUpperCase(),
          supplied:   parseFloat(litresMatch[1]),
          allocated:  parseFloat(litresMatch[1]),
          raw:        line.trim(),
        });
      }
    });

    const preview  = document.getElementById('parsedPreview');
    const count    = document.getElementById('parsedCount');
    const importBtn = document.getElementById('importBtn');
    count.textContent = `(${this._parsed.length} entries)`;

    if (!this._parsed.length) {
      preview.innerHTML = '<div class="empty-state"><p>No entries could be parsed. Check message format.</p></div>';
      importBtn.style.display = 'none';
      return;
    }

    preview.innerHTML = `
      <div class="table-container">
        <table class="table">
          <thead><tr><th>Technician</th><th>Order</th><th>Supplied</th></tr></thead>
          <tbody>
            ${this._parsed.map(e => `<tr>
              <td>${CCS.dom.techAvatar(e.technician)} <span class="ml-2 text-sm">${e.technician}</span></td>
              <td><span class="badge badge-info">${e.orderNo}</span></td>
              <td class="font-mono font-semibold">${CCS.fmt.litres(e.supplied)}</td>
            </tr>`).join('')}
          </tbody>
        </table>
      </div>`;
    importBtn.style.display = 'flex';
  },

  importEntries() {
    if (!this._parsed.length) return;
    const date   = document.getElementById('automationDate')?.value;
    const region = CCS.DB.region();
    if (!region.dailyLog[date]) region.dailyLog[date] = [];

    let imported = 0;
    this._parsed.forEach(e => {
      const idx = region.dailyLog[date].findIndex(ex => ex.technician === e.technician && ex.orderNo === e.orderNo);
      if (idx >= 0) { region.dailyLog[date][idx] = { ...e, addedAt: new Date().toISOString() }; }
      else          { region.dailyLog[date].push({ ...e, addedAt: new Date().toISOString() }); imported++; }

      // Update order totals
      const order = region.orders[e.orderNo];
      if (order) {
        order.suppliedTotal = Object.values(region.dailyLog).flat()
          .filter(ex => ex.orderNo === e.orderNo).reduce((s, ex) => s + (ex.supplied || 0), 0);
      }
    });

    CCS.Layout.save();
    CCS.Toast.show(`Imported ${this._parsed.length} entries`, 'success');
    this._parsed = [];
    document.getElementById('parsedPreview').innerHTML = '<div class="empty-state"><p>Import complete.</p></div>';
    document.getElementById('importBtn').style.display = 'none';
    document.getElementById('parsedCount').textContent = '';
  },
};


/**
 * js/pages/cycles.js
 */
CCS.Pages.Cycles = {
  async render(container) {
    const cycles = CCS.DB.cycles || [];
    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-title"><h1>Cycle Management</h1><p>Manage fuel allocation cycles</p></div>
        <button class="btn btn-primary" onclick="CCS.Pages.Cycles.openNew()">
          <i class="fa-regular fa-plus"></i> New Cycle
        </button>
      </div>

      <div class="card mb-5">
        <h3 class="text-sm font-semibold mb-2" style="color:var(--neutral-600);text-transform:uppercase;letter-spacing:.05em;">Current Cycle</h3>
        <div class="flex items-center gap-4">
          <div class="text-2xl font-bold">${CCS.DB.currentCycleName}</div>
          <div class="badge badge-success">Active</div>
          <div class="text-sm" style="color:var(--neutral-500);">Started ${CCS.fmt.date(CCS.DB.currentCycleStartDate)}</div>
        </div>
      </div>

      <div class="card">
        <h3 class="text-lg font-semibold mb-4">Cycle History</h3>
        ${cycles.length ? `
          <div class="table-container">
            <table class="table">
              <thead><tr><th>Cycle Name</th><th>Start</th><th>End</th><th>Actions</th></tr></thead>
              <tbody>
                ${[...cycles].reverse().map(c => `<tr>
                  <td class="font-semibold">${c.name}</td>
                  <td>${CCS.fmt.date(c.startDate)}</td>
                  <td>${c.endDate ? CCS.fmt.date(c.endDate) : '<span style="color:var(--neutral-400);">Ongoing</span>'}</td>
                  <td>
                    <button class="btn btn-secondary btn-sm" onclick="CCS.Pages.Cycles.restore('${c.name}')">Restore</button>
                  </td>
                </tr>`).join('')}
              </tbody>
            </table>
          </div>` : '<p style="color:var(--neutral-400);">No cycle history yet.</p>'}
      </div>

      <div class="modal-overlay" id="cycleModal">
        <div class="modal-container" style="max-width:420px;">
          <div class="modal-header">
            <h3 class="text-xl font-semibold">New Cycle</h3>
            <button class="btn btn-icon btn-ghost" onclick="CCS.Modal.close('cycleModal')"><i class="fa-regular fa-xmark"></i></button>
          </div>
          <div class="modal-body">
            <div class="input-group">
              <div class="input-wrapper"><input type="text" class="input-field" id="cycleNameInput" placeholder=" "><label class="input-label">Cycle Name *</label></div>
            </div>
            <div class="input-group">
              <div class="input-wrapper"><input type="date" class="input-field" id="cycleStartInput"><label class="input-label">Start Date</label></div>
            </div>
            <p class="text-sm" style="color:var(--status-warning);"><i class="fa-regular fa-triangle-exclamation"></i> Starting a new cycle will archive the current one.</p>
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary" onclick="CCS.Modal.close('cycleModal')">Cancel</button>
            <button class="btn btn-primary" onclick="CCS.Pages.Cycles.create()">Start Cycle</button>
          </div>
        </div>
      </div>`;
  },

  openNew() {
    document.getElementById('cycleNameInput').value  = '';
    document.getElementById('cycleStartInput').value = new Date().toISOString().slice(0,10);
    CCS.Modal.open('cycleModal');
  },

  create() {
    const name  = document.getElementById('cycleNameInput')?.value.trim();
    const start = document.getElementById('cycleStartInput')?.value;
    if (!name) return CCS.Toast.show('Cycle name required', 'warning');

    CCS.DB.cycles.push({ name: CCS.DB.currentCycleName, startDate: CCS.DB.currentCycleStartDate, endDate: start });
    CCS.DB.currentCycleName      = name;
    CCS.DB.currentCycleStartDate = start;
    CCS.Layout.save();
    CCS.Modal.close('cycleModal');
    CCS.Toast.show(`Cycle "${name}" started`, 'success');
    CCS.Router.go('cycles');
  },

  async restore(name) {
    const ok = await CCS.Components.confirm(`Restore cycle <strong>${name}</strong> as current?`, { okLabel: 'Restore' });
    if (!ok) return;
    const c = CCS.DB.cycles.find(c => c.name === name);
    if (!c) return;
    CCS.DB.currentCycleName      = c.name;
    CCS.DB.currentCycleStartDate = c.startDate;
    CCS.Layout.save();
    CCS.Toast.show('Cycle restored', 'success');
    CCS.Router.go('cycles');
  },
};


/**
 * js/pages/regions.js
 */
CCS.Pages.Regions = {
  async render(container) {
    const regions = CCS.DB.listRegions();
    const current = CCS.DB.currentRegion;

    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-title"><h1>Region Management</h1><p>Switch or add regions</p></div>
        <button class="btn btn-primary" onclick="CCS.Pages.Regions.openAdd()">
          <i class="fa-regular fa-plus"></i> Add Region
        </button>
      </div>

      <div class="grid grid-cols-3 gap-4">
        ${regions.map(r => `
          <div class="card${r === current ? ' border-accent-600' : ''}" style="${r === current ? 'border-color:var(--accent-600);border-width:2px;' : ''}">
            <div class="flex items-center justify-between mb-3">
              <div class="font-bold text-lg">${r}</div>
              ${r === current ? '<span class="badge badge-success">Active</span>' : ''}
            </div>
            <div class="text-sm" style="color:var(--neutral-500);">
              ${Object.keys(CCS.DB.data.regions[r]?.orders || {}).length} orders ·
              ${(CCS.DB.data.regions[r]?.technicians || []).length} technicians
            </div>
            ${r !== current ? `
              <div class="flex gap-2 mt-4">
                <button class="btn btn-primary btn-sm" onclick="CCS.Pages.Regions.switchTo('${r}')">Switch to Region</button>
                <button class="btn btn-danger btn-sm" onclick="CCS.Pages.Regions.remove('${r}')"><i class="fa-regular fa-trash"></i></button>
              </div>` : `<div class="mt-4 text-xs" style="color:var(--neutral-400);">Currently active region</div>`}
          </div>`).join('')}
      </div>

      <div class="modal-overlay" id="regionModal">
        <div class="modal-container" style="max-width:400px;">
          <div class="modal-header">
            <h3 class="text-xl font-semibold">Add Region</h3>
            <button class="btn btn-icon btn-ghost" onclick="CCS.Modal.close('regionModal')"><i class="fa-regular fa-xmark"></i></button>
          </div>
          <div class="modal-body">
            <div class="input-group">
              <div class="input-wrapper"><input type="text" class="input-field" id="regionNameInput" placeholder=" "><label class="input-label">Region Name *</label></div>
            </div>
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary" onclick="CCS.Modal.close('regionModal')">Cancel</button>
            <button class="btn btn-primary" onclick="CCS.Pages.Regions.add()">Add Region</button>
          </div>
        </div>
      </div>`;
  },

  openAdd() { document.getElementById('regionNameInput').value = ''; CCS.Modal.open('regionModal'); },
  add() {
    const name = document.getElementById('regionNameInput')?.value.trim();
    if (!name) return CCS.Toast.show('Region name required', 'warning');
    if (CCS.DB.data.regions[name]) return CCS.Toast.show('Region already exists', 'warning');
    CCS.DB.ensureRegion(name);
    CCS.Layout.save();
    CCS.Modal.close('regionModal');
    CCS.Toast.show(`Region "${name}" added`, 'success');
    CCS.Router.go('regions');
  },
  switchTo(name) {
    CCS.DB.currentRegion = name;
    CCS.Layout.save();
    CCS.Layout.updateFooterRegion();
    document.getElementById('topbarRegion').textContent = name;
    CCS.Toast.show(`Switched to ${name}`, 'success');
    CCS.Router.go('dashboard');
  },
  async remove(name) {
    const ok = await CCS.Components.confirm(`Delete region <strong>${name}</strong> and all its data? This cannot be undone.`, { danger: true, okLabel: 'Delete Region' });
    if (!ok) return;
    delete CCS.DB.data.regions[name];
    CCS.Layout.save();
    CCS.Toast.show('Region deleted', 'success');
    CCS.Router.go('regions');
  },
};


/**
 * js/pages/admin.js
 */
CCS.Pages.Admin = {
  async render(container) {
    if (!CCS.Auth.isAdmin()) {
      container.innerHTML = '<div class="card" style="text-align:center;padding:3rem;"><h2>Access Denied</h2><p>Admin access required.</p></div>';
      return;
    }
    const users = CCS.Auth.getUsers();

    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-title"><h1>Admin Panel</h1><p>User management and system settings</p></div>
        <button class="btn btn-primary" onclick="CCS.Modal.open('adminAddModal')">
          <i class="fa-regular fa-user-plus"></i> Add User
        </button>
      </div>

      <div class="card">
        <h3 class="text-lg font-semibold mb-4">Users (${users.length})</h3>
        ${users.map((u, i) => `
          <div class="admin-user-row">
            <div class="admin-user-avatar">${u.email.charAt(0).toUpperCase()}</div>
            <div class="admin-user-info flex-1">
              <div class="admin-user-email">${u.email}</div>
              <div class="admin-user-meta">Joined ${CCS.fmt.date(u.createdAt?.slice(0,10))}</div>
            </div>
            <span class="badge ${u.isAdmin ? 'badge-admin' : 'badge-user'}">${u.isAdmin ? 'Admin' : 'User'}</span>
            <div class="flex gap-1">
              <button class="btn btn-secondary btn-sm" onclick="CCS.Auth.adminToggleRole(${i});CCS.Router.go('admin')">
                ${u.isAdmin ? 'Revoke Admin' : 'Make Admin'}
              </button>
              <button class="btn btn-danger btn-sm" onclick="CCS.Auth.adminDeleteUser(${i});CCS.Router.go('admin')">
                <i class="fa-regular fa-trash"></i>
              </button>
            </div>
          </div>`).join('')}
      </div>

      <!-- Danger zone -->
      <div class="card mt-5" style="border-color:var(--status-danger);border-width:2px;">
        <h3 class="text-lg font-semibold mb-2" style="color:var(--status-danger);">Danger Zone</h3>
        <p class="text-sm mb-4" style="color:var(--neutral-500);">These actions are irreversible.</p>
        <button class="btn btn-danger" onclick="CCS.Pages.Admin.clearAllData()">
          <i class="fa-regular fa-triangle-exclamation"></i> Clear All Application Data
        </button>
      </div>

      <div class="modal-overlay" id="adminAddModal">
        <div class="modal-container" style="max-width:440px;">
          <div class="modal-header">
            <h3 class="text-xl font-semibold">Add User</h3>
            <button class="btn btn-icon btn-ghost" onclick="CCS.Modal.close('adminAddModal')"><i class="fa-regular fa-xmark"></i></button>
          </div>
          <div class="modal-body">
            <div class="input-group"><div class="input-wrapper"><input type="email" class="input-field" id="adminEmail" placeholder=" "><label class="input-label">Email (@ccszambia.com)</label></div></div>
            <div class="input-group"><div class="input-wrapper"><input type="password" class="input-field" id="adminPw" placeholder=" "><label class="input-label">Password</label></div></div>
            <label style="display:flex;align-items:center;gap:8px;font-size:var(--text-sm);cursor:pointer;">
              <input type="checkbox" id="adminIsAdmin"> Grant admin role
            </label>
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary" onclick="CCS.Modal.close('adminAddModal')">Cancel</button>
            <button class="btn btn-primary" onclick="CCS.Pages.Admin.addUser()">Add User</button>
          </div>
        </div>
      </div>`;
  },

  async addUser() {
    const email   = document.getElementById('adminEmail')?.value.trim();
    const pw      = document.getElementById('adminPw')?.value;
    const isAdmin = document.getElementById('adminIsAdmin')?.checked;
    await CCS.Auth.adminAddUser(email, pw, isAdmin);
    CCS.Modal.close('adminAddModal');
    CCS.Router.go('admin');
  },

  async clearAllData() {
    const typed = await CCS.Components.confirm(
      'Type <strong>DELETE</strong> to confirm wiping all application data.',
      { danger: true, input: true, inputLabel: 'Type DELETE to confirm', okLabel: 'Wipe Data', title: 'Clear All Data' }
    );
    if (typed !== 'DELETE') return CCS.Toast.show('Cancelled — data not cleared', 'info');
    CCS.DB.reset();
    CCS.Toast.show('All data cleared', 'success');
    CCS.Router.go('dashboard');
  },
};


/**
 * js/pages/settings.js
 */
CCS.Pages.Settings = {
  async render(container) {
    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-title"><h1>Settings</h1><p>Preferences and configuration</p></div>
      </div>

      <div class="card mb-4">
        <h3 class="text-lg font-semibold mb-4">Appearance</h3>
        <div class="flex items-center justify-between">
          <div>
            <div class="font-medium">Dark Mode</div>
            <div class="text-sm" style="color:var(--neutral-500);">Toggle dark colour scheme</div>
          </div>
          <button class="btn btn-secondary" onclick="CCS.Layout.toggleDarkMode()">
            <i class="fa-regular fa-moon"></i> Toggle Dark Mode
          </button>
        </div>
      </div>

      <div class="card mb-4">
        <h3 class="text-lg font-semibold mb-4">Monthly Target</h3>
        <div class="flex items-center gap-4">
          <input type="number" class="input-field" id="monthlyTargetInput" placeholder="e.g. 50000" style="max-width:200px;"
                 value="${CCS.DB.region()?.monthlyTarget || ''}">
          <button class="btn btn-primary" onclick="CCS.Pages.Settings.saveTarget()">Save Target</button>
        </div>
      </div>

      <div class="card mb-4">
        <h3 class="text-lg font-semibold mb-4">Onboarding Tour</h3>
        <div class="flex items-center justify-between">
          <div class="text-sm" style="color:var(--neutral-500);">Replay the guided onboarding tour.</div>
          <button class="btn btn-secondary" onclick="localStorage.removeItem('ccs_tour_done');CCS.Tour.start();">
            <i class="fa-regular fa-circle-play"></i> Restart Tour
          </button>
        </div>
      </div>

      <div class="card">
        <h3 class="text-lg font-semibold mb-4">Data</h3>
        <div class="flex gap-3 flex-wrap">
          <button class="btn btn-secondary" onclick="CCS.Pages.Settings.exportBackup()">
            <i class="fa-regular fa-file-export"></i> Export Backup (JSON)
          </button>
          <label class="btn btn-secondary" style="cursor:pointer;">
            <i class="fa-regular fa-file-import"></i> Import Backup
            <input type="file" accept=".json" style="display:none;" onchange="CCS.Pages.Settings.importBackup(event)">
          </label>
        </div>
      </div>`;
  },

  saveTarget() {
    const v = parseFloat(document.getElementById('monthlyTargetInput')?.value);
    if (!v || v <= 0) return CCS.Toast.show('Enter a valid target', 'warning');
    CCS.DB.region().monthlyTarget = v;
    CCS.Layout.save();
    CCS.Toast.show('Monthly target saved', 'success');
  },

  exportBackup() {
    const blob = new Blob([JSON.stringify(CCS.DB.data, null, 2)], { type: 'application/json' });
    const url  = URL.createObjectURL(blob);
    const a    = document.createElement('a');
    a.href = url; a.download = `CCS_Backup_${new Date().toISOString().slice(0,10)}.json`;
    a.click(); URL.revokeObjectURL(url);
    CCS.Toast.show('Backup downloaded', 'success');
  },

  importBackup(event) {
    const file = event.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = async e => {
      try {
        const data = JSON.parse(e.target.result);
        const ok = await CCS.Components.confirm('Replace all current data with backup?', { danger: true, okLabel: 'Import' });
        if (!ok) return;
        localStorage.setItem('ccs_fuel_orders_v6', JSON.stringify(data));
        location.reload();
      } catch {
        CCS.Toast.show('Invalid backup file', 'error');
      }
    };
    reader.readAsText(file);
  },
};
