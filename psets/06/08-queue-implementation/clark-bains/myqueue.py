quequeSize  = 10
def enqueue (queue, val):
    if len(queue)<quequeSize:
        queue.append(val)
        return True
    return False
def dequeue (queue):
    if len(queue):
        return queue.pop(0)
    return None
def peek(queue):
    if len(queue):
        return queue[0]
    return None
def isempty(queue):
    return len(queue)==0
def multienqueue(queue, items):
    fit = quequeSize-len(queue)
    if fit:
        #Overshooting ending is fine, limited to len internally
        queue+=items[:fit]
        return fit
    return 0
def multidequeue(queue, number):
    itemsRemoved = []
    if number>=len(queue):
        itemsRemoved = queue[:]
        queue.clear()
    else:
        for i in range (number):
            itemsRemoved.append(queue.pop(0))
    return itemsRemoved

