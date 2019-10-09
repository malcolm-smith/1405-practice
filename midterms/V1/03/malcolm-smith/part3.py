test = input("Is there a test tomorrow? ") == "yes"
midnight = input("Is it past midnight? ") == "yes"

if test:
    print("study")
elif midnight:
    print("sleep")
else:
    print("game")
