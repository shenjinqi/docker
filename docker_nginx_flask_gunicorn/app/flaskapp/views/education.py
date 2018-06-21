from flask import Blueprint, render_template, jsonify

mod = Blueprint('education', __name__, url_prefix='/education')


@mod.route('/')
def index():
    return render_template('education/index.html')

