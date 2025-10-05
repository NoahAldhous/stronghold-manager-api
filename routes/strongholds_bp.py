from flask import Blueprint
from controllers.strongholdsController import create_strongholds_table, insert_stronghold, get_strongholds_by_user_id, get_stronghold_by_id, get_stronghold_by_id_return_all_stronghold_data, update_class_feature_improvement_uses, update_stronghold_level, delete_stronghold_by_id,delete_strongholds_table

strongholds_bp = Blueprint("strongholds", __name__)

@strongholds_bp.route("/", methods=["POST"])
def create_strongholds_table_route():
    return create_strongholds_table()

@strongholds_bp.route("/create", methods=["POST"])
def insert_stronghold_route():
    return insert_stronghold()

@strongholds_bp.route("/user/<user_id>/", methods=["GET"])
def get_strongholds_by_user_id_route(user_id):
    return get_strongholds_by_user_id(user_id)

@strongholds_bp.route("/<stronghold_id>", methods=["GET"])
def get_stronghold_by_id_route(stronghold_id):
    return get_stronghold_by_id(stronghold_id)

@strongholds_bp.route("/data/<stronghold_id>", methods=["GET"])
def get_stronghold_by_id_return_all_stronghold_data_route(stronghold_id):
    return get_stronghold_by_id_return_all_stronghold_data(stronghold_id)

@strongholds_bp.route("/class_feature_improvement_uses/<stronghold_id>", methods=["PATCH"])
def update_class_feature_improvement_uses_route(stronghold_id):
    return update_class_feature_improvement_uses(stronghold_id)

@strongholds_bp.route("/level/<stronghold_id>", methods=["PATCH"])
def update_stronghold_level_route(stronghold_id):
    return update_stronghold_level(stronghold_id)

@strongholds_bp.route("/delete/<stronghold_id>", methods=["DELETE"])
def delete_stronghold_by_id_route(stronghold_id):
    return delete_stronghold_by_id(stronghold_id)

@strongholds_bp.route("/", methods=["DELETE"])
def delete_strongholds_table_route():
    return delete_strongholds_table()