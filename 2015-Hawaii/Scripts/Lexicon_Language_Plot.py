#This script is a modified form of the one provided by ehmatthes of https://github.com/ehmatthes/intro_programming. His tutorial is at:http://introtopython.org/visualization_earthquakes.html
import csv

# Open the earthquake data file.
filename = 'datasets/language_plot.csv'

# Create empty lists for the data we are interested in.
lats, lons = [], []
union_class = []
#timestrings = []

# Read through the entire file, skip the first line,
#  and pull out just the lats and lons.
with open(filename) as f:
    # Create a csv reader object.
    reader = csv.reader(f)
    
    # Ignore the header row.
    next(reader)
    
    # Store the latitudes and longitudes in the appropriate lists.
    for row in reader:
        lats.append(float(row[3]))
        lons.append(float(row[4]))
        union_class.append(float(row[7]))
        #timestrings.append(row[0])
        
# --- Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

def get_marker_color(union_class):
	#To plot the items on the map the union of several classes were formed. These unions were then each assigned a value 1-10 as is indicated in the following table. Due to the nature of the GIS data on hand, and the corespondences between the ISO and the SIL.org datasets, 17 lexical database records, which are identified by ISO language code are not represented on the map. Additionally, 14 Lexical datasets with the code [und] are not plotted. Non-plotted records are not indicated in the stats in the chart below.
#Index Numeric	Quantitiy Total	Quantity Responses	Class
#1	22	6	SIL Archived Endangered --- Blue Circles
#2	24	24	SIL Not-archived Endangered --- Blue Diamond
#3	14	7	Other Archived Endangered --- Green Circles
#4	23	23	Other Not-archived Endangered --- Green Diamonds
#5	123	56	SIL Archived Robust --- Yellow Circles
#6	113	112	SIL Not-archived Robust --- Yellow Diamonds
#7	32	19	Other Archived Robust --- Red Circle
#8	94	94	Other Not-archived Robust --- Red Diamonds
#9	17	16	No availble Coordinants
#10	14	14	Lexical datasets with the code [und]
#Totals	476	371	
#Please Note that these numbers do not represent just the respondents, but also include data as found in the catalogues. Therefore some skew of the data is possible due to over representation of SIL records.
    # Returns Blue circles for SIL responses (Class1), Green circles for non-SIL responses(Class3), Class 2 is Blue Diamond, Class 4 is Green Diamonds 
    if union_class == 6:
        return ('yo')
    elif union_class == 5:
        return ('yD')
    elif union_class == 8:
        return ('ro')
    elif union_class == 2:
        return ('bo')
    elif union_class == 3:
        return ('gD')
    elif union_class == 4:
        return ('go')
    elif union_class == 1:
        return ('bD')
    elif union_class == 7:
        return ('rD')
    else:
        return ('rD')
 
map = Basemap(projection='robin', resolution = 'h', area_thresh = 10.0,
              lat_0=0, lon_0=-120)
#map.drawcoastlines()
map.drawcountries()
#map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color = 'Gainsboro')
#map.bluemarble()
#map.drawrivers(linewidth=0.2, linestyle='solid', color='blue', antialiased=1, ax=None, zorder=None)
map.drawmapboundary()
#map.shadedrelief()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
 
min_marker_size = 7
for lon, lat, union in zip(lons, lats, union_class):
    x,y = map(lon, lat)
    msize = min_marker_size
    marker_string = get_marker_color(union)
    map.plot(x, y, marker_string, markersize=msize)
    
title_string = "Languages Mentioned in Responses and Catalogues\n"
#title_string += "SIL Archived Endangered ---" return ('bD')"\n SIL not archived Endangered --- Blue Diamond\n Non-SIL Archived Endangered --- Green circles\n Non-SIL Not Archived Endangered --- Green Diamonds\n SIL Archived Robust --- Yellow Circles\n SIL not archived Robust --- Yellow Square\n Non-SIL Archived Robust --- Red Circle\n Non-SIL Not Archived Robust --- Red Octagon\n"
plt.title(title_string)
 
plt.show()