import sys
def getItems (filename):
    items = []
    itemFile = open(filename, 'r')
    for item in itemFile:
        item = item.strip()
        descriptors = item.split(',')
        items.append (descriptors)
    itemFile.close()
    return items

def getUserItemIndex (items):
    index = 0
    while True:
        index = 0
        print ("Select an item or [c]heckout: ")
        for item in items:
            if int(item[3])>0:
                print ("\t(",index,") UPC:" + item[0], " - ", item[1] + ", $"+item[2], "\tRemaining: ", item[3])
            index +=1
        userInput = input()
        if userInput.lower() == 'c':
            return None
        selection = int(userInput)
        if selection in range (0, len(items)):
            break
        else:
            print ("Selection is bad")
    return selection

def getUserQuantity(cart, selection, items):
    while True:
        quantity = input ("Enter the quantity you would like or [c]ancel: ")
        if quantity == "":
            return 1
        if quantity.lower() == "c":
            return None
        quantity = int(quantity)
        if quantity < -cart[selection]:
            print ("Quantity must be at least ", -cart[selection])
        if quantity > int(items[selection][3]): #Quantity Remaining
            print ("Only",items[selection][3], "units left")
        else:
            return quantity
def getRecipt (name, items, cart):
    reciept = "Invoice - " + name + "\n"
    index = 0
    total = 0
    for item in cart:
        if item > 0:
            reciept += "(" + str(item) + ")\t-"+str(items[index][1]) + "@ $" + str(items[index][2]) + " each\t$" + str(item*float(items[index][2])) + "\n" 
            total += item*float(items[index][2])
        index +=1
    reciept += "Total: $" + str(total)
    print (reciept)



def rewriteInventory(items, filename):
    contents = ""
    idex0 = 0
    for item in items:
        idex1 = 0
        for data in item:
            contents+=str(data)
            if (idex1 != (len(item)-1)):
                contents += ","
            idex1+=1
        if idex0 != (len(items)-1):
            contents +="\n"
        idex0+=1
    
    file = open (filename,'w')
    file.write(contents)
    file.close()
    
def stockMod (items):
    while True:
        print ("Enter UPC, or [q]uit")
        upc = input ("")
        if upc.lower()=="q":
            break
        itemExists = False
        idex = 0
        for item in items:
            if item[0] == upc:
                itemExists = True
                break
            idex +=1
        if itemExists:
            items[idex] = itemMod(items[idex])
        else:
            items.append(itemMod(["0000","description","price","inventory"]))
    return items

def itemMod (item):
    item[0] = modIfInput (item[0], "UPC")
    item[1] = modIfInput (item[1], "Description")
    item[2] = modIfInput (item[2], "Price")
    item[3] = modIfInput (item[3], "Inventory Level")
    return item

def modIfInput (datapoint, prompt):
    while True:
        user = input ("New " + prompt + "? Current is \"" + str(datapoint) + "\"")
        if not (user=="" or user==None):
                return user
        else:
            return datapoint

print ("Check CWD if error below. ")
items = getItems("inventory.txt")
name = input ("Hello, enter your name: ")
if name == "admin":
    items = stockMod(items)
    rewriteInventory(items, "ordering-system-demos\inventory.txt")
    sys.exit()

cart = []
for i in items:
    cart.append (0)
while True:
    selection = getUserItemIndex(items)
    if selection == None:
        break
    quanity = getUserQuantity(cart, selection, items)
    if quanity == None:
        continue
    cart[selection] += quanity
    items[selection][3] = int(items[selection][3]) - quanity
rewriteInventory(items, "inventory.txt")
getRecipt(name, items,cart)

     
