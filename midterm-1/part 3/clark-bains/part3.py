dirtHere = input ("Is there dirt here? ").lower()=="yes"
emptySpace = input ("Is there empty space ahead? ").lower()=="yes"
if dirtHere:
    print ("vacuum")
elif emptySpace:
    print ("move forward")
else:
    print ("turn right")