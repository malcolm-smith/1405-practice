def validate_brackets(s1):
    bracketList = []
    bracketConversion = {
        "{":"}",
        "(":")",
        "[":"]"
    }
    closeBrackets = {
        "}":"",
        ")":"",
        "]":""
    }
    for char in s1:
        if char in bracketConversion:
            bracketList.append(bracketConversion[char])
        elif char in closeBrackets:
            if len(bracketList)>0 and char == bracketList[-1]:
                bracketList.pop(-1)
            else:
                return False
    if len(bracketList)>0:
        return False
    return True
