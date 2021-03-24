import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")   #将给定的数据文档，通过pandas导入
lat = list(data["LAT"])                   #将经纬度分别提取出来
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, titles="Stamen Terrain")  

fg = folium.FeatureGroup(name="My Map")     #默认地图图标称谓 

for lt, ln, el in zip(lat, lon, elev):               # zip 拉链，将经，纬两个对应数值连接起来。（lt == lat; ln == lon）
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color='green')))    #popup 默认执行string格式，因此此处要指定el的类型。不然程序会出错(实际中，不加str也可以)


map.add_child(fg)

map.save("Map1.html")