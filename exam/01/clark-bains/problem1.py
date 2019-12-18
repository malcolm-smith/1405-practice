#This masterpiece is O(nlogn). The actual median is just getting length, which is most likely done through some abstracted property, and O(1), 
#   and accessing lists at indicies, also O(1)
#The Sort function, mergesort, is O(nlogn), since has to process all of the elements, at every level of recursion. Processing the elements
#   is n, and the levels of reccursion are log_2n, making this whole function O(nlogn)

def median (l1):
    sorted = mergeSort(l1)
    mid = len(sorted)/2
    print (mid)
    #Can't remember the int test, this'll do
    if mid//1 == mid:
        return (sorted[int(mid-1)]+sorted[int(mid)])/2
    return sorted[int(mid-0.5)]

def mergeSort (l1):
    if len(l1) == 1:
        return l1
    return merge(mergeSort(l1[:len(l1)//2]),mergeSort(l1[len(l1)//2:]))
def merge (l1,l2):
    out = []
    minl1 = 0
    minl2 = 0
    while minl1<len(l1) and minl2<len(l2):
        if l1[minl1]<=l2[minl2]:
            out.append(l1[minl1])
            minl1+=1
        else:
            out.append(l2[minl2])
            minl2+=1
    out+=l1[minl1:]+l2[minl2:]
    return out
print (median([1,5,6,1,6,7,3,45,8]))
