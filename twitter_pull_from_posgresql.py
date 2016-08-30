import tweepy
import psycopg2
import psycopg2.extensions
from psycopg2.extensions import AsIs
import psycopg2.extras
import pickle
import string
import pandas as pd
import json

# Connecting to database
try:
    conn = psycopg2.connect("dbname='wrangleDB' user='postgres' host='localhost' password='password'")
    print "postgresql database wrangleDB has been opened and a connection exists"
except:
    print "I am unable to connect to the database"

# Open a cursor to perform database operations
cur = conn.cursor()
try:
    cur.execute("""SELECT * from testJDUMP where Id > 98""")
except:
    print "I can't SELECT from testJDUMP"

rows = cur.fetchall()
print "\nRows: \n"
for row in rows:
    print "   ", row[1]