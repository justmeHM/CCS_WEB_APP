/**
 * js/modules/db.js
 * Centralised data layer.
 * All reads and writes go through CCS.DB — never touch localStorage directly
 * anywhere else. This makes swapping the backend (e.g. IndexedDB, REST API)
 * a single-file change.
 *
 * Schema version: 6  (matching the original KEY 'ccs_fuel_orders_v6')
 */

'use strict';

(function () {
  const STORAGE_KEY = 'ccs_fuel_orders_v6';

  const DEFAULT_DB = {
    currentRegion: 'New CCS',
    currentCycleName: 'INITIAL CYCLE',
    currentCycleStartDate: new Date().toISOString().slice(0, 10),
    cycles: [],
    regions: {
      'New CCS': {
        technicians: [],
        technicianPlates: {},
        orders: {},
        dailyLog: {},
        monthlyTarget: null,
        techMonthlyTargets: {},
        unassignedComments: {},
      },
    },
  };

  /** Load raw data from localStorage and run migrations */
  function load() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      const data = raw ? JSON.parse(raw) : CCS.utils.clone(DEFAULT_DB);
      return migrate(data);
    } catch (e) {
      console.error('[DB] Failed to load — using defaults.', e);
      return CCS.utils.clone(DEFAULT_DB);
    }
  }

  /** Apply any forward migrations to bring old data up to current schema */
  function migrate(data) {
    // v5 → v6: ensure cycles array
    if (!data.cycles) data.cycles = [];
    if (!data.currentCycleName)      data.currentCycleName = 'INITIAL CYCLE';
    if (!data.currentCycleStartDate) data.currentCycleStartDate = new Date().toISOString().slice(0, 10);

    // Ensure every region has all required sub-objects
    Object.values(data.regions || {}).forEach(r => {
      if (!r.unassignedComments) r.unassignedComments = {};
      if (!r.techMonthlyTargets) r.techMonthlyTargets = {};
      if (!r.technicianPlates)   r.technicianPlates   = {};
    });

    return data;
  }

  /** The live data object — treated as a mutable store */
  let _db = load();

  CCS.DB = {
    // ── Raw access (avoid where possible — prefer typed methods below) ──
    get data() { return _db; },

    // ── Persistence ──
    save() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(_db));
      } catch (e) {
        console.error('[DB] Save failed.', e);
      }
    },

    /** Hard reset to defaults (used in tests / dev only) */
    reset() {
      _db = CCS.utils.clone(DEFAULT_DB);
      this.save();
    },

    // ── Region helpers ──
    get currentRegion() { return _db.currentRegion; },
    set currentRegion(name) { _db.currentRegion = name; },

    region(name = _db.currentRegion) { return _db.regions[name]; },

    ensureRegion(name) {
      if (!_db.regions[name]) {
        _db.regions[name] = CCS.utils.clone(DEFAULT_DB.regions['New CCS']);
      }
      return _db.regions[name];
    },

    listRegions() { return Object.keys(_db.regions); },

    // ── Cycle helpers ──
    get currentCycleName()      { return _db.currentCycleName; },
    set currentCycleName(v)     { _db.currentCycleName = v; },
    get currentCycleStartDate() { return _db.currentCycleStartDate; },
    set currentCycleStartDate(v){ _db.currentCycleStartDate = v; },
    get cycles()                { return _db.cycles; },

    // ── Order helpers ──
    orders(regionName = _db.currentRegion) {
      return this.region(regionName)?.orders || {};
    },

    order(orderNo, regionName = _db.currentRegion) {
      return this.orders(regionName)[orderNo];
    },

    // ── Daily log helpers ──
    dailyLog(regionName = _db.currentRegion) {
      return this.region(regionName)?.dailyLog || {};
    },

    entriesForDate(date, regionName = _db.currentRegion) {
      return this.dailyLog(regionName)[date] || [];
    },

    // ── Technician helpers ──
    technicians(regionName = _db.currentRegion) {
      return this.region(regionName)?.technicians || [];
    },
  };
})();
