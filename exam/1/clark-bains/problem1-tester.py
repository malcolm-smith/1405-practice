
import copy
import importlib

modname = "problem1"
funcname = "nextprime"
information = [[[1], 2], [[2], 3], [[3], 5], [[4], 5], [[5], 7], [[55], 59], [[41], 43], [[73], 79], [[18], 19], [[48], 53], [[89], 97], [[51], 53], [[98], 101], [[18], 19], [[79], 83], [[41], 43], [[84], 89], [[97], 101], [[93], 97], [[89], 97], [[80], 83], [[67], 71], [[14], 17], [[21], 23], [[76], 79], [[20], 23], [[47], 53], [[52], 53], [[78], 79], [[15], 17]]
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
		
