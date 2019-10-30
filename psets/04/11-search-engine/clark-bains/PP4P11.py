import re, sys
def indexFiles (fileindex):
    f = open (fileindex, "r")
    files = []
    for line in f:
        files.append("..\\resources\\" + line.strip())
    f.close()
    return files
def searchFile (filename, string):
    f = open (filename, "r")
    relevance = 0
    count = 0
    for line in f:
        if re.match(string.strip(), line, re.IGNORECASE):
            relevance +=1
        count+=len(line.split(" "))
    f.close()
    return relevance/count if count > 0 else 0
try:
    filelist = indexFiles("..\\resources\\pages.txt")
except OSError:
    print ("Can't find file.")
    sys.exit(1)
searchstr = input ("Search String: ")
relevance = []
for filename in filelist:
    relevance.append([filename, searchFile(filename, searchstr)])
maxRel = [0,0]
for rel in relevance:
    if rel[1]>maxRel[1]:
        maxRel = rel
if maxRel[1] != 0:
    print ("Best Relevence in \"" + maxRel[0] + "\" is " + str(maxRel[1])) 
else:
    print ("No Results")