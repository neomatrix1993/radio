from flask import Blueprint, jsonify, render_template

mod = Blueprint('index', __name__)


@mod.route("/")
def main():
    return render_template('index.html')
