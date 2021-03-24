# 对坐标点进行了设置和更改，变成了小的圆形图标，标记了透明度。设置了原始颜色为灰色。
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")   
lat = list(data["LAT"])                  
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Stamen Terrain")  

fg = folium.FeatureGroup(name="My Map")    

for lt, ln, el in zip(lat, lon, elev):              
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m",      #CircleMarker: 变成圆形标记点，后面是半径6
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))            #opacity：透明度

map.add_child(fg)
map.save("Map2.html")