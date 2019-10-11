# Pset 5 Problem 5
# Grade Analysis - **

import random
from operator import itemgetter

# Get first name, last name, grade info and append to list of student info
def getInfo(f):

	firsts = []
	for x, line in enumerate(f): # Reads every first name -- Every multiple of 6 (6, 12, 18)th line
		if x % 6 == 0:
			firsts.append(line.strip())

	f.seek(0) 

	lasts = []
	for line in f.read().split("\n")[1::6]: # Reads every last name -- Every 6th line from the 2nd
		lasts.append(line)

	student_info = [list(pair) for pair in zip(firsts, lasts)] # Store first and last names in list

	for student in student_info: # Store student numbers in same list
		student_num = random.randint(10000, 99999)
		student.append(student_num)
	
	return student_info


# Get each grade (assignment, midterm, exam) and add to student_info
def getGrades(f):

	student_info = getInfo(f)

	f.seek(0)

	assignments = []
	for line in f.read().split("\n")[3::6]: # Reads every 6th line starting from the 4th
		assignments.append(int(line))

	f.seek(0) 

	midterms = []
	for line in f.read().split("\n")[4::6]: # Reads every 6th line starting from the 5th
		midterms.append(int(line))

	f.seek(0)

	exam = []
	for line in f.read().split("\n")[5::6]: # Reads every 6th line starting from the 6th
		exam.append(int(line))

	midterms_avg = sum(midterms)/len(midterms)
	assignments_avg = sum(assignments)/100 # len(assignments) is zero for some reason...
	exam_avg = sum(exam)/len(exam)

	# Appends each of the three grades to the student's list
	for student, grade1, grade2, grade3 in zip(student_info, assignments, midterms, exam):
		grades = [grade1, grade2, grade3]
		student.extend(grades)

	return student_info


# Return the highest final average and who it belongs to
def getHighestGrade(s):

	student_info = s

	for student in student_info:
		student.append(student[3]*.25 + student[4]*.25 + student[5]*.5) # Appends weighted average to each student

	# Gets the highest weighted average 
	name_avg = (max(enumerate(map(itemgetter(-1), student_info)),key=itemgetter(1)))

	name_index = name_avg[0]
	student_first = student_info[name_index][0]
	student_last = student_info[name_index][1]
	student = student_first + " " + student_last

	highest_grade = name_avg[1]

	return [student, highest_grade]


def main():

	filein = open('studentinfo.txt', 'r')

	student_info = getGrades(filein)

	getHighestGrade(student_info)

	student_and_grade = getHighestGrade(student_info)
	student = student_and_grade[0]
	highest_grade = student_and_grade[1]

	print("\nThe student with the highest overall final grade is " + student + " with a final grade of " + str(highest_grade) + ".")

	filein.close()

if __name__ == '__main__':
	main()