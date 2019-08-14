from flask import Flask, request
from operations import add
app = Flask(__name__)

@app.route("/add")
def add_route():
  a = request.args["a"]
  b = request.args["b"]
  added = add(int(a), int(b))
  html = f"<html><body><h1>{added}</h1></body></html>"
  return html



