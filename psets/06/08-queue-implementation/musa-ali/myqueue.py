# Pset 6 Problem 8
# Queue Implementation

global max_size
max_size = 10

def enqueue(queue, value):
	if len(queue) < max_size:
		queue.append(value)
		return True
	else:
		return False


def dequeue(queue):
	if len(queue) > 0:
		return queue.pop(0)
	else:
		return None


def peek(queue):
	if len(queue) > 0:
		first = queue[0]
		return first
	else:
		return None


def is_empty(queue):
	if len(queue) == 0:
		return True
	else:
		return False


def multienqueue(queue, items):
	size = len(queue)
	i = 0
	while i < len(items):
		if size == 10:
			break
		queue.append(items[i])
		i += 1
		size += 1

	return i

def multidequeue(queue, number):
	new = []
	if number > len(queue):
		del queue[:]
		return queue
	else:
		for i in range(number):
			new.append(queue[i])
		del queue[:number]

		return new


