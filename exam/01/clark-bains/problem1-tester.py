
import copy
import importlib

modname = "problem1"
funcname = "median"
information = [[[[9, 17, 13, 0, 11, 15, 8, 6, 11, 9, 6, 7, 14, 10, 19, 0, 9, 4, 8]], 9], [[[3, 6, 20, 16, 10, 6, 9, 15, 7, 5, 0, 20, 13]], 9], [[[20, 11, 8, 2, 15, 1, 12, 19, 1, 11, 12, 9]], 11.0], [[[13, 20, 15, 17, 17, 1, 1, 9]], 14.0], [[[20, 18, 13, 1, 18, 20, 13, 19, 18, 2, 5, 5, 10, 15, 10]], 13], [[[16, 12, 12, 20, 8, 0, 2, 13, 18, 15, 17, 11, 4, 10]], 12.0], [[[13, 13, 2, 5, 9, 17, 9, 10]], 9.5], [[[4, 20, 16, 4, 12, 2, 12]], 12], [[[5, 20, 12, 20, 17, 8, 10, 13, 0, 0, 15, 12, 17, 8, 9, 0, 3, 0, 9, 16]], 9.5], [[[10, 11, 14]], 11], [[[20, 13, 0, 14, 10, 6, 3, 0, 7, 20, 15, 17, 7]], 10], [[[20, 20, 3, 9, 3, 17, 2, 2, 11, 9, 18, 13, 14, 16, 14, 12, 14]], 13], [[[1, 1, 15, 14, 5, 5, 16, 0, 18, 2, 2, 2, 8]], 5], [[[19, 0, 19, 12, 17, 11, 5, 18, 19, 17, 6, 8, 16, 5, 12, 4, 0, 11, 20]], 12], [[[9, 16, 19, 2, 7, 15, 12, 7, 2, 7, 7, 15]], 8.0], [[[2, 5, 6, 4, 15, 12, 1, 7, 4, 2, 0, 15, 6, 18, 1, 13, 10, 18, 5, 2]], 5.5], [[[14]], 14], [[[2, 17, 13, 19, 16, 18]], 16.5], [[[16, 3, 20, 8, 5, 19, 6, 0, 14, 10, 10, 18, 13, 1, 9, 4]], 9.5], [[[14, 11, 20, 8, 13, 7]], 12.0], [[[18, 8, 15, 0]], 11.5], [[[13, 4, 20, 8, 5, 8, 20, 10, 10, 6, 7, 4, 20, 18, 6, 2, 17, 7, 4]], 8], [[[20, 14, 16, 18, 0, 5]], 15.0], [[[8, 9, 9, 18, 17, 9, 2, 4, 9]], 9], [[[10, 1]], 5.5]]
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
    if resulttype == "int":
        success = goal == result
    elif resulttype == "float":
        success = abs(goal - result) < 0.001
    elif resulttype == "string":
        success = goal.lower() == result.lower()

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
		
