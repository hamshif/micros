from flask import Flask
from flask import request
from flask import jsonify

from whisperer.whisperer import *

app = Flask(__name__)

SERVICE_NAME = 'whisperer'


@app.route('/')
def index():
    return 'Index Page'


@app.route("/hello", methods=['GET', 'POST'])
def hello():
    return show_something(SERVICE_NAME)


@app.route("/gossip", methods=['GET', 'POST'])
def gossip():

    if request.method == 'POST':

        reply = {
            'reply': "fantastic",
            'text': show_something(SERVICE_NAME)
        }

        return jsonify(reply)
    else:

        return whisper('yo')




