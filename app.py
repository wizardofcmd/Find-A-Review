import requests
import json
from flask import Flask, render_template, request, jsonify
from sentiment_analysis import ReviewAnalyser

app = Flask(__name__)

@app.route('/')
def index():
    # req = requests.get('https://findabookapp.herokuapp.com/api/book/read.php')
    # json_data = req.content
    # # Turns JSON into python dictionary
    # book_dict = json.loads(json_data)
    #
    # term = "The Odyssey"
    # sentiment = ReviewAnalyser()
    # result = sentiment.search(book_dict, term)
    # sentiment.sentiment_analyse(result)
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    book_rq = request.form['rv']
    print(book_rq)
    print(type(book_rq))
    return jsonify({"help":book_rq})
