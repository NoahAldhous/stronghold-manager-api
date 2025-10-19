from flask import Blueprint
from controllers.units.unitsController import create_ancestry_trait_relations_table, create_unit_ancestries_table, create_unit_equipment_levels_table, create_unit_experience_levels_table, create_unit_size_levels_table, create_unit_traits_table, create_unit_types_table, populate_ancestry_trait_relations_table, populate_unit_ancestries_table, populate_unit_equipment_levels_table, populate_unit_experience_levels_table, populate_unit_size_levels_table, populate_unit_traits_table, populate_unit_types_table

units_bp = Blueprint("units", __name__)

# CREATE

@units_bp.route("/relations/create", methods={"POST"})
def create_ancestry_trait_relations_table_route():
    return create_ancestry_trait_relations_table()

@units_bp.route("/ancestries/create", methods={"POST"})
def create_unit_ancestries_table_route():
    return create_unit_ancestries_table()

@units_bp.route("/equipment_levels/create", methods={"POST"})
def create_unit_equipment_levels_table_route():
    return create_unit_equipment_levels_table()

@units_bp.route("/experience_levels/create", methods={"POST"})
def create_unit_experience_levels_table_route():
    return create_unit_experience_levels_table()

@units_bp.route("/size_levels/create", methods={"POST"})
def create_unit_size_levels_table_route():
    return create_unit_size_levels_table()

@units_bp.route("/traits/create", methods={"POST"})
def create_unit_traits_table_route():
    return create_unit_traits_table()

@units_bp.route("/types/create", methods={"POST"})
def create_unit_types_table_route():
    return create_unit_types_table()

# POPULATE

@units_bp.route("/relations/populate", methods={"POST"})
def populate_ancestry_trait_relations_table_route():
    return populate_ancestry_trait_relations_table()

@units_bp.route("/ancestries/populate", methods={"POST"})
def populate_unit_ancestries_table_route():
    return populate_unit_ancestries_table()

@units_bp.route("/equipment_levels/populate", methods={"POST"})
def populate_unit_equipment_levels_table_route():
    return populate_unit_equipment_levels_table()

@units_bp.route("/experience_levels/populate", methods={"POST"})
def populate_unit_experience_levels_table_route():
    return populate_unit_experience_levels_table()

@units_bp.route("/size_levels/populate", methods={"POST"})
def populate_unit_size_levels_table_route():
    return populate_unit_size_levels_table()

@units_bp.route("/traits/populate", methods={"POST"})
def populate_unit_traits_table_route():
    return populate_unit_traits_table()

@units_bp.route("/types/populate", methods={"POST"})
def populate_unit_types_table_route():
    return populate_unit_types_table()

