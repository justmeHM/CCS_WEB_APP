/**
 * db.js — Data Store
 * Single source of truth for all application data.
 * Handles localStorage persistence.
 */

const DB_KEY = 'ccs_fuel_orders_v4';

const DB_DEFAULT = {
  currentRegion: 'New CCS',
  regions: {
    'New CCS': {
      technicians: [],
      technicianPlates: {},
      orders: {},
      dailyLog: {}
    }
  }
};

// Initialise DB from localStorage or use defaults
export let DB = JSON.parse(localStorage.getItem(DB_KEY)) || structuredClone(DB_DEFAULT);

/** Persist current DB state to localStorage */
export function save() {
  localStorage.setItem(DB_KEY, JSON.stringify(DB));
}

/** Replace entire DB (used by restore) */
export function replaceDB(newDB) {
  DB = newDB;
  save();
}