a=[1,2,3,6,7,9]
b=[5,6,9,10]
newlist = []
while len(a)>0 and len(b)>0:
    newlist.append(a.pop(0) if a[0]<b[0] else b.pop(0))
newlist+=(b+a)
print (newlist)