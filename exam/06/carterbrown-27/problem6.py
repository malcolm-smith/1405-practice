'''
This runs in O(N^2) time for the same reason selection sort does.
The outer loop will iterate over all N elements, and the inner loop will iterate over N-a elements each time.
O(N * (N-1 + N-2 + N-3 ... 0)), which simplifies to O(N^2)
'''
def largest_distance(lst):
    maxDist = 0
    for a in range(0,len(lst)):
        for b in range(a+1,len(lst)):
            maxDist = max(maxDist,manhattan(lst[a],lst[b]))
    return maxDist

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
