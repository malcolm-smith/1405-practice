def analyze(filename):
    evencounter=0
    templongest=0
    for line in filename:
        if int(line)%2==0:
            evencounter+=1
            if counter>templongest:
                templongest=counter
        elif int(line)%2!=0:
            evencounter=0
    return 'The largest sequence of even numbers was' ,templongesst, 'even numbers'

f=input('Enter the file name you wish to open: ')
file=open(f,'r')
print(analyze(f))