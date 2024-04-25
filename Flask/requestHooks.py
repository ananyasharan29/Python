#Request Hooks
from flask import Flask,request

app= Flask(__name__)

# @app.before_first_request
# def before_first_request():
#     print("Executing before the first request") #--get printed as the output of the cell
#     return "Executing before the first request" #--get printed in browser window

@app.before_request
def before_request():
    print("Executing before the request")

@app.after_request
def after_request(response):
    print("Executing after the request")
    return response

@app.teardown_request
def teardown_request(exception = None):
    print("Executing after the teardown request")

@app.route("/")
def index():
    print("Handling the request")
    return "Flask Application with request hooks"

app.run()
