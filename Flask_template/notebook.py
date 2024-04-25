from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
# First Way
# def user(name, age = 25):
#     return render_template('user.html', name=name, age=age)

# Second Way
def user(name):
    return render_template('user.html', name=name, age=25)

app.run(port = 5001)


#Control Structure
# {% if user %}
#     Hello, {{user}}
# {% else %}
#     Hello, Stranger1
# {% endif %}

