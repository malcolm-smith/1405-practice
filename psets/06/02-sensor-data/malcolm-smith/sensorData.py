measurements = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

def measure(num):
    global measurements
    newarr = [ num ]
    newarr += measurements[:len(measurements) - 1]
    measurements = newarr

def average(arr):
    return arr[0]

def min(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

def max(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

def isdanger():
    global measurements
    return abs(min(measurements) - max(measurements)) > 10

print(measurements)
measure(70)
print(measurements)
print(isdanger())