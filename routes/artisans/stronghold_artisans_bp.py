from flask import Blueprint
from controllers.artisans.strongholdArtisans import create_stronghold_artisans_table, get_all_artisans_by_stronghold_id

stronghold_artisans_bp = Blueprint("stronghold_artisans", __name__)

@stronghold_artisans_bp.route("/", methods=["POST"])
def create_stronghold_artisans_table_route():
    return create_stronghold_artisans_table()

@stronghold_artisans_bp.route("/<stronghold_id>", methods=["GET"])
def get_all_artisans_by_stronghold_id_route(stronghold_id):
    return get_all_artisans_by_stronghold_id(stronghold_id)