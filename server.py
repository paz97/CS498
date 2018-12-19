from flask import Flask
from flask import request
from pymongo import MongoClient
from pprint import pprint
from random import randint
import requests
import pymongo

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
    content = request.json
    sensorId = content['sensor_id']
    ret = db.find_one({'_id': sensorId})
    return jsonify(seats_empty=ret['seats_empty'])

@app.route('/updates', methods=['POST'])
def post_update():
    content = request.json
    posts = db.posts

    #TODO: Add check fields
    post_data = {
        '_id':content['sensor_id'],
        'seats_taken':content['seats_taken'],
        'seats_empty':content['seats_empty'],
        'seats_total':content['seats_total']
    }
    result = posts.update({"_id":content['sensor_id']}, post_data, upsert=True)
    return "Success"
