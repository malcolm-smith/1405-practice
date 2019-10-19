#I was thinking there would be more logic
rules = [
    lambda year: year % 4 == 0,
    lambda year: (year % 100 != 0 or year % 400 == 0),
]
year = int(input("Enter a year to check: "))
state = True
for rule in rules:
    #Iterate through rules, efective to x and y and z for all elems
    state = state and rule(year)
print ("Leap year" if state else "no leap year")


