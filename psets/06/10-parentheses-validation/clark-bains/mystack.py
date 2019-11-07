def push(stack, value):
    stack.append(value)
    return stack
def pop(stack):
    if isempty(stack):
        return None
    return stack.pop(len(stack)-1)
def isempty(stack):
    return len(stack)==0
def peek(stack):
    return stack[len(stack)-1]