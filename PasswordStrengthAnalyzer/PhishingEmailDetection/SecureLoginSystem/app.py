from flask import Flask, render_template, redirect, url_for, flash, request
import sqlite3
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = "supersecretkey"

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# ---------------- DATABASE ----------------

def create_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

create_db()

# ---------------- USER CLASS ----------------

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username FROM users WHERE id=?",
        (user_id,)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return User(user[0], user[1])

    return None

# ---------------- HOME ----------------

@app.route("/")
def home():
    return redirect(url_for("login"))

# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        # Input validation
        if len(username) < 3:
            flash("Username must be at least 3 characters")
            return redirect(url_for("register"))

        if len(password) < 6:
            flash("Password must be at least 6 characters")
            return redirect(url_for("register"))

        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            # Prevent SQL Injection using parameterized query
            cursor.execute(
                "INSERT INTO users(username,email,password) VALUES(?,?,?)",
                (username, email, hashed_pw)
            )

            conn.commit()
            conn.close()

            flash("Registration Successful")
            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            flash("User already exists")
            return redirect(url_for("register"))

    return render_template("register.html")

# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, username, password FROM users WHERE email=?",
            (email,)
        )

        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[2], password):
            login_user(User(user[0], user[1]))
            return redirect(url_for("dashboard"))

        flash("Invalid Email or Password")

    return render_template("login.html")

# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template(
        "dashboard.html",
        username=current_user.username
    )

# ---------------- LOGOUT ----------------

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged Out Successfully")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)