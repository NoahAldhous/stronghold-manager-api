from flask import Blueprint
from controllers.retainers.retainersController import create_retainers_table, populate_retainers_table, get_all_retainers

retainers_bp = Blueprint("retainers", __name__)

@retainers_bp.route("/", methods=["POST"])
def create_retainers_table_route():
    return create_retainers_table()

@retainers_bp.route("/populate", methods=["POST"])
def populate_retainers_table_route():
    return populate_retainers_table()

@retainers_bp.route("/", methods=["GET"])
def get_all_retainers_route():
    return get_all_retainers()