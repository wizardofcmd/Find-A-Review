import requests
import json
from flask import Flask, render_template
from sentiment_analysis import ReviewAnalyser

app = Flask(__name__)

@app.route('/')
def index():
    req = requests.get('https://findabookapp.herokuapp.com/api/book/read.php')
    json_data = req.content
    # Turns JSON into python dictionary
    book_dict = json.loads(json_data)
    term = "Yes Man"
    sentiment = ReviewAnalyser()
    result = sentiment.search(book_dict, term)
    sentiment.sentiment_analyse(result)
    return render_template("index.html")

# @app.route('/review')
# def review():
