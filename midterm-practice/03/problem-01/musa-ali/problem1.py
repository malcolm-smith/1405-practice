# PM3 Problem 1

def search_employees(file, keyword):
	matches = []
	with open(file) as f:
		line = f.readline()
		while line != '':
			name = line.split(',')[1]
			if keyword in name:
				matches.append(name.strip())
			line = f.readline()
	return matches


def analyze_pay(file):
	pays = []
	total = 0
	with open(file) as f:
		line = f.readline()
		while line != '':
			pay = line.split(',')[2]
			total += float(pay)
			pays.append(float(pay))
			line = f.readline()
	avg_pay = total / len(pays)
	pays_list = [avg_pay, max(pays), min(pays)]
	return pays_list