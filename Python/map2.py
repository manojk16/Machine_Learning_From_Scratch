#In the prog we will read the cordinates from a file
import pandas
import folium
data=pandas.read_csv("Volcanos.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
map=folium.Map(location=[12.98,77.58],zoom_start=6,tiles="Map Box Bright")
fg=folium.FeatureGroup(name="Manoj_Map")
for lt, lo in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,lo],popup="ItHere",tooltip="You are here",icon=folium.Icon(color="blue")))
map.add_child(fg)
map.save("myMap3.html")
