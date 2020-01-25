#https://linuxize.com/post/how-to-install-flask-on-ubuntu-18-04/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'