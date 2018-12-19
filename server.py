from flask import Flask
from flask import request
import requests
import pymongo
from pymongo import MongoClient


client = MongoClient()
app = Flask(__name__)

@app.route('/', methods=[ 'POST'])
def hello_world():
    if flask.request.method == 'POST':
      return 'POST'
    return 'Hj'

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
