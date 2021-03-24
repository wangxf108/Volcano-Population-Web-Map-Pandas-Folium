import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Stamen Terrain")  

fg = folium.FeatureGroup(name="My Map")      #增加一个featuregroup， 方便后期管理layer

for coordinates in [[38.2, -99.1],[39.2, -97.1]]:              #通过for函数，创造一个loop循环，此处循环两次，标记连个点。
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))   


map.add_child(fg)

map.save("Map1.html")