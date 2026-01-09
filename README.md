📁 Personal Info Manager

A Python Command Line Interface (CLI) application for managing personal user information.
This project is beginner-friendly but designed to be portfolio-ready, showcasing Python skills, file handling, basic security, and CLI development.

 Features

Secure login system

Strong password enforcement (uppercase, lowercase, number, special character)

Password hashing using SHA-256

Compatible with both PyCharm Run Console and terminal

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
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows


Run the program:

python LEARNING.py


⚠️ On first run, you will be asked to create a strong password.

🛠 Usage

After login, you can interact with the menu:

=== Personal Info Manager ===
1. Add user
2. View users
3. Search user
4. Update user
5. Delete user
6. Export to CSV
7. Exit


Enter the number corresponding to the action you want.

All data is stored locally in users.json.

Exported CSV is saved as users.csv.

✅ Project Goals

Learn Python basics: variables, input/output, files, JSON

Practice building a CLI program with a menu system

Understand basic security: password hashing and validation

Manage structured data (CRUD operations)

Prepare a portfolio-ready project for GitHub

📝 Notes

Avoid pushing sensitive files like password.txt or users.csv if they contain real data.

Use .gitignore for safety:

__pycache__/
*.pyc
*.csv
*.json
password.txt

 Technologies Used

Python 

JSON for data storage

CSV for data export

SHA-256 hashing for password security
