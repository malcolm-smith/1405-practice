currency = {
    'cad': 1.33,
    'usd': 1,
    'eur' : .91,
    'jpy' : 108.02,
    'inr' : 71.33
}
print ("Currencies")
for cur in currency:
    print("\t" + cur)
currencyFrom = input("Enter from currency : ")
currencyTo = input("Enter to currency: ")
originalValue = float(input("Amount of " + currencyFrom))
convertedValue = originalValue/currency[currencyFrom] * currency[currencyTo]
print ("Value is " ,convertedValue, currencyTo)

