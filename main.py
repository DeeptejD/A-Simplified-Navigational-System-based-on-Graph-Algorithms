import folium
from folium import plugins
from plotting_resources import *
import requests
import pandas

m = folium.Map([15.4986, 73.8284], zoom_start=10)


def animate_map():
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": line["coordinates"],
            },
            "properties": {
                "times": line["dates"],
                "style": {
                    "color": line["color"],
                    "weight": line["weight"] if "weight" in line else 5,
                },
            },
        }
        for line in lines
    ]

    # Lon, Lat order.
    folium.plugins.TimestampedGeoJson(
        {
            "type": "FeatureCollection",
            "features": features,
        },
        period="PT1M",
        add_last_point=True,
    ).add_to(m)

    m.save("index.html")
