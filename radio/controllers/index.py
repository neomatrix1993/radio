from flask import Blueprint, jsonify, render_template

mod = Blueprint('index', __name__)


@mod.route("/")
def main():
    return render_template('index.html')


@mod.route("/test/<data>", methods=['POST'])
def add(data):
    from radio.services import test_service
    test_service.add(data)

    return jsonify("OK")
