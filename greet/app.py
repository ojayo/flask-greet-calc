from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
  "Return simple Welcome"
  html = "<html><body><h1>Welcome!</h1></body></html>"
  return html

@app.route('/welcome/home')
def go_home():
  "Return Home page"
  html = "<html><body><h1>welcome home</h1></body></html>"
  return html

@app.route('/welcome/back')
def say_welcome_back():
  "Return simple Welcome back"
  html = "<html><body><h1>welcome back</h1></body></html>"
  return html

