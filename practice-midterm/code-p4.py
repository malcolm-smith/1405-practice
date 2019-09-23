import math


def getCoords():
    coords = str.split(input('Enter coords (X Y Name):\t'), ' ')
    coords[0] = float(coords[0])
    coords[1] = float(coords[1])
    return coords


def getDistance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


cities = [getCoords(), getCoords(), getCoords()]
distances = []

distances.append([getDistance(
    cities[0][0], cities[0][1], cities[1][0], cities[1][1]), cities[0][2], cities[1][2]])
distances.append([getDistance(
    cities[0][0], cities[0][1], cities[2][0], cities[2][1]), cities[0][2], cities[2][2]])
distances.append([getDistance(
    cities[1][0], cities[1][1], cities[2][0], cities[2][1]), cities[1][2], cities[2][2]])

lowest = distances[0]
highest = distances[0]
for i in range(2, 3):
    if distances[i][0] < lowest[0]:
        lowest = distances[i]
    elif distances[i][0] > highest[0]:
        highest = distances[i]

print('The lowest distance is %.2f, between %s and %s' %
      (lowest[0], lowest[1], lowest[2]))
print('The highest distance is %.2f, between %s and %s' %
      (highest[0], highest[1], highest[2]))
