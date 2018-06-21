from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import os

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()



class TmallAPI(Resource):
    def get(self):
        return {'message': 'to be done'}
        pass

    def put(self):
        pass

    def post(self):
        json_data = request.get_json(force=True)
        for k in json_data:
            print k, json_data[k]
        #print json_data
        slotEntities = json_data["slotEntities"][0]
        for k in slotEntities:
            print k, slotEntities[k]
        pass

    def delete(self):
        pass

class AuthApi(Resource):
    def get(self):
        return app.send_static_file('./aligenie/1a9e8442db1cd0ed150aee0241f9f997.txt')
        pass

    def put(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

api.add_resource(TmallAPI, '/', endpoint = 'tmall')
api.add_resource(AuthApi, '/aligenie/1a9e8442db1cd0ed150aee0241f9f997.txt', endpoint = 'authen')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)