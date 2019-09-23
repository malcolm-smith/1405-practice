# decide if car should stop at intersection
def intersectionAction(colour, distance, speed):
    timeToStop = distance / speed
    if colour == 'green':
        return False
    elif colour == 'yellow' and timeToStop <= 5.0:
        return False
    elif colour == 'red' and timeToStop <= 2.0:
        return False
    return True


print(intersectionAction('red', 10, 2))
