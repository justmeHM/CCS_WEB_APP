/**
 * regions.js — Regions & Technicians
 * Covers: add/rename/delete regions, add/rename/delete technicians,
 * populating region selectors, and the rename modal.
 */

import { DB, save } from './db.js';
import { populateAllocOrder, populateAllocTech, renderOrders } from './orders.js';
import { renderDailyHistory } from './daily.js';
import { updateOrderCounter } from './ui.js';

/* ── Region selector & counter ─────────────────────────────── */

export function populateRegions() {
  const sel = document.getElementById('regionSelect');
  sel.innerHTML = '';
  Object.keys(DB.regions).forEach(r => {
    const opt = document.createElement('option');
    opt.value = r; opt.textContent = r; sel.appendChild(opt);
  });
  sel.value = DB.currentRegion;

  // Leaderboard filter
  const lbSel = document.getElementById('lbRegionFilter');
  if (lbSel) {
    const prev = lbSel.value;
    lbSel.innerHTML = '<option value="">All Regions</option>';
    Object.keys(DB.regions).forEach(r => {
      const opt = document.createElement('option');
      opt.value = r; opt.textContent = r; lbSel.appendChild(opt);
    });
    if (prev) lbSel.value = prev;
  }

  populateAllocOrder();
  populateAllocTech();
  renderTechList();
  updateOrderCounter();
}

export function changeRegion() {
  DB.currentRegion = document.getElementById('regionSelect').value;
  save();
  populateRegions();
  renderDailyHistory();
}

/* ── Region CRUD ────────────────────────────────────────────── */

export function addRegion() {
  const n = document.getElementById('newRegion').value.trim();
  if (!n || DB.regions[n]) return;
  DB.regions[n] = { technicians: [], technicianPlates: {}, orders: {}, dailyLog: {} };
  document.getElementById('newRegion').value = '';
  save(); populateRegions(); renderRegionList();
}

export function deleteRegion(rName) {
  if (Object.keys(DB.regions).length <= 1) {
    return alert('⚠️ You cannot delete the only region.');
  }
  const r = DB.regions[rName];
  const orderCount = Object.keys(r.orders).length;
  const msg = orderCount > 0
    ? `⚠️ Region "${rName}" has ${orderCount} order(s) and all associated data. Delete permanently?`
    : `Delete region "${rName}"?`;
  if (!confirm(msg)) return;
  delete DB.regions[rName];
  if (DB.currentRegion === rName) DB.currentRegion = Object.keys(DB.regions)[0];
  save(); populateRegions(); renderRegionList();
}

export function renderRegionList() {
  const el = document.getElementById('regionList');
  if (!el) return;
  el.innerHTML = '';
  Object.keys(DB.regions).forEach(r => {
    const div = document.createElement('div');
    div.className = 'tech-item';
    const isCurrent = r === DB.currentRegion;
    div.innerHTML = `
      <div>
        <div class="name">${r}</div>
        <div class="plate" style="color:var(--muted);">
          ${Object.keys(DB.regions[r].orders).length} orders ·
          ${DB.regions[r].technicians.length} techs
          ${isCurrent ? ' · <span style="color:#16a34a;">Active</span>' : ''}
        </div>
      </div>
      <div class="tech-item-actions">
        <button class="edit-btn btn-sm" onclick="App.openRenameRegion('${r}')">✏️ Rename</button>
        <button class="del-btn btn-sm"  onclick="App.deleteRegion('${r}')">🗑</button>
      </div>`;
    el.appendChild(div);
  });
}

/* ── Technician CRUD ────────────────────────────────────────── */

export function addTechnician() {
  const r = DB.currentRegion;
  const t = document.getElementById('techName').value.trim();
  const p = document.getElementById('techPlate').value.trim();
  if (!t || !p) return;
  if (DB.regions[r].technicians.includes(t)) return alert('Technician already exists');
  DB.regions[r].technicians.push(t);
  DB.regions[r].technicianPlates[t] = p;
  document.getElementById('techName').value = '';
  document.getElementById('techPlate').value = '';
  save(); populateAllocTech(); renderTechList();
}

export function renderTechList() {
  const el = document.getElementById('techList');
  el.innerHTML = '';
  const region = DB.regions[DB.currentRegion];
  if (!region.technicians.length) {
    el.innerHTML = '<div class="empty">No technicians added yet</div>'; return;
  }
  region.technicians.forEach(t => {
    const d = document.createElement('div');
    d.className = 'tech-item';
    d.innerHTML = `
      <div>
        <div class="name">${t}</div>
        <div class="plate">${region.technicianPlates[t]}</div>
      </div>
      <div class="tech-item-actions">
        <button class="edit-btn btn-sm" onclick="App.openRenameTech('${t}')">✏️ Rename</button>
        <button class="del-btn btn-sm"  onclick="App.deleteTech('${t}')">🗑</button>
      </div>`;
    el.appendChild(d);
  });
}

export function deleteTech(techName) {
  const r = DB.regions[DB.currentRegion];
  const hasAllocs = Object.values(r.orders).some(o => o.allocations[techName] !== undefined);
  const msg = hasAllocs
    ? `⚠️ "${techName}" has existing allocations. Removing them will not delete supply history. Continue?`
    : `Remove technician "${techName}"?`;
  if (!confirm(msg)) return;
  r.technicians = r.technicians.filter(t => t !== techName);
  delete r.technicianPlates[techName];
  Object.values(r.orders).forEach(o => { delete o.allocations[techName]; });
  save(); populateRegions(); renderTechList();
}

/* ── Rename modal (shared for regions & techs) ─────────────── */

let _renameCtx = null;

export function openRenameRegion(rName) {
  _renameCtx = { type: 'region', name: rName };
  document.getElementById('renameModalTitle').textContent = `✏️ Rename Region: ${rName}`;
  document.getElementById('renameInput').value = rName;
  document.getElementById('renameModal').classList.remove('hidden');
  setTimeout(() => document.getElementById('renameInput').select(), 100);
}

export function openRenameTech(techName) {
  _renameCtx = { type: 'tech', name: techName };
  document.getElementById('renameModalTitle').textContent = `✏️ Rename Technician: ${techName}`;
  document.getElementById('renameInput').value = techName;
  document.getElementById('renameModal').classList.remove('hidden');
  setTimeout(() => document.getElementById('renameInput').select(), 100);
}

export function closeRenameModal(e) {
  if (e && e.target !== document.getElementById('renameModal')) return;
  document.getElementById('renameModal').classList.add('hidden');
  _renameCtx = null;
}

export function confirmRename() {
  if (!_renameCtx) return;
  const newName = document.getElementById('renameInput').value.trim();
  if (!newName) return alert('Please enter a name');

  if (_renameCtx.type === 'region') {
    _renameRegion(_renameCtx.name, newName);
  } else if (_renameCtx.type === 'tech') {
    _renameTech(_renameCtx.name, newName);
  }

  document.getElementById('renameModal').classList.add('hidden');
  _renameCtx = null;
}

function _renameRegion(oldName, newName) {
  if (newName === oldName) return;
  if (DB.regions[newName]) return alert('A region with that name already exists');
  DB.regions[newName] = DB.regions[oldName];
  delete DB.regions[oldName];
  if (DB.currentRegion === oldName) DB.currentRegion = newName;
  save(); populateRegions(); renderRegionList();
}

function _renameTech(oldName, newName) {
  if (newName === oldName) return;
  Object.values(DB.regions).forEach(r => {
    const idx = r.technicians.indexOf(oldName);
    if (idx === -1) return;
    r.technicians[idx] = newName;
    if (r.technicianPlates[oldName] !== undefined) {
      r.technicianPlates[newName] = r.technicianPlates[oldName];
      delete r.technicianPlates[oldName];
    }
    Object.values(r.orders).forEach(o => {
      if (o.allocations[oldName] !== undefined) {
        o.allocations[newName] = o.allocations[oldName];
        delete o.allocations[oldName];
      }
      if (o.overageComments?.[oldName] !== undefined) {
        o.overageComments[newName] = o.overageComments[oldName];
        delete o.overageComments[oldName];
      }
    });
    Object.values(r.dailyLog).forEach(dayEntries => {
      dayEntries.forEach(e => { if (e.technician === oldName) e.technician = newName; });
    });
  });
  save(); populateRegions(); renderTechList();
}