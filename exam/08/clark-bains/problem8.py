#Runtime of O(xn), where x is window size. This is O(n) anyways, assuming x is constant-ish
def isvalidseries(l1,x,max):
    for i in range(len(l1)-x+1):
        if (sumList(l1[i:i+x])>max):
            return False
    return True

def sumList (l1):
    total = 0
    for num in l1:
        total+=num
    return total