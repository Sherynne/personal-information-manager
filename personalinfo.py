import csv
import json
import os
import uuid
import hashlib
from datetime import datetime

DATA_FILE = "users.json"
PASS_FILE = "password.txt"


# ------------------------------
# Environment Detection
# ------------------------------
def in_pycharm_run_console():
    """
    Detect if script is running in PyCharm Run Console.
    """
    return os.environ.get("PYCHARM_HOSTED") == "1"


# ------------------------------
# Password Input
# ------------------------------
def get_password(prompt="Password: "):
    """
    Get password safely:
    - Hidden in terminal
    - Visible in PyCharm Run Console
    """
    if in_pycharm_run_console():
        print("(PyCharm detected: password will be visible)")
        return input(prompt)
    else:
        try:
            import getpass
            return getpass.getpass(prompt)
        except Exception:
            # fallback to visible input
            print("(Warning: password will be visible)")
            return input(prompt)


# ------------------------------
# Security Helpers
# ------------------------------
def strong_password(pw):
    if len(pw) < 8:
        return False
    if not any(c.islower() for c in pw):
        return False
    if not any(c.isupper() for c in pw):
        return False
    if not any(c.isdigit() for c in pw):
        return False
    if not any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|" for c in pw):
        return False
    return True


def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()


def setup_password():
    if not os.path.exists(PASS_FILE):
        print("=== First time setup ===")

        while True:
            pw = get_password("Create a strong password: ")
            confirm = get_password("Confirm password: ")

            if pw != confirm:
                print("Passwords do not match.\n")
                continue

            if strong_password(pw):
                with open(PASS_FILE, "w") as f:
                    f.write(hash_password(pw))
                print("Strong password created.\n")
                break
            else:
                print("\nPassword must have:")
                print("- at least 8 characters")
                print("- uppercase letter")
                print("- lowercase letter")
                print("- number")
                print("- special character\n")


def login():
    if not os.path.exists(PASS_FILE):
        print("No password found. Please run setup first.")
        return False

    stored = open(PASS_FILE).read().strip()
    attempts = 3

    while attempts > 0:
        pw = get_password("Enter password: ")

        if hash_password(pw) == stored:
            print("Access granted.\n")
            return True
        else:
            attempts -= 1
            print(f"Wrong password. Attempts left: {attempts}\n")

    print("Too many failed attempts. Access locked.")
    return False


# ------------------------------
# Data Handling
# ------------------------------
def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_users(users):
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)


def get_valid_age():
    while True:
        age = input("Enter age: ")
        if age.isdigit() and 0 < int(age) < 120:
            return int(age)
        print("Invalid age.")


# ------------------------------
# CRUD Operations
# ------------------------------
def add_user():
    name = input("Name: ").strip()
    age = get_valid_age()

    user = {
        "id": str(uuid.uuid4())[:8],
        "name": name,
        "age": age,
        "created_at": datetime.now().isoformat()
    }

    users = load_users()
    users.append(user)
    save_users(users)
    print("User added.")


def view_users(users=None):
    users = users if users else load_users()
    if not users:
        print("No users found.")
        return

    for u in users:
        print("-" * 30)
        print(u)


def search_user():
    key = input("Search by name or ID: ").lower()
    users = load_users()
    results = [u for u in users if key in u["name"].lower() or key in u["id"]]
    view_users(results)


def delete_user():
    uid = input("Enter user ID to delete: ")
    users = load_users()
    new_users = [u for u in users if u["id"] != uid]

    if len(new_users) == len(users):
        print("User not found.")
    else:
        save_users(new_users)
        print("User deleted.")


def update_user():
    uid = input("Enter user ID to update: ")
    users = load_users()

    for u in users:
        if u["id"] == uid:
            print("Leave blank to keep current value.")
            new_name = input(f"New name ({u['name']}): ")
            new_age = input(f"New age ({u['age']}): ")

            if new_name.strip():
                u["name"] = new_name
            if new_age.isdigit():
                u["age"] = int(new_age)

            save_users(users)
            print("User updated.")
            return

    print("User not found.")


def export_csv():
    users = load_users()
    if not users:
        print("No users to export.")
        return

    with open("users.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=users[0].keys())
        writer.writeheader()
        writer.writerows(users)

    print("Exported to users.csv")


# ------------------------------
# Menu
# ------------------------------
def menu():
    while True:
        print("\n=== Personal Info Manager ===")
        print("1. Add user")
        print("2. View users")
        print("3. Search user")
        print("4. Update user")
        print("5. Delete user")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            search_user()
        elif choice == "4":
            update_user()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            export_csv()
        elif choice == "7":
            break
        else:
            print("Invalid option.")


# ------------------------------
# Main
# ------------------------------
if __name__ == "__main__":
    setup_password()
    if login():
        print("Login successful. Loading menu...\n")
        menu()
        input("\nPress Enter to exit...")  # Keep console open in PyCharm