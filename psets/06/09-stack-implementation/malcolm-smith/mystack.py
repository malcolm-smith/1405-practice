def push(stack, value):
    stack.append(value)
    return stack


def pop(stack):
    if len(stack):
        return stack.pop(-1)
    return None


def isempty(stack):
    return len(stack) == 0


def peek(stack):
    if len(stack):
        return stack[-1]
    return None
