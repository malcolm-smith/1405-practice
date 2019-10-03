fExam = float(input ("Final Exam Mark: "))
fMark = fExam *.4
for i in range (1,4):
     fMark += 0.2 * float(input("Enter your mark for midterm: " + str(i)))

bonusAssignment = input("Enter your bonus mark or leave blank: ")
if (bonusAssignment):
    fMark -= (float(bonusAssignment)/1000) * fExam
    fMark += float(bonusAssignment)/10

print ("Final mark is " + str(fMark))