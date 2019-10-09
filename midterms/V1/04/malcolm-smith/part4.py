prices = input("Enter three prices, separated by spaces ").split(" ")

closest = float(prices[0])
for price in prices:
    if abs((float(price) * 0.87) - 5) < abs(closest - 5):
        closest = float(price)

print("%.2f" % closest)
