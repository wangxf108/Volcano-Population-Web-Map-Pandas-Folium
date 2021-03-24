# 通过geojson，导入国家地图边界点，形成国家区域，通过多边形polygon。
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
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m",     
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))   

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))  #导入国家的数据，形成地图上的国家边界。
                 #上面，加入了“encoding='utf-8-sig'”,属于一种读入的格式，如果不说明，程序会出现错误，然后在加上读入语句 read().
map.add_child(fg)
map.save("Map2.html")