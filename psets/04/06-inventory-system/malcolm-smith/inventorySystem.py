# not complete

inventory = {}

def showmenu():
    count = 1
    for item in inventory:
        print('%d) %s : $%d' % (count, item, inventory[item]))
        count += 1
    return input('Select: ')

def readfile(filename):
    f = open(filename, "r+")
    items = {}
    name = f.readline().strip()
    while name!="":
        price = f.readline().strip()
        items[name] = int(price)
        name = f.readline().strip()
    f.close()
    return items

inventory = readfile("./inventory.txt")
showmenu()