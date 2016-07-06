from flask import Blueprint, jsonify

mod = Blueprint('status', __name__)

@mod.route('/')
def status():
    return jsonify(status='ok')