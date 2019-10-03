
#initialize the board
#spaces can have "X", "O", or " " (blank/available)
#try different configurations to test your code
tl = "X"
tc = "O"
tr = "X"
ml = "X"
mc = " "
mr = " "
bl = "O"
bc = "O"
br = "O"

#print the board, so we can verify easily
print(tl + "|" + tc + "|" + tr)
print("-----")
print(ml + "|" + mc + "|" + mr)
print("-----")
print(bl + "|" + bc + "|" + br)

gameResult = "Winner is "
if (tl == tc == tr != " " or tl == ml == bl != " " or tl == mc == br != " "):
    gameResult += tl
elif (tr == mr == br != " " or tr == mc == bl != " "):
    gameResult += tr
elif mc == mr == ml != " " or tc == mc == bc != " ":
    gameResult += mc
elif bl == bc == br != " ":
    gameResult += bl
else:
    gameResult = "Game not yet over" if " " in [tl,tc,tr,ml,mc,mr,bl,bc,br] else "Game over, Tie"
print (gameResult)

