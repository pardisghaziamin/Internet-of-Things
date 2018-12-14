
# Measuring Temperature &  Humidity and Show them on the webpage live
## First:
Measuring **Temperature** & **Humidity** of the room by **wemos** using **DHT** sensor .

[click here to explain more](https://github.com/pardisghaziamin/Internet-of-Things/tree/master/Raspberry%20pi%20&%20wemos%20D1/storage%20temperature%20as%20a%20csv%20file)

## Second:

Then, create a **website** for show temperature & humidity which is changing autimatically during the time by the **HTML** code below:

    <html>

    <head>
    <style>
    table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    }
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js">

    </script>
    </head>


    <body>

    <script type=text/javascript>
    SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
  


    </script>









    <table style="width:100%">
    <tr>
    <th>Node Name</th>
    <th>Sensor Type</th> 
    <th>Values</th>
    </tr>
    <tr>
    <td><span id="nodeName1"/></td>
    <td><span  id="sensorName1"/></td>
    <td><span id="value1"/></td>
    </tr>
  
    </table>




    </body>
    </html>

we use  this JQuary library for changing data automatically :

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"> </script>

## Third:

 
Then, **receive** data from wemos by run this code below on the **raspberry pi**:

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
"render_template" uses for calling a HTML code ('hh.html').


also it prints on the **terminal** of raspberry pi by this part of code:

    print("nodeName is :%s"%content['sensorName'])
    print("sensorType is :%s"%content['sensorType']) 
    print("Values are :%s"%content['values']) 
    print("Times are :%s"%content['timestamps'])


> notice that these code are seperate.you should first run the python code,then open the web browser of Raspberry pi and search 0.0.0.0:8080 ,so you can see the webpage controller.
> 
## Result:

temperature and humidity has shown on the localhost: 0.0.0.0:8080

> data doesn't change untill we refresh the webpage,then data will be updated


![enter image description here](https://lh3.googleusercontent.com/A1ntU8j_bms79hOVKI5XXCIGNASIMtj_jvG0eh-at1wjKeWMJWPM_j4zRkzeg9OBEe1KjB9rZQM "site")
