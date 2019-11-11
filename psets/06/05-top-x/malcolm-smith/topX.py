def topx(arr, x):
    top = ['']*x
    for i in range(len(top)):
        top[i] = arr[len(arr) - 1 - i]
    for i in range(len(arr) - x - 1, 0, -1):
        flag = False
        smallest = 0
        for j in top:
            if arr[i] > j and j < smallest:
                smallest = j
                flag = True
        if flag:
            top.remove(smallest)
            top.append(i)
    return top

print(topx([56, 4, 12, 3, 4, 4, 7], 2))

