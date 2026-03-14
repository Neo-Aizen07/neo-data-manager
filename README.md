# Neo Data Manager v1.6 🗃️

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
├── search.py          # 🔍 Search by ID or username
├── user_entry.py      # ⌨️  Registration and input handling
├── user_interface.py  # 🎨 ID generation, timestamps
├── Validation.py      # ✅ Username validation rules
├── logger.py          # 📋 Logging system with timestamps
└── file_data.py       # 🛠️  File path diagnostics
```

---

## 🚀 What's New in v1.6

### Architecture
- **Full SQLite Migration:** Replaced `data.json` entirely with SQLite via Python's built-in `sqlite3`. No external dependencies added. This eliminates an entire class of corruption, sync, and state management issues that existed in the JSON layer.
- **Dict Layer Removed:** The in-memory `self.records` dict is gone. Every operation queries SQLite directly. Single source of truth, no sync required.
- **Context Manager Pattern:** Introduced `get_db()` in `storage.py` using `@contextmanager`. Connections auto-commit on success and auto-rollback on failure. No manual connection management anywhere in the codebase.
- **Atomic Transactions:** SQLite's transaction system guarantees all-or-nothing writes. Crash mid-write — SQLite recovers automatically on next open. Stronger than the previous temp file approach.

### Bug Fixes
- Fixed today filter in `log_his()` — was comparing full timestamp including seconds, now matches by date only using `strftime`
- Fixed `par_search_username()` — was printing last enumerate item instead of actual search result due to variable shadowing
- Fixed `display_data()` — silent empty screen on empty DB, now prints "No records found"
- Fixed `delete_1()` — missing commit meant single-user deletions were not persisting across sessions

---

## ✨ Features

- **Fully Offline** — zero internet dependency, zero cloud
- **SQLite Storage** — reliable, structured, corruption-resistant
- **Atomic Transactions** — automatic rollback on failure, SQLite-guaranteed
- **Unique ID Generation** — 10-character hex ID per record via `uuid`
- **Dual Search** — exact username, partial username match, or by ID
- **Validation** — strict username rules enforced before any record is created
- **Logging** — every action logged with timestamp, level, and message. Viewable from CLI.

---

## 🛠️ Core Functions

| Function | File | Description |
|---|---|---|
| `name_enter()` | user_entry.py | Register new user with validation |
| `search_func()` | search.py | Search by ID, exact or partial username |
| `delete_data()` | operations.py | Delete all records with confirmation |
| `delete_person()` | operations.py | Delete single user with confirmation |
| `get_db()` | storage.py | Context manager — handles connect, commit, rollback, close |
| `update_record()` | RecordManager.py | Insert or replace a record |
| `display_data()` | RecordManager.py | Display all records |
| `display_user()` | RecordManager.py | Display single user record |
| `log_menu()` | logger.py | View logs from CLI |
| `verify()` | file_data.py | Diagnose file paths and existence |

---

## ⚠️ Known Limitations

- **Single user only** — no concurrent access support
- **No universal search** — must choose ID or username mode explicitly
- **No multi-field search** — cannot search by name, only username or ID

---

## 🛠️ Installation

```bash
git clone https://github.com/Neo-Aizen07/neo-data-manager.git
cd neo-data-manager
python main.py
```

No external dependencies. Python 3.8+ only.

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
| v1.6 | Full SQLite migration, context manager pattern, dict layer removed, atomic transactions, bug fixes |

---

## 💡 Notes

- Built and debugged manually
- Contributions and feedback welcome
