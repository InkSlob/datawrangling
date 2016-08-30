import tweepy
import psycopg2
import psycopg2.extensions
from psycopg2.extensions import AsIs
import psycopg2.extras
import pickle
import string
import pandas as pd

data = pickle.load( open( "twitter_data_Trump_SINCE.p", "rb" ))

# This is to extract the column names and only uses the first element of the twitter data  
all_data = []
columns = []
data_dict = (data["statuses"][0] )

def recursive_key_value(dct):
    for key, value in dct.iteritems():
        if type(value) == dict:
            recursive_key_value(value)
        else:
            columns.append(key)
            all_data.append(value)


for key, value in data_dict.iteritems():
    if type(value) == dict:
        recursive_key_value(value)
    else:
        columns.append(key)
        all_data.append(value)

print "all_data: ", len(all_data)
print "columns: ", len(columns)
cols_unique_list = []

col_unique = {}
dup_cnt = 1
for name in columns:
    if name in col_unique.keys():
        new_name = name + str(dup_cnt)
        dup_cnt += 1
        col_unique[new_name] = 1
        cols_unique_list.append(new_name)
    else:
        col_unique[name] = 1
        cols_unique_list.append(name)

print "Dictionary of column names: ", len( col_unique )
print "List of data: ", len(all_data)
print "Unique list of columns: ", len(cols_unique_list)

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
cur.execute("CREATE TABLE test2 (master_ID INTEGER PRIMARY KEY)")

query = "ALTER TABLE test2 add column %s text"

for c in cols_unique_list:
    cur.execute(query, (AsIs(c),))
conn.commit()


'''

# Insert Data into Table
count = 0
for d in list_data:
    cur.execute("INSERT INTO test2 (num, tweets) VALUES(%s, %(statuses)s)",(count, data))
    count += 1

conn.commit()
'''