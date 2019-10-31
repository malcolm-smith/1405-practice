# Pset 6 Problem 10
# Parentheses Validation
from mystack import *

opens = ['{', '[', '(']
closed = ['}', ']', ')']


def isvalid(string):
	stack = []
	for char in string:
		if char in opens:
			push(stack, char)
			pars += 1

		elif char in closed:
			i = closed.index(char)
			if not isempty(stack) and (opens[i] == peak(stack)):
				pop(stack)
			else:
				return False

	if isempty(stack):
		return True
