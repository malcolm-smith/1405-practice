filename = input ("Enter File Name: ")
passed = 0
failed = 0
n = 0
itCount = 0
avg = 0
highGrade = 0
highName = ""
lowGrade = 100
lowName = ""
tmpName = ""
tmpGrade = 0

file = open (filename,"r")
for line in file:
    line = line.strip() #Strip Trailing newline
    itCount +=1
    if itCount == 1: #fname
        tmpName = line
    if itCount ==2: #lname
        tmpName += " " + line
    if itCount == 3:
        continue
    if itCount == 4:
        tmpGrade = .25 * int(line)
    if itCount == 5:
        tmpGrade += .25 * int(line)
    if itCount == 6:
        tmpGrade += .50 * int(line)
        itCount = 0
        if tmpGrade >= 50:
            passed += 1
        else:
            failed +=1

        if tmpGrade == highGrade:
            highName = tmpName + ", " + highName
        elif tmpGrade > highGrade:
            highGrade = tmpGrade
            highName = tmpName

        if tmpGrade == lowGrade:
            lowName = tmpName + ", " + lowName
        elif tmpGrade < lowGrade:
            lowGrade = tmpGrade
            lowName = tmpName
        n = n + 1
        avg += tmpGrade
file.close()
avg = avg/n

print ("Number of Passes: " + str(passed))
print ("Number of Fails: " + str(failed))
print ("Average Final Grade: " + str(avg))
print ("The Highest Grade: " + highName + " - " + str(highGrade))
print ("The Lowest Grade: " + lowName + " - " + str(lowGrade))