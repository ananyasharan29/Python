# Flask app with Common Templates
from flask import Flask, render_template
app = Flask(__name__)

# layout.html, index.html, about.html

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')


# base.html, child.html, common.html
# @app.route('/')
# def home():
#     return render_template('child.html')
    
# app.run(port = 5002)

# """
# Create a home page that has name of the university name of the department and name of the year
# In the about page you should have to tags MCA and BCA 
# """

# mcabca.html, baseforBCAMCA.html, bca.html, mca.html
@app.route('/')
def home():
    return render_template('mcabca.html')

@app.route('/home1')
def home1():
    return render_template('mca.html')

@app.route('/home2')
def home2():
    return render_template('bca.html')
    
app.run(port = 5002)