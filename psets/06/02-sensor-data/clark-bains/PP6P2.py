import random
buffer = []
bufferLen = 5
def measure(num):
    global buffer
    buffer.append(num)
    buffer = buffer[len(buffer)-bufferLen:] if len(buffer)>bufferLen else buffer
def average():
    global buffer
    total = 0
    for val in buffer:
        total+=val
    return total/len(buffer)
def minVal():
    global buffer
    minVal = None if not len(buffer) else buffer[0]
    for val in buffer[1:]:
        minVal = val if val<minVal else minVal
    return minVal
def maxVal():
    global buffer
    maxVal = None if not len(buffer) else buffer[0]
    for val in buffer[1:]:
        maxVal = val if val>maxVal else maxVal
    return maxVal
def isDanger ():
    return (maxVal()-minVal())>10

for i in range (0,10):
    measure(random.randint(10,50))

print (minVal())
print (maxVal())
print (average())
print (isDanger())