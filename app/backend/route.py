from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
#import logging
import pandas as pd
import numpy as np
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
        # import chris sysalarm algo to the jup notebk
        # get the column and index for sysalarm last 4xxx rows
        # save as csv
        # open csv
        # return sysalarms
        return {'alarms': 'alarm goes here'}

class TotalAggregation(Resource):
    def get(self, chiller_id):
        shared_directory,current_file = os.path.split(os.path.realpath(__file__))
        del current_file
        files = getFiles(chiller_id)
        aggregated = {}
        for rule in files:
            label = pd.read_csv(shared_directory + '/' + files[rule])
            aggregated[rule] = label.shape[0]

        return aggregated

class DailyAggregation(Resource):
    def get(self, chiller_id):
        shared_directory,current_file = os.path.split(os.path.realpath(__file__))
        del current_file
        files = getFiles(chiller_id)
        aggregated = {}
        # daily = {}
        for rule in files:
            label = pd.read_csv(shared_directory + '/' + files[rule])
        # change stuff from this point tally every 288 rows 
            labels = (label.values // 288) + 1
            labels = labels.astype(int)
            unique, counts = np.unique(labels, return_counts=True)
            aggregated[rule] = dict(zip(unique.astype(int), counts.astype(int)))

        return aggregated
        # return {'hello' : 'world'}

class Signals(Resource):
    def get(self, chiller_id, rule_id):
        shared_directory,current_file = os.path.split(os.path.realpath(__file__))
        del current_file
        filename = shared_directory + '/chiller' + chiller_id + '_' + rule_id + '_signals.csv'
        signal = pd.read_csv(filename) 
        return signal.to_dict('records')

class Labels(Resource):
    def get(self, chiller_id, rule_id):
        shared_directory, current_file = os.path.split(os.path.realpath(__file__))
        del current_file
        filename = shared_directory + '/chiller' + chiller_id + '_' + rule_id + '_labels.csv'
        label = pd.read_csv(filename)
        return label.to_dict('records')

class Submit(Resource):
    def get(self, chiller_id, rule_id, label_id, status):
        shared_directory, current_file = os.path.split(os.path.realpath(__file__))
        del current_file
        filename = shared_directory + '/labels.csv'
        f = open(filename, "a+")
        f.write("Chiller " + chiller_id + ",rule_" + rule_id + "," + label_id + "," + status + "\n")
        f.close()

        return {'submit': 'ticket is submitted'}

class Read(Resource):
    def get(self):
        shared_directory, current_file = os.path.split(os.path.realpath(__file__))
        del current_file
        filename = shared_directory + '/labels.csv'
        f = open(filename, "r")
        contents = f.read()

        return {'data' : contents}


# add polling for new alarms ie. query/collect
class Query(Resource):
    def get(self):
        return {'new alarm': 'false'}

class Collect(Resource):
    def get(self):
        return {'collection': 'alarm metainfo goes here'}

# api.add_resource(HelloWorld, '/hi')
api.add_resource(AlarmList, '/alarm')
api.add_resource(TotalAggregation, '/total/<int:chiller_id>')
api.add_resource(DailyAggregation, '/daily/<int:chiller_id>')
api.add_resource(Signals, '/signal/<string:chiller_id>/<string:rule_id>')
api.add_resource(Labels, '/label/<string:chiller_id>/<string:rule_id>')
api.add_resource(Submit, '/submit/<string:chiller_id>/<string:rule_id>/<string:label_id>/<string:status>')
api.add_resource(Read, '/read')
api.add_resource(Query, '/query')
api.add_resource(Collect, '/collect')

def getFiles(id):
    if id == 1:
        return {
            'ch2' : 'chiller1_ch2_labels.csv',
            'ch8' : 'chiller1_ch8_labels.csv',
            'chwp1' : 'chiller1_chwp1_labels.csv',
            'chwp2' : 'chiller1_chwp2_labels.csv',
            'chwp6' : 'chiller1_chwp6_labels.csv',
            'ct2' : 'chiller1_ct2_labels.csv',
            'ct3' : 'chiller1_ct3_labels.csv'
        }
    else:
        if id == 2:
            return {
                'ch2' : 'chiller2_ch2_labels.csv',
                'ch8' : 'chiller2_ch8_labels.csv',
                'chwp6' : 'chiller2_chwp6_labels.csv',
                'ct2' : 'chiller2_ct2_labels.csv'
            }
        else:
            return {
                'ch8' : 'chiller3_ch8_labels.csv',
                'chwp1' : 'chiller3_chwp1_labels.csv',
                'chwp2' : 'chiller3_chwp2_labels.csv',
                'chwp6' : 'chiller3_chwp6_labels.csv',
                'ct2' : 'chiller3_ct2_labels.csv',
                'ct3' : 'chiller3_ct3_labels.csv'
            }

    