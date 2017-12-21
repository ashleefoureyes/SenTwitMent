import csv

def stat_generate(term, file_read):

    total = 0
    positive = 0
    neutral = 0
    negative = 0

    for row in file_read:
        total = total + 1;
        if row[4] == "positive":
            positive = positive + 1;
        elif row[4] == "neutral":
            neutral+=1;
        elif row[4] == "negative":
            negative+=1;

    print("Statistics for: ", term)
    print("Total # of Tweets: ", total)
    print("Positive Count: ", positive)
    print("Neutral Count: ", neutral)
    print("Negative Count: ", negative)
    results.writerow([term, total, positive, neutral, negative])

termTweets = csv.reader(open('csv_files/tentreetweets.csv', 'r'))
results = csv.writer(open('csv_files/results.csv', 'w'))

stat_generate("tentree", termTweets)