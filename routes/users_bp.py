from flask import Blueprint
from controllers.usersController import get_all_users, create_user, get_user_by_id, delete_user_by_id, update_user_password_by_id, update_user_name_by_id, delete_users_table

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["POST"])
def create_user_route():
    return create_user()

@users_bp.route("/", methods=["GET"])
def get_all_users_route():
    return get_all_users()

@users_bp.route("/<user_id>/", methods=["GET"])
def get_user_route(user_id):
    return get_user_by_id(user_id)

@users_bp.route("/update/password/<user_id>", methods=["PATCH"])
def update_user_password_route(user_id):
    return update_user_password_by_id(user_id)

@users_bp.route("/delete/<user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    return delete_user_by_id(user_id)

@users_bp.route("/update/user_name/<user_id>", methods=["PATCH"])
def update_user_name_route(user_id):
    return update_user_name_by_id(user_id)

@users_bp.route("/", methods=["DELETE"])
def delete_users_table_route():
    return delete_users_table()