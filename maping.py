import pygmaps
import webbrowser
lattitude = -33.98173
longitude = 18.467159
radius = 300

mymap = pygmaps.maps(lattitude, longitude, 12)
prevLong = longitude
prevLat = lattitude
fh = open("telemetry.txt",'r');
count = 0
falseCount = 0
for line in fh.readlines():
    data = line.split(',')
    longitude = float(data[4])
    lattitude = float(data[3])
    if(prevLong == longitude and  prevLat == lattitude):
        # Do nothing - don't want duplicates.
        falseCount += 1
    else:
        mymap.addpoint(lattitude, longitude, "#FF00FF")
        path = [(prevLat, prevLong),(lattitude, longitude)]
        mymap.addpath(path,"#00FF00")
        prevLong = longitude
        prevLat = lattitude
        count += 1

fh.close()
print("Individual readings: " + str(count))
print("Duplicate consecutive readings: " + str(falseCount))
mymap.draw('mymap.draw.html')
url = 'mymap.draw.html'
webbrowser.open_new_tab(url)
