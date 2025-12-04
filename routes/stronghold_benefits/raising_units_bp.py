from flask import Blueprint
from controllers.stronghold_benefits.raisingUnitsController import create_raising_units_table, create_units_raised_table, create_stronghold_raising_units_status_table, populate_raising_units_table, get_units_raised_by_keep_type

raising_units_bp = Blueprint("raising_units", __name__)

# CREATE
@raising_units_bp.route("/create", methods=["POST"])
def create_raising_units_table_route():
    return create_raising_units_table()

@raising_units_bp.route("/units_raised/create", methods=["POST"])
def create_units_raised_table_route():
    return create_units_raised_table()

@raising_units_bp.route("/status/create", methods=["POST"])
def create_stronghold_raising_units_status_table_route():
    return create_stronghold_raising_units_status_table()

# POPULATE
@raising_units_bp.route("/populate", methods=["POST"])
def populate_raising_units_table_route():
    return populate_raising_units_table()

# GET
@raising_units_bp.route("/get/<keep_type>", methods=["GET"])
def get_units_raised_by_keep_type_route(keep_type):
    return get_units_raised_by_keep_type(keep_type)