import csv

prepped = csv.reader(open('csv_files/analyzed.csv', 'r'))

def discard(term):
    tweet_term = csv.writer(open('csv_files/' + term + 'tweets.csv', 'w'))
    counter = 1
    for row in prepped:
        r = row[2].lower()
        r = row[2].strip('#').strip('@')
        if term in r:
            counter +=1
            tweet_term.writerow(row)
    print('# of rows', counter)


discard("tentree")