import pandas
import folium

# imports Volcanoes data from txt file
data = pandas.read_csv("C:/Python_Files/Volcanoes.txt")
lat = list(data["LAT"])  # imports latitiude
lon = list(data["LON"])  # imports longitude
elev = list(data["ELEV"])  # imports elevation


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# creates the base map using Stamen Terrain
map = folium.Map(location=[38.58, -99.09],
                 zoom_start=7, tiles="Stamen Terrain")

# creates a feature group (e.g. a marker is a feature, so is, for example,
# a polygon, etc)
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    # creates popup at point lt,ln; with popup content containing elevavation,
    # with color determind by elevation, marked with a filled circle
    fgv.add_child(
        folium.CircleMarker(
            radius=10,
            location=[
                lt,
                ln],
            popup=str(el) +
            " m",
            fill=True,
            color='grey',
            fill_color=color_producer(el),
            fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(
    folium.GeoJson(
        data=open(
            'c:/Python_Files/world.json',
            'r',
            encoding='utf-8-sig').read(),
        style_function=lambda x: {
                'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)  # passes variable 'fgv' to the add-child argument
map.add_child(fgp)  # passes variable 'fgp' to the add-child argument
map.add_child(folium.LayerControl())

map.save("C:/Python_Files/Map1.html")
