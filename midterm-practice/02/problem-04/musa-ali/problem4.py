x = 20
d1 = []
d2 = []

for i in range(1, 100):
	if 20 % i == 0:
		d1.append(i)
	if 24 % i == 0:
		d2.append(i)

for i in range(1, 100):
	if d1[i] == d2[i]:
		print(d2[i])


print(d1)
print(d2)
# print(y)
