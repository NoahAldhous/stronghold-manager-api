from flask import Blueprint
from controllers.artisans.alchemyTestsController import create_alchemy_tests_table, populate_alchemy_tests_table

alchemy_tests_bp = Blueprint("alchemy_test", __name__)

@alchemy_tests_bp.route("/", methods=["POST"])
def create_alchemy_tests_table_route():
    return create_alchemy_tests_table()

@alchemy_tests_bp.route("populate", methods=["POST"])
def populate_alchemy_tests_table_route():
    return populate_alchemy_tests_table()