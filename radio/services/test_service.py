from radio import db
from radio.models.models import Test


def add(data):
    post = Test(data)
    db.session.add(post)
    db.session.commit()
