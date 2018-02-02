#!/usr/bin/python

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import salama

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

#data = salama.main(['--endtime 2017-08-13T00:00:00', '--starttime 2017-08-12T23:50:00', '--lines 5', '--format array'])
#lats = []
#lons = []

#print(data)
#for row in data:
#    input = row.split(" ")
#    lats.append(float(input[1]))
#    lons.append(float(input[2]))

#map = Basemap(projection='ortho', lat_0=0, lon_0=0)
#map = Basemap(llcrnrlon=0,llcrnrlat=70,urcrnrlon=35,urcrnrlat=50,projection='mill')
#map = Basemap(llcrnrlon=10,llcrnrlat=50,urcrnrlon=35,urcrnrlat=72,resolution='h',projection="merc")
map = Basemap(width=900000,height=1500000,lat_1=50.,lat_2=72,lat_0=65,lon_0=24.,resolution='h',projection="lcc")

#Fill the globe with a blue color 
#map.drawmapboundary(fill_color='white')
#Fill the continents with the land color
#map.fillcontinents(color='#cc9966',lake_color='#99ffff')
#map.fillcontinents(color='white',lake_color='white')
map.drawcountries(linewidth=0.25)
#map.drawcoastlines()
#x,y = map(lons, lats)
#map.plot(x, y, '+r', markersize=0.2)

map.drawmeridians(np.arange(0,360,5))
map.drawparallels(np.arange(-90,90,5))

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines(color='grey',linewidth=0.25)

#x1,y1 = map(18.63,59.46)
#x3,y3 = map(32.19,70.4)
#x2,y2 = map(18.63,70.4)
#x4,y4 = map(32.19,59.64)
#poly = Polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)],facecolor='white',edgecolor='black',linewidth=1)
#plt.gca().add_patch(poly)


lat = [59.0, 59.0, 59.0,]
lon = [23, 24, 25]

x, y = map(lon, lat)
map.plot(x, y, 'o-', markersize=1, linewidth=1)

#plt.show()
#plt.savefig('out.png', bbox_inches='tight', pad_inches=0, dpi=3800, transparent=True)
