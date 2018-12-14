

# Measuring Temperature & Humidity and storage them as a CSV file
 
## First:
Measuring **Temperature** & **Humidity** of the room by **wemos** using **DHT** sensor. for this,first connect DHT sensor to wemos such a this:

>also you can use a removable disk to save data which is shown at this picture:



![
](https://lh3.googleusercontent.com/gt3KlMCswUAynh9uwSEvY8LL76am-SpTU2QWvuFU1I8Pp4k_ZljHJPnlbJbGL5iI9jvxEqtFpLA "dht")
## Second:
run the code below on the wemos  to print temprature & humidity on the serial and  **send** data to Raspberry pi:

> data is sending to raspberry IP by:
> "http://192.168.1.37:8080/postjson"

    #include <ESP8266HTTPClient.h>
    #include <ESP8266WiFi.h>
    #include <ArduinoJson.h>
    #include <SimpleDHT.h>

    int pinDHT11 = 2;
    SimpleDHT11 dht11;

    int ledPin=5;

    void setup() {

    byte temperature = 0;
    byte humidity = 0;
    pinMode(ledPin, OUTPUT);




    Serial.begin(115200);  //Serial connection
    WiFi.begin("pardis amir","66946639Pardis");   //WiFi connection

    while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion

    delay(500);
    Serial.println("Waiting for connection");

    }

    }
    bool toggle=false;
    void loop() {

    if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status

    DynamicJsonBuffer JSONbuffer;
    JsonObject& JSONencoder = JSONbuffer.createObject(); 

    
    JSONencoder["sensorName"] = "myTemper1";
    JSONencoder["sensorType"] = "Temperature";

    JsonArray& values = JSONencoder.createNestedArray("values"); //JSON array
    JsonArray& timestamps = JSONencoder.createNestedArray("timestamps"); //JSON array


    byte temperature;
    byte humidity;
    int err = SimpleDHTErrSuccess;
    if ((err = dht11.read(pinDHT11, &temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
        Serial.print("Read DHT22 failed, err="); Serial.println(err);delay(1000);
        return;
      }

    values.add((int)temperature); //Add value to array
    timestamps.add(String(millis()+0)); //Add value to array

    values.add((int)humidity); //Add value to array
    timestamps.add(String(millis()+1)); //Add value to array


    char JSONmessageBuffer[300];
    JSONencoder.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
    Serial.println(JSONmessageBuffer);

    HTTPClient http;    //Declare object of class HTTPClient

    http.begin("http://192.168.1.37:8080/postjson");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header

    int httpCode = http.POST(JSONmessageBuffer);   //Send the request
    String payload = http.getString();                                        //Get the response payload

    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload

    http.end();  //Close connection

    } else {

    Serial.println("Error in WiFi connection");

    }

    delay(1000);  //Send a request every 1 second
    if(toggle)
        digitalWrite(ledPin, HIGH);
    else
        digitalWrite(ledPin, LOW);
    toggle=!toggle;
    }

that is shown below:
![
](https://lh3.googleusercontent.com/wkL1sYAZvrTHrsRZn3RKloH6ZcasuJXog8_s_59DE8jM4Xn0RMH75jZFlLcl1IAEN57TFP1Ti0A "serial")

## Third:
Then, **receive** data from wemos by run this code below on the **raspberry pi**:

    enter code herefrom flask import Flask, jsonify, render_template, request
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
    


    

also it prints on the **terminal** of raspberry pi by this part of code:

    print("nodeName is :%s"%content['sensorName'])
    print("sensorType is :%s"%content['sensorType']) 
    print("Values are :%s"%content['values']) 
    print("Times are :%s"%content['timestamps'])

actually data saves on this **address** of raspberry pi :  "/media/root/C4C1-5415/data_logged.csv"
by this part of code:

    myfile=open("/media/root/C4C1-5415/data_logged.csv","a")
    if os.stat("/media/root/C4C1-5415/data_logged.csv").st_size==0:
        myfile.write("time,temperature,humidity")
    now=datetime.now()
    myfile.write("%s,%s,%s\n" %(str(now),str(MY_JSON_CONTENTS['values'][1]),str(MY_JSON_CONTENTS['values'][2])))
    myfile.flush()
    time.sleep(.5)    

    myfile.close()
