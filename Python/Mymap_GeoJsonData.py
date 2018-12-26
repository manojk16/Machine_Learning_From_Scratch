#Till now I have add two layer in to map
# 1. Point layer 2. is line layer
# With in this program I ll add another layer
import pandas
import folium
data=pandas.read_csv("Volcanos.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
ele=list(data["ELEV"])


def color_prodecude(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'
map=folium.Map(location=[12.98,77.58],zoom_start=6,tiles="Map Box Bright")
fg=folium.FeatureGroup(name="Manoj_Kumar")

for lt,lo,ele in zip(lat,lon,ele):
    fg.add_child(folium.CircleMarker(location=[lt,lo],radius=6,popup=str(ele)+ " m",fill_color=color_prodecude(ele),color="grey",fill_opacity=0.7))
fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='UTF-8-sig').read()))
map.add_child(fg)
map.save("myMapwithPolygons.html")
