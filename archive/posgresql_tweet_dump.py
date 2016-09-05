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

data_dict = (data["statuses"])

# Connecting to database
try:
    conn = psycopg2.connect("dbname='wrangleDB' user='postgres' host='localhost' password='password'")
    print "postgresql database wrangleDB has been opened and a connection exists"
except:
    print "I am unable to connect to the database"

# Open a cursor to perform database operations
cur = conn.cursor()


cur.execute("CREATE TABLE testyuy(master_id SERIAL PRIMARY KEY, tweet TEXT)")
# Insert Data into Table
query = "INSERT INTO testyuy (master_id, tweet) VALUES (%s, %s)"
serial_count = 0
for t in data_dict:
    t = json.dumps(t)
    data_tuple = (serial_count, t)
    cur.execute(query, data_tuple)
    serial_count += 1
    
conn.commit()
