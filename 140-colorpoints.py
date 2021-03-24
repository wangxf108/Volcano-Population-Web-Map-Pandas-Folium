#设置了颜色变化，可以分辨出不同高度的火山，不同的颜色。 但是把color_loop循环，放在那么靠前的地方有点不能理解。
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
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color=color_producer(el))))   


map.add_child(fg)

map.save("Map1.html")