import folium
from folium import plugins
from plotting_resources import *
import requests
import pandas

m = folium.Map([15.4986, 73.8284], zoom_start=10)
# lines.append(
#     returnline(
#         (139.76451516151428, 35.68159659061569),
#         (139.75964426994324, 35.682590062684206),
#     )
# )

# lines.append(
#     returnline(
#         (139.75964426994324, 35.682590062684206),
#         (139.7575843334198, 35.679505030038506),
#     )
# )

# lines.append(
#     returnline(
#         (139.7575843334198, 35.679505030038506),
#         (139.76337790489197, 35.678040905014065),
#     )
# )

# lines.append(
#     returnline(
#         (139.76337790489197, 35.678040905014065),
#         (139.76451516151428, 35.68159659061569),
#     )
# )

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
