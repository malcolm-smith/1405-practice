def search_employees (s1, s2):
    f = open (s1,"r")
    matching = []
    for line in f:
        if s2.lower() in line.split(',')[1].lower():
            matching.append(line.split(',')[1].strip())
    return matching
def analyze_pay (s1):
    f = open (s1,"r")
    retVal = [None, None, None]
    count = 0
    for line in f:
        nums = line.strip().split(",")
        nums[2]=int(nums[2])
        retVal[0] = retVal[0]+nums[2] if retVal[0] is not None else nums[2]
        retVal[1] = nums[2] if retVal[1] is None else (nums[2] if nums[2]>retVal[1] else retVal[1]) 
        retVal[2] = nums[2] if retVal[2] is  None else (nums[2] if nums[2]<retVal[2] else retVal[2])
        count+=1 
    retVal[0]/=count
    return retVal
print(search_employees("../employee_info0.txt","morg"))
print(analyze_pay("../employee_info0.txt"))

