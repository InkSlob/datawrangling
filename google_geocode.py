#!/usr/bin/python
import urllib
import urllib2
import json
import re
import pickle
from apiclient.discovery import build

locations = pickle.load( open( "lat_lng_locations.p", "rb" ) )

def get_keys():
	keys = open('/home/master/my_python/google_geocode_key.txt', 'rb') 
	geo_key = []
	geo_key = keys.read()
	geo_key = geo_key.split()

	key_dict = {}
	key_dict["key"] = geo_key[1]
	return key_dict

def get_location(location):
	key = get_keys()['key']

	base = "https://maps.googleapis.com/maps/api/geocode/json?address="
	#location = 'detroit'	

	url = base + location + '&key=' + key
	url = url.replace("'", '')
	url = url.replace(" ", '_')

	response = urllib2.urlopen(url)
	#answer = response.read()
	answer = json.load(response)

	d_lat = answer['results'][0]['geometry']['bounds']['northeast']['lat']
	d_lng = answer['results'][0]['geometry']['bounds']['northeast']['lng']

	tuple1 = (d_lat, d_lng)

	if location in locations:
		print "location submitted already exists."
	else:
		locations[location] = tuple1

	pickle.dump( locations, open( "lat_lng_locations.p", "wb" ) )
	return tuple1