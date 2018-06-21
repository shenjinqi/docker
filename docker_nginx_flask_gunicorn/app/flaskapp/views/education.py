from flask import Blueprint, render_template, jsonify
from flask_restful import Api, Resource, reqparse

mod = Blueprint('education', __name__, url_prefix='/education')
api = Api(mod)


@mod.route('/')
def index():
    return render_template('education/index.html')
   
    
class Hi(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(Hi, "/hi")