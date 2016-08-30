import tweepy
import psycopg2
import pickle
import string
import json
import pandas as pd
import numpy as np

data = pickle.load( open( "twitter_data_Trump.p", "rb" ))

a = pd.read_json(data, typ='series', orient='records')

'''
# Connecting to database
try:
    conn = psycopg2.connect("dbname='wrangleDB' user='postgres' host='localhost' password='password'")
    print "postgresql database wrangleDB has been opened and a connection exists"
except:
    print "I am unable to connect to the database"

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute("CREATE TABLE test2(id SERIAL PRIMARY KEY, data_t JSON NOT NULL)") 	
data1 = data[0]
#query = "INSERT INTO test2 (1, data_t) VALUES (%s, %s)"
cur.execute("INSERT INTO test2 (id, data_t) VALUES ((%s, %s), ([1], data1))")


conn.commit()		
'''