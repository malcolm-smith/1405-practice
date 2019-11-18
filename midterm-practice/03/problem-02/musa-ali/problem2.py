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
