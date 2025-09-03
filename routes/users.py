from flask import Blueprint, render_template, request, redirect, url_for
from services import crud_service, filter_service
from database.models import create_table

# Blueprint pentru utilizatori
users_bp = Blueprint("users", __name__, template_folder="../templates/users")

# Creează tabelul dacă nu există
create_table()

@users_bp.route("/")
def list_users():
    sort = request.args.get("sort")
    company = request.args.get("company")

    if sort == "name":
        users = filter_service.sort_by_name()
    elif sort == "age":
        users = filter_service.sort_by_age()
    elif company:
        users = filter_service.filter_by_company(company)
    else:
        users = crud_service.get_all_users()

    return render_template("users/list.html", users=users)

@users_bp.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        crud_service.add_user(
            request.form["firstName"],
            request.form["lastName"],
            int(request.form["age"]),
            request.form["email"],
            request.form["company"]
        )
        return redirect(url_for("users.list_users"))
    return render_template("users/add.html")

@users_bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = crud_service.get_user(user_id)
    if request.method == "POST":
        crud_service.update_user(
            user_id,
            request.form["firstName"],
            request.form["lastName"],
            int(request.form["age"]),
            request.form["email"],
            request.form["company"]
        )
        return redirect(url_for("users.list_users"))
    return render_template("users/edit.html", user=user)

@users_bp.route("/delete/<int:user_id>")
def delete_user(user_id):
    crud_service.delete_user(user_id)
    return redirect(url_for("users.list_users"))

@users_bp.route("/details/<int:user_id>")
def user_details(user_id):
    user = crud_service.get_user(user_id)
    return render_template("users/details.html", user=user)
