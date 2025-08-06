from flask import Blueprint
from controllers.usersController import get_all_users

users_bp = Blueprint("users", __name__)

GET_ALL_USERS = "SELECT * FROM users;"

users_bp.route("/", methods=["GET"])(get_all_users)
