import datetime
name = input ("Enter your name: ")
birthYear = int(input ("What year where you born in " + name + "? "))
currYear = datetime.datetime.now().year
print ("Hello, " + name + ". You are now " + str(currYear-birthYear) + " years old, although you may be a year younger")