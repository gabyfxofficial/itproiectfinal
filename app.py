from flask import Flask, render_template, redirect, url_for, session, request, flash
from routes.users import users_bp
from routes.reports import reports_bp
from routes.auth import auth_bp
from database.models import create_table
from services.seed_service import seed_users_from_api
from services import crud_service

app = Flask(__name__)
app.secret_key = "secret-key"  # Secret key for session and flash messages

# Register Blueprints for modular route organization
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(reports_bp, url_prefix="/reports")
app.register_blueprint(auth_bp, url_prefix="/auth")

# Global access restriction for admin-only routes
@app.before_request
def restrict_access():
    open_routes = ["/auth/login", "/static", "/", "/favicon.ico"]
    # Allow public access to login, home, and static assets (CSS/JS)
    if not any(request.path.startswith(r) for r in open_routes):
        # Deny access if user is not logged in as admin
        if "admin" not in session:
            flash("❌ You must be logged in as Admin to perform this action.", "danger")
            return redirect(url_for("auth.login"))

# Home route
@app.route("/")
def home():
    return render_template("home.html")

# App entry point
if __name__ == "__main__":
    create_table()  # Ensure the users table exists
    # Automatically seed data if the database is empty
    if len(crud_service.get_all_users()) == 0:
        seed_users_from_api()
    app.run(debug=True)  # Run the app in debug mode
