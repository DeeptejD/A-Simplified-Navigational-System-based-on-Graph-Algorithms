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