def getAverageGrade(filename):
    f = open(filename, 'r')
    linein = f.readline()
    numStudents = 0
    gradeSum = 0
    while linein:
        studentNum = linein.strip()
        linein = f.readline()
        grade = int(linein.strip())
        linein = f.readline()
        numStudents += 1
        gradeSum += grade
        print ("Name: ", studentNum, "Grade: ", grade)
    f.close()
    return gradeSum/numStudents

def getBestStudent(filename):
    f = open(filename, 'r')
    linein = f.readline()
    bestStudent = 0
    bestGrade = 0
    while linein:
        studentNum = linein.strip()
        linein = f.readline()
        grade = int(linein.strip())
        linein = f.readline()
        if grade>bestGrade:
            bestGrade=grade
            bestStudent=studentNum
    f.close()
    return bestStudent
print(getAverageGrade("..\\resources\\studentgrades1.txt"))
print(getBestStudent("..\\resources\\studentgrades1.txt"))