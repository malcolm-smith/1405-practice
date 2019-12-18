
import copy
import importlib

modname = "problem6"
funcname = "largest_distance"
information = [[[[[7, -8], [10, 2], [3, 10], [2, 7], [-6, -6], [-6, -2], [-5, 1], [2, 5], [-2, -5], [10, -2]]], 25], [[[[-7, -4], [4, -7], [-7, 3], [1, 4], [8, 8], [-1, -4], [-2, 6], [5, 2], [-3, -2], [0, 4], [5, 10], [-6, 4], [-9, 7], [7, -4], [3, -10], [9, 2], [0, -2], [-3, 0]]], 29], [[[[0, -10], [0, -4], [1, 4], [-10, 4], [0, -9], [2, -5], [10, 6], [-4, 1], [7, 0], [-7, -1], [3, 4], [10, -4], [2, 0]]], 28], [[[[-1, -7], [-7, 8]]], 21], [[[[-8, -10], [-6, -6], [10, 6], [3, -2], [10, -10], [6, 4], [-3, 0], [10, 0], [7, -10], [-1, 3], [3, -10], [1, -2], [-9, -10], [-5, 7], [-8, -3], [0, -8], [-3, 3], [-8, 3], [1, 7], [9, 1]]], 35], [[[[6, -7]]], 0], [[[[6, -3], [-8, -8], [-7, 5], [8, -5], [2, 2], [5, -3], [-6, 9], [-7, 2], [-8, 8], [3, 7], [-8, -4], [-9, -8], [-5, 7], [1, -8], [-1, -4], [-5, 8], [-6, 7], [1, -4], [6, 4]]], 29], [[[[9, -5], [10, -8], [1, -3], [0, -10], [-2, 2], [-10, 7], [10, 2], [-9, 7], [-7, -5], [9, -10], [2, -9], [7, 4]]], 36], [[[[2, 4], [-1, 9], [0, 7]]], 8], [[[[-5, 6], [7, -1], [10, -1]]], 22], [[[[0, -7], [9, 4], [5, -9], [-9, 6], [-3, 2], [9, 10], [0, 5], [-5, 7], [0, 0], [-9, -8], [-5, -2], [0, 3], [8, 10], [-6, 8], [-2, 7], [-1, -5], [2, 6], [-3, -7], [7, -3], [-6, -10]]], 36], [[[[-7, -3], [1, 9], [7, 6], [-7, 2], [0, 1], [3, -6]]], 23], [[[[1, 10], [2, 6], [8, 10], [-7, 7], [7, -1], [-4, -9]]], 31], [[[[6, -1], [-8, 8], [-4, -10], [-5, 8], [9, 3], [-4, -7], [1, 8], [0, -8], [2, -3], [-9, -1], [-2, 0], [-7, 9], [10, 1], [-8, 8]]], 26], [[[[-4, -2], [-4, 5], [10, -6]]], 25], [[[[-10, -1], [-4, -7], [1, -10], [-3, 5], [-9, 3], [3, 9], [-10, -1], [-6, -9], [2, -7], [4, 7], [-9, -4], [4, 7], [4, 10], [4, -3], [10, 5], [0, -2], [2, 5], [10, 0]]], 30], [[[[0, 6]]], 0], [[[[-8, -4], [-1, 3]]], 14], [[[[0, 6], [7, 6], [3, -1], [4, 8], [-4, -3], [-7, -4], [-9, -2], [-7, 2], [-8, 7], [10, -6], [5, 8]]], 31], [[[[-4, -5], [3, 6], [-7, -5], [-1, 6], [-5, 9], [-1, 9], [-3, -3], [2, -3], [-2, -5], [-9, 0], [-9, 5], [-4, -2], [-6, -10], [9, 10], [-4, 9], [9, 1], [4, -7], [7, -4], [10, -7], [2, 3]]], 35], [[[[-10, 5]]], 0], [[[[-10, 4], [1, -4], [10, -5], [-5, -2], [3, 8], [-8, 5], [-2, 7], [-2, -5], [5, -1], [-5, 2], [-8, -3], [0, -7], [-2, 9], [-4, -3], [7, -4], [4, -4], [1, -6], [0, 10], [3, 8], [-4, 3]]], 29], [[[[-10, 6], [-7, 8], [-2, -6], [1, 9], [-10, 2]]], 20], [[[[5, -9], [4, 3], [-2, -2], [1, 8], [-9, 8], [-9, -1], [-1, 3], [2, 2], [-5, -9], [-8, -7], [-2, -9], [4, 8], [4, 1], [-2, 9], [5, -4], [1, -1], [10, -1], [-8, 4], [-6, 3], [6, 1]]], 31], [[[[4, 10], [-1, -6], [-8, 6], [5, 4], [1, 2], [-2, 5], [0, 9], [0, -2]]], 21]]
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
		
