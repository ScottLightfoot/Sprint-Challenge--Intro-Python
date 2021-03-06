import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City():
    """City object with name, lat, lon"""
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)

    def __str__(self):
        return f'("{self.name}", {self.lat}, {self.lon})'


cities = []


def cityreader(cities=[]):
    with open('cities.csv', 'r') as csvf:
        rdr = csv.reader(csvf)
        next(rdr)
        for row in rdr:
            cities.append(City(row[0], row[3], row[4]))

    return cities


cityreader(cities)


# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)


# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the
# `cityreader` function. This function should output all the cities that fall
# within the coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates.
# Hint: normalize the input data so that it's always one or the other,
# then search for cities. In the example below, inputting 32, -120 first and
# then 45, -100 should not change the results of what the `cityreader_stretch`
# function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)


# pt1 = input("lat1, lon1 - ").split(',')
# pt2 = input("lat2, lon2 - ").split(',')

# lat1 = float(pt1[0])
# lon1 = float(pt1[1])
# lat2 = float(pt2[0])
# lon2 = float(pt2[1])

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    lat_min = min(lat1, lat2)
    lat_max = max(lat1, lat2)
    lon_min = min(lon1, lon2)
    lon_max = max(lon1, lon2)

    for c in cities:
        if lat_min <= c.lat <= lat_max and lon_min <= c.lon <= lon_max:
            within.append(c)

    return within
