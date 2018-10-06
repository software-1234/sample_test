import os
import sys

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
import logging
from flask import json,Flask,render_template,request,jsonify

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')


if __name__=="__main__":
     app.run(debug=True)
