from flask import Blueprint
from controllers.strongholdConstructionLevelsController import create_stronghold_construction_levels_table, insert_new_stronghold_construction_level, get_all_stronghold_construction_levels, get_stronghold_construction_by_level, get_stronghold_construction_levels_by_type_id, update_stronghold_construction_level_by_id, delete_stronghold_construction_level_by_id

stronghold_construction_levels_bp = Blueprint("Stronghold_construction_levels", __name__)

@stronghold_construction_levels_bp.route("/", methods=["POST"])
def create_stronghold_construction_levels_table_route():
    return create_stronghold_construction_levels_table()

@stronghold_construction_levels_bp.route("/add", methods=["POST"])
def insert_new_stronghold_construction_level_route():
    return insert_new_stronghold_construction_level()

@stronghold_construction_levels_bp.route("/", methods=["GET"])
def get_all_stronghold_construction_levels_route():
    return get_all_stronghold_construction_levels()

@stronghold_construction_levels_bp.route("/level/<level>", methods=["GET"])
def get_stronghold_construction_by_level_route(level):
    return get_stronghold_construction_by_level(level)

@stronghold_construction_levels_bp.route("/type/<id>", methods=["GET"])
def get_stronghold_construction_levels_by_type_id_route(id):
    return get_stronghold_construction_levels_by_type_id(id)

@stronghold_construction_levels_bp.route("/<id>", methods=["PATCH"])
def update_stronghold_construction_level_by_id_route(id):
    return update_stronghold_construction_level_by_id(id)

@stronghold_construction_levels_bp.route("/<id>", methods=["DELETE"])
def delete_stronghold_construction_level_by_id_route(id):
    return delete_stronghold_construction_level_by_id(id)