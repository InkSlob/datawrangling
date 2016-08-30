import tweepy
import psycopg2
import psycopg2.extensions
from psycopg2.extensions import AsIs
import psycopg2.extras
import pickle
import string
import pandas as pd
import json


data = pickle.load( open( "twitter_data_Trump_SINCE.p", "rb" ))

print type(data)

data_dict = (data["statuses"][0])
dd_Json = json.dumps(data_dict)
print type(dd_Json)

    
'''
# Connecting to database
try:
    conn = psycopg2.connect("dbname='wrangleDB' user='postgres' host='localhost' password='password'")
    print "postgresql database wrangleDB has been opened and a connection exists"
except:
    print "I am unable to connect to the database"

# Open a cursor to perform database operations
cur = conn.cursor()

# list to hold tuples to be loaded into the database
DB_list = []
count = 0
for tweet in data:
    temp_tuple = ()
    # time_zone=u'Eastern Time (US & Canada)
    twtime_zone = tweet.author._json["time_zone"]
    # text=u' ... '
    tweet_text_d = tweet.text
    # id=761286290000244736L
    tweet_id_d = int(tweet.id)
    # favorite_count=0
    favs_d = int(tweet.favorite_count)
    # source=u'Twitter for Android'
    source_d = str(tweet.source)
    # retweeted=False
    retweeted_d = tweet.retweeted
    # http://www.tutorialspoint.com/postgresql/postgresql_data_types.htm
    followers_count_d = int(tweet.author._json["followers_count"])
    # Error not working
    #location_d = str(tweet.author._json["location"])
    # u'friends_count': 1870'
    friends_count_d = int(tweet.author._json["friends_count"])
    # favorite_count=0
    favourites_d_count = int(tweet.author._json["favourites_count"])
    # u'screen_name': u'cre8ivetype',
    screen_name_d = tweet.author._json["screen_name"]
    # u'created_at': u'Tue Oct 23 15:29:20 +0000 2012', 
    created_at_d = str(tweet.author._json["created_at"])
    # Combing all of this data extracted from a raw tweet putting it into a tuple for loading it into the DB
    temp_tuple = (count, twtime_zone, tweet_text_d, tweet_id_d, favs_d, source_d, retweeted_d, followers_count_d, friends_count_d, favourites_d_count, screen_name_d, created_at_d) #location_d, 
    DB_list.append(temp_tuple)
    count += 1


create_cols = "Id INTEGER PRIMARY KEY, twtime_zone TEXT, tweet_text_d TEXT, tweet_id_d INTEGER, favs_d INTEGER, source_d TEXT, retweeted_d TEXT, "\
                "followers_count_d INTEGER, friends_count_d INTEGER, favourites_d_count INTEGER, "\
                "screen_name_d TEXT, created_at_d TEXT"
                #location_d TEXT
col_names = "count, twtime_zone, tweet_text_d, tweet_id_d, favs_d, source_d, retweeted_d, followers_count_d,  "\
            "friends_count_d, favourites_d_count, screen_name_d, created_at_d"
            #location_d,

cur.execute("CREATE TABLE test(Id INTEGER PRIMARY KEY, twtime_zone TEXT, tweet_text_d TEXT, tweet_id_d TEXT, favs_d TEXT, source_d TEXT, retweeted_d TEXT, \
                followers_count_d INTEGER, friends_count_d INTEGER, favourites_d_count INTEGER, \
                screen_name_d TEXT, created_at_d TEXT)")
# Insert Data into Table
query = "INSERT INTO test (Id, twtime_zone, tweet_text_d, tweet_id_d, favs_d, source_d, retweeted_d, followers_count_d, friends_count_d, favourites_d_count, screen_name_d, created_at_d) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
for element in DB_list:
    cur.execute(query, element)
    #print element
conn.commit()
'''