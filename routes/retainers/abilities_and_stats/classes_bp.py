from flask import Blueprint
from controllers.retainers.abilities_and_stats.classesController import create_classes_table, populate_classes_table

classes_bp = Blueprint("classes", __name__)

@classes_bp.route("/", methods=["POST"])
def create_classes_table_route():
    return create_classes_table()

@classes_bp.route("/populate", methods=["POST"])
def populate_classes_table_route():
    return populate_classes_table()