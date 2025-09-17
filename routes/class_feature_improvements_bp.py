from flask import Blueprint
from controllers.classFeatureImprovementsController import create_class_feature_improvements_table, create_class_feature_restrictions_table, populate_class_feature_improvements_table, populate_class_feature_restrictions_table, get_all_class_feature_improvements, get_class_feature_improvement_by_class_id, clear_class_feature_improvements_table, clear_class_feature_restrictions_table

class_feature_improvements_bp = Blueprint("class_feature_improvements", __name__)

@class_feature_improvements_bp.route("/restrictions/create", methods=["POST"])
def create_class_features_restrictions_table_route():
    return create_class_feature_restrictions_table()

@class_feature_improvements_bp.route("/improvements/create", methods=["POST"])
def create_class_feature_improvements_table_route():
    return create_class_feature_improvements_table()

@class_feature_improvements_bp.route("/restrictions/populate", methods=["POST"])
def populate_class_feature_restrictions_table_route():
    return populate_class_feature_restrictions_table()

@class_feature_improvements_bp.route("/improvements/populate", methods=["POST"])
def populate_class_feature_improvements_table_route():
    return populate_class_feature_improvements_table()

@class_feature_improvements_bp.route("/improvements", methods=["GET"])
def get_all_class_feature_improvements_route():
    return get_all_class_feature_improvements()

@class_feature_improvements_bp.route("/improvements/<id>", methods=["GET"])
def get_class_feature_improvement_by_class_id_route(id):
    return get_class_feature_improvement_by_class_id(id)

@class_feature_improvements_bp.route("/restrictions/clear", methods=["DELETE"])
def clear_class_feature_restrictions_table_route():
    return clear_class_feature_restrictions_table()

@class_feature_improvements_bp.route("/improvements/clear", methods=["DELETE"])
def clear_class_feature_improvements_table_route():
    return clear_class_feature_improvements_table()