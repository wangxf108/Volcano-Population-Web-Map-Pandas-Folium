import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6)   #80: latitude  -100:longtitude    zoom:放大倍数
print(map)                                             # A map object inside python and you have to translate it into HTML/Javascript/CSS 
map.save("Map1.html")