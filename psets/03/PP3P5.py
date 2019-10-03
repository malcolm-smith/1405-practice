lightCol = input ("What Colour is the light?")

if lightCol=="green":
    print ("Continue")
elif lightCol=="yellow":
    disToIntersect = int(input ("Distance to intersection: "))
    speed = float(input ("Speed of car: "))
    if disToIntersect/speed < 5:
        print ("Continue")
    else:
        print ("stop")
else:
    print ("stop")