def numDigits (num):
    i = 1
    while (num / 10) >= 1:
        num /= 10
        i +=1
    return i
print ("Digits: ", numDigits(int(input("Num: "))))

