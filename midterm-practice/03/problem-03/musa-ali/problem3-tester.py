
import copy
import importlib

modname = "problem3"
funcname = "jaccard"
information = [[[[15, 22, 21, 24, 8, 2, 7, 16], [3, 20, 15, 21, 18]], 0.18181818181818182], [[[6, 10, 2, 18, 4], [1, 12, 2, 3]], 0.125], [[[1, 3, 0, 3, 1, 8, 12, 7, 8], [1, 15, 16, 17, 19, 8, 1]], 0.2], [[[8, 22, 21, 20, 21, 4], [25, 5, 25]], 0.0], [[[0, 25, 22, 1], [12, 19, 9, 4, 22, 19, 15]], 0.1111111111111111], [[[2, 17, 25, 18, 19, 11, 6, 8, 8, 10], [21, 4, 13, 17, 8, 4]], 0.16666666666666666], [[[25, 19, 18, 20, 10, 8, 1, 0, 22, 4], [1, 25, 6]], 0.18181818181818182], [[[5, 18, 22, 23, 11, 25, 17, 24], [11, 7, 1, 14]], 0.09090909090909091], [[[8, 5, 10, 15, 1], [12, 10, 4, 6, 18, 25, 22, 1]], 0.18181818181818182], [[[20, 23, 6, 16, 19, 23, 24, 12, 0, 19], [23, 5, 19, 4, 7, 1, 19]], 0.16666666666666666], [[[1, 3, 25, 5, 8, 10, 2, 23, 0, 25], [0, 0, 11, 13, 17, 17, 16, 9]], 0.07142857142857142], [[[25, 6, 25, 9, 20, 3, 5, 24], [15, 4, 13, 9]], 0.1], [[[10, 11, 3, 21, 19, 19, 11, 21, 21], [25, 3, 0, 9, 19, 17, 2, 19]], 0.2], [[[23, 9, 6, 5, 25, 18, 1, 17], [7, 3, 6, 12, 22, 0, 18, 12, 7, 12]], 0.15384615384615385], [[[17, 6, 2, 12, 7, 15, 24, 18, 9], [16, 7, 15, 24, 5, 5, 18, 0, 12]], 0.4166666666666667], [[[19, 10, 5, 19, 11, 9, 15], [6, 8, 25, 21, 16, 19, 25, 4]], 0.08333333333333333], [[[4, 4, 1, 4, 9], [8, 2, 24, 15, 17, 24, 13]], 0.0], [[[9, 4, 2, 5, 8, 24], [11, 24, 18, 5, 25, 1]], 0.2], [[[4, 14, 8, 2, 18, 23, 22, 1], [16, 23, 24, 8, 4, 13, 23]], 0.2727272727272727], [[[25, 5, 2, 5, 10, 7], [7, 17, 25, 2, 16, 18]], 0.375], [[[12, 9, 16, 21, 8, 8, 9, 15, 11, 2], [18, 8, 13]], 0.1], [[[9, 9, 16, 7, 7], [6, 0, 19]], 0.0], [[[13, 5, 20], [1, 15, 13, 4, 6, 23, 20]], 0.25], [[[17, 13, 4, 9, 7, 4, 1, 24, 1], [4, 18, 16, 5, 4, 9, 23]], 0.18181818181818182], [[[13, 18, 20, 11], [13, 9, 12, 2, 9, 1, 18]], 0.25]]
resulttype = "float"

try:
    module = importlib.import_module(modname)
    func = getattr(module,funcname)
except:
    print("Error loading module and/or function - check the names?")
    quit()

correct = 0
incorrect = []
print("Checking function with test inputs...")
print()
for info in information:
    inputs = copy.deepcopy(info[0])
    goal = info[1]
    print("Inputs:", str(inputs)[1:-1])
    print("Goal:",goal)
    result = func(*inputs)
    print("Your Result:", result)
    success = False
    if resulttype == "int" and isinstance(result, int):
        success = goal == result
    elif resulttype == "float" and isinstance(result, (int,float)):
        success = abs(goal - result) < 0.001
    elif resulttype == "string" and isinstance(result, str):
        success = goal.lower() == result.lower()
    elif resulttype == "orderedlist" and isinstance(result, list):
        success = False
        if len(goal) == len(result):
            success = True
            for i in range(len(goal)):
                if goal[i] != result[i]:
                    success = False

    if success:
        correct += 1
        print("Good!")
    else:
        incorrect.append([inputs,goal,result])
        print("Incorrect!")
    print()
	
print()
print("Your code produced",correct,"out of", len(information),"correct results.")
print()

if len(incorrect) > 0:
    input("Hit enter to see the incorrect cases...")
    print("The inputs for which your program failed were:")
    print()
    for info in incorrect:
        print("Inputs:", str(info[0])[1:-1])
        print("Goal:", info[1])
        print("Your Result:", info[2])
        print()
		
