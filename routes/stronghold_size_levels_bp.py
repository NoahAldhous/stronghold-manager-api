from flask import Blueprint
from controllers.strongholdSizeLevelsController import create_stronghold_size_levels_table, insert_new_stronghold_size_level, populate_stronghold_size_levels_table, get_all_stronghold_size_levels, get_stronghold_size_by_level, get_stronghold_size_levels_by_type_id, update_stronghold_size_level_by_id, delete_stronghold_size_level_by_id, clear_stronghold_size_levels_table

stronghold_size_levels_bp = Blueprint("stronghold_size_levels", __name__)

@stronghold_size_levels_bp.route("/", methods=["POST"])
def create_stronghold_size_levels_table_route():
    return create_stronghold_size_levels_table()

@stronghold_size_levels_bp.route("/add", methods=["POST"])
def insert_new_stronghold_size_level_route():
    return insert_new_stronghold_size_level()

@stronghold_size_levels_bp.route("/populate", methods=["POST"])
def populate_stronghold_size_levels_table_route():
    return populate_stronghold_size_levels_table()

@stronghold_size_levels_bp.route("/", methods=["GET"])
def get_all_stronghold_size_levels_route():
    return get_all_stronghold_size_levels()

@stronghold_size_levels_bp.route("/level/<level>", methods=["GET"])
def get_stronghold_size_by_level_route(level):
    return get_stronghold_size_by_level(level)

@stronghold_size_levels_bp.route("/type/<id>", methods=["GET"])
def get_stronghold_size_levels_by_type_id_route(id):
    return get_stronghold_size_levels_by_type_id(id)

@stronghold_size_levels_bp.route("/<id>", methods=["PATCH"])
def update_stronghold_size_level_by_id_route(id):
    return update_stronghold_size_level_by_id(id)

@stronghold_size_levels_bp.route("/<id>", methods=["DELETE"])
def delete_stronghold_size_level_by_id_route(id):
    return delete_stronghold_size_level_by_id(id)

@stronghold_size_levels_bp.route("/clear", methods=["DELETE"])
def clear_stronghold_size_levels_table_route():
    return clear_stronghold_size_levels_table