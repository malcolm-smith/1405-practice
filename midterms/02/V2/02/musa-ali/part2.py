# Return average price of houses in given file
def get_average_house_price(filename):
	with open(filename, 'r') as f:
		total = 0
		count = 0
		rooms = f.readline()
		while rooms != "":
			sqfoot = f.readline()
			colour = f.readline()
			price = f.readline().strip()
			count += 1
			total += int(price)
			rooms = f.readline()

	return total/count

# Get file name from user, output average house price for file
house = input("Enter file name: " )
avg = get_average_house_price(house+'.txt')
print("The average house price for the file " + house + ".txt is " + str(avg))