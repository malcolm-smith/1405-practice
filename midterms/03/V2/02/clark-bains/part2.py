def is_palindrome (s1):
    l1 = list(s1)
    l2 = l1[::-1]
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True