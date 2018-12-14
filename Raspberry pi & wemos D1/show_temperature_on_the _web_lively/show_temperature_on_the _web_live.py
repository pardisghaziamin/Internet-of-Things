from flask import Flask, jsonify, render_template, request
from random import *
import threading
import time

app = Flask(__name__)


@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    global MY_JSON_CONTENTS  

    content = request.get_json()
    MY_JSON_CONTENTS=content
    #print (content)
    print("nodeName is :%s"%content['sensorName'])
    print("sensorType is :%s"%content['sensorType'])
    print("Values are :%s"%content['values'])
    print("Times are :%s"%content['timestamps'])
    return 'JSON posted'

@app.route('/_ref')
def add_number2():
    global MY_JSON_CONTENTS
    #print("Refs")
    return jsonify(myresult=MY_JSON_CONTENTS)


@app.route('/')
def index():
    return render_template('hh.html')

app.run(port=8080,threaded=True,host='0.0.0.0');
