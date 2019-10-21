from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import logging

app = Flask(__name__)
api = Api(app)
CORS(app)
logging.basicConfig(level=logging.DEBUG)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World'}
# add class for alarm list/total aggregation/daily aggregation/signals
class AlarmList(Resource):
    def get(self):
        return {'alarms': 'alarm goes here'}

class TotalAggregation(Resource):
    def get(self):
        return {'aggregate': 'data goes here'}

class DailyAggregation(Resource):
    def get(self):
        return {'aggregate': 'data goes here'}

class Signals(Resource):
    def get(self):
        return {'signal': 'raw signal goes here'}
# add polling for new alarms ie. query/collect
class Query(Resource):
    def get(self):
        return {'new alarm': 'false'}

class Collect(Resource):
    def get(self):
        return {'collection': 'alarm metainfo goes here'}

api.add_resource(HelloWorld, '/hi')
api.add_resource(AlarmList, '/alarm')
api.add_resource(TotalAggregation, '/total')
api.add_resource(DailyAggregation, '/daily')
api.add_resource(Signals, '/signal')
api.add_resource(Query, '/query')
api.add_resource(Collect, '/collect')
