import csv
import json
import openrouteservice as ors

# Open both CSV and JSON files to find buildings with classrooms and their coordinates.

finalList = []
# Load JSON and CSV files
f = open('locationdata/Buildings.csv', 'r')  # Open CSV file for reading
g = open('locationdata/locations.json')      # Open JSON file for reading

locations = json.load(g)  # Load JSON data into 'locations' variable

reader = csv.reader(f)  # Create a CSV reader object

classBuildings = set()  # Initialize a set to store unique building codes

# Iterate through the CSV data to identify unique building codes
for code in reader:
    if code[1] == '':
        continue  # Skip empty entries

    if str(code[1]) not in classBuildings:
        classBuildings.add(str(code[1]))

buildingCodes = []
buildingCoords = []
buildingCallSign = []

print(classBuildings)
# Split data into respective lists for buildings with classrooms
for building in locations:
    if building['BLDG'] in classBuildings:
        buildingCodes.append(building['BLDG'])
        buildingCoords.append([building["LON"], building["LAT"]])
        buildingCallSign.append(building["NAME"])
        classBuildings.remove(building['BLDG'])

buildingCoordsY = buildingCoords
buildingCodesY = buildingCodes

# Test: Print building codes and names
print(buildingCodesY)
print(buildingCallSign)

buildingsNew = {}

# Create a dictionary mapping index to building names
for x in range(0, len(buildingCallSign)):
    buildingsNew[str(x)] = buildingCallSign[x]

# ------------------------------------
# Save the 'buildingsNew' dictionary to a JSON file
# This file contains relevant buildings and their corresponding indices
with open('locationdata/BuildingsNew.json', 'w') as f:
    json.dump(buildingsNew, f)

# Here, the algorithm performs its functions by processing data in blocks and making OpenRouteService API calls
for i in range(0, 94, 40):
    xLoc = []
    for x in buildingCodes[i: i + 40]:
        xLoc.append(x)

    for g in range(0, 94, 40):
        yLoc = []
        for y in buildingCodesY[g: g + 40]:
            yLoc.append(y)

tempArray = []

# Process building coordinates in blocks
for i in range(0, len(buildingCoords) - 1, 40):
    xRange = []
    if not i + 40 > len(buildingCoords) - 1:
        for x in range(i, i + 40):
            xRange.append(x)
    else:
        for x in range(i, len(buildingCoords)):
            xRange.append(x)

for g in range(0, buildingCoords.__len__() - 1, 40):
        yRange = []
        if not g + 40 > buildingCoords.__len__() - 1:
            for y in range(g, g + 40):
                yRange.append(y)
        else:
            for y in range(g, buildingCoords.__len__()):
                yRange.append(y)

        rawMatrix = ors.client.distance_matrix(client=ors.Client(
            key="5b3ce3597851110001cf624892ed276aeec94d0a9fc3f9a1dfa170ad"), locations=buildingCoords,
            destinations=xRange, sources=yRange,
            profile='foot-walking',
            metrics=['distance'], validate=False)

        matrix = rawMatrix['distances']

        if len(finalList) != 95:
            for destinations in matrix:
                finalList.append(destinations)
            print(finalList)
        else:
            for destinations in matrix:
                tempArray.append(destinations)

        if len(tempArray) == len(finalList):
            for i in range(0, len(tempArray)):
                finalList[i] = finalList[i] + tempArray[i]
            print(tempArray)
            print(len(tempArray))

            tempArray = []

data = {}

for index in range(0, finalList.__len__()):
    data[str(index)] = finalList[index]

with open("locationdata/final.json", "w") as f:
    json.dump(data, f)

distance = json.load(open('locationdata/final.json'))
halvedDistances = open('locationdata/filteredfinal.json', 'w')
count = 0
filteredData = {}
for t in range(0, len(distance)):
    filteredData[str(t)] = []

# This is removing the upper half of the matrix. X in the vertical and y is the horizontal (I know, its weird, idk why)
for x in distance:
    for y in range(0, distance[x].__len__()):
        if int(x) <= y:
            filteredData[str(y)].append(distance[x][y])
# Now we only save data where the vertical index is less than the horizontal index
json.dump(filteredData, halvedDistances)
