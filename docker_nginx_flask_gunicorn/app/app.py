from flask import Flask, request
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()



class API(Resource):
    def get(self):
        return {'message': 'to be done'}
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)