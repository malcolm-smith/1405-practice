# Pset 6 Problem 9
# Stack Implementation

def push(stack, value):
	stack.append(value)


def pop(stack):
	if not stack:
		return None
	else:
		return stack.pop()


def isempty(stack):
	if not stack:
		return True
	else:
		return False


def peak(stack):
	if not isempty(stack):
		return stack[-1]
	else:
		return None
