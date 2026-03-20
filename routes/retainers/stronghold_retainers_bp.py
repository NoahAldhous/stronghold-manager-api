from flask import Blueprint
from controllers.retainers.strongholdRetainersController import create_stronghold_retainers_table

stronghold_retainers_bp = Blueprint("stronghold_retainers", __name__)

@stronghold_retainers_bp.route("/", methods=["POST"])
def create_stronghold_retainers_table_route():
    return create_stronghold_retainers_table()