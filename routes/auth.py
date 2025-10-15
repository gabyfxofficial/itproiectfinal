from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# Create a Blueprint for authentication routes
auth_bp = Blueprint("auth", __name__, template_folder="../templates/auth")

# Define admin credentials
ADMIN_EMAIL = "admin@usersapp.com"
ADMIN_PASSWORD = "admin123"

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Handle login form submission
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Check if provided credentials match admin credentials
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            # Store admin session and show success message
            session["admin"] = True
            flash("Welcome, Admin!", "success")
            return redirect(url_for("users.list_users"))
        else:
            # Show error message for invalid login
            flash("Invalid credentials!", "danger")
    # Render the login page template
    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    # Remove admin session and show logout message
    session.pop("admin", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
