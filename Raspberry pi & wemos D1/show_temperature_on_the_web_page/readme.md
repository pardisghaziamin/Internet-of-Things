
# Measuring Temperature & Humidity and Show them on the webpage
## First:
Measuring **Temperature** & **Humidity** of the room by **wemos** using **DHT** sensor and storage them as a csv file. that it has explained here:

[click here to explain more](https://github.com/pardisghaziamin/Internet-of-Things/tree/master/Raspberry%20pi%20&%20wemos%20D1/storage%20temperature%20as%20a%20csv%20file)

## Second:
Then, **open** and **read** storaged data from that **address** and show on the website by run this code below on the **raspberry pi** :

    from flask import flask
    import os

    app=Flask(__name__)

    #fun var

    filepath=os.path.join(os.path.dirname(__file__), '/media/root/C4C1-5415/data_logged.csv')
    open_read=open(filepath, 'r')
    page=''

    while True:
    read_data=open_read.readline()
    page+= '<p>%s</p>'%read_data
    if open_read.readline()=='':
        break

    @app.route("/")
    def index():
    return page



    if __name__=="__main__":
    app.run(port=5000,threaded=True,host='127.0.0.1')
that is reading that csv file line by line and show it on the webpage

## Result:

that it will apear when you search 127.0.0.1:5000 on the browser of raspberry pi

> data doesn't change untill we refresh the webpage,then data will be updated


![enter image description here](https://lh3.googleusercontent.com/UYLXOpij-yNKuH2yAyKrRwh134q9FXqAMHikOx0KhyNJO0WxcBIe5w5MT_Bckfou1L8f3K_UUr8 "page")
