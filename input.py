from collections import deque
import math


def haversine(coord1, coord2):
    # Convert latitude and longitude from degrees to radians
    lon1, lat1 = map(math.radians, coord1)
    lon2, lat2 = map(math.radians, coord2)

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6371  # Earth radius in kilometers
    distance = R * c

    return distance


vertices = [
    (73.82836156804251, 15.498612717572485),
    (73.81162281198476, 15.599281625096822),
    (74.00632869171159, 15.408516991424435),
    (73.95717632777243, 15.272719080431443),
]

name_to_longlat = {
    "mapusa": (73.82836156804251, 15.498612717572485),
    "panaji": (73.81162281198476, 15.599281625096822),
    "ponda": (74.00632869171159, 15.408516991424435),
    "margao": (73.95717632777243, 15.272719080431443),
}


longlat_to_name = {
    (73.82836156804251, 15.498612717572485): "mapusa",
    (73.81162281198476, 15.599281625096822): "panaji",
    (74.00632869171159, 15.408516991424435): "ponda",
    (73.95717632777243, 15.272719080431443): "margao",
}

edges = [
    [(73.82836156804251, 15.498612717572485), (73.81162281198476, 15.599281625096822)],
    [(73.82836156804251, 15.498612717572485), (74.00632869171159, 15.408516991424435)],
    [(73.82836156804251, 15.498612717572485), (73.95717632777243, 15.272719080431443)],
    [(73.81162281198476, 15.599281625096822), (73.95717632777243, 15.272719080431443)],
    [(74.00632869171159, 15.408516991424435), (73.95717632777243, 15.272719080431443)],
]

adjacency_list = {}

for v in vertices:
    templist = []
    for src, dst in edges:
        if v == src:
            templist.append((longlat_to_name[dst], haversine(src, dst)))

    adjacency_list[longlat_to_name[v]] = templist
