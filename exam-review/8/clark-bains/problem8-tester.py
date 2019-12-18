
import copy
import importlib

modname = "problem8"
funcname = "xmostfrequent"
information = [[['pear apple kiwi kiwi peach peach kiwi peach peach apple peach', 1], ['peach']], [['apple kiwi peach peach banana banana peach kiwi banana peach', 3], ['peach', 'banana', 'kiwi']], [['peach pear orange kiwi pear banana kiwi banana kiwi pear orange banana pear kiwi kiwi', 4], ['kiwi', 'pear', 'banana', 'orange']], [['apple pear peach pear apple apple banana peach peach apple', 2], ['apple', 'peach']], [['peach orange orange orange peach orange kiwi pear pear apple peach kiwi orange banana apple pear peach apple apple apple apple', 5], ['apple', 'orange', 'peach', 'pear', 'kiwi']], [['pear orange peach kiwi pear peach pear orange peach pear', 4], ['pear', 'peach', 'orange', 'kiwi']], [['banana peach apple banana orange kiwi peach peach apple apple kiwi kiwi apple peach peach', 3], ['peach', 'apple', 'kiwi']], [['pear pear orange banana banana pear', 3], ['pear', 'banana', 'orange']], [['kiwi pear banana orange orange banana kiwi banana kiwi banana', 1], ['banana']], [['pear peach peach banana kiwi apple apple peach pear pear kiwi banana apple pear orange banana peach apple pear peach pear', 6], ['pear', 'peach', 'apple', 'banana', 'kiwi', 'orange']], [['pear apple banana peach apple peach banana peach apple peach', 3], ['peach', 'apple', 'banana']], [['kiwi kiwi kiwi apple apple orange kiwi kiwi banana peach banana banana peach apple apple', 2], ['kiwi', 'apple']], [['banana peach kiwi apple kiwi peach peach peach pear pear apple pear kiwi pear pear', 2], ['pear', 'peach']], [['banana peach banana apple orange kiwi apple peach banana orange apple apple orange orange orange', 1], ['orange']], [['banana banana kiwi apple kiwi kiwi kiwi kiwi kiwi banana peach orange pear kiwi apple pear peach apple apple peach peach peach', 1], ['kiwi']], [['banana kiwi banana pear apple banana apple pear peach peach pear banana peach pear banana', 3], ['banana', 'pear', 'peach']], [['apple kiwi banana peach orange apple apple banana pear peach peach pear banana apple kiwi peach pear pear apple pear apple', 5], ['apple', 'pear', 'peach', 'banana', 'kiwi']], [['kiwi peach pear peach banana peach apple orange orange kiwi banana banana orange kiwi orange pear peach banana orange peach orange', 4], ['orange', 'peach', 'banana', 'kiwi']], [['orange orange peach orange pear orange pear banana orange banana kiwi banana kiwi peach pear pear peach peach peach peach', 2], ['peach', 'orange']], [['apple apple orange peach apple apple orange', 3], ['apple', 'orange', 'peach']], [['orange apple peach banana peach banana kiwi peach peach apple pear orange orange pear apple banana orange banana orange peach orange', 3], ['orange', 'peach', 'banana']], [['kiwi banana banana banana orange pear pear apple kiwi banana kiwi pear orange orange pear banana orange orange banana', 2], ['banana', 'orange']], [['apple kiwi pear orange kiwi orange kiwi apple kiwi banana pear orange apple apple kiwi', 3], ['kiwi', 'apple', 'orange']], [['pear peach apple pear kiwi orange orange orange kiwi orange orange peach kiwi pear kiwi', 4], ['orange', 'kiwi', 'pear', 'peach']], [['banana peach orange pear peach pear orange pear peach pear', 4], ['pear', 'peach', 'orange', 'banana']]]
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
		
