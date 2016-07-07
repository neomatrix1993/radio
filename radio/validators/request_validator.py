from radio.exceptions.validation import ValidationException


def _check_mandatory_fields(request_data, mandatory_fields):
    for mandatory_field in mandatory_fields:
        if mandatory_field not in request_data:
            raise ValidationException("MANDATORY_FIELD_MISSING",
                "Mandatory field '{}' is missing".format(mandatory_field))


def _type_validator(request_data, field_and_types):
    for field_name, field_type in field_and_types.items():
        if field_name in request_data:
            value = request_data[field_name]
            if type(value) != field_type:
                raise ValidationException("FIELD_TYPE_MISMATCH", 'Field {} expected to be of type {} but found of type {}'.format(field_name, field_type, type(value)))


def create_template_validator(request_data):
    mandatory_fields = ['description', 'handler', 'body']
    field_and_types = {
        'description': str,
        'handler': str,
        'body': str
    }

    _check_mandatory_fields(request_data, mandatory_fields)
    _type_validator(request_data, field_and_types)
