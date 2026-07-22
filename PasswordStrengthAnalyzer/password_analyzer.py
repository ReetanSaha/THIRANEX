import string


# Function to check password strength
def check_password_strength(password):

    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    # Check for special characters
    special_characters = string.punctuation

    if any(char in special_characters for char in password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Check uniqueness (simple check)
    common_passwords = [
        "password",
        "123456",
        "admin",
        "qwerty",
        "welcome",
        "password123"
    ]

    if password.lower() not in common_passwords:
        score += 1
    else:
        suggestions.append("Avoid common passwords.")

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


# Function to suggest a stronger password
def suggest_password(password):

    strong_password = password

    if len(strong_password) < 8:
        strong_password += "2025"

    if not any(char.isupper() for char in strong_password):
        strong_password += "A"

    if not any(char.islower() for char in strong_password):
        strong_password += "a"

    if not any(char.isdigit() for char in strong_password):
        strong_password += "1"

    if not any(char in string.punctuation for char in strong_password):
        strong_password += "@"

    return strong_password
import os

def check_reuse(password):

    file_path = "/Users/reetansaha/Documents/PasswordStrengthAnalyzer/old_passwords.txt"

    try:
        with open(file_path, "r") as file:
            old_passwords = file.read().splitlines()

        if password in old_passwords:
            return True

    except FileNotFoundError:
        print("File not found!")

    return False

# Main Program
print("===== Password Strength Analyzer =====")

password = input("Enter your password: ")
if check_reuse(password):
    print("\nWarning: You have used this password before.")

strength, suggestions = check_password_strength(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions:")
    for item in suggestions:
        print("-", item)

print("\nSuggested Strong Password:")
print(suggest_password(password))

