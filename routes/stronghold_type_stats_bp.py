from flask import Blueprint
from controllers.strongholdTypeStatsController import get_all_stronghold_type_stats, get_stronghold_stats_by_type_and_level

stronghold_type_stats_bp = Blueprint("stronghold_type_stats", __name__)

# @stronghold_type_stats_bp.route("/<typeId>", methods = ["GET"])
# def get_stronghold_type_stats_by_type_id_route():
#     return get_stronghold_type_stats_by_type_id()

@stronghold_type_stats_bp.route("/", methods = ["GET"])
def get_all_stronghold_type_stats_route():
    return get_all_stronghold_type_stats()

@stronghold_type_stats_bp.route("/<type>/<level>", methods = ["GET"])
def get_stronghold_stats_by_type_and_level_route(type,level):
    return get_stronghold_stats_by_type_and_level(type,level)