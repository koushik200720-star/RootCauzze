from flask import Blueprint, request, jsonify
from database.models import db, Machine

machine_bp = Blueprint("machine", __name__, url_prefix="/api")

@machine_bp.route("/machines", methods=["POST"])
def register_machine():
    data = request.get_json()

    required_fields = [
        "machine_id",
        "machine_type",
        "purchase_year",
        "production_type"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "status": "error",
                "message": f"{field} is required"
            }), 400

    existing = Machine.query.filter_by(
        machine_id=data["machine_id"]
    ).first()

    if existing:
        return jsonify({
            "status": "error",
            "message": "Machine already exists"
        }), 409

    machine = Machine(
        machine_id=data["machine_id"],
        machine_type=data["machine_type"],
        purchase_year=data["purchase_year"],
        production_type=data["production_type"]
    )

    db.session.add(machine)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Machine registered successfully",
        "machine_id": machine.machine_id
    }), 201
