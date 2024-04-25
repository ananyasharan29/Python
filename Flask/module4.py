#Flask Application
from flask import Flask
app = Flask(__name__)
print(type(app))
print(app)
print(__name__)

@app.route("/hello")
def hello():
    return "Hello, This is my first flask app"

app.run(port = 5001)

# @app.route("/user/<name>")
# def user(name):
#     return "<h1>Hello, {}!!!</h1>".format(name)

# print(user("xyz"))
# app.run()
# app.url_map

# @app.route("/qty/<float:val>")
# def print_qty(val):
#     return "<h1>The Quantity purchased is {} kgs</h1>".format(val)

# app.run()
# app.url_map

# def hello_name(name):
#     return "<h1>Hello {}, How are you?</h1>".format(name)
# app.add_url_rule("/<name>", 'hello_name', hello_name)

# print(app.url_map)
# app.run()