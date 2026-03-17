from flask import Blueprint
from controllers.retainers.abilities_and_stats.abilitiesController import create_abilities_table, populate_abilities_table

abilities_bp = Blueprint("abilities", __name__)

@abilities_bp.route("/", methods=["POST"])
def create_abilities_table_route():
    return create_abilities_table()

@abilities_bp.route("/populate", methods=["POST"])
def populate_abilities_table_route():
    return populate_abilities_table()