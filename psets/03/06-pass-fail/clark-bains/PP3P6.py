lightCol = input ("What Colour is the light?")
disToIntersect = int(input ("Distance to intersection: "))
speed = float(input ("Speed of car: "))
if lightCol=="green":
    print ("Continue")
elif lightCol == "green" or (lightCol=="yellow" and disToIntersect/speed < 5):
    print ("Continue")
else:
    print ("stop")