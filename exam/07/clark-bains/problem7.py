#This is O(nlogn), as I ripped the merge sort right out of the 1st problem. Everything else is O(n) or O(1), and there are no nested O(n) opperations
def sorted_students(filename):
    lines = readFile(filename)
    students = parseLines(lines)
    sorted = mergeSort(students)
    names = extractNames(sorted)
    return names


def extractNames(sortedStudents):
    lout = []
    for student in sortedStudents:
        lout.append(student[0])
    return lout


def parseLines (lines):
    out = []
    for line in lines:
        student = line.strip().split(",")
        total = 0
        weights = {
            1:.2,
            2:.2,
            3:.2,
            4:.4,
        }
        for i in range(1,len(student)):
            total += float (student[i])*weights[int(i)]
        out.append([student[0],total])
    return out

def readFile (filename):
    f = open (filename, "r")
    line = f.readlines()
    f.close()
    return line

def mergeSort (l1):
    if len(l1) == 1:
        return l1
    return merge(mergeSort(l1[:len(l1)//2]),mergeSort(l1[len(l1)//2:]))
def merge (l1,l2):
    out = []
    minl1 = 0
    minl2 = 0
    while minl1<len(l1) and minl2<len(l2):
        if l1[minl1][1]<=l2[minl2][1]:
            out.append(l1[minl1])
            minl1+=1
        else:
            out.append(l2[minl2])
            minl2+=1
    out+=l1[minl1:]+l2[minl2:]
    return out

sorted_students("grades0.txt")