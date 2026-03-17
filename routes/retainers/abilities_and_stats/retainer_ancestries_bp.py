from flask import Blueprint
from controllers.retainers.abilities_and_stats.retainerAncestriesController import create_retainer_ancestries_table, populate_retainer_ancestries_table

retainer_ancestries_bp = Blueprint("retainer_ancestries", __name__)

@retainer_ancestries_bp.route("/", methods=["POST"])
def create_retainer_ancestries_table_route():
    return create_retainer_ancestries_table()

@retainer_ancestries_bp.route("/populate", methods=["POST"])
def populate_retainer_ancestries_table_route():
    return populate_retainer_ancestries_table()