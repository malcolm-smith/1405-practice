# Pset 6 Problem 6
# Getting Rich

# Test case
stonkz = [3.45, 4.32, 1.63, 8.32, 4.19]

max_profit = 0
for i in stonkz:
	for j in stonkz[stonkz.index(i):]:
		buy = i
		sell = j
		profit = sell - buy
		if profit > max_profit:
			max_profit = profit
			best_buy = i
			best_sell = j

print("Largest profit would be $" + str(max_profit) + " if you bought at $" + str(best_buy) + " and sold at $" + str(best_sell) + ".")


