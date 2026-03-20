from flask import Blueprint
from controllers.retainers.actions.specialActionsController import create_special_actions_table, populate_special_actions_table

special_actions_bp = Blueprint("special_actions", __name__)

@special_actions_bp.route("/", methods=["POST"])
def create_special_actions_table_route():
    return create_special_actions_table()

@special_actions_bp.route("/populate", methods=["POST"])
def populate_special_actions_table_route():
    return populate_special_actions_table()