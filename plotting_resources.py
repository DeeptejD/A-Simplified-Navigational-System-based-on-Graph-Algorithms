from datetime import datetime
from folium import plugins
from input import *
import folium
import math

# initialize the map, with a static center
m = folium.Map([15.4986, 73.8284], zoom_start=10)

# array that stores the edges (in object form) to be plotted
lines = []

your_unix_timestamp = 1609459200


# returns the object that can be used to plot coord1 and coord2 (both are (long, lat) pairs)
def returnline(coord1, coord2):
    global your_unix_timestamp
    d1 = str(datetime.utcfromtimestamp(your_unix_timestamp))
    your_unix_timestamp += 450
    d2 = str(datetime.utcfromtimestamp(your_unix_timestamp))

    return {
        "coordinates": [
            [coord1[0], coord1[1]],
            [coord2[0], coord2[1]],
        ],
        "dates": [
            d1[:10] + "T" + d1[11:],
            d2[:10] + "T" + d2[11:],
        ],
        "color": "blue",
    }


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
