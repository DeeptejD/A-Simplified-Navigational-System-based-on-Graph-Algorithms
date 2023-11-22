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
    "mapusa": (73.81131388798627, 15.590057520569246),
    "panaji": (73.828361568041, 15.498612717572783),
    "margao": (73.9578529309122, 15.27239272642025),
    "ponda": (74.00677542556889, 15.400819046721182),
    "vasco da gama": (73.81295939900215, 15.396140967598157),
    "bicholim": (73.94656471799584, 15.586494010793942),
    "pernem": (73.79693355724251, 15.716656049637862),
    "calangute": (73.7631449593016, 15.546140223570873),
    "old goa": (73.91544788608829, 15.500805717621859),
    "valpoi": (74.12218736466468, 15.523959994980771),
}

# ----- WRITE MANUALLY -----
edges = [
    [name_to_longlat["panaji"], name_to_longlat["margao"]],
    [name_to_longlat["panaji"], name_to_longlat["mapusa"]],
    [name_to_longlat["margao"], name_to_longlat["panaji"]],
    [name_to_longlat["margao"], name_to_longlat["vasco da gama"]],
    [name_to_longlat["margao"], name_to_longlat["mapusa"]],
    [name_to_longlat["margao"], name_to_longlat["ponda"]],
    [name_to_longlat["vasco da gama"], name_to_longlat["margao"]],
    [name_to_longlat["vasco da gama"], name_to_longlat["ponda"]],
    [name_to_longlat["vasco da gama"], name_to_longlat["bicholim"]],
    [name_to_longlat["mapusa"], name_to_longlat["panaji"]],
    [name_to_longlat["mapusa"], name_to_longlat["margao"]],
    [name_to_longlat["mapusa"], name_to_longlat["ponda"]],
    [name_to_longlat["ponda"], name_to_longlat["margao"]],
    [name_to_longlat["ponda"], name_to_longlat["mapusa"]],
    [name_to_longlat["ponda"], name_to_longlat["bicholim"]],
    [name_to_longlat["ponda"], name_to_longlat["calangute"]],
    [name_to_longlat["bicholim"], name_to_longlat["vasco da gama"]],
    [name_to_longlat["bicholim"], name_to_longlat["ponda"]],
    [name_to_longlat["bicholim"], name_to_longlat["pernem"]],
    [name_to_longlat["pernem"], name_to_longlat["bicholim"]],
    [name_to_longlat["pernem"], name_to_longlat["calangute"]],
    [name_to_longlat["calangute"], name_to_longlat["ponda"]],
    [name_to_longlat["calangute"], name_to_longlat["old goa"]],
    [name_to_longlat["calangute"], name_to_longlat["pernem"]],
    [name_to_longlat["old goa"], name_to_longlat["calangute"]],
    [name_to_longlat["old goa"], name_to_longlat["valpoi"]],
    [name_to_longlat["valpoi"], name_to_longlat["old goa"]],
]


for edge in edges:
    if [edge[1], edge[0]] not in edges:
        edges.append((edge[1], edge[0]))

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
