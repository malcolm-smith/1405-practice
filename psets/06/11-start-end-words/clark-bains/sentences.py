import re
def startwords (text):
    return uniquify(re.findall("\.\s+([\w]+)", text) + re.findall("^s*([\w]+)", text))
def endwords (text):
    return uniquify(re.findall("([\w]*)\.", text))
def uniquify (l1):
    d1 = {}
    unique = []
    for i in l1:
        d1[i] = True
    for key in d1:
        unique.append(key)
    return unique
print (endwords("Hello. I am Clark. I am."))
