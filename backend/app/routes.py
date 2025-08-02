from flask import Blueprint, jsonify

bp = Blueprint("routes", __name__)

@bp.route("/api/status", methods=["GET"])
def status():
    return jsonify({"status": "ok"})

@bp.route("/", methods=["GET"])
def home():
    return "<h1>PulseWatch API is live!</h1>"
