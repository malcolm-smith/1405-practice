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
		first = queue.pop()
	else:
		return None


def peek(queue):
	if len(queue) > 0:
		first = queue[-1]
	else:
		return None


def is_empty(queue):
	if len(queue) == 0:
		return True
	else:
		return False


def multi_enqueue(queue, items):
	size = len(queue)
	i = 0
	while i < len(items):
		if size == 10:
			break
		queue.append(items[i])
		i += 1
		size += 1

	return i

def multi_dequeue(queue, number):
	new = []
	i = 0
	while len(queue) > 0:
		if i == number:
			break
		new.append(queue[-1])
		queue.pop()
		i += 1
	
	return new




