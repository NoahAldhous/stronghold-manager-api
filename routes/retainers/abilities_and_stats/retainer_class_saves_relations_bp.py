from flask import Blueprint
from controllers.retainers.abilities_and_stats.retainerClassSavesRelationsController import create_retainer_class_saves_relations_table, populate_retainer_class_saves_relations_table

retainer_class_saves_relations_bp = Blueprint("retainer_class_saves_relations", __name__)

@retainer_class_saves_relations_bp.route("/", methods=["POST"])
def create_retainer_class_saves_relations_table_route():
    return create_retainer_class_saves_relations_table()

@retainer_class_saves_relations_bp.route("/", methods=["POST"])
def populate_retainer_class_saves_relations_table_route():
    return populate_retainer_class_saves_relations_table()