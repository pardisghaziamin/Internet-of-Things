---


---

<h1 id="led-control-from-webpage">LED control from webpage</h1>
<p><strong>First:</strong><br>
connect two LED to pin 1 and pin 2 and,<br>
set the wemos D1 to control LED by each key on the website.<br>
run the code below:</p>
<pre><code>#include &lt;ESP8266WiFi.h&gt;

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
</code></pre>
<p><strong>Second:</strong></p>
<p>Then, create a website for controling LED (Turn ON,Turn OFF,Blink)<br>
that, It has two group of key for each LED<br>
with the below code:</p>
<pre><code>String s = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n";
s += "&lt;head&gt;";
s += "&lt;meta charset=\"utf-8\"&gt;";
s += "&lt;meta name=\"viewport\"   content=\"width=device-width, initial-scale=1\"&gt;";
s += "&lt;script src=\"https://code.jquery.com/jquery-  2.1.3.min.js\"&gt;&lt;/script&gt;";
s += "&lt;link rel=\"stylesheet\"   href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/  css/bootstrap.min.css\"&gt;";
s += "&lt;/head&gt;";

s += "&lt;div class=\"container\"&gt;";
s += "&lt;h1&gt;LED Control&lt;/h1&gt;";
s += "&lt;div class=\"row\"&gt;";

s += "&lt;h3&gt;led 1:&lt;/h3&gt;";
s += "&lt;div class=\"col-md-2\"&gt;&lt;input class=\"btn btn-block btn-lg btn-success\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\" type=\"button\" value=\"ON\" onclick=\"off1()\"&gt;&lt;/div&gt;";
s += "&lt;div class=\"col-md-2\"&gt;&lt;input class=\"btn btn-block btn-lg btn-danger\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\"type=\"button\" value=\"OFF\" onclick=\"on1()\"&gt;&lt;/div&gt;";
s += "&lt;div class=\"row\"\"col-md-2\"&gt;&lt;input class=\"btn btn-block btn-lg btn-warning\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\"type=\"button\" value=\"BLINK\" onclick=\"blink1()\"&gt;&lt;/div&gt;";

s += "&lt;h3&gt;led 2:&lt;/h3&gt;";
s += "&lt;div class=\"col-md-2\"&gt;&lt;input class=\"btn btn-block btn-lg btn-success\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\" type=\"button\" value=\"ON\" onclick=\"off2()\"&gt;&lt;/div&gt;";
s += "&lt;div class=\"col-md-2\"&gt;&lt;input class=\"btn btn-block btn-lg btn-danger\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\"type=\"button\" value=\"OFF\" onclick=\"on2()\"&gt;&lt;/div&gt;";
s += "&lt;div class=\"row\"\"col-md-2\"&gt;&lt;input class=\"btn btn-block btn-lg btn-warning\"style=\"font-size:28px;border-radius:100%;height:100px;width:100px;\"type=\"button\" value=\"BLINK\" onclick=\"blink2()\"&gt;&lt;/div&gt;";
s += "&lt;/div&gt;&lt;/div&gt;";

s += "&lt;script&gt;function on1() {$.get(\"/on1\");}&lt;/script&gt;";
s += "&lt;script&gt;function off1() {$.get(\"/off1\");}&lt;/script&gt;";
s += "&lt;script&gt;function blink1() {$.get(\"/blink1\");}&lt;/script&gt;";


s += "&lt;script&gt;function on2() {$.get(\"/on2\");}&lt;/script&gt;";
s += "&lt;script&gt;function off2() {$.get(\"/off2\");}&lt;/script&gt;";
s += "&lt;script&gt;function blink2() {$.get(\"/blink2\");}&lt;/script&gt;";
</code></pre>
<p><strong>Third:</strong></p>
<p>And in continue, for run the Javascript code ,use this code below:</p>
<pre><code>client.print(s);
delay(1);
Serial.println("Client disconnected");
}
</code></pre>
<blockquote>
<p>note:these code must run serially</p>
</blockquote>
<p><strong>Result:</strong></p>
<p>in result we will have this in the web page for controling the 2 LEDs that connected to pin 1 and pin 2 of our board.<br>
<img src="https://picasaweb.google.com/109171916798758731280/6632365268500052321#6632365271315435874" alt="enter image description here" title="webserver"><br>
<img src="https://lh3.googleusercontent.com/e7hIa7RHLz0XGwonNs4HsMxw3lBtZSrIZZLlEYW7WblBult7F55tUDxNhANBp50QM_abF5WDwVk" alt="enter code here" title="web"></p>
<blockquote></blockquote>

