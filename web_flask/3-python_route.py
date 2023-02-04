#!/usr/bin/python3
from flask import Flask
app=Flask(__name__)
@app.route("/",strict_slashes=False)
def Hello_hbnb():
  return “<h1>Hello HBNB!<h1>”
@app.route("/hbnb",strict_slashes=False)
def hbnb():
  return  “<h1>HBNB<h1>”
@app.route("/c/<text>",strict_slashes=False)
def c(text):
  text=text.replace("_"," ")
  return "C {}.format(text)
@app.route("/python/<text>",strict_slashes=False)
def python(text):
  text=text.replace("_"," ")
  return "python {}.format(text)
if __name__="__main__":
  app.run(host="0.0.0.0")
  

  
