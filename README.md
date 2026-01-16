# 📁 Personal Info Manager

A professional Python-based **Command Line Interface (CLI)** application designed for the secure management of personal user records. This project demonstrates core competencies in **Data Engineering**, **Cybersecurity (Hashing)**, and **CRUD Application Logic**.

---

## ✨ Features

### 🔐 Advanced Security
* **Secure Authentication**: Access is protected by a mandatory login system.
* **SHA-256 Hashing**: Passwords are never stored in plain text; they are hashed using the SHA-256 algorithm for maximum security.
* **Strong Password Enforcement**: The system requires a complex password (8+ characters, uppercase, lowercase, numbers, and special characters).

### 🛠️ Data Management (CRUD)
* **Create**: Generate new user records with unique **UUID-based identifiers**.
* **Read**: View a complete list of users or perform targeted searches by Name or ID.
* **Update**: Modify existing user details dynamically.
* **Delete**: Securely remove records from the local database.

### 📊 Reporting & Integrity
* **CSV Data Export**: One-click export of all user data for external reporting or backups.
* **Robust Validation**: Built-in logic to handle incorrect inputs and enforce age limits (0–120).
* **Automated Timestamps**: Every record automatically stores the exact date and time of creation.

---

## 🚀 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/YourUsername/personal-info-manager.git](https://github.com/YourUsername/personal-info-manager.git)
   cd personal-info-manager
Set Up Virtual Environment (Optional but Recommended)

Bash

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
Run the Program

Bash

python LEARNING.py
⚠️ Note: On your first run, you will be prompted to set up a master administrative password.

🛠 Usage
After a successful login, navigate the system using the interactive menu:

Plaintext

=== Personal Info Manager ===
1. Add user
2. View users
3. Search user
4. Update user
5. Delete user
6. Export to CSV
7. Exit
Storage: Persistent data is stored locally in users.json.

Export: Generated reports are saved as users.csv.

💻 Technical Stack
Language: Python 3.x

Data Formats: JSON (Persistent Storage), CSV (Exporting)

Encryption: SHA-256 via Python's hashlib

Identifiers: UUID (Universally Unique Identifier)

📝 Project Goals & Learning Outcomes
This project was developed to master several key software engineering concepts:

Object-Oriented Thinking: Managing structured user data.

Security First: Implementing password validation and secure hashing.

File I/O: Handling asynchronous data reading and writing with JSON and CSV.

CLI Design: Building a user-friendly, menu-driven terminal experience.

⚠️ Security Notice
To ensure data privacy, the following files are excluded from version control via .gitignore:

password.txt (Administrative credentials)

users.json / users.csv (Sensitive user data)

__pycache__/ (Compiled Python files)
