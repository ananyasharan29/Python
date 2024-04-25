from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def num_range():
    numbers = 20
    return render_template('numberRange.html', num=numbers)

app.run(port=5004)