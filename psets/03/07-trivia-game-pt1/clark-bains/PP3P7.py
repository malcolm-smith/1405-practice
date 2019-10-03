import re
problemset = [
    ["Question 1?", "Answer 1"],
    ["Question 2?", "Answer 2"]
]
while problemset:
    problem = problemset.pop()
    print (problem[0])
    ans = re.sub('\W+','', input ("Enter your answer: ").lower())
    sol = re.sub('\W+','', problem[1].lower())
    if ans==sol:
        print ("Answer is correct.")
    else:
        print ("Answer is not correct.")    