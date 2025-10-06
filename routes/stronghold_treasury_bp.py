from flask import Blueprint
from controllers.strongholdTreasuryController import update_stronghold_treasury_currency

stronghold_treasury_bp = Blueprint("stronghold_treasury", __name__)

@stronghold_treasury_bp.route("/update/<id>", methods=["PATCH"])
def update_stronghold_treasury_currency_route(id):
    return update_stronghold_treasury_currency(id)