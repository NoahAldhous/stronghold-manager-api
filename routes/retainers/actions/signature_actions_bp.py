from flask import Blueprint
from controllers.retainers.actions.signatureAbilitiesController import create_signature_abilities_table, populate_signature_abilities_table

signature_abilities_bp = Blueprint("signature_abilities", __name__)

@signature_abilities_bp.route("/", methods=["POST"])
def create_signature_abilities_table_route():
    return create_signature_abilities_table()

@signature_abilities_bp.route("/populate", methods=["POST"])
def populate_signature_abilities_table_route():
    return populate_signature_abilities_table()