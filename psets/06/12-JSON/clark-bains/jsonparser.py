import validator


def findValue (string):
    for i in range (1,len(string)):
        test = string[:i]
        if validator.isvalid(test):
            return test
def removeQuotes (string, quoteStart, quoteEnd):
    if string[0] in quoteStart:
        string = string[1:]
    if string[-1] in quoteEnd:
        string = string[:-1]
    return string

def parseJson (string):
    idex = 0
    a = {}
    for char in string:
        if char == "," or idex == 0 :
            nextColon = string.find(":",idex+1)
            key = string[idex+1:nextColon]
            key = removeQuotes(key, ['“'],['”'])
            value = findValue(string[nextColon+1:])
            if value.startswith('“') and value.endswith('”'):
                a[key]=removeQuotes(value, ['“'],['”'])
            else:
                a[key]=parseJson(value)
        idex +=1
    return a    
b = parseJson('{“key1“:“value1”,“key2”:“value2”,“key3”:“value3”,“key4”:{“key11”:“value11”,“key21”:“value12”},“keyn”:“valuen”}')
print (b)

