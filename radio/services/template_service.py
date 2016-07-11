from radio import db
from radio.models.models import Templates


def create_template(template_data):
    existing_data = Templates.query.filter_by(
        name=template_data['name']).order_by(Templates.version.desc()).first()
    if existing_data:
        template_data['version'] = existing_data.version + 1
        existing_data.is_enabled = False
    else:
        template_data['version'] = 1

    template_data['is_enabled'] = True
    template = Templates(template_data)
    db.session.add(template)
    db.session.commit()

    return template.to_dict()


def get_template(template_name):
    template = [x.to_dict() for x in Templates.query.filter_by(
        name=template_name, is_enabled=True)]

    return template


def disable_template(template_name):
    Templates.query.filter_by(
        name=template_name, is_enabled=True).update(dict(is_enabled=False))
    db.session.commit()
    return "Disabled"


def enable_template(template_name):
    enabled_template = get_template(template_name)
    if not enabled_template:
        template = Templates.query.filter_by(
            name=template_name, is_enabled=False).order_by(
            Templates.version.desc()).first()
        template.is_enabled = True
        db.session.commit()
        return "Enabled"
    else:
        return "Latest Template already enabled"
