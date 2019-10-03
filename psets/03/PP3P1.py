calc = {
    'a':[lambda dim: dim[0]+dim[1],"(A)ddition", "1st number", "2nd number"],
    's':[lambda dim: dim[0]-dim[1],"(S)ubtraction", "1st number", "2nd number"],
    'm':[lambda dim: dim[0]*dim[1],"(M)ultiplication", "1st number", "2nd number"],
    'd':[lambda dim: str(int(dim[0]//dim[1])) + ", remainder " + str (int(dim[0]%dim[1])),"(D)ivision", "1st number", "2nd number"]
}


print ("Calc. Options available are ")
for value in calc:
    print ("\t" + str(calc[value][1]))
    #elem 1 contains the name and key val for operation
op = str(input ("Enter the operation: ")).lower()
if op in calc:
    nums = []
    for item in calc[op][2:]:
        nums.append (float(input ("Enter " + item + ": ")))
    print ("Result is " + str(calc[op][0](nums)))
else:
    print ("Operation \"" + op + "\" not supported")