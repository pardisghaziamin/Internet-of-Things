# LED control from webpage
 
**First:**
connect two LED to pin 1 and pin 2 and,
set the wemos D1 to control LED by each key on the website.
run the code below:

    #include <ESP8266WiFi.h>

    const char* ssid = "Wifi Name"; //Access Point Name
    const char* password = "Password"; //Password

    WiFiServer server(80);

    int output_pin1 = 14; //Output Pin
    int output_pin2 = 15; 

    void setup() { 
    Serial.begin(115200);
    delay(10);

    pinMode(output_pin1, OUTPUT);
    digitalWrite(output_pin1, 0);

    pinMode(output_pin2, OUTPUT);
    digitalWrite(output_pin2, 0);

    Serial.println();
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.begin(ssid, password); //Connect D1 to ssid with password

    while (WiFi.status() != WL_CONNECTED) { //Check the  connection and print dot on the serial monitor until connect
    delay(500);
    Serial.print(".");
    }
     Serial.println("");
    Serial.println("WiFi connected");

    server.begin();
    Serial.println("Server started");

    Serial.println(WiFi.localIP());
    }

    void loop() {
    WiFiClient client = server.available();
    if (!client) {
    return;
    }

    Serial.println("new client"); //If client connect, print new client
    while (!client.available()) {
    delay(1);
    }

    String req = client.readStringUntil('\r');
    Serial.println(req);
    client.flush();


    if (req.indexOf("/on1")!= -1) { //ON,OFF,Blink for 2 LED
    digitalWrite(output_pin1, 0);
    }
    if (req.indexOf("/off1")!= -1) {
    digitalWrite(output_pin1, 1);
    }
    if (req.indexOf("/blink1")!= -1) {
     
    digitalWrite(output_pin1, 0);
    delay(500);
    digitalWrite(output_pin1, 1);
    delay(500);
     digitalWrite(output_pin1, 0);
     delay(500);
    digitalWrite(output_pin1, 1);
    delay(500);
     digitalWrite(output_pin1, 0);
     delay(500);
    digitalWrite(output_pin1, 1);
    delay(500);
    digitalWrite(output_pin1, 0);
     delay(500);
 
    }
    if (req.indexOf("/on2")!= -1) {
    digitalWrite(output_pin2, 0);
    }
    if (req.indexOf("/off2")!= -1) {
    digitalWrite(output_pin2, 1);
    }
    if (req.indexOf("/blink2")!= -1) {
    digitalWrite(output_pin2, 0);
    delay(500);
    digitalWrite(output_pin2, 1);
    delay(500);
    digitalWrite(output_pin2, 0);
    delay(500);
    digitalWrite(output_pin2, 1);
    delay(500);
    digitalWrite(output_pin2, 0);
    delay(500);
    digitalWrite(output_pin2, 1);
    delay(500);
    digitalWrite(output_pin2, 0);
    delay(500);
    }
 
    
    
    client.flush();

**Second:**

 Then, create a website for controling LED (Turn ON,Turn OFF,Blink)
that, It has two group of key for each LED
with the below code:

    String s = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n";
    s += "<head>";
    s += "<meta charset=\"utf-8\">";
    s += "<meta name=\"viewport\"   content=\"width=device-width, initial-scale=1\">";
    s += "<script src=\"https://code.jquery.com/jquery-  2.1.3.min.js\"></script>";
    s += "<link rel=\"stylesheet\"   href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/  css/bootstrap.min.css\">";
    s += "</head>";

    s += "<div class=\"container\">";
    s += "<h1>LED Control</h1>";
    s += "<div class=\"row\">";
  
    s += "<h3>led 1:</h3>";
    s += "<div class=\"col-md-2\"><input class=\"btn btn-block btn-lg btn-success\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\" type=\"button\" value=\"ON\" onclick=\"off1()\"></div>";
    s += "<div class=\"col-md-2\"><input class=\"btn btn-block btn-lg btn-danger\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\"type=\"button\" value=\"OFF\" onclick=\"on1()\"></div>";
    s += "<div class=\"row\"\"col-md-2\"><input class=\"btn btn-block btn-lg btn-warning\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\"type=\"button\" value=\"BLINK\" onclick=\"blink1()\"></div>";

    s += "<h3>led 2:</h3>";
    s += "<div class=\"col-md-2\"><input class=\"btn btn-block btn-lg btn-success\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\" type=\"button\" value=\"ON\" onclick=\"off2()\"></div>";
    s += "<div class=\"col-md-2\"><input class=\"btn btn-block btn-lg btn-danger\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\"type=\"button\" value=\"OFF\" onclick=\"on2()\"></div>";
    s += "<div class=\"row\"\"col-md-2\"><input class=\"btn btn-block btn-lg btn-warning\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\"type=\"button\" value=\"BLINK\" onclick=\"blink2()\"></div>";
    s += "</div></div>";

    s += "<script>function on1() {$.get(\"/on1\");}</script>";
    s += "<script>function off1() {$.get(\"/off1\");}</script>";
    s += "<script>function blink1() {$.get(\"/blink1\");}</script>";


    s += "<script>function on2() {$.get(\"/on2\");}</script>";
    s += "<script>function off2() {$.get(\"/off2\");}</script>";
    s += "<script>function blink2() {$.get(\"/blink2\");}</script>";

 
**Third:**

And in continue, for run the Javascript code ,use this code below:

    client.print(s);
    delay(1);
    Serial.println("Client disconnected");
    }

> note:these code must run serially

 **Result:**

in result we will have this in the web page for controling the 2 LEDs that connected to pin 1 and pin 2 of our board.
![enter image description here](https://lh3.googleusercontent.com/rOa__l7ogEkW99qrLOfyS41YzUYXPEGn-3r8rZUr41ee6g3FiZrMWCUFy94T7m6r421fQA98WSI "web")
> 


