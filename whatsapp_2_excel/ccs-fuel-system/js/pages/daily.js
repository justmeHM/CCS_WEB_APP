/**
 * js/pages/daily.js
 * Daily fuel supply entry page.
 * Records litres supplied per technician per date.
 */

'use strict';

CCS.Pages = CCS.Pages || {};

CCS.Pages.Daily = {
  skeleton: () => CCS.Components.skeleton('daily'),

  async render(container) {
    const today = new Date().toISOString().slice(0, 10);

    container.innerHTML = `
      <div class="page-header">
        <div class="page-header-title">
          <h1>Daily Entry</h1>
          <p>Record fuel supplied per technician for ${CCS.DB.currentRegion}</p>
        </div>
        <div class="flex gap-2">
          <button class="btn btn-secondary" onclick="CCS.Excel.exportDailyLog()">
            <i class="fa-regular fa-file-excel"></i> Export Log
          </button>
          <button class="btn btn-secondary" onclick="CCS.Router.go('automation')">
            <i class="fa-brands fa-whatsapp" style="color:#25D366;"></i> WhatsApp Parser
          </button>
        </div>
      </div>

      <!-- Date selector -->
      <div class="card mb-5">
        <div class="flex items-center gap-4 flex-wrap">
          <div>
            <label class="text-sm font-medium" style="color:var(--neutral-600);display:block;margin-bottom:4px;">Date</label>
            <input type="date" class="input-field" id="dailyDate" value="${today}" 
                   onchange="CCS.Pages.Daily.loadDate(this.value)" style="width:auto;">
          </div>
          <button class="btn btn-secondary btn-sm" onclick="CCS.Pages.Daily.setDate(-1)">
            <i class="fa-regular fa-chevron-left"></i> Prev
          </button>
          <button class="btn btn-secondary btn-sm" onclick="CCS.Pages.Daily.setDate(1)">
            Next <i class="fa-regular fa-chevron-right"></i>
          </button>
          <button class="btn btn-ghost btn-sm" onclick="CCS.Pages.Daily.loadDate('${today}');document.getElementById('dailyDate').value='${today}'">
            Today
          </button>
          <div class="autosave-indicator visible ml-auto" id="dailyAutosave" style="display:none;">
            <div class="autosave-dot"></div>
            <span>Saved</span>
          </div>
        </div>
      </div>

      <!-- Daily summary KPIs -->
      <div id="dailySummary" class="dashboard-kpi-grid mb-5" style="grid-template-columns:repeat(auto-fit,minmax(160px,1fr));"></div>

      <!-- Add entry -->
      <div class="card mb-5">
        <h3 class="text-lg font-semibold mb-4">Add Entry</h3>
        <div class="grid grid-cols-2 gap-4" style="grid-template-columns:repeat(auto-fit,minmax(160px,1fr));">
          <div class="input-group">
            <div class="select-wrapper">
              <select class="select-field" id="dailyTech">
                <option value="">Select Technician</option>
                ${(CCS.DB.technicians()).map(t => `<option value="${t}">${t}</option>`).join('')}
              </select>
            </div>
          </div>
          <div class="input-group">
            <div class="select-wrapper">
              <select class="select-field" id="dailyOrder" onchange="CCS.Pages.Daily.onOrderChange()">
                <option value="">Select Order</option>
                ${Object.keys(CCS.DB.orders()).filter(o => (CCS.DB.order(o).status || 'open') === 'open')
                  .map(o => `<option value="${o}">${o}</option>`).join('')}
              </select>
            </div>
          </div>
          <div class="input-group">
            <div class="input-wrapper">
              <input type="number" class="input-field" id="dailyAllocated" placeholder=" " min="0" step="0.1">
              <label class="input-label">Allocated (L)</label>
            </div>
          </div>
          <div class="input-group">
            <div class="input-wrapper">
              <input type="number" class="input-field" id="dailySupplied" placeholder=" " min="0" step="0.1">
              <label class="input-label">Supplied (L)</label>
            </div>
          </div>
          <div class="input-group" style="grid-column:1/-1;">
            <div class="input-wrapper">
              <input type="text" class="input-field" id="dailyNotes" placeholder=" ">
              <label class="input-label">Notes (optional)</label>
            </div>
          </div>
        </div>
        <div class="flex gap-2 mt-2">
          <button class="btn btn-primary" onclick="CCS.Pages.Daily.addEntry()">
            <i class="fa-regular fa-plus"></i> Add Entry
          </button>
          <button class="btn btn-ghost" onclick="CCS.Pages.Daily.clearForm()">Clear</button>
        </div>
      </div>

      <!-- Entries list -->
      <div class="card">
        <div class="flex items-center justify-between mb-4">
          <h3 class="text-lg font-semibold">Entries for <span id="dailyDateLabel"></span></h3>
          <div class="flex gap-2">
            <button class="btn btn-secondary btn-sm" onclick="CCS.Pages.Daily.exportDay()">
              <i class="fa-regular fa-download"></i> Export Day
            </button>
            <button class="btn btn-danger btn-sm" onclick="CCS.Pages.Daily.clearDay()" id="clearDayBtn" style="display:none;">
              <i class="fa-regular fa-trash"></i> Clear Day
            </button>
          </div>
        </div>
        <div id="dailyEntryList"></div>
      </div>`;

    this.loadDate(today);
  },

  // ── Date helpers ──────────────────────────────────────────────────────────
  setDate(delta) {
    const input = document.getElementById('dailyDate');
    if (!input) return;
    const current = new Date(input.value + 'T00:00:00');
    current.setDate(current.getDate() + delta);
    const newDate = current.toISOString().slice(0, 10);
    input.value = newDate;
    this.loadDate(newDate);
  },

  loadDate(date) {
    const label = document.getElementById('dailyDateLabel');
    if (label) label.textContent = CCS.fmt.date(date);
    this.renderEntries(date);
    this.renderSummary(date);
  },

  // ── Order → allocated prefill ─────────────────────────────────────────────
  onOrderChange() {
    const orderNo = document.getElementById('dailyOrder')?.value;
    const techEl  = document.getElementById('dailyTech');
    const allocEl = document.getElementById('dailyAllocated');
    if (!orderNo || !techEl?.value || !allocEl) return;

    const o    = CCS.DB.order(orderNo);
    const tech = techEl.value;
    if (o?.allocations?.[tech]) allocEl.value = o.allocations[tech];
  },

  // ── Add entry ─────────────────────────────────────────────────────────────
  addEntry() {
    const date      = document.getElementById('dailyDate')?.value;
    const tech      = document.getElementById('dailyTech')?.value;
    const orderNo   = document.getElementById('dailyOrder')?.value;
    const allocated = parseFloat(document.getElementById('dailyAllocated')?.value);
    const supplied  = parseFloat(document.getElementById('dailySupplied')?.value);
    const notes     = document.getElementById('dailyNotes')?.value.trim() || '';

    if (!tech)                      return CCS.Toast.show('Select a technician', 'warning');
    if (!orderNo)                   return CCS.Toast.show('Select an order', 'warning');
    if (isNaN(allocated) || allocated < 0) return CCS.Toast.show('Enter a valid allocated amount', 'warning');
    if (isNaN(supplied)  || supplied  < 0) return CCS.Toast.show('Enter a valid supplied amount', 'warning');

    const region = CCS.DB.region();
    if (!region.dailyLog[date]) region.dailyLog[date] = [];

    // Check for existing entry for same tech+order today — offer to update
    const existIdx = region.dailyLog[date].findIndex(e => e.technician === tech && e.orderNo === orderNo);
    const entry = { technician: tech, orderNo, allocated, supplied, notes, addedAt: new Date().toISOString() };

    if (existIdx >= 0) {
      region.dailyLog[date][existIdx] = entry;
      CCS.Toast.show('Entry updated', 'success');
    } else {
      region.dailyLog[date].push(entry);
      CCS.Toast.show('Entry added', 'success');
    }

    // Update order supplied total
    const order = region.orders[orderNo];
    if (order) {
      order.suppliedTotal = region.dailyLog
        ? Object.values(region.dailyLog).flat().filter(e => e.orderNo === orderNo).reduce((s, e) => s + (e.supplied || 0), 0)
        : 0;
      if (order.suppliedTotal >= order.totalLiters) order.status = 'over';
    }

    CCS.Layout.save();
    this.clearForm();
    this.loadDate(date);
  },

  clearForm() {
    ['dailyTech','dailyOrder','dailyAllocated','dailySupplied','dailyNotes'].forEach(id => {
      const el = document.getElementById(id); if (el) el.value = '';
    });
  },

  // ── Render entries ────────────────────────────────────────────────────────
  renderEntries(date) {
    const list    = document.getElementById('dailyEntryList');
    const clearBtn = document.getElementById('clearDayBtn');
    if (!list) return;

    const entries = CCS.DB.entriesForDate(date);
    if (clearBtn) clearBtn.style.display = entries.length ? 'flex' : 'none';

    if (!entries.length) {
      list.innerHTML = CCS.Components.emptyState('daily');
      return;
    }

    list.innerHTML = `
      <div class="table-container">
        <table class="table">
          <thead>
            <tr>
              <th></th>
              <th>Technician</th>
              <th>Order</th>
              <th>Allocated</th>
              <th>Supplied</th>
              <th>Balance</th>
              <th>Notes</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            ${entries.map((e, i) => {
              const bal  = (e.allocated || 0) - (e.supplied || 0);
              const over = bal < 0;
              return `<tr>
                <td style="padding:8px;"><i class="fa-regular fa-grip-dots-vertical drag-handle" style="color:var(--neutral-300);"></i></td>
                <td><div class="flex items-center gap-2">${CCS.dom.techAvatar(e.technician, 'style="width:28px;height:28px;font-size:.7rem;"')}<span class="text-sm">${e.technician}</span></div></td>
                <td><span class="badge badge-info">${e.orderNo}</span></td>
                <td class="font-mono text-sm">${CCS.fmt.litres(e.allocated || 0)}</td>
                <td class="font-mono text-sm font-semibold">${CCS.fmt.litres(e.supplied || 0)}</td>
                <td class="font-mono text-sm" style="${over ? 'color:var(--status-danger);font-weight:600;' : 'color:var(--status-success);'}">
                  ${over ? '⚠️ ' : ''}${CCS.fmt.litres(Math.abs(bal))}${over ? ' over' : ''}
                </td>
                <td class="text-xs" style="color:var(--neutral-500);max-width:140px;overflow:hidden;text-overflow:ellipsis;">${e.notes || '—'}</td>
                <td>
                  <button class="btn btn-icon btn-ghost" onclick="CCS.Pages.Daily.deleteEntry('${date}', ${i})" title="Delete entry">
                    <i class="fa-regular fa-trash" style="color:var(--status-danger);"></i>
                  </button>
                </td>
              </tr>`;
            }).join('')}
          </tbody>
        </table>
      </div>`;
  },

  // ── Summary KPIs ──────────────────────────────────────────────────────────
  renderSummary(date) {
    const el      = document.getElementById('dailySummary');
    if (!el) return;

    const entries = CCS.DB.entriesForDate(date);
    const totalAlloc = entries.reduce((s, e) => s + (e.allocated || 0), 0);
    const totalSup   = entries.reduce((s, e) => s + (e.supplied  || 0), 0);
    const techCount  = new Set(entries.map(e => e.technician)).size;
    const orderCount = new Set(entries.map(e => e.orderNo)).size;

    el.innerHTML = `
      ${CCS.Components.kpiCard({ icon: 'fa-droplet', iconBg: '#faeaec', iconColor: 'var(--accent-600)', value: CCS.fmt.litres(totalAlloc), label: 'Total Allocated' })}
      ${CCS.Components.kpiCard({ icon: 'fa-truck', iconBg: '#e8f3ef', iconColor: '#2e6b4e', value: CCS.fmt.litres(totalSup), label: 'Total Supplied' })}
      ${CCS.Components.kpiCard({ icon: 'fa-users', iconBg: '#f0ebfc', iconColor: '#6b3a9b', value: techCount, label: 'Technicians' })}
      ${CCS.Components.kpiCard({ icon: 'fa-file-lines', iconBg: '#f0f7fc', iconColor: 'var(--status-info)', value: orderCount, label: 'Orders Covered' })}`;
  },

  // ── Delete entry ──────────────────────────────────────────────────────────
  async deleteEntry(date, idx) {
    const confirmed = await CCS.Components.confirm('Remove this entry?', { danger: true, okLabel: 'Remove' });
    if (!confirmed) return;

    const region = CCS.DB.region();
    const entry  = region.dailyLog[date]?.[idx];
    region.dailyLog[date].splice(idx, 1);

    // Recalculate order supplied total
    if (entry) {
      const order = region.orders[entry.orderNo];
      if (order) {
        order.suppliedTotal = Object.values(region.dailyLog).flat()
          .filter(e => e.orderNo === entry.orderNo)
          .reduce((s, e) => s + (e.supplied || 0), 0);
        if (order.status === 'over' && order.suppliedTotal < order.totalLiters) order.status = 'open';
      }
    }

    CCS.Layout.save();
    this.loadDate(date);
    CCS.Toast.show('Entry removed', 'success');
  },

  // ── Clear day ─────────────────────────────────────────────────────────────
  async clearDay() {
    const date = document.getElementById('dailyDate')?.value;
    const confirmed = await CCS.Components.confirm(
      `Clear all entries for <strong>${CCS.fmt.date(date)}</strong>? This cannot be undone.`,
      { danger: true, okLabel: 'Clear All' }
    );
    if (!confirmed) return;
    const region = CCS.DB.region();
    region.dailyLog[date] = [];
    CCS.Layout.save();
    this.loadDate(date);
    CCS.Toast.show('Day cleared', 'success');
  },

  // ── Export single day ─────────────────────────────────────────────────────
  exportDay() {
    const date    = document.getElementById('dailyDate')?.value;
    const entries = CCS.DB.entriesForDate(date);
    if (!entries.length) return CCS.Toast.show('No entries to export', 'warning');
    CCS.Excel.exportSheet(
      entries.map(e => ({
        Date: CCS.fmt.date(date),
        Technician: e.technician,
        'Order No':     e.orderNo,
        'Allocated (L)': e.allocated,
        'Supplied (L)':  e.supplied,
        Balance: ((e.allocated || 0) - (e.supplied || 0)).toFixed(1),
        Notes: e.notes || '',
      })),
      `CCS_Daily_${date}`, 'Daily Entries'
    );
  },
};
