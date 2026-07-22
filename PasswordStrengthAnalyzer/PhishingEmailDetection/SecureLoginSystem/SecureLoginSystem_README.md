# Secure Login System

A secure web-based login system developed using Flask that provides user authentication with password hashing, session management, and protection against common security vulnerabilities.

## Features

* User Registration
* User Login
* Secure Password Hashing using Bcrypt
* Session Management using Flask-Login
* Logout Functionality
* Input Validation
* SQL Injection Protection using Parameterized Queries
* Protected Dashboard Access
* Optional Two-Factor Authentication (2FA) using OTP
* QR Code Generation for Authenticator Apps

## Technologies Used

* Python 3
* Flask
* SQLite
* Flask-Bcrypt
* Flask-Login
* Flask-WTF
* PyOTP
* QRCode
* HTML

## Project Structure

```text
SecureLoginSystem/
│
├── app.py
├── users.db
├── requirements.txt
├── README.md
├── templates/
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
│
└── venv/
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd SecureLoginSystem
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Security Features

### Password Hashing

User passwords are securely hashed using Bcrypt before storing them in the database.

### SQL Injection Prevention

Parameterized SQL queries are used to prevent SQL injection attacks.

Example:

```python
cursor.execute(
    "SELECT * FROM users WHERE email=?",
    (email,)
)
```

### Session Management

Flask-Login manages user sessions and restricts access to protected pages.

### Logout

Authenticated users can securely terminate their sessions.

## Future Enhancements

* Email Verification
* Password Reset via Email
* Google Authenticator Integration
* Role-Based Access Control
* Account Lockout after Multiple Failed Attempts
* CSRF Protection Enhancements

## Author

Developed by Reetan Saha
