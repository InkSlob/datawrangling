#!/usr/bin/python

import twitter_pull as tp

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

a = config_file()
print a['search 1H']
#a = tp.twitter("hillary Clinton",  2)