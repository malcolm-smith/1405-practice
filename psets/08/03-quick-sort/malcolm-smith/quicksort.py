from math import sqrt

def partition(arr, low, high):
    i = (low-1)
    pivot = sqrt(arr[high][0] * arr[high][1]) # this line modified

    for j in range(low, high):
        if sqrt(arr[j][0] * arr[j][1]) <= pivot: # this line modified
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

    return arr


tosort = [[0, 1], [2, 1], [3, 3], [1, 1]]

print(quicksort(tosort, 0, len(tosort) - 1))
