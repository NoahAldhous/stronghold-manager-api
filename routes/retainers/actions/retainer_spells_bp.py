from flask import Blueprint
from controllers.retainers.actions.retainerSpellsController import create_retainer_spells_table, populate_retainer_spells_table

retainer_spells_bp = Blueprint("retainer_spells", __name__)

@retainer_spells_bp.route("/", methods=["POST"])
def create_retainer_spells_table_route():
    return create_retainer_spells_table()

@retainer_spells_bp.route("/populate", methods=["POST"])
def populate_retainer_spells_table_route():
    return populate_retainer_spells_table()