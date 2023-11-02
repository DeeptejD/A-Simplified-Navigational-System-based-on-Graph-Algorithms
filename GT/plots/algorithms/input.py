from collections import deque
import math


# to get the distance in km between any two pairs of (long, lat)
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


# ----- WRITE MANUALLY -----
# maps name of place to (long, lat) pair
name_to_longlat = {
    "mapusa": (73.82836156804251, 15.498612717572485),
    "panaji": (73.81162281198476, 15.599281625096822),
    "ponda": (74.00632869171159, 15.408516991424435),
    "margao": (73.95717632777243, 15.272719080431443),
}

# ----- WRITE MANUALLY -----
edges = [
    [name_to_longlat["mapusa"], name_to_longlat["panaji"]],
    [name_to_longlat["mapusa"], name_to_longlat["ponda"]],
    [name_to_longlat["mapusa"], name_to_longlat["margao"]],
    [name_to_longlat["panaji"], name_to_longlat["margao"]],
    [name_to_longlat["ponda"], name_to_longlat["margao"]],
]

vertices = []
for nm in name_to_longlat:
    vertices.append(name_to_longlat[nm])

# maps (long, lat) pair to place name
longlat_to_name = {}
for nm in name_to_longlat:
    longlat_to_name[name_to_longlat[nm]] = nm


adjacency_list = {}

for v in vertices:
    templist = []
    for src, dst in edges:
        if v == src:
            templist.append((longlat_to_name[dst], haversine(src, dst)))

    adjacency_list[longlat_to_name[v]] = templist
