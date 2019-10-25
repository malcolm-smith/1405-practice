import urllib.request
import sys

#returns the string contents of the page at url, or "" if there is an error
def readurl(url):
	try:
		fp = urllib.request.urlopen(url)
		mybytes = fp.read()

		mystr = mybytes.decode(sys.stdout.encoding)
		fp.close()
		return mystr
	except:
		return ""
		
#returns a list of all addresses that are contained in the given text
def getlinks(text):
	links = []
	
	linkstart = text.find("<a ", 0)
	while linkstart >= 0:
		linkend = text.find(">", linkstart)
		link = text[linkstart:linkend+1]
		linkparts = link.split()
		for part in linkparts:
			if "href" in part:
				address = part.split("=")[1].strip('">')
				address = address.strip("/")
				links.append(address)
		linkstart = text.find("<a ", linkend)

	return links
	
#strips out all contents between < > (including < and >), returns the resulting string
def striphtml(text):
	index = text.find("<")
	while index >= 0:
		endindex = text.find(">", index)
		if endindex > index and endindex < len(text):
			text = text[:index] + text[endindex+1:]
		else:
			break
		index = text.find("<")
	return text
	
	
	
	
	
	
	
def getwordfreqs(test):
	words = test.split()
	result = {}
	for word in words:
		if word not in result:
			result[word] = 0
		result[word] += 1
	return result
	
#print(readurl("http://sikaman.dyndns.org:8888/courses/4601/resources/N-0.html"))