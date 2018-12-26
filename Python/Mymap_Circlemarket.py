# with in this program I am going to categorize the marker in to three different category
# 1. green -> elevation 0 to 999
# 2. Red-> Volcano more then 3000m height
# 3. Orange-> 1000 to 2000
import pandas
import folium
data=pandas.read_csv("Volcanos.txt")
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data["ELEV"])

def color_prodecude(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[12.98,77.58],zoom_start=6,tiles="Map Box Bright")
fg=folium.FeatureGroup(name="Manoj_Kumar")

for lt,lo,el in zip(lat,lon,elev):
    #fg.add_child(folium.Marker(location=[lt,lo],popup=str(el)+" m",icon=folium.Icon(color=color_prodecude(el))))
     fg.add_child(folium.CircleMarker(location=[lt,lo],radius=6,popup=str(el)+ " m",fill_color=color_prodecude(el),color="grey",fill_opacity=0.7))
map.add_child(fg)
map.save("MapwithCircleMarker.html")
