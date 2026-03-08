from flask import Blueprint
from controllers.artisans.artisanShopsController import create_artisan_shops_table, populate_artisan_shops_table, get_all_artisan_shops

artisan_shops_bp = Blueprint("artisan_shops", __name__)

@artisan_shops_bp.route("/", methods=["POST"])
def create_artisans_shops_table_route():
    return create_artisan_shops_table()

@artisan_shops_bp.route("/populate", methods=["POST"])
def populate_artisan_shops_table_route():
    return populate_artisan_shops_table()

@artisan_shops_bp.route("/", methods=["GET"])
def get_all_artisan_shops_route():
    return get_all_artisan_shops()