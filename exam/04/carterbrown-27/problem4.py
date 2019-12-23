def permutation_palindrome(s):
    freqs = {}
    for c in s:
        # ignores only spaces
        if c == " ": continue
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1

    numberOfOdds = 0
    for k,v in freqs.items():
        if v % 2 > 0:
            numberOfOdds += 1
            if numberOfOdds > 1:
                return False
    return True
