import tweepy
import psycopg2
import pickle

print "importing data from twitter."

print "\n\n"
def get_keys():
	keys = open('/home/master/my_python/twitter_keys.txt', 'rb') 
	twitter_keys = []
	twitter_keys = keys.read()
	twitter_keys = twitter_keys.split()

	key_dict = {}
	key_dict["consumer_key"] = twitter_keys[2]
	key_dict["consumer_secret"] = twitter_keys[5]
	key_dict["access_token"] = twitter_keys[8]
	key_dict["access_token_secret"] = twitter_keys[11]
	return key_dict



print "Calling function to get secret Twitter API keys."
key_dict = get_keys()
consumer_key = key_dict["consumer_key"]
consumer_secret = key_dict["consumer_secret"]
access_token = key_dict["access_token"]
access_token_secret = key_dict["access_token_secret"]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


public_tweets = api.search(q="Donald Trump", count=100, lang="en") #  since="2013-06-01" ,  show_user="true"


pickle.dump( public_tweets, open( "twitter_data_Trump_SINCE.p", "wb" ) )


print "END"