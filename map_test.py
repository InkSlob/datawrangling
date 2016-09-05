#!/usr/bin/python

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap, cm
from google_geocode import get_location
import string

def make_map(df):
  m = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49, projection='lcc', lat_1=33, lat_2=45,
    			    lon_0=-95, resolution='h', area_thresh=10000)
  # creates a list of integers
  places_count = df[['location']].groupby('location').size().tolist()
  places=df['location'].unique().tolist()
  
  cities = []
  i = 0
  for x in places:
    cmb = None
    cnt = places_count[i]
    cmb = str(x) + '::' + str(cnt)
    cities.append(cmb)
    i += 1
  lat, lng = [], []
  for place in places:
    try:
      spot = get_location(place)
      lat.append(spot[0])
      lng.append(spot[1])
    except:
      print "The twitter location: %s cannot be located" % place

  x,y =m(lng, lat)
  #cities=['Los Angeles::1','Culver City::2','Burbank::3','San Francisco::4','New York City::5','Chicago::6','Austin::8','Atlanta::9','Las Vegas::10']

  m.bluemarble()
  m.drawcoastlines()
  m.drawcountries(linewidth=3)
  m.drawmapboundary()
  m.drawstates()
  m.drawparallels(np.arange(25,65,20),labels=[1,0,0,0])
  m.drawmeridians(np.arange(-120,-40,20),labels=[0,0,0,1])


  plt.plot(x, y, 'yo')
  for city, xc, yc in zip(cities, x, y):
      if city =='Culver City::2':
          plt.text(xc-400000, yc+150000, 2,bbox=dict(facecolor='red', alpha=0.6))
      elif city =='Burbank::3':
          plt.text(xc-250000, yc-200000, 3,bbox=dict(facecolor='yellow', alpha=0.6))
      else:
          plt.text(xc+150000, yc-100000, 4,bbox=dict(facecolor='green', alpha=0.6))

  plt.title("Politics & Twitter: Where are the Tweets?")

  plt.show()
  return
