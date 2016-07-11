from flask import Blueprint, jsonify, request
from radio.validators import request_validator
from radio.exceptions.validation import ValidationException

mod = Blueprint('templates', __name__)


@mod.route('/new', methods=["POST"])
def add_template():
    request_data = request.json

    try:
        request_validator.create_template_validator(request_data)
    except ValidationException as e:
        return jsonify(e.to_dict())

    from radio.services import template_service

    return_data = template_service.create_template(request_data)

    return jsonify(return_data)


@mod.route('/<template_name>', methods=["GET"])
def get_template(template_name):

    from radio.services import template_service

    template = template_service.get_template(template_name)

    return jsonify(template)


@mod.route('/<template_name>/disable', methods=["POST"])
def disable_template(template_name):

    from radio.services import template_service

    status = template_service.disable_template(template_name)

    return jsonify(template_name=template_name, message=status)


@mod.route('/<template_name>/enable', methods=["POST"])
def enable_template(template_name):

    from radio.services import template_service

    status = template_service.enable_template(template_name)

    return jsonify(template_name=template_name, message=status)
