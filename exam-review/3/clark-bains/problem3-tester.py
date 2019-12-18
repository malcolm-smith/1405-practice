
import copy
import importlib

modname = "problem3"
funcname = "mode"
information = [[[[2, 4, 1, 5, 1, 2, 0, 1, 1, 2, 5, 2, 2]], 2], [[[2, 3, 5, 1, 5, 2, 0, 2, 2, 0, 2, 4, 3, 1, 5, 2]], 2], [[[5, 3, 0, 2, 4, 5, 4, 2, 0, 0, 1, 0]], 0], [[[2, 2, 3, 4, 2, 4, 2, 4, 1, 4, 2, 1, 2]], 2], [[[0, 3, 3, 4, 5, 3, 4, 1, 0, 0, 4, 0]], 0], [[[1, 3, 1, 1, 1, 1, 1, 3, 4, 4, 5, 3, 1, 3, 0, 0, 1, 0, 4, 1]], 1], [[[0, 2, 4, 1, 1, 5, 4, 1, 5, 2, 4, 0, 3, 5, 4, 4]], 4], [[[2, 4, 5, 2, 5, 4, 2, 5, 0, 0, 3, 3, 3, 3]], 3], [[[3, 4, 0, 3, 0, 1, 4, 5, 5, 2, 3]], 3], [[[2, 4, 3, 1, 0, 5, 1, 1, 4, 4, 0, 5, 5, 1, 1, 1]], 1], [[[2, 5, 5, 4, 1, 2, 2, 1, 2, 5, 1, 5, 4, 2]], 2], [[[4, 1, 4, 3, 2, 5, 1, 3, 1, 4, 3, 0, 4, 4, 2, 4]], 4], [[[0, 1, 3, 0, 5, 3, 1, 0, 1, 0, 1, 3, 0, 3, 1, 0, 0]], 0], [[[3, 2, 4, 5, 1, 5, 5, 4, 3, 5, 0, 4, 1, 3, 5]], 5], [[[5, 2, 2, 0, 3, 2, 4, 0, 0, 1, 5, 0, 3, 1, 1, 0, 0]], 0], [[[1, 2, 2, 0, 5, 1, 5, 3, 1, 1, 1, 1, 0, 4, 3, 2, 1, 3, 1]], 1], [[[5, 2, 5, 2, 3, 0, 4, 4, 1, 1, 5, 1, 4, 3, 1, 3, 2, 3, 1, 1]], 1], [[[3, 1, 1, 0, 5, 4, 2, 3, 1, 4, 2, 1, 0, 2, 2, 2, 1, 2]], 2], [[[4, 1, 0, 3, 2, 1, 3, 2, 4, 5, 2, 0, 4, 0, 4, 5, 4, 3, 4]], 4], [[[5, 2, 5, 2, 1, 2, 3, 4, 1, 2, 2, 0, 3, 1, 2, 0, 0, 2]], 2], [[[0, 3, 2, 4, 5, 0, 0, 0, 0, 3, 2, 5, 2, 2, 1, 2, 5, 2]], 2], [[[3, 5, 0, 5, 4, 1, 1, 2, 2, 4, 5, 5, 5]], 5], [[[3, 5, 5, 3, 4, 4, 5, 0, 4, 4, 2, 3, 2, 2, 5, 4]], 4], [[[5, 4, 4, 0, 3, 0, 1, 5, 0, 4, 5, 4, 5, 4, 4, 3, 4]], 4], [[[2, 5, 0, 5, 1, 4, 0, 5, 4, 0, 0, 4, 5, 5]], 5]]
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
		
