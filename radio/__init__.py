from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from radio.controllers import status
from radio.controllers import sender
from radio.controllers import templates
from radio.controllers import index


app = Flask(__name__)


app.register_blueprint(status.mod, url_prefix='/status')
app.register_blueprint(sender.mod, url_prefix='/send')
app.register_blueprint(templates.mod, url_prefix='/template')
app.register_blueprint(index.mod)
