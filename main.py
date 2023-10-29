import geopandas
import folium

gdf = geopandas.read_file(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/subway_stations.geojson"
)

gdf.head()

gdf["href"] = '<a href="' + gdf.url + '">' + gdf.url + "</a>"
gdf["service_level"] = gdf.notes.str.split(", ").apply(
    lambda x: len([v for v in x if "all" in v])
)
gdf["lines_served"] = gdf.line.str.split("-").apply(lambda x: len(x))

service_levels = gdf.service_level.unique().tolist()
service_levels

colors = ["orange", "yellow", "green", "blue"]

m = folium.Map(location=[40.75, -73.95], zoom_start=13)


def style_function(feature):
    props = feature.get("properties")
    markup = f"""
        <a href="{props.get('url')}">
            <div style="font-size: 0.8em;">
            <div style="width: 10px;
                        height: 10px;
                        border: 1px solid black;
                        border-radius: 5px;
                        background-color: orange;">
            </div>
            {props.get('name')}
        </div>
        </a>
    """
    return {"html": markup}


folium.GeoJson(
    gdf,
    name="Subway Stations",
    marker=folium.Marker(icon=folium.DivIcon()),
    tooltip=folium.GeoJsonTooltip(fields=["name", "line", "notes"]),
    popup=folium.GeoJsonPopup(fields=["name", "line", "href", "notes"]),
    style_function=style_function,
    zoom_on_click=True,
).add_to(m)

m
