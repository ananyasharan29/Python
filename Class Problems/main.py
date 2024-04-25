from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def main_page():
#     num = 5
#     return render_template('index.html', number=num)

@app.route('/') #--When you will pass dynamic argument it should have only positive value
def main_page():
    num = -8
    return render_template('index.html', number=num)

app.run(port = 5001)