from datetime import datetime

your_unix_timestamp = 1609459200

def returnline(coord1, coord2):
    global your_unix_timestamp
    d1 = str(datetime.utcfromtimestamp(your_unix_timestamp))
    your_unix_timestamp += 1200
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


lines = []

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


# print(lines)
