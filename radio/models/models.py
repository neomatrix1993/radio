from radio import db


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Text)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Templates(db.Model):
    __tablename__ = 'templates'
    id = db.Column('id', db.Integer, primary_key=True),
    name = db.Column('name', db.String(128), nullable=False, unique=True),
    description = db.Column('description', db.String(256), nullable=False),
    body = db.Column('body', db.Text, nullable=False),
    version = db.Column('version', db.Integer, nullable=False),
    handler = db.Column('handler', db.String(16), nullable=False),
    is_enabled = db.Column('is_enabled', db.Boolean, nullable=False)

    def __init__(self, request_data):
        self.name = request_data.get('name')
        self.description = request_data.get('description')
        self.handler = request_data.get('handler')
        self.body = request_data.get('body')

    def to_dict(self):
        return {
            'description': self.description,
            'handler': self.handler,
            'body': self.body
        }
