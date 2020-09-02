import tweepy
import json
import time
## dd/mm/yyyy format
dates = time.strftime("%Y-%m-%d")



consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

fecha="2020-09-01"

search_terms = ['covid']

def stream_tweets(search_term):
    data = [] # empty list to which tweet_details obj will be added
    counter = 0 # counter to keep track of each iteration
    for tweet in tweepy.Cursor(api.search, q='\"{}\" -filter:retweets'.format(search_term), count=150, lang='es', tweet_mode='extended', since_id=dates).items():

        tweet_details = {}
        tweet_details['name'] = tweet.user.screen_name
        tweet_details['tweet'] = tweet.full_text
        tweet_details['retweets'] = tweet.retweet_count
        tweet_details['location'] = tweet.user.location
        tweet_details['created'] = tweet.created_at.strftime("%d-%b-%Y")
        tweet_details['followers'] = tweet.user.followers_count
        tweet_details['is_user_verified'] = tweet.user.verified
        data.append(tweet_details)
        counter += 1
        if counter == 1000:
            break
        else:
            pass
    with open('data/{}.json'.format(search_term+dates), 'w') as f:
        json.dump(data, f)
    print('done!')

if __name__ == "__main__":
    print('Starting to stream...')
    for search_term in search_terms:
        stream_tweets(search_term)
    print('finished!')
