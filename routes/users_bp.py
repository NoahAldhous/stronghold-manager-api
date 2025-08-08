from flask import Blueprint
from controllers.usersController import get_all_users, create_user, get_user_by_id

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
def get_all():
    return get_all_users()
@users_bp.route("/", methods=["POST"])
def create():
    return create_user()
@users_bp.route("/<user_id>/", methods=["GET"])
def get_user(user_id):
    return get_user_by_id(user_id)