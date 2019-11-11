import mystack
def isvalid(string):
    closeToOpen = {"}":"{","]":"[",")":"("}
    closing = closeToOpen.keys()
    opening = closeToOpen.values()
    openStack = []
    for i in string:
        if i in opening:
            mystack.push(openStack, i)
        elif i in closing:
            if not mystack.isempty(openStack) and closeToOpen[i] == mystack.peek(openStack):
                mystack.pop(openStack)
                continue
            return False
    return mystack.isempty(openStack)
            

