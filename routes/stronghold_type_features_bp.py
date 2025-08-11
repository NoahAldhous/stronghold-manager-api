from flask import Blueprint
from controllers.strongholdTypeFeaturesController import create_stronghold_type_features_table, populate_stronghold_type_features_table, add_new_stronghold_type_feature, get_all_stronghold_type_features, get_stronghold_type_feature_by_id, update_stronghold_type_feature_by_id, delete_stronghold_type_feature_by_id

stronghold_type_features_bp = Blueprint("stronghold_type_features", __name__)

@stronghold_type_features_bp.route("/", methods=["POST"])
def create_stronghold_type_features_table_route():
    return create_stronghold_type_features_table()

@stronghold_type_features_bp.route("/populate", methods=["POST"])
def populate_stronghold_type_features_table_route():
    return populate_stronghold_type_features_table()

@stronghold_type_features_bp.route("/add", methods=["POST"])
def add_new_stronghold_type_feature_route():
    return add_new_stronghold_type_feature()

@stronghold_type_features_bp.route("/", methods=["GET"])
def get_all_stronghold_type_features_route():
    return get_all_stronghold_type_features()

@stronghold_type_features_bp.route("/<id>", methods=["GET"])
def get_stronghold_type_feature_by_id_route(id):
    return get_all_stronghold_type_features(id)

@stronghold_type_features_bp.route("/<id>", methods=["UPDATE"])
def update_stronghold_type_feature_by_id_route(id):
    return update_stronghold_type_feature_by_id(id)

@stronghold_type_features_bp.route("/<id>", methods=["DELETE"])
def delete_stonghold_type_feature_by_id_route(id):
    return delete_stronghold_type_feature_by_id(id)