from flask import Blueprint
from controllers.artisans.strongholdArtisansController import create_stronghold_artisans_table, get_all_artisans_by_stronghold_id, delete_stronghold_artisans_table, insert_stronghold_artisan, update_stronghold_artisan, delete_stronghold_artisan

stronghold_artisans_bp = Blueprint("stronghold_artisans", __name__)

@stronghold_artisans_bp.route("/", methods=["POST"])
def create_stronghold_artisans_table_route():
    return create_stronghold_artisans_table()

@stronghold_artisans_bp.route("/<stronghold_id>", methods=["GET"])
def get_all_artisans_by_stronghold_id_route(stronghold_id):
    return get_all_artisans_by_stronghold_id(stronghold_id)

@stronghold_artisans_bp.route("/add", methods=["POST"])
def insert_stronghold_artisan_route():
    return insert_stronghold_artisan()

@stronghold_artisans_bp.route("/update", methods=["PATCH"])
def update_stronghold_artisan_route():
    return update_stronghold_artisan()

@stronghold_artisans_bp.route("/delete_table", methods=["DELETE"])
def delete_stronghold_artisans_table_route():
    return delete_stronghold_artisans_table()

@stronghold_artisans_bp.route("/delete/<artisan_id>", methods=["DELETE"])
def delete_stronghold_artisan_route(artisan_id):
    print(artisan_id)
    return delete_stronghold_artisan(artisan_id)