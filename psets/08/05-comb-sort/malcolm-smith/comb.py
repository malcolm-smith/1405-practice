from math import floor, sqrt

def combsort(input):
    gap = len(input)
    shrink = 1.3
    sorted = False
    while sorted == False:
        gap = floor(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while (i + gap) < len(input):
            if (sqrt((input[i][0]**2) * (input[i][1]**2))) > (sqrt((input[i + gap][0]**2) * (input[i + gap][1]**2))):
                input[i], input[i + gap] = input[i + gap], input[i]
                sorted = False
            i += 1
    return input

print(combsort([[2, 1], [2, 2], [3, 3], [3, 1], [1, 1], [1, 2]]))
