from flask import Blueprint
from controllers.strongholdTypesController import create_stronghold_types_table, populate_stronghold_types_table, add_new_stronghold_type, get_all_stronghold_types, get_stronghold_type_and_features_by_id, update_stronghold_type_by_id, delete_stronghold_type_by_id

stronghold_types_bp = Blueprint("stronghold_typs", __name__)

@stronghold_types_bp.route("/", methods=["POST"])
def create_stronghold_types_table_route():
    return create_stronghold_types_table()

@stronghold_types_bp.route("/populate", methods=["POST"])
def populate_stronghold_types_table_route():
    return populate_stronghold_types_table()

@stronghold_types_bp.route("/add", methods=["POST"])
def add_new_stronghold_type_route():
    return add_new_stronghold_type()

@stronghold_types_bp.route("/", methods=["GET"])
def get_all_stronghold_types_route():
    return get_all_stronghold_types()

@stronghold_types_bp.route("/<id>", methods=["GET"])
def get_stronghold_type_and_features_by_id_route(id):
    return get_stronghold_type_and_features_by_id(id)

@stronghold_types_bp.route("/<id>", methods=["UPDATE"])
def update_stronghold_type_by_id_route(id):
    return update_stronghold_type_by_id(id)

@stronghold_types_bp.route("/<id>", methods=["DELETE"])
def delete_stronghold_type_by_id_route(id):
    return delete_stronghold_type_by_id(id)