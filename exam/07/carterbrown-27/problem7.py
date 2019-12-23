def sorted_students(filename):
    f = open(filename)
    students = {}
    for line in f:
        arr = line.split(",")
        name = arr[0]
        t1 = int(arr[1])
        t2 = int(arr[2])
        t3 = int(arr[3])
        exam = int(arr[4])

        students[name] = (t1*0.2 + t2*0.2 + t3*0.2 + exam*0.4)
    f.close()

    result = []
    while len(students) > 0:
        lowest = 10000
        lowestName = "?"
        for name, grade in students.items():
            if grade < lowest:
                lowest = grade
                lowestName = name
        result.append(lowestName)
        students.pop(lowestName)

    return result
