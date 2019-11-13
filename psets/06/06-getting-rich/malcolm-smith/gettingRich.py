def largestprofit(stockprices):
    biggestprofit = 0
    returnlist = []
    for buy in range(0, len(stockprices)):
        for sell in range(buy, len(stockprices)):
            profit = stockprices[sell] - stockprices[buy]
            if profit > biggestprofit:
                biggestprofit = profit
                returnlist = [stockprices[buy], stockprices[sell]]
    return returnlist


stockprices = [9, 5, 6, 7, 1, 5, 6, 8, 2, 10]

print(largestprofit(stockprices))
