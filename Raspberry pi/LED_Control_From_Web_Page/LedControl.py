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
