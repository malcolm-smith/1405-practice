def getVolume (l1):
    return l1[0]*l1[1]*l1[2]

def sortvolumes (l1):
    if len (l1) == 1:
        return l1
    return merge(sortvolumes(l1[:len(l1)//2]),sortvolumes(l1[len(l1)//2:]))
    
def merge(l1,l2):
    l = []
    minl1 = 0
    minl2 = 0
    for n in l1+l2:
        if len(l1[minl1:]) ==0 or len(l2[minl2:]) == 0:
            break
        if getVolume(l1[minl1])<getVolume(l2[minl2]) :
            l.append(l1[minl1])
            minl1 +=1
        else:
            l.append(l2[minl2])
            minl2+=1
    l+=l2[minl2:] + l1[minl1:]
    return l

       
    

    
