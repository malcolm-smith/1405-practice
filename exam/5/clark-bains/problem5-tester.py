
import copy
import importlib

modname = "problem5"
funcname = "kthsmallest"
information = [[[[0], 1], 0], [[[4, 2, 0], 1], 0], [[[4, 2, 0], 2], 2], [[[4, 2, 0], 3], 4], [[[0, 1, 2, 3, 4], 5], 4], [[[13, 12, 31, 7], 1], 7], [[[17, 47, 15, 10, 6, 28, 21, 3, 46, 28, 15, 32], 11], 46], [[[8, 0, 16, 39, 19, 34, 44, 46, 7, 38, 13, 1], 4], 8], [[[47, 5, 6, 27], 3], 27], [[[12, 17, 0, 2, 42, 6, 34, 48, 44, 1, 18, 48, 34, 40, 7], 2], 1], [[[19, 6, 3, 41], 1], 3], [[[9, 14, 45, 45, 19, 13, 43], 2], 13], [[[45, 19, 13, 11, 40, 6, 2, 49, 40], 1], 2], [[[12, 35, 10, 12, 47, 50, 7, 14, 16, 37, 38, 40, 36, 30, 30], 13], 40], [[[43, 15, 48, 39, 45, 21, 44, 18, 30, 8, 5, 32, 13, 12, 35], 10], 35], [[[49, 0, 49, 29, 32, 7, 9, 15, 30, 40, 1, 9], 11], 49], [[[7, 31, 23, 5, 38, 30, 15, 10, 21, 8, 30, 19, 11, 47, 50], 12], 31], [[[26, 37, 45, 11, 29, 14, 44, 44, 16], 9], 45], [[[19, 34, 25, 38, 12, 3, 40, 46, 27, 8, 43, 3, 10, 10], 13], 43], [[[33, 22, 45, 17, 42, 8, 9, 8, 23, 8, 38], 6], 22], [[[50, 32, 21, 16, 0, 3], 4], 21], [[[50, 19, 39, 46, 49, 31, 3, 34, 35, 36, 32, 46, 29], 2], 19], [[[23, 10, 18, 49, 28, 27], 4], 27], [[[6, 15, 15, 35, 18, 43, 44, 17, 13], 1], 6], [[[16, 37, 0, 19, 36, 30], 6], 37], [[[42, 49, 37, 4, 48, 39, 29, 43, 32], 7], 43], [[[13, 0, 7, 0, 11, 14, 45, 30, 37, 4, 24], 2], 0], [[[49, 29, 27, 31, 23, 35], 2], 27], [[[43, 19, 32, 43, 44, 37, 25, 31, 49, 39, 9], 7], 39], [[[0, 46, 34, 29, 2, 25, 42, 36, 7, 36, 45, 46, 13], 2], 2]]
resulttype = "int"

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
		
