from flask import Flask
from flask import blueprints

app = Flask(__name__)

from radio.controllers import status
from radio.controllers import sender

app.register_blueprint(status.mod, url_prefix='/status')
app.register_blueprint(sender.mod, url_prefix='/send')
