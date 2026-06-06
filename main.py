import re
import random
import string
common_passwords = [
    "123456",
    "password",
    "qwerty",
    "admin",
    "welcome",
    "letmein"
]

def analyze_password(password):

    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase length to at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    if password.lower() in common_passwords:
        suggestions.append("Avoid commonly used passwords.")
        score = 0

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score <= 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print("-", s)
    else:
        print("\nExcellent password!")

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))

    print("\nGenerated Password:")
    print(password)

while True:

    print("\n===== PASSWORD TOOL =====")
    print("1. Analyze Password")
    print("2. Generate Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pwd = input("Enter Password: ")
        analyze_password(pwd)

    elif choice == "2":
        generate_password()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
        