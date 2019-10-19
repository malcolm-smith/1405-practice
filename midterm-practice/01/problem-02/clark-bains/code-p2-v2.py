assignment_grade = int (input("Assignment grade: "))
midterm_grade = int (input("Midterm grade: "))
exam_grade = int (input("Exam grade: "))
finalGrade = .3*assignment_grade + .3*midterm_grade+.4*exam_grade
if exam_grade > 50 and finalGrade > 60:
    print ("You passed")
else:
    print ("You Failed")