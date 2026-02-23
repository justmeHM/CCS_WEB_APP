/**
 * orders.js — Orders Module
 * Covers: create orders, fuel allocation, rendering order cards,
 * order date editing, deletion, overage comments, and clone modal.
 */

import { DB, save } from './db.js';
import { updateOrderCounter } from './ui.js';

/* ── Populate selects ───────────────────────────────────────── */

export function populateAllocOrder() {
  const sel = document.getElementById('allocOrder');
  sel.innerHTML = '<option value="">— Select Order —</option>';
  Object.values(DB.regions[DB.currentRegion].orders)
    .filter(o => o.status === 'OPEN')
    .forEach(o => {
      const opt = document.createElement('option');
      opt.value = o.orderNo;
      opt.textContent = `${o.orderNo} (${o.vehiclePlate})`;
      sel.appendChild(opt);
    });
}

export function populateAllocTech() {
  const sel = document.getElementById('allocTech');
  sel.innerHTML = '<option value="">— Select Technician —</option>';
  DB.regions[DB.currentRegion].technicians.forEach(t => {
    const opt = document.createElement('option');
    opt.value = t; opt.textContent = t; sel.appendChild(opt);
  });
}

/* ── Create order ───────────────────────────────────────────── */

export function createOrder() {
  const r  = DB.currentRegion;
  const no = document.getElementById('orderNo').value.trim();
  if (!no || DB.regions[r].orders[no]) return alert('Invalid or duplicate order number');

  const orderDate = document.getElementById('orderDate').value || new Date().toISOString().split('T')[0];

  DB.regions[r].orders[no] = {
    orderNo:       no,
    vehiclePlate:  document.getElementById('vehiclePlate').value.trim(),
    totalLiters:   +document.getElementById('totalLiters').value,
    suppliedTotal: 0,
    allocations:   {},
    status:        'OPEN',
    createdDate:   orderDate
  };

  ['orderNo', 'vehiclePlate', 'totalLiters', 'orderDate'].forEach(id => {
    document.getElementById(id).value = '';
  });

  save(); populateAllocOrder(); renderOrders();
}

/* ── Allocate fuel ──────────────────────────────────────────── */

export function allocateFuel() {
  const r        = DB.currentRegion;
  const orderKey = document.getElementById('allocOrder').value;
  const o        = DB.regions[r].orders[orderKey];
  const t        = document.getElementById('allocTech').value;
  const amt      = +document.getElementById('allocAmount').value;
  if (!o || !t || !amt) return alert('Fill in all allocation fields');
  if (o.allocations[t]) return alert(`${t} already has an allocation on this order`);
  const used = Object.values(o.allocations).reduce((a, b) => a + b, 0);
  if (used + amt > o.totalLiters) return alert('Allocation exceeds order total litres');
  o.allocations[t] = amt;
  document.getElementById('allocAmount').value = '';
  document.getElementById('allocInfo').textContent = `✅ ${amt}L allocated to ${t} on order ${o.orderNo}`;
  save();
}

/* ── Filter & date helpers ──────────────────────────────────── */

export function clearOrderFilter() {
  document.getElementById('orderFilterFrom').value = '';
  document.getElementById('orderFilterTo').value   = '';
  const tf = document.getElementById('orderFilterTech');
  if (tf) tf.value = '';
  renderOrders();
}

/* ── Render orders ──────────────────────────────────────────── */

export function renderOrders() {
  const container = document.getElementById('ordersBody');
  container.innerHTML = '';
  const region = DB.regions[DB.currentRegion];
  let orders   = Object.values(region.orders);

  // Filters
  const from       = document.getElementById('orderFilterFrom')?.value;
  const to         = document.getElementById('orderFilterTo')?.value;
  const techFilter = document.getElementById('orderFilterTech')?.value;
  if (from) orders = orders.filter(o => o.createdDate >= from);
  if (to)   orders = orders.filter(o => o.createdDate <= to);
  if (techFilter) orders = orders.filter(o => Object.keys(o.allocations || {}).includes(techFilter));

  // Repopulate tech filter dropdown
  const tf = document.getElementById('orderFilterTech');
  if (tf) {
    const prev = tf.value;
    tf.innerHTML = '<option value="">All Technicians</option>';
    region.technicians.forEach(t => {
      const opt = document.createElement('option');
      opt.value = t; opt.textContent = t; tf.appendChild(opt);
    });
    tf.value = prev;
  }

  if (!orders.length) {
    container.innerHTML = '<div class="empty">No orders yet. Create one above.</div>';
    save(); populateAllocOrder(); updateOrderCounter(); return;
  }

  orders.forEach(o => {
    const card = _buildOrderCard(o, region);
    container.appendChild(card);
  });

  save(); populateAllocOrder(); updateOrderCounter();
}

function _buildOrderCard(o, region) {
  const bal        = o.totalLiters - o.suppliedTotal;
  if (bal <= 0 && o.status !== 'CLOSED') o.status = 'CLOSED';

  const today       = new Date();
  const created     = o.createdDate ? new Date(o.createdDate + 'T00:00:00') : null;
  const daysOpen    = created ? Math.floor((today - created) / 86400000) : 0;
  const pctSupplied = o.totalLiters > 0 ? (o.suppliedTotal / o.totalLiters) : 1;
  const isStale     = o.status === 'OPEN' && daysOpen > 7 && pctSupplied < 0.5;

  // Per-technician supply totals from daily log
  const techSupply = {};
  Object.values(region.dailyLog).flat()
    .filter(e => e.orderNo === o.orderNo)
    .forEach(e => { techSupply[e.technician] = (techSupply[e.technician] || 0) + e.supplied; });

  const anyOver     = Object.entries(o.allocations).some(([t, alloc]) => (techSupply[t] || 0) > alloc);
  const headerClass = anyOver ? 'over-order' : o.status === 'OPEN' ? 'open-order' : 'closed-order';
  const badgeHtml   = o.status === 'OPEN'
    ? `<span class="badge badge-open">OPEN</span>`
    : `<span class="badge badge-closed">CLOSED</span>`;
  const staleBadge  = isStale ? `<span class="badge-stale">⏰ STALE ${daysOpen}d</span>` : '';
  const staleBanner = isStale
    ? `<div class="stale-banner">⏰ This order has been open for <strong>${daysOpen} days</strong> with only <strong>${Math.round(pctSupplied * 100)}%</strong> supplied. Consider following up.</div>`
    : '';

  const techEntries  = Object.entries(o.allocations);
  const techRowsHtml = techEntries.length
    ? techEntries.map(([tech, allocAmt]) => _buildTechAllocRow(tech, allocAmt, o, techSupply, region)).join('')
    : '<div class="no-alloc-note">No technicians allocated yet</div>';

  const creationDateDisplay = o.createdDate
    ? new Date(o.createdDate).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
    : '—';

  const progColor = pctSupplied >= 1 ? '#d97706' : pctSupplied >= 0.75 ? '#16a34a' : pctSupplied >= 0.4 ? '#2563eb' : '#dc2626';
  const progPct   = Math.min(100, Math.round(pctSupplied * 100));

  const card = document.createElement('div');
  card.className = 'order-card';
  card.id = `ocard_${o.orderNo}`;
  card.innerHTML = `
    <div class="order-card-header ${headerClass}" onclick="App.toggleOrderCard('${o.orderNo}')">
      <div class="order-card-info">
        <div class="order-card-no">${o.orderNo} ${anyOver ? '<span class="badge-over" style="font-size:0.6rem;">⚠️ OVERAGE</span>' : ''}${staleBadge}</div>
        <div class="order-card-sub">🚗 ${o.vehiclePlate} · ${techEntries.length} tech${techEntries.length !== 1 ? 's' : ''} allocated</div>
      </div>
      <div class="order-card-right">
        ${badgeHtml}
        <span class="order-litres" style="color:${bal < 0 ? 'var(--red)' : bal === 0 ? '#d97706' : '#15803d'}">${o.suppliedTotal}/${o.totalLiters}L</span>
      </div>
      <span class="order-chevron" id="chev_${o.orderNo}">▼</span>
    </div>
    <div class="order-card-body" id="obody_${o.orderNo}">
      ${staleBanner}
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-bottom:12px;text-align:center;">
        <div><div class="field-label">Total</div><div class="info-val" style="color:#2563eb;">${o.totalLiters}L</div></div>
        <div><div class="field-label">Supplied</div><div class="info-val" style="color:#15803d;">${o.suppliedTotal}L</div></div>
        <div><div class="field-label">Balance</div><div class="info-val" style="color:${bal < 0 ? 'var(--red)' : 'var(--muted)'};">${bal}L</div></div>
      </div>
      <div class="order-progress-label">
        <span>⛽ Fulfilment Progress</span>
        <span class="pct" style="color:${progColor}">${progPct}%</span>
      </div>
      <div class="order-progress-wrap">
        <div class="order-progress-bar" style="width:${progPct}%;background:${progColor};"></div>
      </div>
      <div class="field-label" style="margin-bottom:8px;">Allocated Technicians</div>
      ${techRowsHtml}
      <div style="margin-top:12px;padding-top:10px;border-top:1px dashed #e2e8f0;">
        <div style="display:flex;align-items:center;gap:8px;justify-content:space-between;">
          <div style="font-size:0.82rem;color:var(--muted);">Created:</div>
          <div style="display:flex;align-items:center;gap:6px;">
            <span id="createdDate_${o.orderNo}" style="font-weight:600;">${creationDateDisplay}</span>
            <button class="edit-btn btn-sm" onclick="App.toggleEditOrderDate('${o.orderNo}')">✏️</button>
          </div>
        </div>
        <div id="dateEditRow_${o.orderNo}" style="display:none;margin-top:8px;">
          <input type="date" id="editDateInput_${o.orderNo}" value="${o.createdDate || ''}" style="width:160px;" />
          <div style="margin-top:6px;display:flex;gap:8px;">
            <button class="btn btn-green btn-sm" onclick="App.saveOrderDate('${o.orderNo}')">Save</button>
            <button class="btn btn-ghost btn-sm" onclick="App.cancelOrderDateEdit('${o.orderNo}')">Cancel</button>
          </div>
        </div>
      </div>
      <div class="order-card-footer">
        <span style="font-size:0.75rem;color:var(--muted);">Order #${o.orderNo}</span>
        <div style="display:flex;gap:6px;">
          <button class="edit-btn" style="font-size:0.78rem;padding:4px 10px;" onclick="App.openCloneModal('${o.orderNo}')">📋 Clone</button>
          <button class="del-btn" onclick="App.deleteOrder('${o.orderNo}')">🗑 Delete</button>
        </div>
      </div>
    </div>`;
  return card;
}

function _buildTechAllocRow(tech, allocAmt, o, techSupply, region) {
  const supplied    = techSupply[tech] || 0;
  const techBal     = allocAmt - supplied;
  const isOver      = supplied > allocAmt;
  const overage     = supplied - allocAmt;
  const techPlate   = region.technicianPlates[tech] || '—';
  const overComment = (o.overageComments && o.overageComments[tech]) || '';
  const overBadge   = isOver ? `<span class="badge-over">⚠️ OVER +${overage.toFixed(1)}L</span>` : '';
  const overCmt     = isOver && overComment ? `<div class="over-comment">💬 ${overComment}</div>` : '';
  const editOverBtn = isOver
    ? `<button class="edit-btn" style="font-size:0.72rem;padding:3px 7px;" onclick="App.openOverageComment('${o.orderNo}','${tech}')">✏️ Comment</button>`
    : '';

  return `
    <div class="alloc-row">
      <div class="alloc-row-info">
        <div class="alloc-tech-name">${tech} ${overBadge}</div>
        <div class="alloc-tech-plate">🚗 ${techPlate}</div>
        <div class="alloc-stats">
          <span class="alloc-stat stat-alloc">Alloc: ${allocAmt}L</span>
          <span class="alloc-stat stat-supply">Supplied: ${supplied}L</span>
          <span class="alloc-stat ${isOver ? 'stat-over' : 'stat-bal'}">
            ${isOver ? 'Over: +' + overage.toFixed(1) + 'L' : 'Bal: ' + Math.max(0, techBal) + 'L'}
          </span>
        </div>
        ${overCmt}
        <div class="alloc-edit-row" id="allocEditRow_${o.orderNo}_${tech}" style="display:none;">
          <input type="number" class="alloc-edit-input" id="allocEditInput_${o.orderNo}_${tech}" value="${allocAmt}" min="0" step="0.1" placeholder="New amount" />
          <button class="btn btn-green btn-sm" onclick="App.saveAllocEdit('${o.orderNo}','${tech}')">Save</button>
          <button class="btn btn-ghost btn-sm" onclick="App.cancelAllocEdit('${o.orderNo}','${tech}')">✕</button>
        </div>
      </div>
      <div style="flex-shrink:0;display:flex;flex-direction:column;gap:4px;align-items:flex-end;">
        ${editOverBtn}
        <button class="edit-btn" style="font-size:0.72rem;padding:3px 7px;" onclick="App.toggleAllocEdit('${o.orderNo}','${tech}')">✏️ Edit Alloc</button>
      </div>
    </div>`;
}

/* ── Order card toggle ──────────────────────────────────────── */

export function toggleOrderCard(orderNo) {
  document.getElementById(`obody_${orderNo}`)?.classList.toggle('expanded');
  document.getElementById(`chev_${orderNo}`)?.classList.toggle('expanded');
}

/* ── Order date editing ─────────────────────────────────────── */

export function toggleEditOrderDate(orderNo) {
  document.getElementById(`createdDate_${orderNo}`).style.display = 'none';
  document.getElementById(`dateEditRow_${orderNo}`).style.display = 'block';
}

export function cancelOrderDateEdit(orderNo) {
  document.getElementById(`createdDate_${orderNo}`).style.display = 'inline';
  document.getElementById(`dateEditRow_${orderNo}`).style.display = 'none';
}

export function saveOrderDate(orderNo) {
  const o = DB.regions[DB.currentRegion].orders[orderNo];
  if (!o) return;
  const newDate = document.getElementById(`editDateInput_${orderNo}`).value.trim();
  if (!newDate) return alert('Please select a date');
  o.createdDate = newDate;
  const disp = document.getElementById(`createdDate_${orderNo}`);
  disp.textContent = new Date(newDate).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });
  disp.style.display = 'inline';
  document.getElementById(`dateEditRow_${orderNo}`).style.display = 'none';
  save(); renderOrders();
}

/* ── Delete order ───────────────────────────────────────────── */

export function deleteOrder(orderNo) {
  const r = DB.currentRegion;
  const o = DB.regions[r].orders[orderNo];
  if (!o) return;
  const label = o.suppliedTotal > 0
    ? `⚠️ Order "${orderNo}" has ${o.suppliedTotal}L already supplied. Deleting will remove all its data. Continue?`
    : `Delete order "${orderNo}"?`;
  if (!confirm(label)) return;
  delete DB.regions[r].orders[orderNo];
  Object.keys(DB.regions[r].dailyLog).forEach(date => {
    DB.regions[r].dailyLog[date] = DB.regions[r].dailyLog[date].filter(e => e.orderNo !== orderNo);
  });
  save(); renderOrders();
}

/* ── Allocation inline editing ──────────────────────────────── */

export function toggleAllocEdit(orderNo, tech) {
  const row = document.getElementById(`allocEditRow_${orderNo}_${tech}`);
  if (row) row.style.display = row.style.display === 'none' ? 'flex' : 'none';
}

export function cancelAllocEdit(orderNo, tech) {
  const row = document.getElementById(`allocEditRow_${orderNo}_${tech}`);
  if (row) row.style.display = 'none';
}

export function saveAllocEdit(orderNo, tech) {
  const o = DB.regions[DB.currentRegion].orders[orderNo];
  if (!o) return;
  const input  = document.getElementById(`allocEditInput_${orderNo}_${tech}`);
  const newAmt = parseFloat(input.value);
  if (isNaN(newAmt) || newAmt < 0) return alert('Please enter a valid amount');
  const otherAllocs = Object.entries(o.allocations).filter(([t]) => t !== tech).reduce((s, [, v]) => s + v, 0);
  if (otherAllocs + newAmt > o.totalLiters) {
    return alert(`⚠️ Total allocations (${otherAllocs + newAmt}L) would exceed order total (${o.totalLiters}L)`);
  }
  o.allocations[tech] = newAmt;
  save(); renderOrders();
}

/* ── Overage comments ───────────────────────────────────────── */

let _overCtx = null;

export function openOverageComment(orderNo, tech) {
  const o = DB.regions[DB.currentRegion].orders[orderNo];
  if (!o) return;
  _overCtx = { orderNo, tech };
  const alloc    = o.allocations[tech] || 0;
  const supplied = Object.values(DB.regions[DB.currentRegion].dailyLog).flat()
    .filter(e => e.orderNo === orderNo && e.technician === tech)
    .reduce((s, e) => s + e.supplied, 0);
  const over = supplied - alloc;
  document.getElementById('overageModalMeta').innerHTML =
    `<strong>${tech}</strong> supplied <span style="color:var(--red);font-weight:700;">${supplied}L</span> against allocation of <strong>${alloc}L</strong> — overage of <span style="color:var(--red);font-weight:700;">+${over.toFixed(1)}L</span>`;
  document.getElementById('overageCommentInput').value = (o.overageComments && o.overageComments[tech]) || '';
  document.getElementById('overageModal').classList.remove('hidden');
  setTimeout(() => document.getElementById('overageCommentInput').focus(), 100);
}

export function closeOverageModal(e) {
  if (e && e.target !== document.getElementById('overageModal')) return;
  document.getElementById('overageModal').classList.add('hidden');
  _overCtx = null;
}

export function saveOverageComment() {
  if (!_overCtx) return;
  const { orderNo, tech } = _overCtx;
  const comment = document.getElementById('overageCommentInput').value.trim();
  if (!comment) {
    document.getElementById('overageCommentInput').style.borderColor = 'var(--red)';
    return alert('Please enter a reason for the overage');
  }
  const o = DB.regions[DB.currentRegion].orders[orderNo];
  if (!o.overageComments) o.overageComments = {};
  o.overageComments[tech] = comment;
  save();
  document.getElementById('overageModal').classList.add('hidden');
  _overCtx = null;
  renderOrders();
}

/* ── Clone order modal ──────────────────────────────────────── */

let _cloneSourceOrderNo = null;

export function openCloneModal(orderNo) {
  const o = DB.regions[DB.currentRegion].orders[orderNo];
  if (!o) return;
  _cloneSourceOrderNo = orderNo;
  const techCount  = Object.keys(o.allocations).length;
  const totalAlloc = Object.values(o.allocations).reduce((s, v) => s + v, 0);
  document.getElementById('clonePreview').innerHTML = `
    <div style="margin-bottom:6px;"><strong>${o.orderNo}</strong> → 🚗 ${o.vehiclePlate}</div>
    <div style="color:var(--muted);font-size:0.78rem;">📦 ${o.totalLiters}L total · 👥 ${techCount} technician${techCount !== 1 ? 's' : ''} · 🔗 ${totalAlloc}L allocated</div>
    <div style="color:var(--muted);font-size:0.78rem;margin-top:4px;">Supply history starts fresh at 0L on the new order.</div>`;
  document.getElementById('cloneNewOrderNo').value   = '';
  document.getElementById('cloneNewOrderDate').value = new Date().toISOString().slice(0, 10);
  document.getElementById('cloneModal').classList.remove('hidden');
  setTimeout(() => document.getElementById('cloneNewOrderNo').focus(), 120);
}

export function closeCloneModal(e) {
  if (e && e.target !== document.getElementById('cloneModal')) return;
  document.getElementById('cloneModal').classList.add('hidden');
  _cloneSourceOrderNo = null;
}

export function confirmClone() {
  const region = DB.regions[DB.currentRegion];
  const src    = region.orders[_cloneSourceOrderNo];
  if (!src) return;
  const newNo = document.getElementById('cloneNewOrderNo').value.trim();
  if (!newNo) {
    document.getElementById('cloneNewOrderNo').style.borderColor = 'var(--red)';
    return alert('Please enter a new order number');
  }
  if (region.orders[newNo]) return alert(`⚠️ Order "${newNo}" already exists in this region`);
  const newDate = document.getElementById('cloneNewOrderDate').value || new Date().toISOString().slice(0, 10);
  region.orders[newNo] = {
    orderNo:       newNo,
    vehiclePlate:  src.vehiclePlate,
    totalLiters:   src.totalLiters,
    suppliedTotal: 0,
    allocations:   { ...src.allocations },
    status:        'OPEN',
    createdDate:   newDate
  };
  save();
  document.getElementById('cloneModal').classList.add('hidden');
  _cloneSourceOrderNo = null;
  renderOrders();
  populateAllocOrder();
  alert(`✅ Order "${newNo}" created — 🚗 ${src.vehiclePlate}, ${src.totalLiters}L, ${Object.keys(src.allocations).length} allocation${Object.keys(src.allocations).length !== 1 ? 's' : ''} copied.`);
}