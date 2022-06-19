import json
import time
import requests
import tweepy
import os
from flask import Flask
from os import environ
from dotenv import load_dotenv


ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
RapidAPI_Key = os.getenv("X-RapidAPI-Key")
load_dotenv()
url1 = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
    "X-RapidAPI-Key": RapidAPI_Key,
    "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
}

# get API response
response = requests.request("GET", url1, headers=headers)
x = response.text
z = "\n   ⁓ "

# convert json to dictionary
x_dict = json.loads(x)
y = x_dict["content"] + z + x_dict["originator"]["name"]

# authenticate tweeter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

interval = 60 * 60


def create_tweet():
    api.update_status(y)
    time.sleep(interval)


app = Flask(__name__)
app.run(host='https://quoteer.herokuapp.com/', port=environ.get('PORT'))
