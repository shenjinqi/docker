from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
es.indices.create(index='test-index', ignore=400)
es.index(index="test-index",doc_type="test-type", body={"any":"data01","timestamp":datetime.now()})
#es.index(index="test-index",doc_type="test-type", body={"any":"data02","timestamp":datetime.now()})

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
            print (k, json_data[k])
        #print json_data
        slotEntities = json_data["slotEntities"][0]
        for k in slotEntities:
            print (k, slotEntities[k])
        pass

    def delete(self):
        pass
        
class IotGateWayMessage(Resource):
    def get(self):
        #es = Elasticsearch("elasticsearch")
        #info =  str(es.info())
        #health = str(es.cluster.health())
        res = es.search(index="test-index", body={"query":{"match_all":{}}})
        #res = 'oops'
        return {'result': res}
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


api.add_resource(TmallAPI, '/', endpoint = 'tmall')
api.add_resource(IotGateWayMessage, '/api/iot/gateway/msg/', endpoint = 'iotgateway')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)