from flask import Flask
from flask import request
import requests
import pymongo
from pymongo import MongoClient


client = MongoClient()
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


@app.route('/yolo', methods=['GET', 'POST'])
def add_message():
    db = client.testDB
    content = request.json
    print (content['yo'])
    posts = db.posts
    post_data = {
        'content':content['yo']
    }
    result = posts.insert_one(post_data)
    return "hello"
