import math
def getDistance (x0, y0, x1, y1):
    val = float(x0-x1)**2
    val+= float(y0-y1)**2
    return math.sqrt(val)

xlast = 0
ylast = 0
distance = 0
while True:
    xnew = input ("X-coord")
    ynew = input ("Y-coord")
    if ("q" in [xnew, ynew]):
        break
    ynew = int(ynew)
    xnew = int(xnew)
    distance += getDistance(xlast,ylast,xnew,ynew)
    xlast = xnew
    ylast = ynew
print ("Total distance", distance)