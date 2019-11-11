import mystack
def isvalid(string):
    closeToOpen = {"}":"{","]":"[",")":"(", "\"":"\"","”":"“"}
    closing = closeToOpen.keys()
    opening = closeToOpen.values()
    openStack = []
    for i in string:
        if i in opening:
            #print ("Adding", i, openStack)
            mystack.push(openStack, i)
        elif i in closing:
            if not mystack.isempty(openStack) and closeToOpen[i] == mystack.peek(openStack):
                #print ("Removing", closeToOpen[i], i, openStack)
                mystack.pop(openStack)
                continue
            return False
    #print (openStack)
    return mystack.isempty(openStack)
#print(isvalid('{“key1”:“value1”,“key2”:“value2”,“key3”:“value3”,“key4”:{“key11”:“value11”,“key21”:“value12”},“keyn”:“valuen”}'))
            

