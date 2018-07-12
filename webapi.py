#! /bin/python

import pyowm
import tweepy

owm = pyowm.OWM('2c0b2586cd1e818f35673de04a929b8c')
observation = owm.weather_at_place('london,uk')
w = observation.get_weather()

w.get_wind()
w.get_humidity()


print(w.get_wind())
print(w.get_humidity())

# doing the same thing for tweetter
print("\n\n\n\n\n")

auth = tweepy.OAuthHandler('w7s57itoNtMhAJcn0EspXfqFu','Lsms6LUGmZmBRMjn5N6pWzEzLJ1qN90f4t8PumcQSV8nvUxsdv')

auth.set_access_token('887426463145893888-aBQ17X2yZ4CAQZkYnchtSFk4KR6emnt','bXxTqp7jSovdkso4oI7qzKaaEQ2HFanKIy6ZVI5ivULiG')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
