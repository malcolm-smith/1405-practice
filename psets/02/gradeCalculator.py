finalGrade = 0
for i in range(1, 4):
    finalGrade += (int(input('Enter your #%d midterm grade:\t' % i)) * 0.2)
finalGrade += (int(input('Enter your final grade:\t')) * 0.4)
print(round(finalGrade, 4))
