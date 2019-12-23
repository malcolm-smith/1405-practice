'''
The worst-case time complexity for this algorithm is O(N^2), as all operations run in constant-time
except for the function "selection_sort" (called on line 9), which, by nature runs in O(N^2) time.
It does so because it must go through each index of the list as a starting point, then search through
the rest of the list (elements succeeding the starting index) to find the min value to swap.
Therefore, it runs in O(n * (n-1 + n-2 + n-3 ... 1)) time, which simplifies to O(n^2)
'''
def median(lst):
    selection_sort(lst)
    if len(lst) % 2 > 0:
        return lst[len(lst)//2]
    else:
        return (lst[int(len(lst)/2)-1] + lst[int(len(lst)/2)]) / 2

def selection_sort(lst):
    start = 0
    while start < len(lst):
        min = lst[start]
        minIndex = start
        for i in range(start+1,len(lst)):
            if lst[i] < min:
                min = lst[i]
                minIndex = i
        lst[start], lst[minIndex] = lst[minIndex], lst[start]
        start += 1
    return lst
