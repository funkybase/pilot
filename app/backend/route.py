from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import logging
import pandas as pd

app = Flask(__name__)
api = Api(app)
CORS(app)
logging.basicConfig(level=logging.DEBUG)

#class HelloWorld(Resource):
#    def get(self):
#        return {'message': 'Hello World'}
## add class for alarm list/total aggregation/daily aggregation/signals
# logical clusters CH2 == chwst chwrt flowrate
# ch8 = runstatus efficiency
# chwp1 = dp sp
# chwp2 = dp sp
# chwp6 = vsd dp
# ct2 = cwst cwrt flowrate
# ct3 = cwst cwrt flowrate

chiller = 0

chiller1_map = {
        'ch2': [8, 11, 23],
        'ch8': [16, 0],
        'chwp1': [10,19],
        'chwp2': [10, 19],
        'chwp6': [4, 10],
        'ct2': [12, 6, 23],
        'ct3': [12, 6, 23]
    }

chiller2_map = {
        'ch2': [30, 39, 24],
        'ch8': [27, 40],
        'chwp1': [46, 44],
        'chwp2': [46, 44],
        'chwp6': [25, 46],
        'ct2': [36, 26, 24],
        'ct3': [36, 26, 24]
    }

chiller3_map = {
        'ch2': [80, 88, 81],
        'ch8': [74, 78],
        'chwp1': [89, 76],
        'chwp2': [89, 76],
        'chwp6': [86, 89],
        'ct2': [82, 71, 81],
        'ct3': [82, 71, 81]
    }



class AlarmList(Resource):
    def get(self):
        # return sysalarms
        return {'alarms': 'alarm goes here'}

class TotalAggregation(Resource):
    def get(self):
        return {'aggregate': 'data goes here'}

class DailyAggregation(Resource):
    def get(self):
        # import data.csv and related chiller labels as frames
        # remove null for ALL major columns in same chiller
        # remove same index for labels
        # tally total amount of labels by modulo of signals each day ie 288
        return {'aggregate': 'data goes here'}

class Signals(Resource):
    def get(self, chiller_id, rule_id):
        if chiller_id = 1:
            chiller = chiller1_map
        else:
            if chiller_id = 2:
                chiller = chiller2_map
            else:
                chiller = chiller3_map

        result_index = chiller[rule_id]
        # import data.csv and related labels as frames
        # do some preprocessing to remove null for major column. 
        # remove same index for labels
        # convert resulting frame to dictionary
        # return dictionary
        return {'signal': 'raw signal goes here'}

class Submit(Resource):
    def get(self):

        return {'submit': 'ticket is submitted'}
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
api.add_resource(Signals, '/signal/<int:chiller_id>/<string:rule_id>')
api.add_resource(Query, '/query')
api.add_resource(Collect, '/collect')

def list_alarms() :
    return 404
    # combined label view from database/storage/memory
    # read from file for now

def total_aggregation():
    return 404
    # aggregated from all data that we have  with regards to specific rule

def daily_aggregation() :
    return 404
    # aggregated from day to day data with regards to specific rule

def signal() :
    return 404

def submit() :
    return 404
    
def query() :
    return 404

def collect() :
    return 404
