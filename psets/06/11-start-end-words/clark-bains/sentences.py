import re
def startwords (text):
    return uniquify(re.findall(r"\.\s+([\w]+)", text) + re.findall(r"^s*([\w]+)", text))
def endwords (text):
    return uniquify(re.findall(r"([\w]*)\.", text))
def uniquify (l1):
    d1 = {}
    for i in l1:
        d1[i]=i 
    return [key for key in d1]
print (endwords("Hello. I am Clark. I am."))
