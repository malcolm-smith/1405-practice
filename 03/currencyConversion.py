import re

# convert between CAD, USD, GBP, EUR, JPY

currencyList = {
    "CAD": 1.00,
    "USD": 0.75,
    "EUR": 0.68,
    "GBP": 0.60,
    "JPY": 81.50
}

startCurr = None
endCurr = None
startVal = None
endVal = None

start = input('Enter your currency, amount: ').upper()
end = input('Type of currency to convert to: ').upper()

# check if what the user entered is a valid currency
flag = 0
for key in currencyList.keys():
    if start.__contains__(key):
        startCurr = key
        flag += 1
    if end.__contains__(key):
        endCurr = key
        flag += 1
if flag == 2:
    startVal = float(re.search(r'\d+', start).group())
    endVal = startVal * currencyList[endCurr] / currencyList[startCurr]
    print('%.2f %s is equal to %.2f %s' %
          (startVal, startCurr, endVal, endCurr))
else:
    print('Cannot convert that currency')
