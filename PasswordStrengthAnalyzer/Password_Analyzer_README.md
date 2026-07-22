# Password Strength Analyzer

## Project Overview

The Password Strength Analyzer is a beginner-friendly Python project that evaluates the strength of a user-entered password. The program checks various password characteristics such as length, complexity, and uniqueness, and provides suggestions for creating stronger passwords.

This project is useful for understanding basic Python concepts like functions, conditional statements, loops, file handling, and string manipulation.

---

## Features

* Checks password length.
* Verifies the presence of uppercase letters.
* Verifies the presence of lowercase letters.
* Checks for numeric digits.
* Checks for special characters.
* Detects commonly used weak passwords.
* Classifies passwords as:

  * Weak
  * Medium
  * Strong
* Suggests stronger password alternatives.
* Optional feature to prevent reuse of old passwords.

---

## Project Structure

```text
PasswordStrengthAnalyzer/
│
├── password_analyzer.py
├── old_passwords.txt
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python 3
* Built-in Python modules:

  * string
  * os (optional)

---

## How to Run the Project

### Step 1: Clone or Download the Project

Download the project files and place them in a folder named:

```text
PasswordStrengthAnalyzer
```

### Step 2: Open Terminal

Navigate to the project directory:

```bash
cd PasswordStrengthAnalyzer
```

### Step 3: Run the Program

```bash
python3 password_analyzer.py
```

---

## Sample Output

```text
===== Password Strength Analyzer =====
Enter your password: Hello123

Password Strength: Medium

Suggestions:
- Add at least one special character.

Suggested Strong Password:
Hello123@
```

---

## Optional Feature: Password Reuse Detection

The program can optionally check whether the entered password has already been used.

Store previously used passwords inside:

```text
old_passwords.txt
```

Example:

```text
Hello@123
Admin@2025
Password@123
```

If a user enters one of these passwords again, the program displays a warning.

---

## Future Enhancements

* Develop a graphical user interface using Tkinter.
* Store passwords in a database.
* Encrypt stored passwords.
* Add a password generator.
* Integrate with a web application.

---

## Author

Reetan Saha
