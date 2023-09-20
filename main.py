# import json
#
# f = open('jsonformatter.json', encoding='utf8')
#
# location = json.load(f)
#
# uniqueSet = set()
#
# for i in location['courses']:
#     for x in i['sections']:
#         for g in x['meetTimes']:
#             if g['meetBldgCode'] != "" and g['meetBldgCode'] != 'WEB' and not uniqueSet.__contains__(g['meetBldgCode']):
#                 uniqueSet.add(g['meetBldgCode'])
#
#
#
# print(uniqueSet.__len__())

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
g = open('jsonformatter.json', encoding='utf8')

classLocations = json.load(g)

uniqueSet = set()

for i in classLocations['courses']:
    for x in i['sections']:
        for g in x['meetTimes']:
            if g['meetBldgCode'] != "" and g['meetBldgCode'] != 'WEB' and not uniqueSet.__contains__(g['meetBldgCode']):
                uniqueSet.add(str(g['meetBldgCode']))

bldgLocations = json.load(f)

filteredLocations = []

for i in bldgLocations:
    if uniqueSet.__contains__(i['BLDG']):
        filteredLocations.append(i)
        uniqueSet.remove(str(i['BLDG']))


coordArrayRow = []

index = 1

for x in filteredLocations:
    coordArrayRow.append([x['LON'], x['LAT']])

coordArrayCol = coordArrayRow

print(coordArrayCol)


# matrix = client_ORS.distance_matrix(
#     locations=coordArray,
#     profile='foot-walking',
#     metrics=['distance', 'duration'],
#     validate=False,
# )
#
# print(matrix)






























# def search_building_coords(building, key):
#     coordinates_base_url = "https://api.tomtom.com/search/2/search/" + urlparse.quote(building) + ".json?minFuzzyLevel=1&maxFuzzyLevel=2&view=Unified&relatedPois=off&key=" + key
#     json_response = requests.get(coordinates_base_url).json()
#     latitude = json_response['results'][0]['position']['lat']
#     longitude = json_response['results'][0]['position']['lon']
#     position = str(latitude) + "," + str(longitude)
#     return position
#
# departure_point = "1310 Museum Rd, Gainesville, FL 32612"
# arrival_point = "1310 Museum Rd, Gainesville, FL 32612"
# #Route Parameters
# start = "29.651989,-82.340536"
# end = "29.644952,-82.339475"
# routeType = "fastest"
# travelMode = "pedestrian"
# departAt = "now"
# key = "89kvYiCK6GOJGjb7DbtyMoW7KXy1d3R3"
#
# baseUrl = "https://api.tomtom.com/routing/1/calculateRoute/"
#
# requestsParams = (urlparse.quote(start) + ":" + urlparse.quote(end)
#                   + "/json?routeType=" + routeType
#                   + "&travelMode=" + travelMode
#                   + "&departAt=" + urlparse.quote(departAt))
#
# requestUrl = baseUrl + requestsParams + "&key=" + key
#
# response = requests.get(requestUrl)
#
# if response.status_code == 200:
#     jsonResult = response.json()
#
#
#     routeSummary = jsonResult['routes'][0]['summary']
#
#     distance = routeSummary["lengthInMeters"]
#
#     travelTime = routeSummary['travelTimeInSeconds'] / 60
#
#     print(f"Distance(m): {distance}, Travel time: {travelTime:.2f}min")
# else:
#     print("Error")
#     print(response.status_code)
# #Matherly: 29.651989,-82.340536
# #Cypresss: 29.644952,-82.339475
