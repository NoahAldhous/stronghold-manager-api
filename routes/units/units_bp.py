from flask import Blueprint, request
from controllers.units.unitsController import get_all_unit_ancestries, get_all_unit_equipment_levels, get_all_unit_experience_levels,get_all_unit_sizes, get_all_unit_types, create_ancestry_trait_relations_table, create_unit_ancestries_table, create_unit_equipment_levels_table, create_unit_experience_levels_table, create_unit_size_levels_table, create_unit_traits_table, create_unit_types_table, populate_ancestry_trait_relations_table, populate_unit_ancestries_table, populate_unit_equipment_levels_table, populate_unit_experience_levels_table, populate_unit_size_levels_table, populate_unit_traits_table, populate_unit_types_table, clear_unit_size_levels_table, create_units_table, add_unit, get_units_by_user_id, get_units_by_user_and_stronghold_id

units_bp = Blueprint("units", __name__)

# UNITS TABLE

@units_bp.route("/create", methods=["POST"])
def create_units_table_route():
    return create_units_table()

@units_bp.route("/add", methods=["POST"])
def add_unit_route():
    return add_unit()

@units_bp.route("/user/<user_id>", methods=["GET"])
def get_units_by_user_id_route(user_id):
    return get_units_by_user_id(user_id)

@units_bp.route("/", methods=["GET"])
def get_units_by_user_and_stronghold_id_route():
    user_id = request.args.get("user_id")
    stronghold_id = request.args.get("stronghold_id")
    return get_units_by_user_and_stronghold_id(user_id, stronghold_id)

# REFERENCE TABLES

# CREATE

@units_bp.route("/relations/create", methods=["POST"])
def create_ancestry_trait_relations_table_route():
    return create_ancestry_trait_relations_table()

@units_bp.route("/ancestries/create", methods=["POST"])
def create_unit_ancestries_table_route():
    return create_unit_ancestries_table()

@units_bp.route("/equipment_levels/create", methods=["POST"])
def create_unit_equipment_levels_table_route():
    return create_unit_equipment_levels_table()

@units_bp.route("/experience_levels/create", methods=["POST"])
def create_unit_experience_levels_table_route():
    return create_unit_experience_levels_table()

@units_bp.route("/size_levels/create", methods=["POST"])
def create_unit_size_levels_table_route():
    return create_unit_size_levels_table()

@units_bp.route("/traits/create", methods=["POST"])
def create_unit_traits_table_route():
    return create_unit_traits_table()

@units_bp.route("/types/create", methods=["POST"])
def create_unit_types_table_route():
    return create_unit_types_table()

# POPULATE

@units_bp.route("/relations/populate", methods=["POST"])
def populate_ancestry_trait_relations_table_route():
    return populate_ancestry_trait_relations_table()

@units_bp.route("/ancestries/populate", methods=["POST"])
def populate_unit_ancestries_table_route():
    return populate_unit_ancestries_table()

@units_bp.route("/equipment_levels/populate", methods=["POST"])
def populate_unit_equipment_levels_table_route():
    return populate_unit_equipment_levels_table()

@units_bp.route("/experience_levels/populate", methods=["POST"])
def populate_unit_experience_levels_table_route():
    return populate_unit_experience_levels_table()

@units_bp.route("/size_levels/populate", methods=["POST"])
def populate_unit_size_levels_table_route():
    return populate_unit_size_levels_table()

@units_bp.route("/traits/populate", methods=["POST"])
def populate_unit_traits_table_route():
    return populate_unit_traits_table()

@units_bp.route("/types/populate", methods=["POST"])
def populate_unit_types_table_route():
    return populate_unit_types_table()


# GET

@units_bp.route("/types", methods=["GET"])
def get_all_unit_types_route():
    return get_all_unit_types()

@units_bp.route("/size_levels", methods=["GET"])
def get_all_unit_sizes_route():
    return get_all_unit_sizes()

@units_bp.route("/experience_levels", methods=["GET"])
def get_all_unit_experience_levels_route():
    return get_all_unit_experience_levels()

@units_bp.route("/equipment_levels", methods=["GET"])
def get_all_unit_equipment_levels_route():
    return get_all_unit_equipment_levels()

@units_bp.route("/ancestries", methods=["GET"])
def get_all_unit_ancestries_route():
    return get_all_unit_ancestries()

# CLEAR

@units_bp.route("/size_levels/clear", methods=["DELETE"])
def clear_unit_size_levels_table_route():
    return clear_unit_size_levels_table()