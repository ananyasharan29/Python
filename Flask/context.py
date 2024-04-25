# Flask Application - Application context and Request Context
from flask import Flask,g,request
from datetime import datetime

app= Flask(__name__)

app_data={"message: This data is available for all requests"}

@app.route("/")
def index():
    app_message=app_data["message"]
    g.request_time = datetime.now()
    return f"""
    <h1>Application Context</h1>
    <p>{app_message}</p>
    <h1>Request Context</h1>
    <p>Time since request started is{g.request_time}</p>
    """
app.run()

