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
    app.run()