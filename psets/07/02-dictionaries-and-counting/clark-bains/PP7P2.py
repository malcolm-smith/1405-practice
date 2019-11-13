import time, random
def factorial(num):
    total = 1
    for i in range (num, 1, -1):
        total*=i
    return total

def cachedFactorial(num, dic):
    if num in dic:
        return dic[num]
    else:
        total = 1
        for i in range (num, 1, -1):
            if i in dic:
                total*=dic[i]
                break
            else:
                total*=i
    dic[num] = total
    return total
cache = {}
a = time.time()
for i in range (5000):
    factorial(random.randrange(1,5000))
print ("Reg: ", (time.time()-a))

b = time.time()
for i in range (5000):
    cachedFactorial(random.randrange(1,5000), cache)
print ("Cache: ", (time.time()-b))

