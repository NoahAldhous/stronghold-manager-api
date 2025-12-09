from flask import Blueprint
from controllers.stronghold_benefits.raisingUnitsController import update_stronghold_raising_units_status_by_stronghold_id, add_unit_raised, create_raising_units_table, create_units_raised_table, create_stronghold_raising_units_status_table, populate_raising_units_table, get_stronghold_raising_units_status_by_stronghold_id, get_units_raised_by_keep_type

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

# INSERT
@raising_units_bp.route("units_raised/add", methods=["POST"])
def add_unit_raised_route():
    return add_unit_raised()

# GET
@raising_units_bp.route("/get/<keep_type>", methods=["GET"])
def get_units_raised_by_keep_type_route(keep_type):
    return get_units_raised_by_keep_type(keep_type)

@raising_units_bp.route("/status/get/<stronghold_id>", methods=["GET"])
def get_stronghold_raising_units_status_by_stronghold_id_route(stronghold_id):
    return get_stronghold_raising_units_status_by_stronghold_id(stronghold_id)

# UPDATE
@raising_units_bp.route("/status/update/<stronghold_id>", methods=["PATCH"])
def update_strongold_raising_units_status_by_stronghold_id_route(stronghold_id):
    return update_stronghold_raising_units_status_by_stronghold_id(stronghold_id)