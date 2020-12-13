import string
import json
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class ReviewAnalyser():
    """Class containing methods to search for book reviews and analyse
    sentiment"""

    # Constructor
    def __init__(self):
        self.analysis = {}

    def search(self, books, item):
        """The search returns all the reviews existing for a book and
        cleans up the data when loading it into variables."""
        reviews = []
        temp = []
        for record in books['records']:
            for key in record.keys():
                if record[key].lower() == item.lower():
                    temp = list(record.values())
                    # Book name will always appear as first item, therefore
                    # removal is necessary using pop().
                    temp.pop(0)
                    # Cleaning the text by removing punctuation
                    temp[0] = temp[0].translate(str.maketrans('', '', string.punctuation))
                    reviews.append(temp)
        return reviews

    # Creating the sentiment analyser function
    def sentiment_analyse(self, list):
        # Converting all reviews to long string instead of list items
        list = ' '.join(map(str, list))
        # Removing the [] and '' characters
        list = re.sub(r'[^A-Za-z0-9 ]+', '', list)
        # Using VADER lexicon to analyse the reviews
        points = SentimentIntensityAnalyzer().polarity_scores(list)
        neg = points['neg']
        pos = points['pos']
        neu = points['neu']
        # Calling sentiment_json method to export json file based on results
        if neg > pos and neg > neu:
            sentiment = "neg"
            self.sentiment_json(sentiment, points)
        elif pos > neg and pos > neu:
            sentiment = "pos"
            self.sentiment_json(sentiment, points)
        else:
            sentiment = "neu"
            self.sentiment_json(sentiment, points)

    # Dumping the analysis data in JSON format (Sentiment, Points)
    def sentiment_json(self, sentiment, points):
        if sentiment == 'pos':
            # Data format of JSON file
            self.analysis = {
                "sentiment":"positive",
                "points":points
            }
            # Writing to a JSON file
            with open("sentiment.json", "w") as file_object:
                json.dump(self.analysis, file_object)
        elif sentiment == 'neg':
            self.analysis = {
                "sentiment":"negative",
                "points":points
            }
            with open("sentiment.json", "w") as file_object:
                json.dump(self.analysis, file_object)
        else:
            self.analysis = {
                "sentiment":"neutral",
                "points":points
            }
            with open("sentiment.json", "w") as file_object:
                json.dump(self.analysis, file_object)
