from flask import Blueprint
from controllers.artisans.artisanBonusesController import create_artisan_bonuses_table, populate_artisan_bonuses_table

artisan_bonuses_bp = Blueprint("artisan_bonuses", __name__)

@artisan_bonuses_bp.route("/", methods=["POST"])
def create_artisan_bonuses_table_route():
    return create_artisan_bonuses_table()

@artisan_bonuses_bp.route("/populate", methods=["POST"])
def populate_artisan_bonuses_table_route():
    return populate_artisan_bonuses_table()    