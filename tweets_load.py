import csv
import tweepy


tweets = csv.writer(open('csv_files/loaded.csv', 'w'))

def search(keyterm):

    api_key = 'PDEIa5zExerTYtpgc7hnrJmaF'
    api_key_secret = 'gTv1kP5msxoX3WC2ZrBwlbLXdxthLqFqoa1W5ZYPCcAVhlObJO'
    access_token = '917857438505865216-BusHvSeDVEZOXoUZSIgBt1UNZAWBxKy'
    access_token_secret = 'VvEr5GI3XqeHVGK7vdNPMW5jlbSgl9UctexCwAl1ZE8qt'

    authorization = tweepy.OAuthHandler(api_key, api_key_secret)
    authorization.set_access_token(access_token, access_token_secret)
    api = tweepy.API(authorization)

    counter = 1
    for tweet in api.search(keyterm, 'en', count = 60):
        tweet_time = tweet.created_at
        tweet_id = tweet.id_str
        tweet_content = tweet.text

        print ("loaded tweet ", counter)
        counter += 1
        tweets.writerow([tweet_time, tweet_id, tweet_content])

file = open('termfiles/keyterms.txt', 'r')
search_list = file.readlines()


for s in search_list:
    print("-----")
    print(s)
    search(s)


