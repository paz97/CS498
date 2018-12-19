from flask import Flask
from flask import request
import requests
import pymongo
from pymongo import MongoClient
from pprint import pprint
from random import randint

ss='mongodb+srv://dbUser:pwd@ccs498-xdjtt.mongodb.net/test?retryWrites=true'
client = MongoClient(ss)
db=client.test
app = Flask(__name__)

#This is a test endpoint
@app.route('/', methods=[ 'POST'])
def hello_world():
      return 'POST SUCEESS'

@app.route('/updates',methods=['GET'])
def get_update():
    '''
    Should be changed to get new updates from the database
    '''
    return 'GET SUCCESS'

@app.route('/updates', methods=['POST'])
def post_update():
    content = request.json
    posts = db.posts
    post_data = {
        'device':content['device_id'],
        'content':content['seat_avail']
    }
    result = posts.insert_one(post_data)
    return "Success"
