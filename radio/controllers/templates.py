from flask import Blueprint, jsonify, request
from radio.validators import request_validator
from radio.exceptions import RadioException
from radio.exceptions.validation import ValidationException

mod = Blueprint('templates', __name__)


@mod.route('/<template_name>', methods=["POST"])
def add_template(template_name):
    request_data = request.json

    try:
        request_validator.create_template_validator(request_data)
    except ValidationException as e:
        return jsonify(e.to_dict())

    request_data["template_name"]=template_name
    return jsonify(request_data)


@mod.route('/<template_name>', methods=["GET"])
def get_template(template_name):

    return jsonify(template_name=template_name)


@mod.route('/<template_name>/disable', methods=["POST"])
def disable_template(template_name):
    
    return jsonify(template_name="disabled")


@mod.route('/<template_name>/enable', methods=["POST"])
def enable_template(template_name):
    
    return jsonify(template_name="enabled")