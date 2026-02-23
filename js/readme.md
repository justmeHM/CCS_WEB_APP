# CCS Fuel System — Modular Architecture

## Project Structure

```
ccs-fuel-system/
├── index.html              # HTML shell only (zero inline CSS/JS)
├── css/
│   └── styles.css          # All styles in one organised file
└── js/
    ├── app.js              # Entry point — imports modules, exposes App namespace, bootstraps app
    └── modules/
        ├── db.js           # Data store: DB object, save(), replaceDB()
        ├── nav.js          # Page routing, Escape key listener
        ├── ui.js           # Shared UI helpers (updateOrderCounter)
        ├── regions.js      # Region & technician CRUD + rename modal
        ├── orders.js       # Order create/allocate/render/clone/edit/delete + overage modal
        ├── daily.js        # Daily log: add/save/edit/delete entries, accordion, summary modal
        ├── leaderboard.js  # Leaderboard render + tech history modal
        └── reports.js      # XLSX export, JSON backup/restore, unalloc report, backup banner
```

## Module Responsibilities

| Module | Responsibility |
|---|---|
| `db.js` | Single source of truth. All reads/writes go through `DB` and `save()`. |
| `nav.js` | Switches active section, keeps nav buttons in sync, fires page-specific init. |
| `ui.js` | Shared DOM helpers used by multiple modules (stat tiles, counter badge). |
| `regions.js` | All region and technician CRUD, rename modal logic. |
| `orders.js` | Full order lifecycle: create → allocate → render → edit → clone → delete. Also owns overage comment modal. |
| `daily.js` | Daily fuel entry workflow, log view, history cards, edit/delete entries, daily summary modal. |
| `leaderboard.js` | Leaderboard rendering with filters, tech history drill-down modal. |
| `reports.js` | XLSX export (3 sheets), JSON backup/restore, unallocated report, backup status banner. |

## Global `App` Namespace

All HTML `onclick` attributes reference `App.functionName()`. This keeps the global
scope clean — only one name (`App`) is added to `window`.

```html
<!-- HTML -->
<button onclick="App.createOrder()">Create</button>
```

```js
// app.js wires it up
window.App = { createOrder, allocateFuel, ... };
```

## Adding a New Feature

1. Add business logic to the relevant module (or create a new one in `js/modules/`).
2. Export the new function(s).
3. Import them in `app.js` and add to `window.App`.
4. Add any new HTML to `index.html`, any new styles to `css/styles.css`.

## Deployment

The app is a **fully static single-page app** — no build step required.
Just serve the folder from any static host or open `index.html` directly in a browser.

> **Note:** Because `js/app.js` uses ES module `import` statements (`type="module"`),
> the files must be served over HTTP/HTTPS (not `file://`). Use a simple local server:
> ```bash
> npx serve .
> # or
> python3 -m http.server 8080
> ```