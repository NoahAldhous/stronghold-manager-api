from flask import Blueprint
from controllers.usersController import create_users_table, register_user, login_user, refresh, whoami, get_all_users, get_user_by_id, delete_user_by_id, update_user_password_by_id, update_user_permission_by_id, update_user_name_by_id, delete_users_table
from flask_jwt_extended import jwt_required
from utils.auth import roles_required

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["POST"])
def create_users_table_route():
    return create_users_table()

@users_bp.route("/register", methods=["POST"])
def register_user_route():
    return register_user()

@users_bp.route("/login", methods=["POST"])
def login_user_route():
    return login_user()

@users_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh_route():
    return refresh();

@users_bp.route("/me", methods=["GET"])
@jwt_required()
def whoami_route():
    return whoami()

@users_bp.route("/", methods=["GET"])
@roles_required("admin")
def get_all_users_route():
    return get_all_users()

@users_bp.route("/<user_id>/", methods=["GET"])
def get_user_route(user_id):
    return get_user_by_id(user_id)

@users_bp.route("/update/password/<user_id>", methods=["PATCH"])
def update_user_password_route(user_id):
    return update_user_password_by_id(user_id)

@users_bp.route("/update/permissions/<user_id>", methods=["PATCH"])
def update_user_permission_route(user_id):
    return update_user_permission_by_id(user_id)

@users_bp.route("/delete/<user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    return delete_user_by_id(user_id)

@users_bp.route("/update/user_name/<user_id>", methods=["PATCH"])
def update_user_name_route(user_id):
    return update_user_name_by_id(user_id)

@users_bp.route("/", methods=["DELETE"])
def delete_users_table_route():
    return delete_users_table()