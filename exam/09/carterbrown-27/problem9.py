def validate_brackets(s):
    bracketPairs = {
        "{":"}",
        "[":"]",
        "(":")"
    }
    closingBrackets = set(("}","]",")"))
    openBrackets = []
    for c in s:
        if c in bracketPairs:
            openBrackets.append(c)
        elif c in closingBrackets:
            # debug: print(openBrackets, c)
            if len(openBrackets) > 0:
                if c == bracketPairs[openBrackets[-1]]:
                    openBrackets.pop(-1)
                else:
                    return False
            else:
                return False

    return len(openBrackets) == 0
