# PM3 Problem 2

def removehtml(string):
	words = []
	# Example string: '<html><head><title>Page Title<title><head><html>'
	# While there is still html in the string
	while '<' in string:
		# while string is not empty and the first letter is '<'
		while len(string) > 0 and string[0] == '<':
			# get the index of '>'
			b = string.find('>')
			''' Slice the string to remove the html tag
			Example: 
			string --> '<html><head><title>Page Title<title><head><html>'
			string[0] --> '<'
			string.find('>') --> 5
			string[5+1:] --> '<head><title>Page Title<title><head><html>'''
			string = string[b+1:]

		# if the string is not empty and the first letter is NOT '<'
		if len(string) > 0 and string[0] != '<':
			# get the index of '<'
			a = string.find('<')
			''' Append the found word to the list of words
			Example:
			string --> 'Page Title<title><head><html>' (we get to this step after going through the above while loop a couple times)
			string[0] --> 'P', which is not '<'
			string.find('<') --> 10
			string[:10] --> 'Page Title' ---> THIS IS A WORD and NOT HTML! '''
			words.append(string[:a])
			''' Slice the string so we can look at the string excluding the word we just found
			Example:
			string --> 'Page Title<title><head><html>'
			a --> 10
			string[a:] --> '<title><head><html>' '''
			string = string[a:]

	# convert list of words to a string, seperated by spaces, and return it
	return " ".join(words)
