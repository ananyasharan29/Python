# Flask Application - if inside App
from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def main_page():
#     # is_afternoon = True
#     is_afternoon = False
#     if is_afternoon:
#         message = 'Good Afternoon!!!'
#     else:
#         message = 'Hello!!!'
#     return render_template('index.html', message = message)

# app.run(port = 5001)

#Flask Application - if construct inside the template
# @app.route('/')
# def new_page():
#     # is_afternoon = True
#     is_afternoon = False
#     return render_template('ifConstruct.html', is_afternoon=is_afternoon)

# app.run(port = 5001)

#Flask Application - For Construct
# @app.route('/')
# def displayfor():
#     fruits = ['mango', 'jackfruit', 'apple', 'cherry', 'kiwi', 'dragonfruits']
#     return render_template('displayfor.html', fruits = fruits)

# app.run(port=5002)

#Flask Application- macro Construct
@app.template_global()
def format_price(price):
    if price >= 1000:
        return f'{price/1000:.2f}K'
    else:
        return f'{price:.2f}'
    
@app.route('/')
def home():
    products = [
        {'name':'Laptop', 'Price':45000},
        {'name':'Smart phone', 'Price':25000},
        {'name':'Soap', 'Price':40.50},
        {'name':'Flowers', 'Price':89.50},
    ]
    return render_template('home.html', products = products)

app.run(port = 5003)