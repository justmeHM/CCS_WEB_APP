/**
 * daily.js — Daily Supply Log
 * Covers: add/save/edit/delete daily entries, log view, history,
 * daily summary modal, and accordion toggling.
 */

import { DB, save } from './db.js';
import { renderOrders, openOverageComment } from './orders.js';
import { updateOrderCounter } from './ui.js';

/* ── Accordion ──────────────────────────────────────────────── */

export function toggleAccordion(key) {
  const body = document.getElementById(`acc-${key}-body`);
  const chev = document.getElementById(`acc-${key}-chev`);
  const hdr  = document.getElementById(`acc-${key}-hdr`);
  if (!body) return;
  const isOpen = body.classList.contains('open');
  body.classList.toggle('open', !isOpen);
  if (chev) chev.classList.toggle('open', !isOpen);
  if (hdr)  hdr.classList.toggle('open', !isOpen);
}

/* ── Load / render ──────────────────────────────────────────── */

export function loadDailyLog() {
  const d = document.getElementById('dailyDate').value;
  document.getElementById('dailyEntries').innerHTML = '';
  ['add'].forEach(k => {
    ['body', 'chev', 'hdr'].forEach(part => {
      document.getElementById(`acc-${k}-${part}`)?.classList.remove('open');
    });
  });
  renderLogView(d);
  renderDailyHistory();
}

export function renderLogView(d) {
  const region  = DB.regions[DB.currentRegion];
  const logCard = document.getElementById('logViewCard');
  const body    = document.getElementById('logViewBody');
  const entries = (d && region.dailyLog[d]) ? region.dailyLog[d] : [];

  // Day stat row
  const todayRow = document.getElementById('todayStatRow');
  if (d && entries.length) {
    const allocTotal   = entries.filter(e => !e.unallocated).reduce((s, e) => s + e.supplied, 0);
    const unallocTotal = entries.filter(e =>  e.unallocated).reduce((s, e) => s + e.supplied, 0);
    const dayTotal     = allocTotal + unallocTotal;
    document.getElementById('todayStatDate').textContent   = d;
    document.getElementById('dayStAlloc').textContent      = allocTotal + 'L';
    document.getElementById('dayStUnalloc').textContent    = unallocTotal + 'L';
    document.getElementById('dayStTotal').textContent      = dayTotal + 'L';
    todayRow.style.display = 'block';
  } else {
    todayRow.style.display = 'none';
  }

  if (!d || !entries.length) { logCard.style.display = 'none'; return; }
  logCard.style.display = 'block';

  const countEl = document.getElementById('logEntryCount');
  if (countEl) countEl.textContent = `(${entries.length} entr${entries.length !== 1 ? 'ies' : 'y'})`;

  body.innerHTML = '';

  entries.forEach((entry, idx) => {
    const order   = entry.orderNo ? region.orders[entry.orderNo] : null;
    const row     = document.createElement('div');
    row.className = 'log-entry' + (entry.unallocated ? ' unalloc-entry' : '');

    const badgeHtml = entry.unallocated
      ? `<span class="badge badge-unalloc" style="font-size:0.62rem;padding:2px 7px;border-radius:999px;font-family:Rajdhani,sans-serif;font-weight:700;margin-left:4px;">UNALLOC</span>`
      : '';
    const metaHtml = entry.unallocated
      ? `<div class="log-meta">No order assigned${badgeHtml}</div>${entry.comment ? `<div class="log-comment">💬 ${entry.comment}</div>` : ''}`
      : `<div class="log-meta">Order: <strong>${entry.orderNo}</strong>${order ? ' · ' + order.vehiclePlate : ''}</div>`;

    row.innerHTML = `
      <div class="log-info">
        <div class="log-tech">${entry.technician}</div>${metaHtml}
      </div>
      <div class="log-litres" style="color:${entry.unallocated ? '#d97706' : '#15803d'}">${entry.supplied} L</div>
      <button class="edit-btn" onclick="App.openEditModal('${d}', ${idx})" title="Edit">✏️</button>
      <button class="del-btn"  onclick="App.deleteDailyEntry('${d}', ${idx})" title="Delete">🗑</button>`;
    body.appendChild(row);
  });

  // Totals row
  const dayTotal     = entries.reduce((s, e) => s + e.supplied, 0);
  const allocTotal   = entries.filter(e => !e.unallocated).reduce((s, e) => s + e.supplied, 0);
  const unallocTotal = entries.filter(e =>  e.unallocated).reduce((s, e) => s + e.supplied, 0);
  const totRow = document.createElement('div');
  totRow.style.cssText = 'padding:8px 4px 2px;font-family:Rajdhani,sans-serif;font-weight:700;font-size:0.82rem;color:var(--muted);display:flex;justify-content:flex-end;gap:16px;flex-wrap:wrap;border-top:1px solid var(--border);margin-top:6px;padding-top:8px;';
  totRow.innerHTML = `
    <span style="color:#15803d;">Allocated: ${allocTotal} L</span>
    ${unallocTotal > 0 ? `<span style="color:#d97706;">Unallocated: ${unallocTotal} L</span>` : ''}
    <span style="color:var(--text);font-weight:700;">Day total: ${dayTotal} L</span>`;
  body.appendChild(totRow);

  // Open the saved-entries accordion automatically
  const accBody = document.getElementById('acc-log-body');
  const accChev = document.getElementById('acc-log-chev');
  const accHdr  = document.getElementById('acc-log-hdr');
  if (accBody && !accBody.classList.contains('open')) {
    accBody.classList.add('open');
    if (accChev) accChev.classList.add('open');
    if (accHdr)  accHdr.classList.add('open');
  }
}

export function renderDailyHistory() {
  const region = DB.regions[DB.currentRegion];
  const el     = document.getElementById('dailyHistoryBody');
  if (!el) return;
  el.innerHTML = '';

  const dates = Object.keys(region.dailyLog).sort((a, b) => b.localeCompare(a));
  if (!dates.length) { el.innerHTML = '<div class="log-empty">No supply history yet.</div>'; return; }

  const today    = new Date().toISOString().slice(0, 10);
  const toShow   = dates.filter(d => d === today);
  const display  = toShow.length > 0 ? toShow : [dates[0]];

  display.forEach(date => {
    const entries = region.dailyLog[date];

    // Summarise per technician
    const techSummaries = {};
    entries.forEach(e => {
      if (!techSummaries[e.technician]) {
        techSummaries[e.technician] = { technician: e.technician, supplied: 0, orderNo: e.orderNo || '—', balance: 0 };
      }
      techSummaries[e.technician].supplied += e.supplied;
    });
    Object.values(techSummaries).forEach(ts => {
      if (ts.orderNo !== '—') {
        const order = region.orders[ts.orderNo];
        if (order) ts.balance = order.totalLiters - order.suppliedTotal;
      }
    });

    const dateObj = new Date(date + 'T00:00:00');
    const dateStr = dateObj.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });
    const card    = document.createElement('div');
    card.className = 'daily-summary-card';
    card.onclick   = () => {
      document.getElementById('dailyDate').value = date;
      loadDailyLog();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    const fieldsHtml = Object.values(techSummaries).map(ts => `
      <div class="dsc-field"><div class="dsc-label">👤 Technician</div><div class="dsc-value tech">${ts.technician}</div></div>
      <div class="dsc-field"><div class="dsc-label">📄 Order No</div><div class="dsc-value order">${ts.orderNo}</div></div>
      <div class="dsc-field"><div class="dsc-label">⛽ Supplied</div><div class="dsc-value supplied">${ts.supplied}L</div></div>
      <div class="dsc-field"><div class="dsc-label">⚖️ Balance</div><div class="dsc-value balance">${ts.balance}L</div></div>`).join('');

    card.innerHTML = `
      <div class="dsc-header">
        <div class="dsc-date">📅 ${dateStr}</div>
        <div class="dsc-count">${entries.length} ENTR${entries.length !== 1 ? 'IES' : 'Y'}</div>
      </div>
      <div class="dsc-grid">${fieldsHtml}</div>`;
    el.appendChild(card);
  });
}

/* ── Add entry card ─────────────────────────────────────────── */

export function addDailyEntry() {
  const region    = DB.regions[DB.currentRegion];
  const container = document.getElementById('dailyEntries');
  const id        = 'entry_' + Date.now();
  const card      = document.createElement('div');
  card.className  = 'entry-card';
  card.id         = id;

  let techOpts = '<option value="">— Select Technician —</option>';
  region.technicians.forEach(t => { techOpts += `<option value="${t}">${t}</option>`; });

  card.innerHTML = `
    <button class="remove-btn" onclick="document.getElementById('${id}').remove()">✕ Remove</button>
    <div class="info-block" style="margin-top:4px;">
      <div class="field-label">Technician</div>
      <select class="tech-sel" onchange="App.techSelected(this)">${techOpts}</select>
    </div>
    <div class="grid2" style="margin-bottom:4px;">
      <div class="info-block"><div class="field-label">Order No</div><div class="info-val order-no-val" style="color:#2563eb;">—</div></div>
      <div class="info-block"><div class="field-label">Order Vehicle</div><div class="info-val order-plate-val" style="color:#2563eb;">—</div></div>
    </div>
    <div class="grid2" style="margin-bottom:4px;">
      <div class="info-block"><div class="field-label">Tech Vehicle</div><div class="info-val tech-plate-val" style="color:var(--red);">—</div></div>
      <div class="info-block"><div class="field-label">Allocated</div><div class="info-val alloc-val" style="color:#2563eb;">—</div></div>
    </div>
    <div class="grid2" style="margin-bottom:4px;">
      <div class="info-block"><div class="field-label">Supplied So Far</div><div class="info-val used-val" style="color:#dc2626;">—</div></div>
      <div class="info-block"><div class="field-label">Remaining</div><div class="info-val left-val" style="color:#15803d;">—</div></div>
    </div>
    <hr class="divider"/>
    <div class="info-block">
      <div class="field-label">Litres Supplied Now</div>
      <input type="number" class="supp-input" placeholder="Enter litres" min="0" step="0.1" />
    </div>
    <div class="warn no-alloc-warn" style="display:none;"></div>`;
  container.appendChild(card);
}

/* ── Tech selection logic ───────────────────────────────────── */

export function techSelected(sel) {
  const card   = sel.closest('.entry-card');
  const tech   = sel.value;
  const region = DB.regions[DB.currentRegion];

  const reset = () => {
    ['order-no-val','order-plate-val','tech-plate-val','alloc-val','used-val','left-val']
      .forEach(c => card.querySelector('.' + c).textContent = '—');
    card.querySelector('.supp-input').max = '';
    card.querySelector('.supp-input').value = '';
    card.querySelector('.no-alloc-warn').style.display = 'none';
    card.querySelector('.unalloc-section')?.remove();
    card.querySelector('.unalloc-banner') && (card.querySelector('.unalloc-banner').style.display = 'none');
    card.querySelector('.order-dropdown')?.remove();
    card.classList.remove('unalloc');
    card.removeAttribute('data-order');
    card.removeAttribute('data-unallocated');
  };

  if (!tech) { reset(); return; }

  card.querySelector('.tech-plate-val').textContent = region.technicianPlates[tech] || '—';

  const assignedOrders = Object.values(region.orders).filter(
    o => o.status === 'OPEN' && Object.prototype.hasOwnProperty.call(o.allocations, tech)
  );

  if (assignedOrders.length === 0) {
    // No allocation — mark as unallocated
    card.classList.add('unalloc');
    card.setAttribute('data-unallocated', 'true');
    card.removeAttribute('data-order');
    card.querySelector('.order-no-val').textContent = 'None';
    ['order-plate-val','alloc-val','used-val','left-val'].forEach(c => card.querySelector('.' + c).textContent = '—');
    card.querySelector('.supp-input').removeAttribute('max');

    let banner = card.querySelector('.unalloc-banner');
    if (!banner) {
      banner = document.createElement('div');
      banner.className = 'unalloc-banner';
      banner.innerHTML = '⚠️ No open order allocation — entry will be logged as <strong>unallocated</strong>';
      card.querySelector('.divider').insertAdjacentElement('afterend', banner);
    }
    banner.style.display = 'flex';

    let ua = card.querySelector('.unalloc-section');
    if (!ua) {
      ua = document.createElement('div');
      ua.className = 'unalloc-section info-block';
      ua.innerHTML = `<div class="field-label" style="margin-top:8px;">Comment / Reason <span style="color:var(--red);">*</span></div><input type="text" class="comment-input" placeholder="e.g. Emergency top-up, awaiting order" />`;
      card.appendChild(ua);
    }
    ua.style.display = 'block';
    card.querySelector('.no-alloc-warn').style.display = 'none';
    return;
  }

  card.classList.remove('unalloc');
  card.removeAttribute('data-unallocated');
  card.querySelector('.unalloc-section') && (card.querySelector('.unalloc-section').style.display = 'none');
  card.querySelector('.unalloc-banner') && (card.querySelector('.unalloc-banner').style.display = 'none');
  card.querySelector('.no-alloc-warn').style.display = 'none';

  if (assignedOrders.length === 1) {
    updateOrderDetails(card, assignedOrders[0], tech, region);
  } else {
    card.querySelector('.order-no-val').textContent    = `${assignedOrders.length} orders`;
    card.querySelector('.order-plate-val').textContent = '—';
    card.querySelector('.alloc-val').textContent       = '—';
    card.querySelector('.used-val').textContent        = '—';
    card.querySelector('.left-val').textContent        = '—';

    let dropdown = card.querySelector('.order-dropdown');
    if (dropdown) dropdown.remove();
    dropdown = document.createElement('div');
    dropdown.className = 'order-dropdown info-block';
    dropdown.style.marginTop = '8px';
    dropdown.innerHTML = `
      <div class="field-label">⚠️ Select Order for this Supply</div>
      <select class="order-select" onchange="App.orderDropdownChanged(this)">
        <option value="">— Choose which order to supply —</option>
        ${assignedOrders.map(o => {
          const allocated  = o.allocations[tech] || 0;
          const usedSoFar  = Object.values(region.dailyLog).flat()
            .filter(e => e.orderNo === o.orderNo && e.technician === tech)
            .reduce((s, e) => s + e.supplied, 0);
          const left = Math.max(0, allocated - usedSoFar);
          return `<option value="${o.orderNo}">${o.orderNo} - ${o.vehiclePlate} (${left}L remaining)</option>`;
        }).join('')}
      </select>`;
    card.querySelector('.divider').insertAdjacentElement('afterend', dropdown);
  }
}

export function orderDropdownChanged(selectEl) {
  const card    = selectEl.closest('.entry-card');
  const orderNo = selectEl.value;
  const tech    = card.querySelector('.tech-sel').value;
  const region  = DB.regions[DB.currentRegion];
  if (!orderNo) {
    ['order-plate-val','alloc-val','used-val','left-val'].forEach(c => card.querySelector('.' + c).textContent = '—');
    card.querySelector('.supp-input').max = '';
    card.removeAttribute('data-order');
    return;
  }
  const order = region.orders[orderNo];
  if (order) updateOrderDetails(card, order, tech, region);
}

export function updateOrderDetails(card, order, tech, region) {
  card.querySelector('.order-no-val').textContent    = order.orderNo;
  card.querySelector('.order-plate-val').textContent = order.vehiclePlate;
  const allocated  = order.allocations[tech] || 0;
  const usedSoFar  = Object.values(region.dailyLog).flat()
    .filter(e => e.orderNo === order.orderNo && e.technician === tech)
    .reduce((s, e) => s + e.supplied, 0);
  const left     = Math.max(0, allocated - usedSoFar);
  const orderBal = order.totalLiters - order.suppliedTotal;
  card.querySelector('.alloc-val').textContent    = allocated + ' L';
  card.querySelector('.used-val').textContent     = usedSoFar + ' L';
  card.querySelector('.left-val').textContent     = left + ' L';
  card.querySelector('.supp-input').max           = Math.min(left, orderBal);
  card.setAttribute('data-order', order.orderNo);
}

/* ── Save daily entries ─────────────────────────────────────── */

export function saveDaily() {
  const d = document.getElementById('dailyDate').value;
  if (!d) return alert('Please select a date first');

  const region = DB.regions[DB.currentRegion];
  if (!region.dailyLog[d]) region.dailyLog[d] = [];

  const cards = document.querySelectorAll('.entry-card');
  if (!cards.length) return alert('No entries to save');

  let saved = 0, skipped = 0;

  cards.forEach(card => {
    const tech     = card.querySelector('.tech-sel').value;
    const supplied = +card.querySelector('.supp-input').value || 0;
    const isUnalloc = card.getAttribute('data-unallocated') === 'true';
    if (!tech || supplied <= 0) return;

    if (isUnalloc) {
      const commentEl = card.querySelector('.comment-input');
      const comment   = commentEl ? commentEl.value.trim() : '';
      if (!comment) {
        skipped++;
        if (commentEl) commentEl.style.borderColor = 'var(--red)';
        return;
      }
      region.dailyLog[d].push({ technician: tech, supplied, comment, unallocated: true });
      saved++;
      return;
    }

    const orderNo = card.getAttribute('data-order');
    if (!orderNo) return;
    const o = region.orders[orderNo];
    if (!o || o.status === 'CLOSED') return;

    const maxAllowed = +card.querySelector('.supp-input').max || Infinity;
    const actual     = Math.min(supplied, maxAllowed);
    o.suppliedTotal  += actual;
    region.dailyLog[d].push({ orderNo, technician: tech, supplied: actual });
    saved++;
  });

  Object.values(region.orders).forEach(o => {
    if (o.suppliedTotal >= o.totalLiters) o.status = 'CLOSED';
  });

  save();
  renderOrders();
  document.getElementById('dailyEntries').innerHTML = '';
  renderLogView(d);
  renderDailyHistory();

  let msg = `✅ ${saved} entr${saved === 1 ? 'y' : 'ies'} saved for ${d}`;
  if (skipped > 0) msg += `\n⚠️ ${skipped} unallocated entr${skipped === 1 ? 'y' : 'ies'} skipped — comment required.`;
  alert(msg);

  // Prompt for overage comments if any new overages exist
  for (const [orderNo, o] of Object.entries(region.orders)) {
    for (const [tech, alloc] of Object.entries(o.allocations)) {
      const supplied = Object.values(region.dailyLog).flat()
        .filter(e => e.orderNo === orderNo && e.technician === tech)
        .reduce((s, e) => s + e.supplied, 0);
      if (supplied > alloc && !(o.overageComments && o.overageComments[tech])) {
        openOverageComment(orderNo, tech);
        return;
      }
    }
  }
}

/* ── Edit daily entry modal ─────────────────────────────────── */

let _editCtx = null;

export function openEditModal(date, idx) {
  const region  = DB.regions[DB.currentRegion];
  const entries = region.dailyLog[date];
  if (!entries || !entries[idx]) return;
  const entry = entries[idx];
  _editCtx = { date, idx };

  document.getElementById('editModalTitle').textContent = `✏️ Edit — ${entry.technician}`;
  const order = entry.orderNo ? region.orders[entry.orderNo] : null;
  document.getElementById('editModalMeta').textContent = entry.unallocated
    ? `📅 ${date}  ·  Unallocated entry`
    : `📅 ${date}  ·  Order: ${entry.orderNo}${order ? ' · ' + order.vehiclePlate : ''}`;

  document.getElementById('editSupplied').value = entry.supplied;
  const commentBlock = document.getElementById('editCommentBlock');
  const commentInput = document.getElementById('editComment');
  if (entry.unallocated) {
    commentBlock.style.display = 'block';
    commentInput.value         = entry.comment || '';
  } else {
    commentBlock.style.display = 'none';
    commentInput.value         = '';
  }

  if (!entry.unallocated && entry.orderNo) {
    const o = region.orders[entry.orderNo];
    if (o) {
      const allocated  = o.allocations[entry.technician] || 0;
      const usedOthers = Object.values(region.dailyLog).flat()
        .filter(e => e !== entry && e.orderNo === entry.orderNo && e.technician === entry.technician)
        .reduce((s, e) => s + e.supplied, 0);
      document.getElementById('editSupplied').max = Math.max(0, Math.min(
        allocated - usedOthers,
        o.totalLiters - (o.suppliedTotal - entry.supplied)
      ));
    }
  } else {
    document.getElementById('editSupplied').removeAttribute('max');
  }

  document.getElementById('editModal').classList.remove('hidden');
  setTimeout(() => document.getElementById('editSupplied').focus(), 100);
}

export function closeEditModal(e) {
  if (e && e.target !== document.getElementById('editModal')) return;
  document.getElementById('editModal').classList.add('hidden');
  _editCtx = null;
}

export function saveEditEntry() {
  if (!_editCtx) return;
  const { date, idx } = _editCtx;
  const region  = DB.regions[DB.currentRegion];
  const entries = region.dailyLog[date];
  if (!entries || !entries[idx]) return;
  const entry      = entries[idx];
  const newSupply  = +document.getElementById('editSupplied').value;
  const newComment = document.getElementById('editComment').value.trim();
  if (!newSupply || newSupply <= 0) return alert('Please enter a valid litres value');
  if (entry.unallocated && !newComment) {
    document.getElementById('editComment').style.borderColor = 'var(--red)';
    return alert('Comment is required for unallocated entries');
  }

  const diff = newSupply - entry.supplied;
  if (!entry.unallocated && entry.orderNo) {
    const o = region.orders[entry.orderNo];
    if (o) {
      o.suppliedTotal = Math.max(0, o.suppliedTotal + diff);
      if (o.status === 'CLOSED' && o.suppliedTotal < o.totalLiters) o.status = 'OPEN';
      if (o.suppliedTotal >= o.totalLiters) o.status = 'CLOSED';
    }
  }

  entries[idx].supplied = newSupply;
  if (entry.unallocated) entries[idx].comment = newComment;

  save(); updateOrderCounter();
  document.getElementById('editModal').classList.add('hidden');
  _editCtx = null;
  renderLogView(date);
  renderDailyHistory();
  if (document.getElementById('page-orders').classList.contains('active')) renderOrders();
}

/* ── Delete daily entry ─────────────────────────────────────── */

export function deleteDailyEntry(date, idx) {
  const region  = DB.regions[DB.currentRegion];
  const entries = region.dailyLog[date];
  if (!entries || !entries[idx]) return;
  const entry = entries[idx];
  const label = entry.unallocated
    ? `Delete ${entry.supplied}L (unallocated) supplied by ${entry.technician} on ${date}?`
    : `Delete ${entry.supplied}L supplied by ${entry.technician} on ${date}?`;
  if (!confirm(label)) return;

  if (!entry.unallocated && entry.orderNo) {
    const order = region.orders[entry.orderNo];
    if (order) {
      order.suppliedTotal = Math.max(0, order.suppliedTotal - entry.supplied);
      if (order.status === 'CLOSED' && order.suppliedTotal < order.totalLiters) order.status = 'OPEN';
    }
  }

  entries.splice(idx, 1);
  if (entries.length === 0) delete region.dailyLog[date];

  save(); updateOrderCounter(); renderLogView(date); renderDailyHistory();
  if (document.getElementById('page-orders').classList.contains('active')) renderOrders();
}

/* ── Daily summary modal ────────────────────────────────────── */

export function openDailySummary() {
  const date = document.getElementById('dailyDate').value;
  if (!date) return alert('Please select a date first');
  document.getElementById('summaryStartDate').value = date;
  document.getElementById('summaryEndDate').value   = date;
  document.getElementById('summaryModal').classList.remove('hidden');
  loadSummaryForDateRange();
}

export function loadSummaryForDateRange() {
  const startDate = document.getElementById('summaryStartDate').value;
  const endDate   = document.getElementById('summaryEndDate').value;
  if (!startDate || !endDate) return alert('Please select both start and end dates');
  if (startDate > endDate)    return alert('Start date must be before or equal to end date');

  const region = DB.regions[DB.currentRegion];

  // Collect dates in range with log data
  const dates = [];
  let cur      = new Date(startDate + 'T00:00:00');
  const last   = new Date(endDate   + 'T00:00:00');
  while (cur <= last) {
    const ds = cur.toISOString().slice(0, 10);
    if (region.dailyLog[ds]) dates.push(ds);
    cur.setDate(cur.getDate() + 1);
  }

  if (!dates.length) {
    document.getElementById('summaryModalBody').innerHTML = '<div class="log-empty">No entries found for the selected date range</div>';
    return;
  }

  const allEntries = dates.flatMap(date =>
    (region.dailyLog[date] || []).map(entry => ({ ...entry, date }))
  );

  const totalFuelOrdered = Object.values(region.orders).reduce((s, o) => s + o.totalLiters, 0);
  const totalSupplied    = allEntries.reduce((s, e) => s + e.supplied, 0);
  const totalBalance     = totalFuelOrdered - Object.values(region.orders).reduce((s, o) => s + o.suppliedTotal, 0);
  const entriesCount     = allEntries.length;

  const startObj = new Date(startDate + 'T00:00:00');
  const endObj   = new Date(endDate   + 'T00:00:00');
  const rangeStr = startDate === endDate
    ? startObj.toLocaleDateString('en-GB', { weekday: 'long', day: '2-digit', month: 'long', year: 'numeric' })
    : `${startObj.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })} - ${endObj.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })}`;

  document.getElementById('summaryModalTitle').textContent = `📊 Summary Report: ${rangeStr}`;

  const rows = allEntries.map(entry => {
    const order     = entry.orderNo ? region.orders[entry.orderNo] : null;
    const orderNo   = entry.orderNo || '—';
    const orderTotal = order ? order.totalLiters : 0;
    const balance   = order ? (order.totalLiters - order.suppliedTotal) : 0;
    const dateDisplay = new Date(entry.date + 'T00:00:00').toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });
    return `<tr>
      <td class="tech-cell">${entry.technician}</td>
      <td class="order-cell">${orderNo}</td>
      <td class="date-cell">${dateDisplay}</td>
      <td class="supplied-cell">${entry.supplied}L</td>
      <td class="ordered-cell">${orderTotal}L</td>
      <td class="balance-cell">${balance}L</td>
    </tr>`;
  }).join('');

  document.getElementById('summaryModalBody').innerHTML = `
    <div class="summary-stats">
      <div class="summary-stat"><div class="summary-stat-label">📦 Total Fuel Ordered</div><div class="summary-stat-value purple">${totalFuelOrdered}L</div></div>
      <div class="summary-stat"><div class="summary-stat-label">✅ Total Supplied</div><div class="summary-stat-value green">${totalSupplied}L</div></div>
      <div class="summary-stat"><div class="summary-stat-label">⚖️ Balance Remaining</div><div class="summary-stat-value red">${totalBalance}L</div></div>
      <div class="summary-stat"><div class="summary-stat-label">📋 Total Entries</div><div class="summary-stat-value blue">${entriesCount}</div></div>
    </div>
    <table class="summary-table">
      <thead><tr>
        <th>👤 Technician</th><th>📄 Order No</th><th>📅 Date</th>
        <th>⛽ Fuel Supplied</th><th>📦 Order Total</th><th>⚖️ Balance Remaining</th>
      </tr></thead>
      <tbody>${rows}</tbody>
    </table>`;
}

export function closeSummaryModal(e) {
  if (e && e.target !== document.getElementById('summaryModal')) return;
  document.getElementById('summaryModal').classList.add('hidden');
}