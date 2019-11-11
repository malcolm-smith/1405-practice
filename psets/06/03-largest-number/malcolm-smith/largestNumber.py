def maxvalue(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest