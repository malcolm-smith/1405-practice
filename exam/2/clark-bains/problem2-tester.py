
import copy
import importlib

modname = "problem2"
funcname = "minarea"
information = [[[[[20, 11], [7, 11], [25, 1], [24, 22]]], [25, 1]], [[[[7, 23], [15, 5], [11, 4], [18, 18], [2, 5]]], [2, 5]], [[[[3, 23], [3, 9], [7, 22], [18, 15], [14, 3], [14, 19]]], [3, 9]], [[[[18, 8], [14, 2], [10, 23], [13, 23], [7, 3], [12, 10], [15, 11], [25, 19], [19, 6], [3, 19]]], [7, 3]], [[[[19, 12], [18, 19], [3, 14], [11, 12], [14, 4], [14, 17], [22, 11]]], [3, 14]], [[[[22, 4], [9, 16], [1, 25]]], [1, 25]], [[[[12, 16], [9, 12], [8, 13], [23, 12], [20, 7]]], [8, 13]], [[[[16, 24], [4, 23], [25, 9], [3, 22], [22, 20], [6, 25], [18, 3]]], [18, 3]], [[[[24, 9], [1, 5], [24, 15], [19, 17]]], [1, 5]], [[[[3, 7], [14, 25], [18, 23], [16, 14], [4, 7], [15, 22]]], [3, 7]], [[[[20, 8], [3, 16], [19, 3], [20, 16], [22, 6], [3, 4], [6, 6], [8, 14], [10, 10], [21, 5]]], [3, 4]], [[[[18, 1], [9, 18], [16, 22], [1, 1]]], [1, 1]], [[[[21, 14], [23, 7], [15, 24], [23, 10], [18, 11], [2, 4], [20, 1], [8, 12], [9, 20], [6, 2]]], [2, 4]], [[[[23, 12], [16, 2], [9, 10], [19, 9], [10, 2], [17, 1]]], [17, 1]], [[[[5, 18], [19, 1], [22, 7], [12, 12], [11, 25], [11, 12], [14, 10]]], [19, 1]], [[[[8, 15], [2, 8], [4, 21], [8, 1]]], [8, 1]], [[[[25, 23], [9, 7], [16, 10], [25, 3], [7, 12], [1, 20]]], [1, 20]], [[[[21, 2], [5, 9], [14, 2], [16, 13], [20, 22], [2, 20]]], [14, 2]], [[[[11, 2], [9, 9], [16, 11], [22, 17], [7, 6], [12, 16], [10, 5], [18, 4], [2, 8], [13, 2]]], [2, 8]], [[[[6, 20], [12, 6], [7, 10], [7, 15], [24, 12], [1, 4]]], [1, 4]], [[[[1, 1], [4, 6], [14, 8], [19, 5], [21, 23], [19, 10]]], [1, 1]], [[[[3, 6], [20, 18], [19, 9], [5, 16], [1, 22]]], [3, 6]], [[[[1, 21], [5, 16], [20, 20], [20, 10], [3, 1]]], [3, 1]], [[[[20, 4], [12, 23], [23, 1], [10, 21], [1, 15], [11, 23], [11, 9], [21, 25], [22, 15]]], [1, 15]], [[[[23, 5], [3, 12], [13, 5], [1, 3], [16, 7], [13, 7], [10, 9], [15, 14], [6, 17]]], [1, 3]]]
resulttype = "orderedlist"

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
		
