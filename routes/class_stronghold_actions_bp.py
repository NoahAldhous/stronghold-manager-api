from flask import Blueprint
from controllers.classStrongoldActionsController import create_class_stronghold_actions_table, populate_class_stronghold_actions_table, get_all_class_stronghold_actions, get_class_stronghold_actions_by_class_id, clear_class_stronghold_actions_table

class_stronghold_actions_bp = Blueprint("class_stronghold_actions", __name__)

@class_stronghold_actions_bp.route("/create", methods=["POST"])
def create_class_stronghold_actions_table_route():
    return create_class_stronghold_actions_table()

@class_stronghold_actions_bp.route("/populate", methods=["POST"])
def populate_class_stronghold_actions_table_route():
    return populate_class_stronghold_actions_table()

@class_stronghold_actions_bp.route("/", methods=["GET"])
def get_all_class_stronghold_actions_route():
    return get_all_class_stronghold_actions()

@class_stronghold_actions_bp.route("/id/<id>", methods=["GET"])
def get_class_stronghold_actions_by_class_id_route(id):
    return get_class_stronghold_actions_by_class_id(id)

@class_stronghold_actions_bp.route("/clear", methods=["DELETE"])
def clear_class_stronghold_actions_table_route():
    return clear_class_stronghold_actions_table()