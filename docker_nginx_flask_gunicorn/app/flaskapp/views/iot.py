from flask import Blueprint, render_template, jsonify

mod = Blueprint('iot', __name__, url_prefix='/iot')


@mod.route('/')
def index():
    return render_template('iot/index.html')

