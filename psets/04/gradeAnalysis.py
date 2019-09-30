class Student(object):

    def __init__(self, first_name, last_name, student_num, assignment, midterm, exam):
        self.first_name = first_name
        self.last_name = last_name
        self.student_num = student_num
        self.assignment = assignment
        self.midterm = midterm
        self.exam = exam
        self.final_grade = 0.25 * assignment + 0.25 * midterm + 0.5 * exam
        self.passes = self.final_grade >= 50 and self.exam >= 50
        self.summary = [self.first_name, self.last_name, self.student_num, self.assignment, self.midterm, self.exam, self.final_grade, self.passes]


grades = open('psets/04/grades.txt', 'r')

lines = grades.read().split('\n')
students = []

for i in range(0, len(lines), 6):
    students.append(Student(lines[i], lines[i + 1], int(lines[i + 2]), int(lines[i + 3]), int(lines[i + 4]), int(lines[i + 5])))

total_passes = 0
final_grade_average = 0
for student in students:
    final_grade_average += student.final_grade
    if student.passes:
        total_passes += 1
final_grade_average = final_grade_average / len(students)

lowest_student = students[0]
highest_student = students[0]
for i in range(1, len(students)):
    if students[i].final_grade < lowest_student.final_grade:
        lowest_student = students[i]
    if students[i].final_grade > highest_student.final_grade:
        highest_student = students[i]

print('There was %d students that passed the class' % total_passes)
print('The class average was %d' % final_grade_average)
print('%s had the lowest average of %d' % (lowest_student.first_name, lowest_student.final_grade))
print('%s had the highest average of %d' % (highest_student.first_name, highest_student.final_grade))