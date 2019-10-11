fp = open('studentinfo.txt', 'r')

for x, line in enumerate(fp):
	if x%6 == 0:
		print(line, end = "")


fp.close()