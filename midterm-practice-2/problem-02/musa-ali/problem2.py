# Practice Midterm 2
# Student Grades

# Gets the average grade from each file
def get_average_grade(filename):
	with open(filename, "r") as fin:

		total = 0
		count = 0

		# Reads every second line (even lines), adds to count and total
		for x, line in enumerate(fin, start=1):
			if x % 2 == 0:
				count += 1
				total += int(line)

		average_grade = total/count
		return average_grade


# Gets the ID of the best student (student with highest grade) from each file
def get_best_student(filename):
	with open(filename, "r") as fin:

		max_grade = 0

		# Get highest grade
		for num, line in enumerate(fin, start=1):
			if num % 2 == 0:
				if int(line) > max_grade:
					max_grade = int(line)

		fin.seek(0)

		# Get student number associated with highest grade
		for x, line in enumerate(fin, start=1):
			if x % 2 == 0:
				if int(line) == max_grade:
					student_line = x-2

		fin.seek(0)

		lines = fin.readlines()
		best_student = lines[student_line]

		return best_student	


def main():

	filenames = ["studentgrades1.txt", "studentgrades2.txt", "studentgrades3.txt"]

	# Prints information for each file
	for file in filenames:
		average = get_average_grade(file)
		best_student = get_best_student(file)

		print("\n    File: " + file)
		print("    Average grade: " + "%.2f" % average)
		print("    Best student: " + best_student)


if __name__ == '__main__':
	main()