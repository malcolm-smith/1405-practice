def getAverageGrade(filename):
    counter = 0
    sum = 0
    for line in open(filename):
        counter += 1
        if counter % 2 == 0:
            sum += float(line)
    return sum / (counter / 2)


def getBestStudent(filename):
    counter = 1
    bestGrade = 0
    currentStudent = 0
    bestStudent = 0
    for line in open(filename):
        if counter % 2 != 0:
            currentStudent = int(line)
        else:
            if float(line) > bestGrade:
                bestStudent = currentStudent
                bestGrade = float(line)
        counter += 1

files = [
    'studentgrades1.txt',
    'studentgrades2.txt',
    'studentgrades3.txt',
]

for file in files:
    print('%s: %.2f average, %d best student' % (file, getAverageGrade(file), getBestStudent(file)))