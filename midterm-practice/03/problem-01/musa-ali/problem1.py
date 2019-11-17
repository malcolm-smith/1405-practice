# PM3 Problem 1

def search_employees(file, keyword):
	matches = []
	with open(file) as f:
		employee = f.readline()
		while employee != '':
			name = employee.split(',')[1]
			if keyword in name:
				matches.append(name.strip())
			employee = f.readline()
	return matches


def analyze_pay(file):
	pays = []
	total = 0
	with open(file) as f:
		employee = f.readline()
		while employee != '':
			pay = employee.split(',')[2]
			total += float(pay)
			pays.append(float(pay))
			employee = f.readline()
	avg_pay = total / len(pays)
	pays_list = [avg_pay, max(pays), min(pays)]
	return pays_list