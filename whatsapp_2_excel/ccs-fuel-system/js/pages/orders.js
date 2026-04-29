/**
 * js/pages/orders.js
 * Orders page — create, view, allocate, close fuel orders.
 */

'use strict';

CCS.Pages = CCS.Pages || {};

CCS.Pages.Orders = {
  skeleton: () => CCS.Components.skeleton('orders'),

  async render(container) {
    const region = CCS.DB.region();
    const orders = Object.values(region?.orders || {});

    container.innerHTML = `
      <!-- Page header -->
      <div class="page-header">
        <div class="page-header-title">
          <h1>Orders</h1>
          <p>Manage fuel orders and technician allocations for ${CCS.DB.currentRegion}</p>
        </div>
        <div class="flex gap-2">
          <button class="btn btn-secondary" onclick="CCS.Excel.exportOrders()">
            <i class="fa-regular fa-file-excel"></i> Export
          </button>
          <button class="btn btn-primary" onclick="CCS.Pages.Orders.openCreateModal()">
            <i class="fa-regular fa-plus"></i> New Order
          </button>
        </div>
      </div>

      <!-- Search & filters -->
      <div class="flex gap-3 mb-5 flex-wrap">
        <input type="text" class="input-field" id="ordersSearch" placeholder="Search orders…" style="max-width:280px;"
               oninput="CCS.Pages.Orders.filter(this.value)">
        <select class="select-field" id="ordersStatusFilter" style="max-width:160px;"
                onchange="CCS.Pages.Orders.filter(document.getElementById('ordersSearch').value)">
          <option value="">All statuses</option>
          <option value="open">Open</option>
          <option value="closed">Closed</option>
          <option value="over">Over-supplied</option>
          <option value="unassigned">Unassigned</option>
        </select>
        <div style="margin-left:auto;display:flex;align-items:center;gap:8px;font-size:var(--text-sm);color:var(--neutral-500);">
          <span id="ordersCount">${orders.length} orders</span>
        </div>
      </div>

      <!-- Orders list -->
      <div id="ordersList">
        ${orders.length ? orders.map(o => this._orderCardHTML(o, region)).join('') : CCS.Components.emptyState('orders', 'Create Order', 'CCS.Pages.Orders.openCreateModal()')}
      </div>

      <!-- Create/Edit Order modal -->
      <div class="modal-overlay" id="orderModal">
        <div class="modal-container" style="max-width:560px;">
          <div class="modal-header">
            <h3 class="text-xl font-semibold" id="orderModalTitle">New Order</h3>
            <button class="btn btn-icon btn-ghost" onclick="CCS.Modal.close('orderModal')"><i class="fa-regular fa-xmark"></i></button>
          </div>
          <div class="modal-body">
            <div class="grid grid-cols-2 gap-4">
              <div class="input-group">
                <div class="input-wrapper">
                  <input type="text" class="input-field" id="orderNoInput" placeholder=" ">
                  <label class="input-label">Order Number *</label>
                </div>
              </div>
              <div class="input-group">
                <div class="input-wrapper">
                  <input type="number" class="input-field" id="orderLitresInput" placeholder=" " min="0" step="0.1">
                  <label class="input-label">Total Litres *</label>
                </div>
              </div>
              <div class="input-group">
                <div class="input-wrapper">
                  <input type="text" class="input-field" id="orderCustomerInput" placeholder=" ">
                  <label class="input-label">Customer / Site</label>
                </div>
              </div>
              <div class="input-group">
                <div class="input-wrapper">
                  <input type="date" class="input-field" id="orderDateInput">
                  <label class="input-label">Date</label>
                </div>
              </div>
            </div>
            <div class="input-group">
              <div class="input-wrapper">
                <textarea class="input-field" id="orderNotesInput" placeholder=" " rows="2"></textarea>
                <label class="input-label">Notes</label>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary" onclick="CCS.Modal.close('orderModal')">Cancel</button>
            <button class="btn btn-primary" onclick="CCS.Pages.Orders.saveOrder()">
              <i class="fa-regular fa-floppy-disk"></i> Save Order
            </button>
          </div>
        </div>
      </div>

      <!-- Allocate modal -->
      <div class="modal-overlay" id="allocateModal">
        <div class="modal-container" style="max-width:520px;">
          <div class="modal-header">
            <h3 class="text-xl font-semibold">Allocate Technicians <span id="allocateOrderNo" style="color:var(--accent-600);"></span></h3>
            <button class="btn btn-icon btn-ghost" onclick="CCS.Modal.close('allocateModal')"><i class="fa-regular fa-xmark"></i></button>
          </div>
          <div class="modal-body" id="allocateModalBody"></div>
          <div class="modal-footer">
            <button class="btn btn-secondary" onclick="CCS.Modal.close('allocateModal')">Cancel</button>
            <button class="btn btn-primary" onclick="CCS.Pages.Orders.saveAllocations()">
              <i class="fa-regular fa-floppy-disk"></i> Save Allocations
            </button>
          </div>
        </div>
      </div>`;
  },

  _orderCardHTML(o, region) {
    const supplied = o.suppliedTotal || 0;
    const pct = o.totalLiters > 0 ? (supplied / o.totalLiters) * 100 : 0;
    const nearly = pct >= 90 && pct < 100;
    const status = o.status || (Object.keys(o.allocations || {}).length === 0 ? 'unassigned' : 'open');

    const statusMap = {
      open: { cls: 'badge-success', label: 'Open', ind: 'status-open' },
      closed: { cls: 'badge-warning', label: 'Closed', ind: 'status-closed' },
      over: { cls: 'badge-danger', label: 'Over', ind: 'status-over' },
      unassigned: { cls: 'badge-neutral', label: 'Unassigned', ind: 'status-unassigned' },
    };
    const sm = statusMap[status] || statusMap.open;

    const techs = Object.entries(o.allocations || {});

    return `
      <div class="order-card${nearly ? ' nearly-full' : ''}" id="orderCard_${o.orderNo}">
        <div class="order-header" onclick="CCS.Pages.Orders.toggleCard('${o.orderNo}')">
          <div class="order-status-indicator ${sm.ind}"></div>
          <div class="order-info">
            <div class="order-title">${o.orderNo}</div>
            <div class="order-meta">
              ${o.customer ? `<span><i class="fa-regular fa-building"></i> ${o.customer}</span>` : ''}
              ${o.date ? `<span><i class="fa-regular fa-calendar"></i> ${CCS.fmt.date(o.date)}</span>` : ''}
              <span class="badge ${sm.cls}">${sm.label}</span>
              ${nearly ? '<span class="badge badge-warning"><i class="fa-regular fa-triangle-exclamation"></i> Nearly Full</span>' : ''}
            </div>
          </div>
          <div class="order-stats">
            <div style="text-align:right;">
              <div class="font-mono font-bold">${CCS.fmt.litres(supplied)} / ${CCS.fmt.litres(o.totalLiters)}</div>
              <div style="font-size:.7rem;color:var(--neutral-400);">${pct.toFixed(1)}% used</div>
            </div>
            ${CCS.Components.progressBar(pct, { label: false })}
            <i class="fa-regular fa-chevron-down order-chevron" id="chevron_${o.orderNo}"></i>
          </div>
        </div>

        <div class="order-body" id="orderBody_${o.orderNo}" style="display:none;">
          <!-- Progress detail -->
          <div class="mb-4">
            ${CCS.Components.progressBar(pct)}
            <div style="display:flex;justify-content:space-between;font-size:.75rem;color:var(--neutral-500);margin-top:4px;">
              <span>Balance: <strong>${CCS.fmt.litres(o.totalLiters - supplied)}</strong></span>
              <span>Allocated: <strong>${CCS.fmt.litres(techs.reduce((s,[,v]) => s+v, 0))}</strong></span>
            </div>
          </div>

          <!-- Technician allocations -->
          <h4 class="text-sm font-semibold mb-2" style="color:var(--neutral-600);text-transform:uppercase;letter-spacing:.05em;">Technicians</h4>
          ${techs.length ? `
            <div class="table-container mb-4">
              <table class="table">
                <thead><tr><th>Technician</th><th>Allocated</th><th>Supplied</th><th>Balance</th></tr></thead>
                <tbody>
                  ${techs.map(([tech, alloc]) => {
                    const sup = Object.values(region?.dailyLog || {}).flat()
                      .filter(e => e.orderNo === o.orderNo && e.technician === tech)
                      .reduce((s, e) => s + (e.supplied || 0), 0);
                    const bal = alloc - sup;
                    const over = bal < 0;
                    return `<tr>
                      <td><div class="flex items-center gap-2">${CCS.dom.techAvatar(tech, 'style="width:28px;height:28px;font-size:.7rem;"')}<span>${tech}</span></div></td>
                      <td class="font-mono">${CCS.fmt.litres(alloc)}</td>
                      <td class="font-mono">${CCS.fmt.litres(sup)}</td>
                      <td class="font-mono ${over ? 'badge-danger' : ''}" style="${over ? 'color:var(--status-danger);font-weight:600;' : ''}">${over ? '⚠️ ' : ''}${CCS.fmt.litres(bal)}</td>
                    </tr>`;
                  }).join('')}
                </tbody>
              </table>
            </div>` : `<p class="text-sm mb-4" style="color:var(--neutral-400);">No technicians allocated yet.</p>`}

          <!-- Actions -->
          <div class="flex gap-2 flex-wrap">
            <button class="btn btn-primary btn-sm" onclick="CCS.Pages.Orders.openAllocate('${o.orderNo}')">
              <i class="fa-regular fa-user-plus"></i> Allocate Technicians
            </button>
            <button class="btn btn-secondary btn-sm" onclick="CCS.Pages.Orders.openEdit('${o.orderNo}')">
              <i class="fa-regular fa-pen"></i> Edit
            </button>
            <button class="btn btn-secondary btn-sm" onclick="CCS.Pages.Orders.toggleStatus('${o.orderNo}')">
              <i class="fa-regular fa-circle-check"></i> ${status === 'closed' ? 'Reopen' : 'Close'} Order
            </button>
            <button class="btn btn-danger btn-sm" onclick="CCS.Pages.Orders.deleteOrder('${o.orderNo}')">
              <i class="fa-regular fa-trash"></i> Delete
            </button>
          </div>

          ${o.notes ? `<div class="mt-3 text-xs" style="color:var(--neutral-500);border-top:1px solid var(--neutral-200);padding-top:.75rem;">
            <i class="fa-regular fa-note"></i> ${o.notes}
          </div>` : ''}
        </div>
      </div>`;
  },

  // ── Card toggle ───────────────────────────────────────────────────────────
  toggleCard(orderNo) {
    const body    = document.getElementById('orderBody_' + orderNo);
    const chevron = document.getElementById('chevron_' + orderNo);
    if (!body) return;
    const open = body.style.display === 'none';
    body.style.display = open ? 'block' : 'none';
    chevron?.classList.toggle('expanded', open);
  },

  // ── Create modal ──────────────────────────────────────────────────────────
  openCreateModal() {
    this._editingOrder = null;
    document.getElementById('orderModalTitle').textContent = 'New Order';
    ['orderNoInput','orderLitresInput','orderCustomerInput','orderNotesInput'].forEach(id => {
      const el = document.getElementById(id); if (el) el.value = '';
    });
    document.getElementById('orderDateInput').value = new Date().toISOString().slice(0, 10);
    CCS.Modal.open('orderModal');
  },

  openEdit(orderNo) {
    const o = CCS.DB.order(orderNo);
    if (!o) return;
    this._editingOrder = orderNo;
    document.getElementById('orderModalTitle').textContent = 'Edit Order';
    document.getElementById('orderNoInput').value       = o.orderNo;
    document.getElementById('orderLitresInput').value   = o.totalLiters;
    document.getElementById('orderCustomerInput').value = o.customer || '';
    document.getElementById('orderDateInput').value     = o.date || '';
    document.getElementById('orderNotesInput').value    = o.notes || '';
    CCS.Modal.open('orderModal');
  },

  saveOrder() {
    const orderNo = document.getElementById('orderNoInput')?.value.trim();
    const litres  = parseFloat(document.getElementById('orderLitresInput')?.value);

    if (!orderNo) return CCS.Toast.show('Order number required', 'warning');
    if (!litres || litres <= 0) return CCS.Toast.show('Enter a valid litres amount', 'warning');

    const region = CCS.DB.region();
    if (!this._editingOrder && region.orders[orderNo]) {
      return CCS.Toast.show(`Order ${orderNo} already exists`, 'error');
    }

    const existing = this._editingOrder ? region.orders[this._editingOrder] : {};
    region.orders[orderNo] = {
      ...existing,
      orderNo,
      totalLiters:    litres,
      customer:       document.getElementById('orderCustomerInput')?.value.trim() || '',
      date:           document.getElementById('orderDateInput')?.value || new Date().toISOString().slice(0, 10),
      notes:          document.getElementById('orderNotesInput')?.value.trim() || '',
      allocations:    existing.allocations || {},
      suppliedTotal:  existing.suppliedTotal || 0,
      status:         existing.status || 'open',
      createdAt:      existing.createdAt || new Date().toISOString(),
    };

    // If editing with a new order number, remove old key
    if (this._editingOrder && this._editingOrder !== orderNo) {
      delete region.orders[this._editingOrder];
    }

    CCS.Layout.save();
    CCS.Modal.close('orderModal');
    CCS.Toast.show(this._editingOrder ? 'Order updated' : 'Order created', 'success');
    CCS.Router.go('orders');
  },

  // ── Allocate modal ────────────────────────────────────────────────────────
  openAllocate(orderNo) {
    this._allocatingOrder = orderNo;
    const o      = CCS.DB.order(orderNo);
    const region = CCS.DB.region();
    const techs  = region.technicians || [];

    document.getElementById('allocateOrderNo').textContent = orderNo;

    const body = document.getElementById('allocateModalBody');
    if (!techs.length) {
      body.innerHTML = '<p style="color:var(--neutral-400);text-align:center;">No technicians in this region.</p>';
    } else {
      body.innerHTML = `
        <p class="text-sm mb-4" style="color:var(--neutral-500);">
          Set litre allocation per technician. Total order: <strong>${CCS.fmt.litres(o.totalLiters)}</strong>
        </p>
        ${techs.map(t => `
          <div class="flex items-center gap-3 mb-3">
            ${CCS.dom.techAvatar(t)}
            <span class="text-sm font-medium" style="flex:1;">${t}</span>
            <input type="number" class="input-field" id="alloc_${t.replace(/\s/g,'_')}" 
                   value="${o.allocations?.[t] || ''}" placeholder="0" min="0" step="0.1"
                   style="width:120px;padding:8px 12px;">
            <span class="text-xs" style="color:var(--neutral-400);">L</span>
          </div>`).join('')}`;
    }
    CCS.Modal.open('allocateModal');
  },

  saveAllocations() {
    const orderNo = this._allocatingOrder;
    const o       = CCS.DB.order(orderNo);
    const region  = CCS.DB.region();
    const techs   = region.technicians || [];

    const allocations = {};
    let totalAlloc = 0;
    for (const t of techs) {
      const val = parseFloat(document.getElementById('alloc_' + t.replace(/\s/g,'_'))?.value || 0);
      if (val > 0) { allocations[t] = val; totalAlloc += val; }
    }

    if (totalAlloc > o.totalLiters) {
      return CCS.Toast.show(`Total allocations (${CCS.fmt.litres(totalAlloc)}) exceed order size (${CCS.fmt.litres(o.totalLiters)})`, 'warning');
    }

    o.allocations = allocations;
    CCS.Layout.save();
    CCS.Modal.close('allocateModal');
    CCS.Toast.show('Allocations saved', 'success');
    CCS.Router.go('orders');
  },

  // ── Status toggle ─────────────────────────────────────────────────────────
  toggleStatus(orderNo) {
    const o = CCS.DB.order(orderNo);
    if (!o) return;
    o.status = o.status === 'closed' ? 'open' : 'closed';
    CCS.Layout.save();
    CCS.Toast.show(`Order ${orderNo} ${o.status}`, 'success');
    CCS.Router.go('orders');
  },

  // ── Delete ────────────────────────────────────────────────────────────────
  async deleteOrder(orderNo) {
    const confirmed = await CCS.Components.confirm(
      `Delete order <strong>${orderNo}</strong>? This will also remove all associated daily entries.`,
      { title: 'Delete Order', danger: true, okLabel: 'Delete' }
    );
    if (!confirmed) return;
    const region = CCS.DB.region();
    delete region.orders[orderNo];
    // Clean daily log
    Object.keys(region.dailyLog).forEach(date => {
      region.dailyLog[date] = (region.dailyLog[date] || []).filter(e => e.orderNo !== orderNo);
    });
    CCS.Layout.save();
    CCS.Toast.show('Order deleted', 'success');
    CCS.Router.go('orders');
  },

  // ── Filter ────────────────────────────────────────────────────────────────
  filter(query) {
    const q      = (query || '').toLowerCase();
    const status = document.getElementById('ordersStatusFilter')?.value || '';
    const region = CCS.DB.region();
    const orders = Object.values(region?.orders || {});

    const filtered = orders.filter(o => {
      const s = o.status || (Object.keys(o.allocations || {}).length === 0 ? 'unassigned' : 'open');
      const matchQuery  = !q || o.orderNo.toLowerCase().includes(q) || (o.customer || '').toLowerCase().includes(q);
      const matchStatus = !status || s === status;
      return matchQuery && matchStatus;
    });

    document.getElementById('ordersCount').textContent = `${filtered.length} of ${orders.length} orders`;
    const list = document.getElementById('ordersList');
    if (!list) return;
    list.innerHTML = filtered.length
      ? filtered.map(o => this._orderCardHTML(o, region)).join('')
      : '<div class="empty-state"><p>No orders match your filter.</p></div>';
  },
};
