from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap, cm
from google_geocode import get_location

#print get_location('falls church, VA')


m = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64,
  			urcrnrlat=49, projection='lcc', lat_1=33, lat_2=45,
  			lon_0=-95, resolution='h', area_thresh=10000)

places=['Los Angeles','Culver City','Burbank','San Francisco','New York City','Chicago','Austin','Atlanta','Las Vegas']
lat, lng = [], []
for place in places: 
	spot = get_location(place)
	lat.append(spot[0])
	lng.append(spot[1])


#Lats=[34.053717,34.0211224,34.1816482,37.7792768,40.7305991,41.8755546,30.2711286,33.7490987,36.1662859]
#Long=[-118.2427266,-118.3964665,-118.3258554,-122.4192704,-73.9865812,-87.6244212,-97.7436995,-84.3901849,-115.149225]
#x,y = m(Long,Lats)
x,y =m(lng, lat)
cities=['Los Angeles::1','Culver City::2','Burbank::3','San Francisco::4','New York City::5','Chicago::6','Austin::8','Atlanta::9','Las Vegas::10']


#m.bluemarble()
#m.drawcoastlines()
#m.drawcountries(linewidth=3)
#m.drawmapboundary()
#m.drawmapboundary(fill_color='aqua')
#m.drawstates()
#m.fillcontinents(color='coral',lake_color='blue')

m.bluemarble()
#m.etopo()
#m.shadedrelief()
#m.shadedrelief()
m.drawcoastlines()
m.drawcountries(linewidth=3)
m.drawmapboundary()
#m.drawmapboundary(fill_color='#202020')
m.drawstates()
#m.fillcontinents(color='#CC9900')
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

#m.drawgreatcircle(-118.2427266,34.053717,-118.3964665,34.0211224,linewidth=2,color='r')
#m.drawgreatcircle(-118.3964665,34.0211224,-118.3258554,34.1816482,linewidth=2,color='r')
#m.drawgreatcircle(-118.3258554,34.1816482,-122.4192704,37.7792768,linewidth=2,color='r')
#m.drawgreatcircle(-122.4192704,37.7792768,-73.9865812,40.7305991,linewidth=3,color='r',alpha=0.5)
#m.drawgreatcircle(-73.9865812,40.7305991,-87.6244212,41.8755546,linewidth=1,color='r',alpha=1)
#m.drawgreatcircle(-87.6244212,41.8755546,-98.5796704771825,39.82818485,linewidth=2,color='r')
#m.drawgreatcircle(-98.5796704771825,39.82818485,-97.7436995,30.2711286,linewidth=2,color='r')
#m.drawgreatcircle(-97.7436995,30.2711286,-84.3901849,33.7490987,linewidth=2,color='r')
#m.drawgreatcircle(-84.3901849,33.7490987,-115.149225,36.1662859,linewidth=2,color='r')
#m.drawgreatcircle(-115.149225,36.1662859,-118.2427266,34.053717,linewidth=2,color='b')

plt.title("Politics & Twitter: Where are the Tweets?")

plt.show()
