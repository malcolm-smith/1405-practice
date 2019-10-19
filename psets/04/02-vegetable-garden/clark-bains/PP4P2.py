daysSinceLastRain = 0
while (daysSinceLastRain < 3):
    daysSinceLastRain += 1 if input("Rain?").lower()=="false" else (0-daysSinceLastRain)
print ("Water Plants")