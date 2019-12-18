#This is O(n^2) On line 9-13 are run n times, and the for loop on line 10 runs n times.
#Nested means that the inner one runs in a time equal to the product of all of the nested operations, so nn, or n^2
#
#
def calcDist (l1,l2):
    return (((l1[0]-l2[0])**2)**.5)+(((l1[1]-l2[1])**2)**.5) 
def largest_distance (l1):
    maxVal = 0
    for i in l1:
        for o in l1:
            dist = calcDist(i, o)
            if dist>maxVal:
                maxVal=dist
    return maxVal