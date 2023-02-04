#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
"""
from flask import Flask
app=Flask(__name__)

@app.route("/",strict_slashes=False)
def Hello_hbnb():
    return "Hello HBNB!"

@app.route("/hbnb",strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>",strict_slashes=False)
def c(text):
    text=text.replace("_"," ")
    return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>",strict_slashes=False)
def python(text="is cool"):
    text=text.replace("_"," ")
    return "python {}".format(text)
if __name__="__main__":
    app.run(host="0.0.0.0")
  

  
