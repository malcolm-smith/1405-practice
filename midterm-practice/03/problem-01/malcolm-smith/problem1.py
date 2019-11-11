import sys

def search_employees(filename, keyword):
    names_list = []
    for line in open(filename):
        name = (line.strip().split(',')[1][1:])
        if keyword.lower() in name.lower():
            names_list.append(name)
    return names_list

def analyze_pay(filename):
    average_pay = 0
    largest_pay = -1 * sys.maxsize
    smallest_pay = sys.maxsize
    count = 0
    for line in open(filename):
        count += 1
        pay = int(line.strip().split(',')[2])
        average_pay += pay
        if pay > largest_pay: largest_pay = pay
        if pay < smallest_pay: smallest_pay = pay
    return [average_pay / count, float('%.1f' % largest_pay), float('%.1f' % smallest_pay)]

employeefiles = ['../employee_info0.txt', '../employee_info1.txt', '../employee_info2.txt', '../employee_info3.txt', '../employee_info4.txt']

for employeefile in employeefiles:
    print(search_employees(employeefile, 'will'))
    print(analyze_pay(employeefile))