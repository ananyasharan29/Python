#Abort
from flask import Flask,request, abort
app= Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Flask Application. Go to /users/user_id"

@app.route("/users/<user_id>")
def get_user(user_id):
    users = {'admin':'administrator', 'guest':'guest_user'}
    if user_id not in users:
        abort(404, f'User with id {user_id} not found')
    return f'User ID : {user_id}, Name: {users[user_id]}'

app.run(port = 5002)