from flask import Blueprint
from controllers.artisans.artisanUpgradeCostsController import create_artisan_upgrade_costs_table, populate_artisan_upgrade_costs_table, get_all_artisan_upgrade_costs

artisan_upgrade_costs_bp = Blueprint("artisan_upgrade_costs", __name__)

@artisan_upgrade_costs_bp.route("/", methods=["POST"])
def create_artisan_upgrade_costs_table_route():
    return create_artisan_upgrade_costs_table()

@artisan_upgrade_costs_bp.route("/populate", methods=["POST"])
def populate_artisan_upgrade_costs_table_route():
    return populate_artisan_upgrade_costs_table()

@artisan_upgrade_costs_bp("/", methods=["GET"])
def get_all_artisan_upgrade_costs_route():
    return get_all_artisan_upgrade_costs()