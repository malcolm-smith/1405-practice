
def isvalidseries (l1, x,max):
    for i in range (len(l1)-x+1):
        window = l1[i:i+x]
        windowSum = 0
        for elm in window:
            windowSum +=elm
        print (windowSum)
        if windowSum > max:
            return False
    return True