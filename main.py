import json
import time
import requests
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
RapidAPI_Key = os.environ.get("X-RapidAPI-Key")


def get_key():
    return RapidAPI_Key


url1 = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
    "X-RapidAPI-Key": '' + get_key(),
    "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
}


# get API response
def get_quotes():
    response = requests.request("GET", url1, headers=headers)
    x = response.text
    z = "\n   ⁓ "

    # convert json to dictionary
    x_dict = json.loads(x)["content"] + z + json.loads(x)["originator"]["name"]
    y = x_dict

    return y


# authenticate twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

interval = 60 * 60


def create_tweet():
    if len(get_quotes()) >= 280:
        print("Quotes more than 280 characters")
        time.sleep(60)
    while len(get_quotes()) <= 280:
        try:
            api.update_status(get_quotes())
            time.sleep(interval)
        except tweepy.TwitterServerError as e:
            print(e.reason)


if __name__ == '__main__':
    create_tweet()
