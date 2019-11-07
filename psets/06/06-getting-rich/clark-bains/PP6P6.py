stocks = [1,2,3,4,5,6,4,3,2,1,6,7,8,9,10,1,2,3,0]
best = 0
#O(.5n^2) I think
for i in range(len(stocks)):
    for o in range(i,len(stocks)):
        if (stocks[o]-stocks[i])>best:
            best = stocks[o]-stocks[i]

print (best)