dic = {}
def addword(dic, str):
    tmpdic = dic
    for i in range(len(str)):
        
        if str[i] not in tmpdic:
            tmpdic[str[i]] = {} if i < len(str)-1 else {'.':1}
        tmpdic = tmpdic[str[i]]
        
def checkword (dic,str):
    tmpdic = dic
    str += '.'
    for i in range(len(str)):
        if str[i] not in tmpdic:
            return False    
        tmpdic = tmpdic[str[i]]
    return True
def initialize(dic, fname):
    f = open (fname, 'r')
    for line in f:
        addword(dic,line.strip())

initialize(dic, "testfile2.txt")
print (checkword(dic, "able"))
print (checkword(dic, "apple"))

