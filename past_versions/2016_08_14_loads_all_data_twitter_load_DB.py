import tweepy
import psycopg2
import psycopg2.extensions
from psycopg2.extensions import AsIs
import psycopg2.extras
import pickle
import string
import pandas as pd

data = pickle.load( open( "/home/master/my_python/data_wrangling/twitter_data_Trump_SINCE.p", "rb" ))


# used only for naming the columns 
all_cols = ["follow_request_sent", "has_extended_profile", "profile_use_background_image", \
            "profile_sidebar_fill_color", "id1", "verified", "entities", "profile_image_url_https",\
            "geo_enabled", "profile_text_color", "followers_count", "profile_sidebar_border_color", \
            "id_str", "default_profile_image", "location", "is_translation_enabled", "utc_offset", \
            "statuses_count", "description", "friends_count", "profile_link_color", \
            "profile_image_url", "notifications", "profile_background_image_url_https", \
            "profile_background_color", "profile_banner_url", "profile_background_image_url",\
            "screen_name", "lang", "profile_background_tile", "favourites_count", \
            "name", "url", "created_at", "contributors_enabled", "time_zone", "protected", \
            "default_profile", "is_translator", "listed_count","contributors","truncated", \
            "text", "is_quote_status", "in_reply_to_status_id", "id2", "favorite_count", \
            "author", "geo", "in_reply_to_user_id_str", "lang2", "created_at2", \
            "in_reply_to_status_id_str", "place", "source", "retweeted", "sentiment"]

print "Number of columns: ", len(all_cols)

# Connecting to database
try:
    conn = psycopg2.connect("dbname='wrangleDB' user='postgres' host='localhost' password='password'")
    print "postgresql database wrangleDB has been opened and a connection exists"
except:
    print "I am unable to connect to the database"

# Open a cursor to perform database operations
cur = conn.cursor()
#dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Create a Table
cur.execute("CREATE TABLE testAll (master_ID INTEGER PRIMARY KEY)")
print "Table test2 created."
query = "ALTER TABLE testAll add column %s text"

for c in all_cols:
    cur.execute(query, (AsIs(c),))

print "New columns added to table."

conn.commit()

print "END [][][][][][][][][][][][][]"