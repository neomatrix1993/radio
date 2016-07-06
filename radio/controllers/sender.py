from flask import Blueprint, jsonify

mod = Blueprint('sender', __name__)


@mod.route('/one')
def send_one():
    return jsonify(sender='DATA TO ONE')
