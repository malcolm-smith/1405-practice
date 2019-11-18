def addend(list, dict, value):
    if value not in dict:
        dict[value]=1
    else:
        dict[value] +=1
    list.append(value)
    
def removestart(list,dict):
    if len(list) == 0:
        return None
    val = list.pop(0)
    dict[val] -=1
    if dict[val] < 1:
        del dict[val]
    return val

def containsHash(dict, value):
    return value in dict and dict[value] > 0
    
import random
list = []
hash = {}
for i in range(25):
    if random.randint(0,100) < 75:
        num = random.randint(0,10)
        print("Adding", num)
        addend(list,hash,num)
    else:
        num = removestart(list,hash)
        print("Removed", num)
    print(list)
    print(hash)