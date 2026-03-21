# Neo Data Manager v1.7 🗃️

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A privacy-first, offline CLI database management system built in Python. No cloud. No internet required. Your data stays on your machine.

---

## 📂 Project Structure

```
neo-data-manager/
├── main.py            # 🟢 Entry point, menu loop
├── RecordManager.py   # 🧠 Core logic, all DB operations
├── storage.py         # 💾 SQLite connection, context manager
├── operations.py      # ⚙️  Deletion logic with confirmation
├── search.py          # 🔍 Combined search — ID, exact and partial username
├── user_entry.py      # ⌨️  Registration and input handling
├── user_interface.py  # 🎨 ID generation, timestamps, intro
├── Validation.py      # ✅ Username validation rules
├── logger.py          # 📋 Logging system with level filtering
├── file_data.py       # 🛠️  System status checker
└── neo_db.py          # 🧪 pytest test suite
```

---

## 🚀 What's New in v1.7

### Code Quality
- **Type Hints:** Full type annotations across all files — function parameters, return types, and imported types via `TYPE_CHECKING` to avoid circular imports.
- **pytest Suite:** 11 automated tests covering validation, insert, delete, search, and edge cases. Run with `pytest neo_db.py`.
- **Schema Hardening:** Added `NOT NULL` and `UNIQUE` constraints to the SQLite schema. Database rejects incomplete or duplicate data at the storage level, not just the application level.

### Features
- **Combined Search:** Single input searches by ID first, then exact username, then partial username match — automatically, in one flow. No more choosing search mode manually.
- **Rich Terminal Formatting:** All output now uses the `rich` library — bordered tables for records, colored panels for user details, color-coded log entries, and styled error/success messages.
- **Log Level Filtering:** Log menu now supports filtering by INFO, WARNING, ERROR, and CRITICAL separately, in addition to today and all-logs views.
- **System Status:** Menu option 5 replaced the old debug dump with a clean status table showing database path, total record count, and log file status.

### Bug Fixes
- Fixed `log_his()` crash — `lines` variable referenced instead of `line` in the loop, causing `AttributeError` on every log view
- Fixed `display_data()` — table rendered before empty check, now shows "No records found" correctly
- Fixed log message — "Record not displayed and found" replaced with accurate message and correct log level
- Removed leftover `test_record_insertions` method that was incorrectly placed inside `RecordManager` class

### UX Fixes
- Menu labels rewritten — "Enter Details (For First Time Data Entry)" → "Register New User"
- Intro screen cleaned — removed raw file path, replaced with styled privacy-first tagline
- Validation error messages now styled in red via rich
- `user_entry.py` typos fixed — "stores" → "stored", "Usermane" → "Username"
- Minimum username length increased from 3 to 5 characters
- All error and success messages consistently styled across the codebase

---

## ✨ Features

- **Fully Offline** — zero internet dependency, zero cloud
- **SQLite Storage** — reliable, structured, corruption-resistant
- **Atomic Transactions** — automatic rollback on failure, SQLite-guaranteed
- **Unique ID Generation** — 10-character hex ID per record via `uuid`
- **Combined Search** — one input searches ID, exact username, and partial username automatically
- **Validation** — strict username rules enforced before any record is created
- **Rich Display** — color-coded tables, panels, and messages throughout
- **Logging** — every action logged with timestamp and level, filterable from CLI

---

## 🛠️ Core Functions

| Function | File | Description |
|---|---|---|
| `name_enter()` | user_entry.py | Register new user with validation |
| `combined_search()` | search.py | Search by ID, exact or partial username in one flow |
| `delete_data()` | operations.py | Delete all records with confirmation |
| `delete_person()` | operations.py | Delete single user with confirmation |
| `get_db()` | storage.py | Context manager — handles connect, commit, rollback, close |
| `update_record()` | RecordManager.py | Insert a record, rejects duplicates |
| `display_data()` | RecordManager.py | Display all records as rich table |
| `display_user()` | RecordManager.py | Display single user as rich panel |
| `log_menu()` | logger.py | View and filter logs from CLI |
| `verify()` | file_data.py | System status — DB, records count, log file |

---

## ⚠️ Known Limitations

- **Single user only** — no concurrent access support
- **No multi-field search** — search by username or ID only

---

## 🛠️ Installation

```bash
git clone https://github.com/Neo-Aizen07/neo-data-manager.git
cd neo-data-manager
pip install rich
python main.py
```

**Run tests:**
```bash
pytest neo_db.py
```

Python 3.8+ required.

---

## 📈 Version History

| Version | Highlights |
|---|---|
| v1.0 | Initial release, basic CRUD |
| v1.1 | Fixed logic errors, improved JSON serialization, UUID generation |
| v1.2 | Username indexing, UI processing effects |
| v1.3 | Validation fixes, keyboard QR close, separate delete operations |
| v1.4 | Data persistence fix, atomic saves, file verification, case-insensitive search |
| v1.5 | Duplicate username fix, partial search, standard logging, mutable state overhaul |
| v1.6 | Full SQLite migration, context manager pattern, dict layer removed, atomic transactions |
| v1.7 | Type hints, pytest suite, combined search, rich formatting, log level filtering, schema hardening, UX fixes |

---

## 💡 Notes

- Built and debugged manually
- Contributions and feedback welcome
