from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint("auth", __name__, template_folder="../templates/auth")

ADMIN_EMAIL = "admin@usersapp.com"
ADMIN_PASSWORD = "admin123"

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session["admin"] = True
            flash("Welcome, Admin!", "success")
            return redirect(url_for("users.list_users"))
        else:
            flash("Invalid credentials!", "danger")
    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("admin", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))
