import csv
import json
import openrouteservice as ors
import numpy as np

finalList = []

f = open('locationdata/Buildings.csv', 'r')
g = open('locationdata/locations.json')

locations = json.load(g)

reader = csv.reader(f)

classBuildings = set()

for code in reader:
    if code[1] == '':
        continue

    if not classBuildings.__contains__(str(code[1])):
        classBuildings.add(str(code[1]))

buildingCodes = []
buildingCoords = []
buildingCallSign = []

print(classBuildings)

for building in locations:
    if classBuildings.__contains__(building['BLDG']):
        buildingCodes.append(building['BLDG'])
        buildingCoords.append([building["LON"], building["LAT"]])
        buildingCallSign.append(building["NAME"])
        classBuildings.remove(building['BLDG'])

buildingCoordsY = buildingCoords
buildingCodesY = buildingCodes

print(buildingCodesY)
print(buildingCallSign)

buildingsNew = {}

for x in range(0, buildingCallSign.__len__()):
    buildingsNew[str(x)] = buildingCallSign[x]

with open('locationdata/BuildingsNew.json', 'w') as f:
    json.dump(buildingsNew, f)


# for i in range(0, 94, 40):
#     xLoc = []
#     for x in buildingCodes[i: i + 40]:
#
#         xLoc.append(x)
#
#     for g in range(0, 94, 40):
#         yLoc = []
#         for y in buildingCodesY[g: g + 40]:
#             yLoc.append(y)
# tempArray = []
#
# for i in range(0, buildingCoords.__len__() - 1, 40):
#     xRange = []
#     if not i + 40 > buildingCoords.__len__() - 1:
#         for x in range(i, i + 40):
#             xRange.append(x)
#     else:
#         for x in range(i, buildingCoords.__len__()):
#             xRange.append(x)
#
#     for g in range(0, buildingCoords.__len__() - 1, 40):
#         yRange = []
#         if not g + 40 > buildingCoords.__len__() - 1:
#             for y in range(g, g + 40):
#                 yRange.append(y)
#         else:
#             for y in range(g, buildingCoords.__len__()):
#                 yRange.append(y)
#
#         rawMatrix = ors.client.distance_matrix(client=ors.Client(
#             key="5b3ce3597851110001cf6248b5572d28507d4d8097e3630d88f745a7"), locations=buildingCoords,
#             destinations=xRange, sources=yRange,
#             profile='foot-walking',
#             metrics=['distance'], validate=False)
#
#         matrix = rawMatrix['distances']
#
#         if len(finalList) != 95:
#             for destinations in matrix:
#                 finalList.append(destinations)
#             print(finalList)
#         else:
#             for destinations in matrix:
#                 tempArray.append(destinations)
#
#         if len(tempArray) == len(finalList):
#             for i in range(0, len(tempArray)):
#                 finalList[i] = finalList[i] + tempArray[i]
#             print(tempArray)
#             print(len(tempArray))
#
#             tempArray = []
#
#
# data = {}
#
# for index in range(0, finalList.__len__()):
#     data[str(index)] = finalList[index]
#
# with open("locationdata/final.json", "w") as f:
#     json.dump(data, f)

# distance = json.load(open('locationdata/final.json'))
# halvedDistances = open('locationdata/filteredfinal.json', 'w')
# count = 0
# filteredData = {}
# for t in range(0, len(distance)):
#     filteredData[str(t)] = []
#
# for x in distance:
#     for y in range(0, distance[x].__len__()):
#         if int(x) <= y:
#             filteredData[str(y)].append(distance[x][y])
#
# json.dump(filteredData, halvedDistances)
#
