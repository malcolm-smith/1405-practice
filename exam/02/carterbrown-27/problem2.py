# runs in O(n) time
def largestbox(lst):
    maxVolume = 0
    maxIndex = 0
    for i in range(0,len(lst)):
        volume = calcVolume(lst[i])
        if volume > maxVolume:
            maxVolume = volume
            maxIndex = i
    return lst[maxIndex]

def calcVolume(box):
    return box[0] * box[1] * box[2]
