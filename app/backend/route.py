from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
#import logging
import pandas as pd
import os

app = Flask(__name__)
api = Api(app)
CORS(app)
#logging.basicConfig(level=logging.DEBUG)

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
        shared_directory,current_file = os.path.split(os.path.realpath(__file__))
        x = 5
        app.logger.info("hello world")
        app.logger.info(type(x))
        app.logger.info(type(chiller_id))
        filename = ""
        filename = filename + shared_directory + '/chiller' + chiller_id + '_' + rule_id + '_signals.csv'
        # join string with join()
        signal = pd.read_csv(filename) 
        # convert resulting frame to dictionary
        # return dictionary
        return signal.to_dict('records')

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

# api.add_resource(HelloWorld, '/hi')
api.add_resource(AlarmList, '/alarm')
api.add_resource(TotalAggregation, '/total')
api.add_resource(DailyAggregation, '/daily')
api.add_resource(Signals, '/signal/<string:chiller_id>/<string:rule_id>')
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
