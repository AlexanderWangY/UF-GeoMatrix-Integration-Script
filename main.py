# Authors: Javier Martinex & Alexander Wang

'''
1) Extract locations.json and parse it to show only locations with JTYPE = "BLDG"
2) Use Open route service api to make a matrix of locations
3) Enter data into CSV file
Origin | Destination | Distance | Estimated Time (minutes)
xxxxxx | yyyyyyyyyyy | gggggggg | hhhhhhhhhhhhhhhhhhhhhhh
xxxxxx | yyyyyyyyyyy | gggggggg | hhhhhhhhhhhhhhhhhhhhhhh
xxxxxx | yyyyyyyyyyy | gggggggg | hhhhhhhhhhhhhhhhhhhhhhh
xxxxxx | yyyyyyyyyyy | gggggggg | hhhhhhhhhhhhhhhhhhhhhhh
'''

import json
import openrouteservice as ors

f = open('locations.json')

locations = json.load(f)

filteredLocations = [i for i in locations if i['JTYPE'] == 'BLDG' and not i['ABBREV']]

coordArrayRow = []

index = 1

for x in filteredLocations:
    coordArrayRow.append([x['LON'], x['LAT']])
    print(index)
    index += 1

coordArrayCol = coordArrayRow

client_ORS = ors.Client(key='5b3ce3597851110001cf6248b5572d28507d4d8097e3630d88f745a7')
# matrix = client_ORS.distance_matrix(
#     locations=coordArray,
#     profile='foot-walking',
#     metrics=['distance', 'duration'],
#     validate=False,
# )
#
# print(matrix)



