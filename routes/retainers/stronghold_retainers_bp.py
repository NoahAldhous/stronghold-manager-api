from flask import Blueprint
from controllers.retainers.strongholdRetainersController import create_stronghold_retainers_table, add_stronghold_retainer, get_stronghold_retainers_by_stronghold_id

stronghold_retainers_bp = Blueprint("stronghold_retainers", __name__)

@stronghold_retainers_bp.route("/", methods=["POST"])
def create_stronghold_retainers_table_route():
    return create_stronghold_retainers_table()

@stronghold_retainers_bp.route("/add", methods=["POST"])
def add_stronghold_retainer_route():
    return add_stronghold_retainer()

@stronghold_retainers_bp.route("/<stronghold_id>", methods=["GET"])
def get_stronghold_retainers_by_stronghold_id_route(stronghold_id):
    return get_stronghold_retainers_by_stronghold_id(stronghold_id)