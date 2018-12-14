from flask import Flask, jsonify, render_template, request
from random import *
import threading
import os,time
from time import sleep
from datetime import datetime
import csv
import logging.handlers
app = Flask(__name__)
# def thrdLoop():
#     global my_rand   
#     while True:
#         time.sleep(2)
#         my_rand=randint(1, 100)
#         #print(my_rand)


# t = threading.Thread(target=thrdLoop)
# #t.daemon = True
# t.start()







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
    
    myfile=open("/media/root/C4C1-5415/data_logged.csv","a")
    if os.stat("/media/root/C4C1-5415/data_logged.csv").st_size==0:
        myfile.write("time,temperature,humidity")
    now=datetime.now()
    myfile.write("%s,%s,%s\n" %(str(now),str(MY_JSON_CONTENTS['values'][1]),str(MY_JSON_CONTENTS['values'][2])))
    myfile.flush()
    time.sleep(.5)    

    myfile.close()
    return 'JSON posted'
    


@app.route('/')
def index():
    return render_template('index.html')


app.run(port=8080,threaded=True,host='0.0.0.0');


