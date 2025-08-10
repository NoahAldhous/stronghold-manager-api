from flask import Blueprint
# from controllers.strongholdsController import create_strongholds_table

strongholds_bp = Blueprint("strongholds", __name__)

# @strongholds_bp.route("/", methods=["POST"])
# def create_strongholds_table_route():
#     return create_strongholds_table()