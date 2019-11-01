def ismultiple (num1, num2):
    return (num1%num2)==0
def commonmultiple (num1, num2, num3):
    return ismultiple(num3, num2) and ismultiple(num3, num1)
a = int(input ("Num1: "))
b = int(input ("Num2: "))
for i in range (1, 101):
    if commonmultiple(a,b,i):
        print (i) 