distance1 = 1.6*float(input("Enter the first distance (in miles): "))
distance2 = 1.6*float(input("Enter the second distance (in miles): "))
distance3 = 1.6*float(input("Enter the third distance (in miles): "))
closeness1 = abs (15-distance1)
closeness2 = abs (15-distance2)
closeness3 = abs (15-distance3)
if closeness1<=closeness2 and closeness1<=closeness3:
    print (distance1/1.6)
elif closeness2<closeness1 and closeness2<=closeness3:
    print (distance2/1.6)
elif closeness3<closeness1 and closeness3<closeness2:
    print (distance3/1.6)