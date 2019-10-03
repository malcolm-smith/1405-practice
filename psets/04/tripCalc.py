import sys
import math
def getDistance (x0, y0, x1, y1):
    val = float(x0-x1)**2
    val+= float(y0-y1)**2
    return math.sqrt(val)
def getItems (filename):
    items = []
    itemFile = open(filename, 'r')
    for item in itemFile:
        item = item.strip()
        descriptors = item.split(',')
        items.append (descriptors)
    itemFile.close()
    return items
def rewriteLocations(items, filename):
    contents = ""
    idex0 = 0
    for item in items:
        idex1 = 0
        for data in item:
            contents+=str(data)
            if (idex1 != (len(item)-1)):
                contents += ","
            idex1+=1
        if idex0 != (len(items)-1):
            contents +="\n"
        idex0+=1
    
    file = open (filename,'w')
    file.write(contents)
    file.close()
def listLocations (cities):
    idex = 0
    for city in cities:
        print ("(" + str(idex) + ")\t" + city[0])
        idex+=1
    print ("")
cities = getItems("locations")
while True:
    print ("1\tAdd City")
    print ("2\tRemove City")
    print ("3\tList City")
    print ("4\tPlan Trip")
    print ("5\tQuit")
    choice = input ("Choice? ")
    if choice == "1":
        cities.append([
            input("City Name: "),
            input("x: "),
            input("y: ")
            ])
    elif choice == "2":
        listLocations(cities)
        elm = input ("Line Num?")
        cities.remove(cities[int(elm)])
    elif choice == "3":
        listLocations(cities)
    elif choice == "4":
        xlast = 0
        ylast = 0
        distance = 0
        while True:
            elm = input ("(q to quit) City: ")
            if ("q" in elm.lower()):
                break
            ynew = int(cities[int(elm)][2])
            xnew = int(cities[int(elm)][1])
            distance += getDistance(xlast,ylast,xnew,ynew)
            xlast = xnew
            ylast = ynew
        print ("Total distance: ", distance)

    elif choice == "5":
        break

rewriteLocations(cities, "locations")
