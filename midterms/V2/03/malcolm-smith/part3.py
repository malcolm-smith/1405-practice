dirt = input("Is there dirt here? ") == "yes"
emptySpace = input("Is there empty space ahead? ") == "yes"

if dirt:
    print('vacuum')
elif emptySpace:
    print('move forward')
else:
    print('turn right')
