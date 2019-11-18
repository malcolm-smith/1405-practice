maxsize = 10


def enqueue(queue, value):
    if len(queue) < maxsize:
        queue.append(value)
        return True
    return False


def dequeue(queue):
    if len(queue):
        return queue.pop(0)
    return None


def peek(queue):
    if len(queue):
        return queue[0]
    return None


def isempty(queue):
    return len(queue) == 0


def multienqueue(queue, item):
    count = 0
    while enqueue(queue, item.pop(0)):
        count += 1
    return count


def multidequeue(queue, number):
    removed = []
    if number < len(queue):
        for i in range(number):
            removed.append(queue.pop(0))
    else:
        removed = queue[:]
        queue.clear()
    return removed
