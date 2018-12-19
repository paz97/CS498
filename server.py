from flask import Flask
from flask import jsonify
from flask import request
from pymongo import MongoClient
from pprint import pprint
from random import randint
import requests
import pymongo
import sys

ss='mongodb+srv://dbUser:pwd@ccs498-xdjtt.mongodb.net/test?retryWrites=true'
client = MongoClient(ss)
db=client.test
app = Flask(__name__)

#This is a test endpoint.
@app.route('/', methods=[ 'POST'])
def hello_world():
      return 'POST SUCEESS'

@app.route('/updates',methods=['GET'])
def get_update():
    sensor_id = int(request.args.get('sensor_id'))
    ret = db.posts.find_one({'_id': sensor_id})
    print(sensor_id, file=sys.stderr)
    print(type(sensor_id), file=sys.stderr)
    print(ret, file=sys.stderr)
    return jsonify(seats_empty=ret['seats_empty'])

@app.route('/updates', methods=['POST'])
def post_update():
    content = request.get_json()
    posts = db.posts

    post_data = {
        '_id':content['sensor_id'],
        'seats_taken':content['seats_taken'],
        'seats_empty':content['seats_empty'],
        'seats_total':content['seats_total']
    }
    result = posts.update({"_id":content['sensor_id']}, post_data, upsert=True)

    return "Success"
