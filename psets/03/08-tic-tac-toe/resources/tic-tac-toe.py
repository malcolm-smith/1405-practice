
#initialize the board
#spaces can have "X", "O", or " " (blank/available)
#try different configurations to test your code
tl = "X"
tc = "O"
tr = "X"
ml = "X"
mc = " "
mr = " "
bl = " "
bc = "O"
br = " "

#print the board, so we can verify easily
print(tl + "|" + tc + "|" + tr)
print("-----")
print(ml + "|" + mc + "|" + mr)
print("-----")
print(bl + "|" + bc + "|" + br)

#write if/elif/else blocks to print out one of the following cases:
#1. X has won the game
#2. O has won the game
#3. The game is a tie (all spaces filled)
#4. The game is still going (blank spaces remain)
