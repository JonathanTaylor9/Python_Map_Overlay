import pandas
import folium

# imports Volcanoes data from txt file
data = pandas.read_csv("C:/Python_Files/Volcanoes.txt")
lat = list(data["LAT"])  # imports latitiude
lon = list(data["LON"])  # imports longitude
elev = list(data["ELEV"])  # imports elevation

# creates function to determine circle elevation color
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

# creates a feature group so all volcanoes are contained in one layer,
# rather than one layer per volcanoe
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    # creates child layer popup at point lt,ln; with popup content containing elevavation,
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

# creates feature group for population - feature group utilised rather
# than single map for continuity versus previous section
fgp = folium.FeatureGroup(name="Population")

# creates child layer overlay of country outlines, filled with color denoting populations
# Uses lambda to insert an anonymous function
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
map.add_child(folium.LayerControl())  # adds layer control panel

map.save("C:/Python_Files/Map1.html")
