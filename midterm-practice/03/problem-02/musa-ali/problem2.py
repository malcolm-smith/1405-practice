# PM3 Problem 2

def removehtml(string):
	words = []
	while '<' in string:
		while len(string) > 0 and string[0] == '<':
			a = string.find('<')
			b = string.find('>')
			string = string[b+1:]
		if len(string) > 0 and string[0] != '<':
			a = string.find('<')
			words.append(string[:a])
			string = string[a:]
	return " ".join(words)

print(removehtml('<html><head><title>Page Title<title><head><html>'))
print(removehtml('<a href=”p1”>Link 1</a><a href=”p2”>Link 2</a>'))
print(removehtml('<p>Click <a href=”here.html”>here</a></p>'))
