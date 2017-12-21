import csv
from textblob import TextBlob

tweets = csv.reader(open('csv_files/loaded.csv', 'r'))
anys_tweets = csv.writer(open('csv_files/analyzed.csv', 'w'))

for row in tweets:
    blob = TextBlob(row[2])
    print(blob.sentiment.polarity)
    if blob.sentiment.polarity > 0:
        anys_tweets.writerow([row[0], row[1], row[2], blob.sentiment.polarity, "positive"])
    elif blob.sentiment.polarity == 0.0:
        anys_tweets.writerow([row[0], row[1], row[2], blob.sentiment.polarity, "neutral"])
    elif blob.sentiment.polarity < 0:
        anys_tweets.writerow([row[0], row[1], row[2], blob.sentiment.polarity, "negative"])


