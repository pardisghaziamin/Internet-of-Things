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

