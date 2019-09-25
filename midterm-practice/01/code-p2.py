assignmentGrade = 0.3 * float(input('Assignment Grade: '))
midtermGrade = 0.3 * float(input('Midterm Grade: '))
examGrade = 0.4 * float(input('Exam Grade: '))

finalGrade = assignmentGrade + midtermGrade + examGrade
coursePass = examGrade >= 50 * 0.4 and finalGrade >= 60

print('Final Grade: %.2f\n%s' % (finalGrade, coursePass))