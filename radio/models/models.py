from radio import db


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Text)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<id {}>'.format(self.id)
