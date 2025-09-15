from flask import Blueprint
from controllers.strongholdToughnessLevelsController import create_stronghold_toughness_levels_table, populate_stronghold_toughness_levels_table, insert_new_stronghold_toughness_level, get_all_stronghold_toughness_levels, get_stronghold_toughness_by_level, get_stronghold_toughness_levels_by_type_id, update_stronghold_toughness_level_by_id, delete_stronghold_toughness_level_by_id, clear_stronghold_toughness_levels_table

stronghold_toughness_levels_bp = Blueprint("stronghold_toughness_levels", __name__)

@stronghold_toughness_levels_bp.route("/", methods=["POST"])
def create_stronghold_toughness_levels_table_route():
    return create_stronghold_toughness_levels_table()

@stronghold_toughness_levels_bp.route("/populate", methods=["POST"])
def populate_stronghold_toughness_levels_table_route():
    return populate_stronghold_toughness_levels_table()

@stronghold_toughness_levels_bp.route("/add", methods=["POST"])
def insert_new_stronghold_toughness_level_route():
    return insert_new_stronghold_toughness_level()

@stronghold_toughness_levels_bp.route("/", methods=["GET"])
def get_all_stronghold_toughness_levels_route():
    return get_all_stronghold_toughness_levels()

@stronghold_toughness_levels_bp.route("/type/<id>", methods=["GET"])
def get_stronghold_toughness_levels_by_type_id_route(id):
    return get_stronghold_toughness_levels_by_type_id(id)

@stronghold_toughness_levels_bp.route("/level/<id>", methods=["GET"])
def get_stronghold_toughness_by_level_route(id):
    return get_stronghold_toughness_by_level(id)

@stronghold_toughness_levels_bp.route("/<id>", methods=["PATCH"])
def update_stronghold_toughness_level_by_id_route(id):
    return update_stronghold_toughness_level_by_id(id)

@stronghold_toughness_levels_bp.route("/<id>", methods=["DELETE"])
def delete_stronghold_toughness_level_by_id(id):
    return delete_stronghold_toughness_level_by_id(id)

@stronghold_toughness_levels_bp.route("/clear", methods=["DELETE"])
def clear_stronghold_toughness_levels_table():
    return clear_stronghold_toughness_levels_table()
    