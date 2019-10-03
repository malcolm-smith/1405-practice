location1 = input ("Location Name? ")
x1 = int (input("X-coordinate: "))
y1 = int (input("Y-coordinate: "))
location2 = input ("Location Name? ")
x2 = int (input("X-coordinate: "))
y2 = int (input("Y-coordinate: "))
location3 = input ("Location Name? ")
x3 = int (input("X-coordinate: "))
y3 = int (input("Y-coordinate: "))

d12 = (((x1-x2)**2) + ((y1-y2)**2))**.5
d13 = (((x1-x3)**2) + ((y1-y3)**2))**.5
d23 = (((x3-x2)**2) + ((y3-y2)**2))**.5

if d12 < d13 and d12 < d23:
    closestCity = location1 + " " + location2
elif d13<d12 and d13< d23:
     closestCity = location1 + " " + location3
elif d23<d12 and d23< d13:
     closestCity = location2 + " " + location3
else:
    closestCity = "Outside of the scope of assignment"

if d12 > d13 and d12 > d23:
    furthestCity = location1 + " " + location2
elif d13 > d12 and d13 > d23:
     furthestCity = location1 + " " + location3
elif d23 > d12 and d23 > d13:
     furthestCity = location2 + " " + location3
else:
    furthestCity = "Outside of the scope of assignment"
print ("Closest Cities: " + closestCity)
print ("Furthest Cities: " + furthestCity)