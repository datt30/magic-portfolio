from app import app
from flask import jsonify

from app.config.config_twitter import *
import tweepy

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


@app.route('/magic-portfolio/v1/tweets/<string:twitter_user_name>', methods=['GET'])
def get_tweets(twitter_user_name):
    try:
        tweets_list = api.user_timeline(twitter_user_name, count=5)
        return jsonify({'tweets': [tweet.text for tweet in tweets_list]}), 201
    except Exception as e:
        # usually for server security, the error must be stored in a log,
        # but for practical purposes of the poc we will show it in the response
        return jsonify({'message': 'server error', 'error': str(e)}), 500

