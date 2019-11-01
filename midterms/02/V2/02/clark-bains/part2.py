def get_average_house_price(filename):
    f = open (filename, 'r')
    line = f.readline()
    count = 0
    total = 0
    while line!="":
        if count%4 == 3:
            total += int(line.strip())
        count +=1
        line = f.readline()
    f.close()
    #print (total, count/4, total/(count/4))
    return total/(count/4)
print(get_average_house_price("houses0.txt"))