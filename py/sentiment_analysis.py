import string
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analysis = {}
result = ''
filename = "negative.txt"

# Opening the file and storing its content into a variable
with open(filename) as file_object:
    content = file_object.read()

# Cleaning the text by removing punctuation
content = content.translate(str.maketrans('', '', string.punctuation))

dict = {'records': [{'book': '1984', 'review': 'Fantastic read. I loved it.'},
{'book': 'Yes Man', 'review': 'Boring read. Terrible book.'},
{'book': 'Yes Man', 'review': 'I hate this book. The writing is bad.'},
{'book': 'Yes Man', 'review': 'Awful. Worst book ever do not read at all.'}]}

def search(books, item):
    reviews = []
    temp = []
    for record in books['records']:
        for key in record.keys():
            if record[key].lower() == item.lower():
                temp = list(record.values())
                # Book name will always appear as first item, therefore
                # removal is necessary using pop().
                temp.pop(0)
                reviews.append(temp)
    if len(reviews) > 0:
        return reviews
    elif len(reviews) <= 0:
        return False

# Creating the sentiment analyser function
def sentiment_analyse(text):
    points = SentimentIntensityAnalyzer().polarity_scores(text)
    neg = points['neg']
    pos = points['pos']
    if neg > pos:
        sentiment = "neg"
        sentiment_json(sentiment, points)
    elif pos > neg:
        sentiment = "pos"
        sentiment_json(sentiment, points)
    else:
        sentiment = "neu"
        sentiment_json(sentiment, points)

# Dumping the analysis data in JSON format (Sentiment, Points)
def sentiment_json(sentiment, points):
    if sentiment == 'pos':
        # Data format of JSON file
        analysis = {
            "sentiment":"positive",
            "points":points
        }
        # Writing to a JSON file
        with open("sentiment.json", "w") as file_object:
            json.dump(analysis, file_object)
    elif sentiment == 'neg':
        analysis = {
            "sentiment":"negative",
            "points":points
        }
        with open("sentiment.json", "w") as file_object:
            json.dump(analysis, file_object)
    else:
        analysis = {
            "sentiment":"neutral",
            "points":points
        }
        with open("sentiment.json", "w") as file_object:
            json.dump(analysis, file_object)

# Calling the function
# sentiment_analyse(content)

term = "Táin"
result = search(dict, term)
print(result)
