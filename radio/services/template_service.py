from radio import db
from radio.models.models import Templates


def create_template(data):
    template_data = Templates(data)
    db.session.add(template_data)
    db.session.commit()
