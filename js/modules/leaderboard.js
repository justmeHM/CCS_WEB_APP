/**
 * leaderboard.js — Technician Leaderboard
 * Covers: rendering the leaderboard with region/date filters,
 * and the tech history modal.
 */

import { DB } from './db.js';

/* ── Populate leaderboard region filter ─────────────────────── */

export function populateLbRegionFilter() {
  const sel = document.getElementById('lbRegionFilter');
  if (!sel) return;
  const prev = sel.value;
  sel.innerHTML = '<option value="">All Regions</option>';
  Object.keys(DB.regions).forEach(r => {
    const opt = document.createElement('option');
    opt.value = r; opt.textContent = r; sel.appendChild(opt);
  });
  if (prev) sel.value = prev;
}

/* ── Render leaderboard ─────────────────────────────────────── */

export function renderLeaderboard() {
  const el = document.getElementById('leaderboardBody');
  if (!el) return;
  el.innerHTML = '';

  const regionFilter = document.getElementById('lbRegionFilter')?.value || '';
  const dayFilter    = parseInt(document.getElementById('lbDateFilter')?.value) || 0;
  const cutoff       = dayFilter ? new Date(Date.now() - dayFilter * 86400000).toISOString().slice(0, 10) : null;

  // Aggregate totals per technician
  const totals = {};
  Object.entries(DB.regions).forEach(([rName, r]) => {
    if (regionFilter && rName !== regionFilter) return;
    Object.entries(r.dailyLog).forEach(([date, entries]) => {
      if (cutoff && date < cutoff) return;
      entries.forEach(e => {
        if (!totals[e.technician]) totals[e.technician] = { litres: 0, region: rName };
        totals[e.technician].litres += e.supplied;
      });
    });
  });

  const sorted = Object.entries(totals).sort((a, b) => b[1].litres - a[1].litres);
  if (!sorted.length) {
    el.innerHTML = '<div class="log-empty">No supply data found for this filter.</div>'; return;
  }

  const max       = sorted[0][1].litres || 1;
  const rankIcon  = ['🥇', '🥈', '🥉'];
  const rankClass = ['gold', 'silver', 'bronze'];

  sorted.forEach(([tech, data], i) => {
    const pct  = Math.round((data.litres / max) * 100);
    const rc   = i < 3 ? rankClass[i] : 'other';
    const icon = i < 3 ? rankIcon[i] : `#${i + 1}`;

    const card = document.createElement('div');
    card.className = 'lb-card';
    card.onclick   = () => openTechHistory(tech);
    card.innerHTML = `
      <div class="lb-rank ${rc}">${icon}</div>
      <div class="lb-info">
        <div class="lb-name">${tech}</div>
        <div class="lb-region">📍 ${data.region}</div>
        <div class="lb-bar-wrap"><div class="lb-bar" style="width:${pct}%"></div></div>
      </div>
      <div class="lb-litres">${data.litres.toFixed(1)} L</div>`;
    el.appendChild(card);
  });
}

/* ── Tech history modal ─────────────────────────────────────── */

export function openTechHistory(techName) {
  const modal = document.getElementById('techHistModal');
  const title = document.getElementById('techHistModalTitle');
  const body  = document.getElementById('techHistModalBody');
  const stats = document.getElementById('techHistModalStats');

  title.textContent = `📋 ${techName} — Supply History`;
  body.innerHTML = '';
  stats.innerHTML = '';

  // Gather all entries for this tech across regions
  const entries = [];
  Object.entries(DB.regions).forEach(([rName, r]) => {
    Object.entries(r.dailyLog).forEach(([date, dayEntries]) => {
      dayEntries.filter(e => e.technician === techName).forEach(e => {
        entries.push({ ...e, date, region: rName });
      });
    });
  });
  entries.sort((a, b) => b.date.localeCompare(a.date));

  const totalL = entries.reduce((s, e) => s + e.supplied, 0);
  const days   = new Set(entries.map(e => e.date)).size;
  const orders = new Set(entries.filter(e => e.orderNo).map(e => e.orderNo)).size;

  stats.innerHTML = `
    <div class="stat-tile green" style="padding:10px;"><div class="tile-val" style="color:#16a34a;font-size:1.4rem;">${totalL.toFixed(1)}</div><div class="tile-lbl">Total Litres</div></div>
    <div class="stat-tile blue"  style="padding:10px;"><div class="tile-val" style="color:#2563eb;font-size:1.4rem;">${days}</div><div class="tile-lbl">Days Active</div></div>
    <div class="stat-tile amber" style="padding:10px;"><div class="tile-val" style="color:#d97706;font-size:1.4rem;">${orders}</div><div class="tile-lbl">Orders Served</div></div>`;

  if (!entries.length) {
    body.innerHTML = '<div class="log-empty">No supply history for this technician.</div>';
  } else {
    entries.forEach(e => {
      const dateStr = new Date(e.date + 'T00:00:00').toLocaleDateString('en-GB', { weekday: 'short', day: '2-digit', month: 'short', year: 'numeric' });
      const div = document.createElement('div');
      div.className = 'th-entry' + (e.unallocated ? ' unalloc-entry' : '');
      div.innerHTML = `
        <div class="th-entry-info">
          <div class="th-entry-date">📅 ${dateStr}</div>
          <div class="th-entry-meta">${e.unallocated ? '⚠️ Unallocated' : `Order: <strong>${e.orderNo}</strong>`} · 📍 ${e.region}${e.comment ? ` · 💬 ${e.comment}` : ''}</div>
        </div>
        <div class="th-entry-litres" style="color:${e.unallocated ? '#d97706' : '#15803d'}">${e.supplied} L</div>`;
      body.appendChild(div);
    });
  }
  modal.classList.remove('hidden');
}

export function closeTechHistModal(e) {
  if (e && e.target !== document.getElementById('techHistModal')) return;
  document.getElementById('techHistModal').classList.add('hidden');
}