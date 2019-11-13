def removehtml(s1):
    state  = None
    stateIdex = 0
    tagsAndText=s1.split("<")
    for i in range(len(tagsAndText)):
        if ">" in tagsAndText[i]:
            tagsAndText[i]=tagsAndText[i].split(">")[1]
    retval=""
    for tag in tagsAndText:
        if len(tag)>0:
            retval+=tag
    return retval
print(removehtml('<a href="p1">Link 1</a><a href="p2">Link 2</a>'))

            
