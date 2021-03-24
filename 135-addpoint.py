import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Stamen Terrain")  

fg = folium.FeatureGroup(name="My Map")      #增加一个featuregroup， 方便后期管理layer
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))      # popup:弹出窗口   icon:图标
map.add_child(fg)

map.save("Map1.html")