from flask import Flask, render_template
from routes.users import users_bp
from routes.reports import reports_bp
from database.models import create_table
from services.seed_service import seed_users_from_api
from services import crud_service

app = Flask(__name__)
app.secret_key = "secret-key"

# Blueprint-uri
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(reports_bp, url_prefix="/reports")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    create_table()
    # Populează baza de date din API dacă e goală
    if len(crud_service.get_all_users()) == 0:
        seed_users_from_api()
    app.run(debug=True)
