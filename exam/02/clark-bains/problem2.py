#O(n), since it only does O(1) operations in the O(n) loop
def getVol(l1):
    return l1[0]*l1[1]*l1[2]

def largestbox (l1):
    maxVol = getVol(l1[0])
    maxBox = l1[0]
    for box in l1:
        if getVol(box)>maxVol:
            maxVol = getVol(box)
            maxBox = box
    return maxBox