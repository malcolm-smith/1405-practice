#O(n) since it has a flat structure, and all nested operations are O(1), inside O(n) loops
def  permutation_palindrome(s1):
    freqDic = {}
    for char in s1:
        if char not in freqDic:
            freqDic[char] = 0
        if not char == " ":
            freqDic[char] += 1
    numSingles = 0
    print (freqDic)
    for key in freqDic:
        if (freqDic[key]%2) == 1:
            numSingles +=1
    return numSingles <=1
print(permutation_palindrome("a toyotas a toyota"))
