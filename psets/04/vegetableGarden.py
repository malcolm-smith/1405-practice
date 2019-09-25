from random import randint

counter = 0

while counter < 3:
    if randint(0, 1):
        counter = 0
        print('It rained today!')
    else:
        print('It did not rain today')
        counter += 1

print('Quick! Water your garden before all the plants die and you starve to death!')
