# Neo Data Manager (v1.4) 🗃️ : Data Persistence & QR Engine 
Python Version | License: MIT

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

\`\`\`text
neo-data-manager/
├── main.py                # Entry point
├── RecordManager.py       # Core Class Logic
├── operations.py          # Search & Delete operations
├── storage.py             # JSON persistence logic
├── user_entry.py          # User input & validation
├── user_interface.py      # UI helpers & ID generation
├── qr_code.py             # QR Code generation engine
├── file_data.py           # Path verification utility
├── data.json              # Local database file
└── requirements.txt       # Library dependencies
\`\`\`

## 🚀 What's New in v1.4
This version is a major logic overhaul focusing on **Data Persistence** and **Search Accuracy**.

### 🛠️ Key Bug Fixes
* **Persistence Fix:** Resolved the "Data Amnesia" bug where records were being wiped on every restart.

* **Search Logic:** Fixed the "Loop Ghosting" error in `operations.py`. The system no longer prints "Not Found" multiple times for a single search.

* **Freedom of Entry:** Implemented `.lower().strip()` logic. Search is now case-insensitive and ignores accidental spaces.

* **State Management:** Fixed the `storage.py` loading error by correctly updating the `RecordManager` object attributes.

### ✨ New Feature: Advanced File Verification

* **Path Integrity Check:** Added a "Verify" utility that performs a deep scan of the system to locate the `data.json` file.

* **Environment Diagnostics:** The system now prints the Current Working Directory (CWD) and lists all items in the Base Directory to help users debug file permission or pathing issues.

* **Existence Validation:** Real-time feedback on whether the database file exists before attempting read/write operations.

A lightweight CLI-based database management system built for structured data storage, unique ID generation, and QR code output. Designed as a learning project for a first-year undergraduate, this tool demonstrates OOP, JSON handling, and basic data validation.

## 🚀 **Features**
Persistent Storage: JSON-based storage ensures all records are saved and retrievable.

Unique ID Generation: Each record gets a 10-character hexadecimal ID using uuid.

QR Code Export: Display any user’s record as a QR code with easy deletion after viewing.

## **Data Validation :**
Usernames cannot start/end with special characters or uppercase letters.

Names cannot have numbers, spaces, or special characters.

Interactive CLI Menu: Add, search, delete, or generate QR codes for users.

Safety Layer for Deletion: Confirms deletion for both individual users and the entire database to prevent mistakes.

## ✨ **Core Functions**

### **name_enter()**
Add a new user with username, first & last name, and unique ID.

### **search_func()**
Search users by username, full name, or ID.

### **delete_data()**
Delete all records with confirmation.

### **delete_person()**
Delete a single user’s data with confirmation.

### **qr_code()**
Generate and display a QR code for any user record.

### **file_load()**
Load existing records from lost.json.

### **save_names()**
Save all records back to lost.json.


## 🛠️ **Usage**
Navigate through the menu to add users, search, generate QR codes, or delete data.

The QR code will be automatically deleted after you close it.

Deletion operations always require confirmation to prevent accidental data loss.
## ⚠️ **Limitations & Known Issues**

### 1. Data Structure Boundaries

* **Duplicate Name Handling:** Currently, if two users have the same name (e.g., two "Manoj" entries), the search will only return the *first* one it finds. 

* **Username Sensitivity:** While Names are "free," Usernames are still strict keys. If you change a username manually in the JSON, the link to the record may break.

### 2. Search Constraints

* **Exact Match Only:** The search requires the full name. Searching for "Man" will not find "Manoj" (Partial matching is planned for v1.5).

* **Search Context:** You must select the specific search mode (ID vs. Name). A "Universal Search" that checks all fields at once is not yet implemented.

### 3. File System & Concurrency
* **No Multi-User Support:** The program is designed for a single user. If two instances of the program try to save to `data.json` at the same exact time, data corruption could occur.

* **JSON Dependency:** If the `data.json` file is manually edited and a comma is missed, the program will fail to boot until the JSON syntax is fixed.

* **Manual JSON Editing:** The program relies on strict JSON formatting. If a user manually edits `data.json` and breaks the syntax (e.g., a missing comma), the program will crash on boot.

### **QR Code Display**: 
**Works on most systems but may fail on some non-GUI environments.**

### **Error Handling**: 
**Minor exceptions are caught; however, incorrect manual file edits in lost.json may break loading.**

### **Readme Generated by AI**:
**Descriptions and technical highlights are AI-assisted; code is original.**

## 💡 **Notes**
This project is a learning experiment, not for production use.

Code can be extended for integrations like payment systems, temporary storage, or data sharing via QR.

Contributions and feedback are welcome!
## 📸 Gallery
<details>
  <summary>Click to see the Manager in action!</summary>
  
  ### Main Menu
  ![Menu](screenshots/menu.png)
  
  ### Adding Records (UUID Generation)
  ![Add](screenshots/add_record.png)
  
  ### Searching & QR Export
  ![QR](screenshots/qr_export.png)
</details>

---

## 🛠️ Installation & Setup

1. **Clone the Repo**

```bash
   git clone [https://github.com/Neo-Aizen07/neo-data-manager.git](https://github.com/Neo-Aizen07/neo-data-manager.git)
   cd neo-data-manager
   ```
2. **Install Dependencies**

 ```bash
 pip install -r requirements.txt
 ```

3. **Run the engine**
```bash
python main.py
📈 Version History
v1.0: Initial release with basic CRUD operations.
```bash
v1.1 : Fixed logic errors, improved JSON serialization, and optimized UUID generation.

v1.2 : Fixed logic errors, introduced username indexing, and added UI processing effects.

v1.3 Fixed username/first & last name validation errors.
Added keyboard input to close QR code instead of fixed sleep.
Enhanced menu for separate delete operations (entire data vs single user).

v1.4 (current) : Fixed data persistence, optimized search loops,file verification layers and added case-insensitive matching.
```