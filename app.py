import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    req = requests.get('https://findabookapp.herokuapp.com/api/book/read.php')
    json_data = req.content
    # Turns JSON into python dictionary
    book_dict = json.loads(json_data)
    return render_template("index.html")

# @app.route('/review')
# def review():
