
def topx (y, x):
    y[:].sort() 
    return y[-x:]
    
def insertIntoSorted (y, x):
    idex = len(y)
    for i in range(len(y)):
        if x<y[i]:
            idex = i
            break
    y.insert(idex,x)

def topxWithoutCheating (y,x):
    z = [y[0] if len(y) else None]
    for val in y[1:]:
        if len(z)<x:
            insertIntoSorted(z,val)
        elif val>z[0]:
            z.pop(0)
            insertIntoSorted(z,val)
    return z





z = [1,2,3,4,5,6,7,8,11,9,10,11]

print (topx(z,5))
print (topxWithoutCheating(z,5))
