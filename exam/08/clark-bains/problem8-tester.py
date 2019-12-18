
import copy
import importlib

modname = "problem8"
funcname = "isvalidseries"
information = [[[[8, 4, 8, 3, 1, 2, 7, 9], 3, 19], False], [[[2, 4, 8, 3, 1, 2, 7, 9], 3, 19], True], [[[2, 4, 8, 3, 1, 2, 7, 9], 3, 16], False], [[[5, 5, 5, 5, 5, 5, 5, 5], 3, 19], True], [[[5, 5, 5, 5, 5, 5, 5, 5], 4, 19], False], [[[5, 5, 5, 5, 5, 5, 5, 5], 4, 20], True], [[[1, 4, 6, 6, 8, 10, 9, 2, 4, 8, 1, 2, 9, 9, 1], 5, 32], False], [[[1, 3, 8, 4, 8, 6, 5, 5], 4, 25], False], [[[8, 6, 6, 2, 10, 2, 7, 3, 6], 4, 27], True], [[[8, 4, 2, 8, 5, 5, 2, 9, 1, 2, 2, 6, 5, 7, 5, 1], 4, 22], False], [[[9, 10, 8, 6, 8, 3, 5, 10, 10], 4, 38], True], [[[2, 3, 7, 7, 9, 2, 3, 6, 6, 9, 3, 4, 7], 6, 36], True], [[[6, 7, 9, 3, 7, 9, 10, 7, 4, 3, 10, 10, 5, 7, 1, 5, 2, 5, 10, 9, 8, 2], 6, 44], False], [[[10, 8, 9, 8, 5, 8, 7, 7, 4, 5, 7, 4, 1, 8, 7, 6, 1], 6, 43], False], [[[8, 4, 10, 5, 8, 9, 4, 10, 9, 5, 6, 6], 6, 49], True], [[[1, 10, 4, 10, 10, 5, 1, 10], 5, 38], False], [[[7, 7, 1, 7, 3, 4, 9, 1, 6, 2], 3, 18], True], [[[6, 8, 6, 6, 7, 8, 5, 6, 7, 8], 4, 33], True], [[[8, 10, 7, 5, 5, 4, 4, 4, 5, 9, 6, 9, 2, 4, 4, 1, 3], 6, 37], False], [[[10, 2, 7, 5, 9, 3, 3, 7, 3, 6, 10, 5], 6, 40], True], [[[5, 6, 4, 2, 3, 4, 3, 5, 2, 10, 7, 3, 7, 9, 8, 5, 6, 7], 5, 32], False], [[[6, 2, 8, 3, 4, 2, 5, 5, 9, 6, 6, 4, 2, 9, 9], 6, 37], True], [[[6, 4, 2, 9, 8, 1, 3, 8, 4, 4, 2, 6, 7, 10], 4, 26], True], [[[7, 2, 7, 6, 4, 3, 5, 1, 3, 5, 4, 8, 4, 6, 5], 3, 18], True], [[[6, 9, 6, 2, 7, 6, 4, 2, 3], 3, 20], False]]
resulttype = "bool"

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
    elif resulttype == "bool" and isinstance(result, bool):
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
		
