'''
runs in O(X*N) time, and given X is small enough to be considered constant, runs in O(N) time.
'''
def isvalidseries(L,X,SUM):
    for i in range(0,len(L)-X+1):
        seqSum = 0
        for j in range(i,i+X):
            seqSum += L[j]
        if seqSum > SUM:
            return False
    return True
