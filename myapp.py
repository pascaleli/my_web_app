from flask import Flask , render_template ,Markup
import tweepy

app=Flask(__name__)



auth = tweepy.OAuthHandler('w7s57itoNtMhAJcn0EspXfqFu','Lsms6LUGmZmBRMjn5N6pWzEzLJ1qN90f4t8PumcQSV8nvUxsdv')
auth.set_access_token('887426463145893888-aBQ17X2yZ4CAQZkYnchtSFk4KR6emnt','bXxTqp7jSovdkso4oI7qzKaaEQ2HFanKIy6ZVI5ivULiG')
api = tweepy.API(auth)
user = api.get_user('pascalhugues014')
friends =[]
followers =[]

@app.route('/')
def twee(name ='pascal'):
	print("\n\n\n\n\n")

	public_tweets = api.home_timeline()
	a ="  "
	for tweet in public_tweets:
		a = a + Markup('<br>') + tweet.text +  Markup('</br>')

#	a.append(public_tweets)
	return (render_template('index.html', tto=a , to=name,gfr=friends,gfo=followers))	
	


@app.route('/ff')
def get_friend():
	for f in user.friends():
		friends.append(f.screen_name)
	return (render_template('index.html' ,gfr = friends))  
@app.route('/f')
def get_followers():
	for f in tweepy.Cursor(api.followers).items():
		followers.append(f.screen_name)	
	return (render_template('index.html' ,gfo = followers))



if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')











