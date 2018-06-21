from datetime import datetime
from flask import Flask, session, g, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from flaskapp.views import iot
from flaskapp.views import education

app.register_blueprint(iot.mod)
app.register_blueprint(education.mod)


class API(Resource):
    def get(self):
        return {'message': 'to be done', 'datetime':str(datetime.now())}
        pass

    def put(self):
        pass

    def post(self):
        json_data = request.get_json(force=True)
        for k in json_data:
            print (k, json_data[k])
        #print json_data
        slotEntities = json_data["slotEntities"][0]
        for k in slotEntities:
            print (k, slotEntities[k])
        pass

    def delete(self):
        pass
        
        
api.add_resource(API, '/', endpoint = 'api')
