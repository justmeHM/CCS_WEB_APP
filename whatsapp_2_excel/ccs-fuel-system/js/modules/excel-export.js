/**
 * js/modules/excel-export.js
 * Centralised Excel/XLSX generation.
 * All xlsx-writing logic lives here so page modules stay thin.
 */

'use strict';

(function () {
  function _wb() { return XLSX.utils.book_new(); }

  function _autoWidth(ws, data) {
    if (!data.length) return;
    const keys = Object.keys(data[0]);
    ws['!cols'] = keys.map(k => ({
      wch: Math.max(k.length, ...data.map(r => String(r[k] ?? '').length)) + 2,
    }));
  }

  function _headerStyle() {
    return { font: { bold: true, color: { rgb: 'FFFFFF' } }, fill: { fgColor: { rgb: 'C41E3A' } }, alignment: { horizontal: 'center' } };
  }

  /** Generic export: array of objects → single sheet xlsx */
  function exportSheet(data, filename, sheetName = 'Sheet1') {
    if (!data || !data.length) return CCS.Toast.show('No data to export', 'warning');
    const wb = _wb();
    const ws = XLSX.utils.json_to_sheet(data);
    _autoWidth(ws, data);
    XLSX.utils.book_append_sheet(wb, ws, sheetName);
    XLSX.writeFile(wb, filename.endsWith('.xlsx') ? filename : filename + '.xlsx');
    CCS.Toast.show('Exported: ' + filename, 'success');
  }

  /** Export the full daily log for a region as a multi-sheet workbook */
  function exportDailyLog(regionName) {
    regionName = regionName || CCS.DB.currentRegion;
    const region = CCS.DB.region(regionName);
    if (!region) return CCS.Toast.show('Region not found', 'error');

    const wb = _wb();
    const log = region.dailyLog || {};
    const dates = Object.keys(log).sort();

    if (!dates.length) return CCS.Toast.show('No daily log data to export', 'warning');

    // One sheet per month
    const byMonth = CCS.utils.groupBy(dates, d => d.slice(0, 7));
    Object.entries(byMonth).forEach(([month, monthDates]) => {
      const rows = monthDates.flatMap(date =>
        (log[date] || []).map(e => ({
          Date: CCS.fmt.date(date),
          Technician: e.technician,
          'Order No': e.orderNo,
          'Allocated (L)': e.allocated,
          'Supplied (L)': e.supplied,
          Balance: (e.allocated - e.supplied).toFixed(1),
          Notes: e.notes || '',
        }))
      );

      const ws = XLSX.utils.json_to_sheet(rows);
      _autoWidth(ws, rows);
      XLSX.utils.book_append_sheet(wb, ws, month);
    });

    const filename = `CCS_DailyLog_${regionName}_${new Date().toISOString().slice(0, 10)}.xlsx`;
    XLSX.writeFile(wb, filename);
    CCS.Toast.show('Daily log exported', 'success');
  }

  /** Export orders summary */
  function exportOrders(regionName) {
    regionName = regionName || CCS.DB.currentRegion;
    const region = CCS.DB.region(regionName);
    if (!region) return;

    const rows = Object.values(region.orders).map(o => ({
      'Order No': o.orderNo,
      'Customer': o.customer || '',
      'Date': CCS.fmt.date(o.date),
      'Total (L)': o.totalLiters,
      'Supplied (L)': o.suppliedTotal || 0,
      'Balance (L)': (o.totalLiters - (o.suppliedTotal || 0)).toFixed(1),
      'Status': o.status || 'open',
      'Technicians': Object.keys(o.allocations || {}).join(', '),
    }));

    exportSheet(rows, `CCS_Orders_${regionName}_${new Date().toISOString().slice(0, 10)}`, 'Orders');
  }

  /** Export leaderboard */
  function exportLeaderboard(regionName) {
    regionName = regionName || CCS.DB.currentRegion;
    const region = CCS.DB.region(regionName);
    if (!region) return;

    const techMap = {};
    Object.values(region.dailyLog).flat().forEach(e => {
      if (!techMap[e.technician]) techMap[e.technician] = { allocated: 0, supplied: 0, entries: 0 };
      techMap[e.technician].allocated += e.allocated || 0;
      techMap[e.technician].supplied  += e.supplied  || 0;
      techMap[e.technician].entries++;
    });

    const rows = Object.entries(techMap)
      .sort((a, b) => b[1].supplied - a[1].supplied)
      .map(([name, s], i) => ({
        Rank: i + 1,
        Technician: name,
        'Allocated (L)': s.allocated.toFixed(1),
        'Supplied (L)': s.supplied.toFixed(1),
        'Entries': s.entries,
        'Efficiency %': s.allocated > 0 ? ((s.supplied / s.allocated) * 100).toFixed(1) : '0.0',
      }));

    exportSheet(rows, `CCS_Leaderboard_${regionName}_${new Date().toISOString().slice(0, 10)}`, 'Leaderboard');
  }

  /** Export all regions as separate sheets */
  function exportAllRegions() {
    const wb = _wb();
    let hasData = false;

    Object.entries(CCS.DB.data.regions).forEach(([rName, region]) => {
      const rows = Object.values(region.orders).map(o => ({
        Region: rName,
        'Order No': o.orderNo,
        'Total (L)': o.totalLiters,
        'Supplied (L)': o.suppliedTotal || 0,
        Status: o.status || 'open',
      }));
      if (!rows.length) return;
      hasData = true;
      const ws = XLSX.utils.json_to_sheet(rows);
      _autoWidth(ws, rows);
      XLSX.utils.book_append_sheet(wb, ws, rName.slice(0, 31));
    });

    if (!hasData) return CCS.Toast.show('No data across any region', 'warning');
    XLSX.writeFile(wb, `CCS_AllRegions_${new Date().toISOString().slice(0, 10)}.xlsx`);
    CCS.Toast.show('All regions exported', 'success');
  }

  CCS.Excel = {
    exportSheet,
    exportDailyLog,
    exportOrders,
    exportLeaderboard,
    exportAllRegions,
  };
})();
