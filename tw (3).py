#!/usr/bin/python
import tweepy
import csv #Import csv
consumer_key="LJdrKUWrVaoPJYReHnK238zRw"
consumer_secret="kZU0uqGIYmNwWzN10UNHbZESnEP3OBUpZNnMnFu0IgbK2PL8ZB"
access_token="1174317217078366209-Z3pshHswwUvBO3DibTBhpT0k8pXGL0"
access_token_secret="4Z0OVDrB2SfNZMFo7Cko6YZ6dNaPAocDHpUPhjIoip64V"
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('databaru.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "anjay",
                           since = "2020-08-25",
                           until = "2020-09-2",
                           lang = "id").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print(tweet.created_at, tweet.text)
csvFile.close()
