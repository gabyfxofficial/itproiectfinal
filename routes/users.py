from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services import crud_service, filter_service
from database.models import create_table

# Create a Blueprint for user-related routes
users_bp = Blueprint("users", __name__, template_folder="../templates/users")

# Ensure the users table is created before using it
create_table()

# Check if the current session belongs to an admin
def admin_required():
    if "admin" not in session:
        flash("You must be logged in as admin to perform this action.", "danger")
        return False
    return True

@users_bp.route("/")
def list_users():
    # Retrieve sorting and filtering options from query parameters
    sort = request.args.get("sort")
    company = request.args.get("company")

    # Sort or filter users based on provided parameters
    if sort == "name":
        users = filter_service.sort_by_name()
    elif sort == "age":
        users = filter_service.sort_by_age()
    elif company:
        users = filter_service.filter_by_company(company)
    else:
        users = crud_service.get_all_users()

    # Render the list of users
    return render_template("users/list.html", users=users)

@users_bp.route("/details/<int:user_id>")
def user_details(user_id):
    # Get details for a specific user
    user = crud_service.get_user(user_id)
    if not user:
        flash("User not found.", "warning")
        return redirect(url_for("users.list_users"))
    return render_template("users/details.html", user=user)

@users_bp.route("/add", methods=["GET", "POST"])
def add_user():
    # Allow only admin to add a new user
    if not admin_required():
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        # Add user with form data
        crud_service.add_user(
            firstName=request.form.get("firstName", "").strip(),
            lastName=request.form.get("lastName", "").strip(),
            age=int(request.form.get("age") or 0),
            email=request.form.get("email", "").strip(),
            company=request.form.get("company", "").strip(),
            phone=request.form.get("phone", "").strip(),
            iban=request.form.get("iban", "").strip(),
            country=request.form.get("country", "").strip(),
            address_street=request.form.get("address_street", "").strip(),
            address_city=request.form.get("address_city", "").strip(),
            address_state=request.form.get("address_state", "").strip(),
            address_postal=request.form.get("address_postal", "").strip(),
            role=request.form.get("role", "").strip()
        )
        flash("User added successfully!", "success")
        return redirect(url_for("users.list_users"))

    # Render the Add User page
    return render_template("users/add.html")

@users_bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    # Allow only admin to edit users
    if not admin_required():
        return redirect(url_for("auth.login"))

    user = crud_service.get_user(user_id)
    if not user:
        flash("User not found.", "warning")
        return redirect(url_for("users.list_users"))

    if request.method == "POST":
        # Update user details
        crud_service.update_user(
            user_id=user_id,
            firstName=request.form.get("firstName", "").strip(),
            lastName=request.form.get("lastName", "").strip(),
            age=int(request.form.get("age") or 0),
            email=request.form.get("email", "").strip(),
            company=request.form.get("company", "").strip(),
            phone=request.form.get("phone", "").strip(),
            iban=request.form.get("iban", "").strip(),
            country=request.form.get("country", "").strip(),
            address_street=request.form.get("address_street", "").strip(),
            address_city=request.form.get("address_city", "").strip(),
            address_state=request.form.get("address_state", "").strip(),
            address_postal=request.form.get("address_postal", "").strip(),
            role=request.form.get("role", "").strip()
        )
        flash("User updated successfully!", "success")
        return redirect(url_for("users.user_details", user_id=user_id))

    # Render the Edit User page
    return render_template("users/edit.html", user=user)

@users_bp.route("/delete/<int:user_id>")
def delete_user(user_id):
    # Allow only admin to delete users
    if not admin_required():
        return redirect(url_for("auth.login"))

    crud_service.delete_user(user_id)
    flash("User deleted successfully!", "info")
    return redirect(url_for("users.list_users"))
