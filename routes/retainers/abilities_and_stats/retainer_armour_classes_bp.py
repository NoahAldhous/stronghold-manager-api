from flask import Blueprint
from controllers.retainers.abilities_and_stats.retainerArmourClassesController import create_retainer_armour_classes_table, populate_retainer_armour_classes_table

retainer_armour_classes_bp = Blueprint("retainer_armour_classes", __name__)

@retainer_armour_classes_bp.route("/", methods=["POST"])
def create_retainer_armour_classes_table_route():
    return create_retainer_armour_classes_table()

@retainer_armour_classes_bp.route("/populate", methods=["POST"])
def populate_retainer_armour_classes_table_route():
    return populate_retainer_armour_classes_table()