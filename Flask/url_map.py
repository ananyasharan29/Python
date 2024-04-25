from flask import Flask, jsonify
import sys
app= Flask(__name__)

@app.route("/")
def index():
    return "Welcome to home page"

@app.route("/about", methods=['GET','POST'])
def about():
    return "This is the about page"

print(app.url_map)

def get_routes_info():
    routes=[]
    for rule in app.url_map.iter_rules():
        route={
            'endpoint':rule.endpoint,
            'methods':','.join(rule.methods -set(['HEAD', 'OPTIONS'])),
            'path':str(rule)
        }
        routes.append(route)
    return routes

@app.route("/routes")
def show_routes():
    routes=get_routes_info()
    return jsonify(routes=routes)

app.run()