from flask import Flask
from flask import request
from flask import jsonify

from whisperer.whisperer import *

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route("/hello")
def hello():
    return show_something()


@app.route("/gossip", methods=['GET', 'POST'])
def gossip():

    if request.method == 'POST':

        reply = {
            'reply': "fantastic",
            'text': show_something()
        }

        return jsonify(reply)
    else:

        return whisper('yo')




