from radio.controllers.hello import db


class test(db.Model):
    __tablename__ = 'test'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<id {}>'.format(self.id)
