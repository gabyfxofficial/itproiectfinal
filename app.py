from flask import Flask, render_template, redirect, url_for, session, request, flash
from routes.users import users_bp
from routes.reports import reports_bp
from routes.auth import auth_bp
from database.models import create_table
from services.seed_service import seed_users_from_api
from services import crud_service

app = Flask(__name__)
app.secret_key = "secret-key"

# Blueprints
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(reports_bp, url_prefix="/reports")
app.register_blueprint(auth_bp, url_prefix="/auth")

# Restrictii globale pentru acces
@app.before_request
def restrict_access():
    open_routes = ["/auth/login", "/static", "/", "/favicon.ico"]
    # acces liber la home, login, css/js
    if not any(request.path.startswith(r) for r in open_routes):
        # nu e logat ca admin
        if "admin" not in session:
            flash("❌ You must be logged in as Admin to perform this action.", "danger")
            return redirect(url_for("auth.login"))

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    create_table()
    if len(crud_service.get_all_users()) == 0:
        seed_users_from_api()
    app.run(debug=True)
