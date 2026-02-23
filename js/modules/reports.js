/**
 * reports.js — Export, Backup & Restore
 * Covers: XLSX export, JSON backup/restore, unallocated supply report,
 * and backup status banner.
 */

import { DB, replaceDB } from './db.js';
import { populateRegions } from './regions.js';
import { renderDailyHistory } from './daily.js';

/* ── Excel Export ───────────────────────────────────────────── */

export function exportOrders() {
  const wb = XLSX.utils.book_new();

  // Orders sheet
  const ws1 = [['Region', 'Order', 'Vehicle', 'Total', 'Supplied', 'Balance', 'Status']];
  Object.entries(DB.regions).forEach(([rName, r]) => {
    Object.values(r.orders).forEach(o => {
      ws1.push([rName, o.orderNo, o.vehiclePlate, o.totalLiters, o.suppliedTotal, o.totalLiters - o.suppliedTotal, o.status]);
    });
  });
  XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet(ws1), 'Orders');

  // Unallocated log sheet
  const ws2 = [['Region', 'Date', 'Technician', 'Litres Supplied', 'Comment']];
  Object.entries(DB.regions).forEach(([rName, r]) => {
    Object.entries(r.dailyLog).forEach(([date, entries]) => {
      entries.filter(e => e.unallocated).forEach(e => {
        ws2.push([rName, date, e.technician, e.supplied, e.comment || '']);
      });
    });
  });
  XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet(ws2), 'Unallocated Log');

  // Daily supply log sheet
  const ws3 = [['Region', 'Date', 'Order No', 'Vehicle Plate', 'Technician', 'Litres Supplied']];
  Object.entries(DB.regions).forEach(([rName, r]) => {
    Object.entries(r.dailyLog).sort((a, b) => a[0].localeCompare(b[0])).forEach(([date, entries]) => {
      entries.filter(e => !e.unallocated && e.orderNo).forEach(e => {
        const order = r.orders[e.orderNo];
        ws3.push([rName, date, e.orderNo, order ? order.vehiclePlate : '—', e.technician, e.supplied]);
      });
    });
  });
  XLSX.utils.book_append_sheet(wb, XLSX.utils.aoa_to_sheet(ws3), 'Daily Supply Log');

  XLSX.writeFile(wb, 'CCS_Orders.xlsx');
}

/* ── JSON Backup & Restore ──────────────────────────────────── */

export function backupData() {
  const json = JSON.stringify(DB, null, 2);
  const blob = new Blob([json], { type: 'application/json' });
  const url  = URL.createObjectURL(blob);
  const a    = document.createElement('a');
  a.href     = url;
  a.download = `CCS_Backup_${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(url);
  localStorage.setItem('ccs_last_backup', new Date().toISOString());
  renderBackupStatus();
}

export function restoreData(event) {
  const file = event.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = e => {
    try {
      const parsed = JSON.parse(e.target.result);
      if (!parsed.regions || !parsed.currentRegion) {
        return alert('❌ Invalid backup file. Please select a valid CCS backup.');
      }
      if (!confirm('⚠️ This will REPLACE all current data with the backup. Are you sure?')) return;
      replaceDB(parsed);
      populateRegions();
      renderDailyHistory();
      renderUnallocReport();
      alert('✅ Data restored successfully!');
    } catch {
      alert('❌ Failed to read backup file. Please ensure it is a valid JSON backup.');
    }
    event.target.value = '';
  };
  reader.readAsText(file);
}

/* ── Backup status banner ───────────────────────────────────── */

export function renderBackupStatus() {
  const banner  = document.getElementById('backupStatusBanner');
  const text    = document.getElementById('backupStatusText');
  if (!banner || !text) return;

  const lastRaw = localStorage.getItem('ccs_last_backup');
  if (!lastRaw) {
    banner.className = 'backup-status never';
    banner.querySelector('.bs-icon').textContent = '🔴';
    text.textContent = 'No backup has ever been made. Export a backup to protect your data.';
    banner.style.display = 'flex';
    return;
  }

  const last      = new Date(lastRaw);
  const daysSince = Math.floor((Date.now() - last) / 86400000);
  const dateStr   = last.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
                  + ' ' + last.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' });

  if (daysSince >= 7) {
    banner.className = 'backup-status warn';
    banner.querySelector('.bs-icon').textContent = '⚠️';
    text.textContent = `Last backup: ${dateStr} — ${daysSince} days ago. Consider backing up soon.`;
  } else {
    banner.className = 'backup-status ok';
    banner.querySelector('.bs-icon').textContent = '✅';
    text.textContent = `Last backup: ${dateStr}${daysSince === 0 ? ' (today)' : ` — ${daysSince} day${daysSince !== 1 ? 's' : ''} ago`}.`;
  }
  banner.style.display = 'flex';
}

/* ── Unallocated supply report ──────────────────────────────── */

export function renderUnallocReport() {
  const el     = document.getElementById('unallocReport');
  const region = DB.regions[DB.currentRegion];
  el.innerHTML = '';

  const rows = [];
  Object.entries(region.dailyLog).forEach(([date, entries]) => {
    entries.filter(e => e.unallocated).forEach(e => { rows.push({ date, ...e }); });
  });

  if (!rows.length) {
    el.innerHTML = '<div class="log-empty">No unallocated entries for this region.</div>'; return;
  }

  rows.sort((a, b) => b.date.localeCompare(a.date));
  const totalUnalloc = rows.reduce((s, r) => s + r.supplied, 0);

  rows.forEach(row => {
    const div = document.createElement('div');
    div.className = 'log-entry unalloc-entry';
    div.style.marginBottom = '7px';
    div.innerHTML = `
      <div class="log-info">
        <div class="log-tech">${row.technician}</div>
        <div class="log-meta">📅 ${row.date}</div>
        ${row.comment ? `<div class="log-comment">💬 ${row.comment}</div>` : ''}
      </div>
      <div class="log-litres" style="color:#d97706;">${row.supplied} L</div>`;
    el.appendChild(div);
  });

  const tot = document.createElement('div');
  tot.style.cssText = 'text-align:right;padding:8px 4px 2px;font-family:Rajdhani,sans-serif;font-weight:700;font-size:0.85rem;color:#d97706;';
  tot.textContent = `Total unallocated: ${totalUnalloc} L`;
  el.appendChild(tot);
}