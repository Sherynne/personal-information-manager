📁 Personal Info Manager

A Python Command Line Interface (CLI) application for managing personal user information.
This project is beginner-friendly but designed to be portfolio-ready, showcasing Python skills, file handling, basic security, and CLI development.

 Secure login system

Strong password enforcement:

At least 8 characters

Uppercase letter

Lowercase letter

Number

Special character

Password hashing using SHA-256

Compatible with PyCharm Run Console and terminal

CRUD operations for users

Add new users with UUID-based IDs

View all users

Search by name or ID

Update user details

Delete users

Data export

Export user data to CSV for reporting or backup

Input validation

Age validation (0–120)

Prevents invalid inputs

Time-stamped records

Each user entry stores creation date and time

💻 Installation

Clone this repository:

git clone https://github.com/your-username/personal-info-manager.git


Navigate into the project folder:

cd personal-info-manager


(Optional) Create a virtual environment:

python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate


Run the program:

python LEARNING.py


⚠️ On first run, you will be asked to create a strong password.

🛠 Usage

After login, the menu appears:

=== Personal Info Manager ===
1. Add user
2. View users
3. Search user
4. Update user
5. Delete user
6. Export to CSV
7. Exit


Type the number corresponding to the action you want.

All data is stored locally in users.json.

Exported CSV is saved as users.csv.

✅ Project Goals

Learn Python basics:

Variables

Input/output

Files and JSON handling

Practice building a menu-driven CLI program

Understand basic security: password hashing & validation

Manage structured data (CRUD operations)

Prepare a portfolio-ready GitHub project

📝 Notes

Avoid pushing sensitive files like:

password.txt

users.csv (if it contains real data)

Use .gitignore for safety:

__pycache__/
*.pyc
*.csv
*.json
password.txt

🔖 Technologies Used

Python 3.x

JSON for data storage

CSV for data export

SHA-256 hashing for password security
