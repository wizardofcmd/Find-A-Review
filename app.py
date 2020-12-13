import requests
import json
from flask import Flask, render_template, request, jsonify
from sentiment_analysis import ReviewAnalyser

# Setting up flask app
app = Flask(__name__)

# Returning home page
@app.route('/')
def index():
    return render_template("index.html")

# Receiving POST request from user searching for book sentiment
@app.route('/process', methods=['POST'])
def process():
    book_rq = request.form['rv']
    req = requests.get('https://findabookapp.herokuapp.com/api/book/read.php')
    json_data = req.content
    # Turns JSON into python dictionary
    book_dict = json.loads(json_data)

    # Creaitng instance of sentiment analyser class
    sentiment = ReviewAnalyser()
    result = sentiment.search(book_dict, book_rq)
    if result:
        sentiment.sentiment_analyse(result)
        return jsonify({"success":"true"})
    return jsonify({"success":"false"})

# Returning sentiment.json to JavaScript file
@app.route('/analysis', methods=['GET'])
def analysis():
    f = open('sentiment.json')
    data = json.load(f)
    f.close()
    return data
