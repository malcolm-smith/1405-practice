
import copy
import importlib

modname = "problem7"
funcname = "sorted_students"
information = [[['grades0.txt'], ['Heidi Jones', 'Larry Zimmerman', 'Jerald Phillips', 'Mamie Donaldson', 'Coleen Bone', 'Richard Moffat', 'Ruth Klena', 'Ronald Carrion']], [['grades1.txt'], ['Steven Smith', 'Trudy Blackwell', 'Sidney Watson', 'Joshua Young', 'Jacqueline Soren', 'Robert Knight', 'Ian Kerns', 'Edward Inoue', 'Lynda Vasquez', 'Timothy Person', 'Classie Heath', 'Maria Sandy', 'Michael Studivant', 'Geraldine Gill']], [['grades2.txt'], ['Ignacio Mcclung', 'Roger Noble', 'Max Kirby', 'Sean Fields', 'John Hoover']], [['grades3.txt'], ['Cheryl Pfeiffer', 'Anita Shields', 'John Angles', 'Brandon Dubill', 'Edward Williams', 'Gayle Reiss', 'Anastasia Lewis', 'Brenda Norman', 'Carol Knighten', 'Scott Price', 'Carmen Solomon', 'John Leos', 'Erica Ramirez', 'Ruth Mckee', 'Robert Norris', 'Robin Torres', 'Chad Harrison', 'Ethel Dorsey', 'Larry Soder', 'David Barros', 'Thelma Willis', 'Thomas Mckeithan', 'Mary Vargas', 'Araceli Pierce', 'Joseph Trevino']], [['grades4.txt'], ['Damian Payne', 'Jonathan Graff', 'Jeffrey Heck', 'Tiffany Mclavrin', 'Marina Maggio', 'Annette Young', 'Michael Reed', 'Alisha Streiff', 'Margaret Hall', 'Dale Ballantyne', 'Eleanor Terrell', 'Rita Cronin', 'James Uber']], [['grades5.txt'], ['Jason Woodhouse', 'Patricia Guerra', 'Steven Molina', 'Hugh Williams', 'Geraldine Johnson', 'Alex Hadley', 'Latoya Wilson', 'Daniel Fuller', 'Bobby Bauman', 'David Murphy', 'Amanda Okon']], [['grades6.txt'], ['Gary King', 'Rose Alberding', 'Patsy Davis', 'Jillian Perine', 'Elizabeth Williams', 'Donna Shae', 'Jack Womack', 'Ryan Young', 'Stephen Clement', 'Brian Pratt', 'Desiree Barker', 'Joseph Deshields', 'David Hernandez', 'Mary Vela', 'Jose Capps', 'Stephanie Weinzierl', 'Esther Day', 'William Hodgins', 'Stephanie Wade']], [['grades7.txt'], ['Larry Haines', 'James Wilbanks', 'Anthony Mceachern', 'Timothy Ramirez', 'Ethel Snell', 'Susan Ladue', 'Jose Gilbert', 'Donald Anderson', 'Denise Sterner']], [['grades8.txt'], ['Linda Cissell', 'Andrew Cunha', 'Dorothy Mosley', 'Joseph Butorac', 'Thomas Lott', 'William Pauley', 'Jose Chapman', 'Jaunita Mendez', 'John Tunnell', 'Kathryn Holderby', 'Timothy Mcrae', 'Kristina Mcdonald', 'Aline Berger', 'David Lanz', 'Shannon Jones', 'Walter Burchett', 'Gayla Willis']], [['grades9.txt'], ['Whitney Warden', 'Luis Deibert', 'Anne Schrunk', 'Orlando Treat', 'Billie Creech', 'Brittany Dean', 'Phillip Cooke', 'Tom Febus', 'John Major', 'Derick Dunn', 'Jane Latham', 'Charles Scott', 'Sally Pavlosky', 'David Fikes', 'Michael Perez', 'Howard Santos', 'Jennifer Arabian', 'Justin Griffin']]]
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
		
