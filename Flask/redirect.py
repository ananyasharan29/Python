#Abort
from flask import Flask,redirect, url_for
app= Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('about'))

@app.route("/about")
def about():
    return "This is about the page"

@app.route("/external")
def external_redirect():
    return redirect('https://www.google.com')

app.run(port = 5001)