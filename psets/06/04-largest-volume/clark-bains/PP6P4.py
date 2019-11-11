def reduceList (listIn, func):
    #Me? Creating javascript methods in python? Of course not
    return func(listIn)
def maxvolume (x):
    x=x[:]#Comment to mutate original Array
    for i in range (len(x)):
        x[i] = reduceList(x[i] ,lambda x: x[0]*x[1]*x[2])
    maxVol = None if not len(x) else x[0]
    for val in x[1:]:
        maxVol = val if val>maxVol else maxVol
    return maxVol
    
y = [[4,5,6], [9,10,11],[7,8,9]]
print (maxvolume(y))
print (y)