from flask import Flask, abort
from flask import request
from flask import redirect


app=Flask(__name__)
print(app.url_map)

# @app.route("/hello")
# def index_1():
#     user_agent = request.headers.get('user_agent')
#     return "<h1>The browser is {}</h1>".format(user_agent)

# app.run()

# @app.route("/")
# def index_1():
#     return redirect("http://www.example.com")

# app.run(port = 5001)

@app.route("/user/<int:id>")
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return "<h1>Hello {}</h1>".format(user.name)

app.run(port=5001)