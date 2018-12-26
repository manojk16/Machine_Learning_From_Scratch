import folium
map=folium.Map(location=[12.98,77.58],zoom_start=6,tiles="Map Box Bright")
#FeatureGroup(Layer):  Create a FeatureGroup layer ; you can put things in it and handle them in a single layer.  For example, you can add a LayerControl to
#tick/untick the whole group.
fg=folium.FeatureGroup(name="MyMapLayer",) # this feature to add layer control feature
#marker is the FeatureGroup
#map.add_child(folium.Marker(location=[12.95,77.35],popup="manojMarker",tooltip="Marker is here",icon=folium.Icon(color="green")))
# To add the marker multiple times we need to write below line multiple times and times with different -2 location
"""fg.add_child(folium.Marker(location=[12.95,77.35],popup="manojMarker",tooltip="Marker1 is here",icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[11.95,76.35],popup="manojMarker",tooltip="Marker2 is here",icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[13.95,78.35],popup="manojMarker",tooltip="Marker3 is here",icon=folium.Icon(color="green")))"""
# Heere instead of repitive task we can use for loop
for cordinates in [[12.95,77.35],[11.95,76.35],[13.95,78.35]]:
    fg.add_child(folium.Marker(location=cordinates,popup="manojMarker",tooltip="Marker3 is here",icon=folium.Icon(color="green")))
map.add_child(fg)

map.save("Manoj_map2.html")
#Adding the point in to map
