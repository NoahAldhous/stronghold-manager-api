from flask import Blueprint
from controllers.classDemesneEffectsController import create_class_demesne_effects_table, populate_class_demesne_effects_table, get_all_class_demesne_effects, get_class_demesne_effects_by_class_id, clear_class_demesne_effects_table

class_demesne_effects_bp = Blueprint("class_demesne_effects", __name__)

@class_demesne_effects_bp.route("/create", methods=["POST"])
def create_class_demesne_effects_table_route():
    return create_class_demesne_effects_table()

@class_demesne_effects_bp.route("/populate", methods=["POST"])
def populate_class_demesne_effects_table_route():
    return populate_class_demesne_effects_table()

@class_demesne_effects_bp.route("/", methods=["GET"])
def get_all_class_demesne_effects_route():
    return get_all_class_demesne_effects()

@class_demesne_effects_bp.route("/id/<id>", methods=["GET"])
def get_class_demesne_effects_by_class_id_route(id):
    return get_class_demesne_effects_by_class_id(id)

@class_demesne_effects_bp.route("/", methods=["DELETE"])
def clear_class_demesne_effects_table_route():
    return clear_class_demesne_effects_table()
