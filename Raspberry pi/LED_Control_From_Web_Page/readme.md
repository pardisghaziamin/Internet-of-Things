
# LED control from webpage
 
**First:**
connect two LED to pin 1 and pin 2 and,
set the Raspberry pi to control LED by each key on the website.
run the python code below :

    from flask import Flask,render_template,request
    import RPi.GPIO as GPIO
    import time

    app=Flask(__name__)

    GPIO.setmode(GPIO.BCM)


    @app.route('/login/<myname>',methods=['GET','POST'])
    def myfunc(myname):
    if request.method=='POST':
        my_command=request.form['command']
        myarray=my_command.split()
        pin_from_out=int(myarray[0])
        GPIO.setup(pin_from_out,GPIO.OUT)
        GPIO.output(pin_from_out,GPIO.LOW)
        if (myarray[1]=="0"):
            GPIO.output(pin_from_out,GPIO.LOW)
        elif(myarray[1]=="1"):
            GPIO.output(pin_from_out,GPIO.HIGH)
        elif (myarray[1]=="blinker"):
            a=0
            for a in range(0,3):
                print(a)
                GPIO.output(pin_from_out,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(pin_from_out,GPIO.LOW)
                time.sleep(0.5)
        
        return render_template('ledHTML.html',myname=myname,command=my_command)
    
    return render_template('ledHTML.html',myname=myname,command=None)


    if __name__=='__main__':
    app.run()


"render_template" uses for calling a HTML code ('ledHTML.html')

**Second:**

 Then, create a website for controling LED (Turn ON,Turn OFF,Blink)
that, It has two group of key for each LED
with the HTML code below:

    <html>
    <head>
    <meta charset="utf-8">
    <meta name="viewport"   content="width=device-width, initial-scale=1">
    <script src="https://code.jquery.com/jquery-2.1.3.min.js"></script>
    <link rel="stylesheet"href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    </head>
 
    <body>
    <h1>
    hello {{myname}}
    </h1>
 

    {% if command %}
    <h1>
    the command is {{command}}
    </h1>
    {%endif%}


    <h1>led control</h1>

    <form id="iform" action="/login/{{myname}}" method="post">
        <input type="hidden" id="command" name="command">
    </form>
        
    <div class="container">
    <table class="table table-bordered">
    <thead>
    <tr>
	<td><h5>#</h5></td>
	<td><h5>on</h5></td>
	<td><h5>off</h5></td>
	<td><h5>blink</h5></td>
    </tr>
    </thead>
	<tbody>
		<tr>
    <td><h3>led 1</h3></td>

    <td><input class="btn btn-block btn-lg btn-success"style="font-size:28px;border-radius:100%;height:180px;width:180px;"type="button" value=" on " onclick="on_1()"></td>

    <td><input class="btn btn-block btn-lg btn-danger"style="font-size:28px;border-radius:100%;height:180px;width:180px;"type="button" value=" off " onclick="off_1()"></td> 


    <td><input class="btn btn-block btn-lg btn-warning"style="font-size:28px;border-radius:100%;height:180px;width:180px;"type="button" value=" blink " onclick="blink_1()"></td>
    </tr>
    <tr> 

    <td><h3>led 2</h3></td>

    <td><input class="btn btn-block btn-lg btn-success"style="font-size:28px;border-radius:100%;height:180px;width:180px;"type="button" value=" on " onclick="on_2()"></td> 


    <td><input class="btn btn-block btn-lg btn-danger"style="font-size:28px;border-radius:100%;height:180px;width:180px;"type="button" value=" off " onclick="off_2()"></td>


    <td><input class="btn btn-block btn-lg btn-warning"style="font-size:28px;border-radius:100%;height:180px;width:180px;"type="button" value=" blink " onclick="blink_2()"></td>
    </tr>
    </tbody>
    </table>
    </div> 
   
    <script>
     form=document.getElementById("iform");
     node=document.getElementById("command");

      function on_1(){
           
         node.value="12 1";
         form.submit();
      }
      function off_1(){
         node.value="12 0";
         form.submit();
      }
       function blink_1(){
         node.value="12 blinker";
         form.submit();
      }
      
      </script>
    <script>
     form=document.getElementById("iform");
     node=document.getElementById("command");

      function on_2(){  
         node.value="16 1";
         form.submit();
      }
      function off_2(){
         node.value="16 0";
         form.submit();
      }
       function blink_2(){
         node.value="16 blinker";
         form.submit();
      }
      
      </script> 

    </body>
    </html>

part of this code is for login setting,the name of user saves in "login/myname"
also the key status saves in "my_command"

> notice that these code are seperate.you should first run the python code,then open the web browser of Raspberry pi and search 127.0.0.1:5000/login/user ,so you can see the webpage controller.

**Result:**

it will apear on the browser:

![enter image description here](https://lh3.googleusercontent.com/XhMMqNK7kztJwIZlhTgyfHaobBkwknkZfAq34BZZbQNPJrlfLa4ROzmu9uQZCJujaQ9Miex30dM "web")

