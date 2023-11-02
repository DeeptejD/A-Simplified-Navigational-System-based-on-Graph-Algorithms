import folium
import math
from folium import plugins
from .input import *
from .plotting_resources import *
import requests
# import pandas

m = folium.Map([15.4986, 73.8284], zoom_start=10)


# function that animates the map using array lines and updates the html file
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


# returns num_points number of coordinates around a give (long, lat) pair with specified radius
def calculate_circle_coordinates(center_lat, center_lon, radius_km, num_points=100):
    circle_coordinates = []
    for i in range(num_points):
        angle = math.radians(i * (360 / num_points))
        x = center_lon + (radius_km / 111.32) * math.cos(
            angle
        )  # 111.32 km is approximately one degree in kilometers
        y = center_lat + (radius_km / 111.32) * math.sin(angle)
        circle_coordinates.append([y, x])  # Latitude, Longitude
    return circle_coordinates


def radial_plotting(centercoords, radius_km):
    # Calculate circle coordinates
    circle_coordinates = calculate_circle_coordinates(
        centercoords[0], centercoords[1], radius_km
    )

    folium.Polygon(
        locations=circle_coordinates, color="green", fill=True, fill_opacity=0.3
    ).add_to(m)
