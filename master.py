#!/usr/bin/python
import pickle 
import pandas as pd

import twitter_pull as tp
import make_table as mt
import table_exist as cx
import insert_data as da
import text_sentiment_analysis as sen
import map_test as mp

def config_file():
	config = open('config.txt', 'rb') 
	twitter_config = []
	twitter_config = config.read()
	twitter_config = twitter_config.split(':')

	config_dict = {}
	config_dict["search 1T"] = twitter_config[3]
	config_dict["search 2T"] = twitter_config[5]
	config_dict["search 3T"] = twitter_config[7]
	config_dict["search 4T"] = twitter_config[9]
	config_dict["search 5T"] = twitter_config[11]
	config_dict["search 1H"] = twitter_config[15]
	config_dict["search 2H"] = twitter_config[17]
	config_dict["search 3H"] = twitter_config[19]
	config_dict["search 4H"] = twitter_config[21]
	config_dict["search 5H"] = twitter_config[23]

	return config_dict

# Function to see if a table has already been created for the data dump
tbl_exist = cx.check_if_exist()
if (tbl_exist):
	print "Table Exists"
else:
	mt.create_table()

config = config_file()
for key, val in config.items():
	data = tp.twitter(val, 3 )
	topic = str(val)
	topic = topic.replace('"','')
	# Function to see if a table has already been created for the data dump
	tbl_exist = cx.check_if_exist()
	print "insert ", topic
	da.insert_data(data, topic)
	
	#data = pickle.load( open( "/home/master/my_python/data_wrangling/twitter_data_Trump_SINCE.p", "rb" ))
geo_cols = ['topic', 'sentiment', 'location']	
geo_df = pd.DataFrame(columns=geo_cols)
for key, val in config.items():
	topic = str(val)
	topic = topic.replace('"','')
	print topic
	current_df = sen.sentiment_overall(topic)
	geo_df = geo_df.append(current_df)

mp.make_map(geo_df)

print "END"