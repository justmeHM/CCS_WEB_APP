# Copilot instructions for this repo

This file captures the minimal, actionable knowledge an AI coding agent needs to be immediately productive working on this project.

## Big picture
- Single Python application: `main.py` is the entrypoint and contains modular sections (Configuration, Parser, Normalizer, Excel manager, Updater, Data Propagator, GUI). Treat the file as a small monorepo split by clearly labelled sections.
- Purpose: parse WhatsApp refuelling messages ("REFUELING TEMPLATE") and update an Excel workbook. Also supports a data propagation step that backfills previous visit dates and diesel levels.

## Key components & boundaries
- `Config`: default paths and parsing variations (`variation_mapping`, `numeric_fields`, `allowed_sources`). Update here for site-specific mappings.
- `MessageParser` / `DataNormalizer`: responsibility — extract fields from raw chat text and normalize (site id, date, supplier, numeric values). Date format expected: `dd/mm/yy` or `dd/mm/YYYY`.
- `ExcelManager` / `DataUpdater`: read/write Excel using `openpyxl`. Excel header discovery searches first 20 rows for required column names.
- `DataPropagator`: independent module that runs propagation logic and creates a backup before modifying the workbook.
- `AutomationGUI` / `AutomationController`: GUI calls controller methods; controller orchestrates parse → export unmatched → update → propagate.

## Important file/dir conventions
- Excel file path: configured in `Config.excel_file`. Example defaults point to `Desktop/.../new ccs report.xlsx` — change to your environment.
- Backups are placed in `<excel_dir>/backups/` and unmatched blocks CSVs in `<excel_dir>/unmatched_blocks/`.
- Required/recognized Excel columns (examples): `SITE ID`, `CURRENT VISIT DATE`, `CURRENT DG RUN HOURS`, `NAME OF TECHNICIAN`. DataPropagator expects `PREVIOUS VISIT DATE`, `PREVIOUS DIESEL LEVEL`, `FUEL LEFT ON SITE`.

## Parsing and data rules (explicit)
- Message delimiter: parser splits on the literal `REFUELING TEMPLATE` (case insensitive).
- Site ID normalization looks for tokens like `CBT123A` and converts to `IHS_CBT_123A` style.
- Date extraction uses regex `Date[: -] dd/mm/yy` and accepts `%d/%m/%y` and `%d/%m/%Y`.
- Numeric conversion: commas removed; returns integer or float; when configured with `allow_faulty=True` returns the sentinel string `FAULTY` when conversion fails.
- Duplicate check for adding rows: key is `(CURRENT DG RUN HOURS, SITE ID)` as strings and entries older-or-equal to the sheet's `last_date` are skipped.

## Developer workflows & commands
- Run GUI (Windows PowerShell):
```
python main.py
```
- Dependencies: `openpyxl` is required (Tkinter is provided by standard Python on most Windows installs). If missing, install with:
```
pip install openpyxl
```
- Quick programmatic runs (non-GUI): import `AutomationController` from `main.py` and call `run(chat_file)` or `run_propagation()` in a separate script or REPL.

## Patterns and gotchas for contributors
- The code is a single-file modular layout; prefer editing existing named sections rather than adding scattered functions.
- Header discovery is fuzzy: headers are matched by substring and uppercase. If tests fail to find headers, check your workbook header row and exact column names.
- Date comparisons rely on the sheet's parsed `CURRENT VISIT DATE` format. Ensure the Excel date cells are either datetimes or strings formatted as `dd/mm/YYYY`.
- Large `SITE_TECHNICIAN_MAP` exists in the file — update here if mapping changes. It's authoritative for technician names.

## When to create/update tests
- Add unit tests around `DataNormalizer.normalize_site_id`, `normalize_date`, and `MessageParser._parse_block` — these encapsulate the fragile parsing rules.

## What to ask the repo owner (if unclear)
- Preferred default Excel path and canonical sheet names (fuel vs MS sheet).
- Any site ID patterns that differ from the assumed `CBT` naming.

---
If you'd like, I can: (a) add a minimal `requirements.txt`, (b) extract modules into a package layout, or (c) add a small script that runs `AutomationController` headlessly for CI. Which would you prefer?
