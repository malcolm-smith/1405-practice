# PM3 Problem 1

def search_employees(file, keyword):
	matches = []
	# Open the file
	with open(file) as f:
		# Read first line
		line = f.readline()
		# Continue reading lines until we reach the end of the file
		while line != '':
			''' Split the line by commas and assigns the first index to 'name'
			EXAMPLE: 
			line --> 1776209, Morgan Williams, 129242
			line.split(',') --> ["1776209", "Morgan Williams", "129242"]
			line.split(',')[1] --> "Morgan Williams" '''
			name = line.split(',')[1]
			# Check if keyword is in any part of name 
			if keyword in name:
				# Add the name to a list of matches
				matches.append(name.strip())
			# Read next line in file
			line = f.readline()

	return matches


def analyze_pay(file):
	pays = []
	total = 0
	# Opens the file
	with open(file) as f:
		# Read first line
		line = f.readline()
		# Continue reading lines until we reach the end of the file
		while line != '':
			# Use same concept as used in the first function, this time to get second index (the pay)
			pay = line.split(',')[2]
			# Add pay to the total
			total += float(pay)
			# Add pay to a list of pays
			pays.append(float(pay))
			# Read next line in file
			line = f.readline()
	# Calculate the average
	avg_pay = total / len(pays)
	# Make a list of the average, maximum, and minimum pays
	pays_list = [avg_pay, max(pays), min(pays)]

	return pays_list