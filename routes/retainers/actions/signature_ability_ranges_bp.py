from flask import Blueprint
from controllers.retainers.actions.signatureAbilityRangesController import create_signature_ability_ranges_table, populate_signature_ability_ranges_table

signature_ability_ranges_bp = Blueprint("signature_ability_ranges", __name__)

@signature_ability_ranges_bp.route("/", methods=["POST"])
def create_signature_ability_ranges_table_route():
    return create_signature_ability_ranges_table()

@signature_ability_ranges_bp.route("/populate", methods=["POST"])
def populate_signature_ability_ranges_table_route():
    return populate_signature_ability_ranges_table()