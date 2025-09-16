from flask import Blueprint
from controllers.strongholdClassesController import create_stronghold_classes_table, populate_stronghold_classes_table, get_all_stronghold_classes, get_stronghold_class_by_class_name, get_stronghold_class_by_class_id, clear_stronghold_classes_table

stronghold_classes_bp = Blueprint("stronghold_classes", __name__)

@stronghold_classes_bp.route("/create", methods=["POST"])
def create_stronghold_classes_table_route():
    return create_stronghold_classes_table()

@stronghold_classes_bp.route("/populate", methods=["POST"])
def populate_stronghold_classes_table_route():
    return populate_stronghold_classes_table()

@stronghold_classes_bp.route("/", methods=["GET"])
def get_all_stronghold_classes_route():
    return get_all_stronghold_classes()

@stronghold_classes_bp.route("/name/<name>", methods=["GET"])
def get_stronghold_class_by_class_name_route(name):
    return get_stronghold_class_by_class_name(name)

@stronghold_classes_bp.route("/id/<id>", methods=["GET"])
def get_stronghold_class_by_class_id_route(id):
    return get_stronghold_class_by_class_id(id)

@stronghold_classes_bp.route("/clear", methods=["DELETE"])
def clear_stronghold_classes_table_route():
    return clear_stronghold_classes_table()