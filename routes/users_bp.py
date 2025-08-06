from flask import Blueprint
from controllers.usersController import get_all_users, create_user, get_user_by_id

users_bp = Blueprint("users", __name__)

users_bp.route("/", methods=["GET"])(get_all_users)
users_bp.route("/", methods=["POST"])(create_user)
users_bp.route("/<id>", methods=["GET"])(get_user_by_id(id))