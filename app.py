import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    req = requests.get('https://findabookapp.herokuapp.com/api/book/read.php')
    print(req.content)
    return render_template("index.html")

# @app.route('/review')
# def review():
