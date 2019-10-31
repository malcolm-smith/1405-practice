import os

def largestvolume(filename):
    largestvolume = 0
    volume = 0
    boxes = open(filename, 'r')
    while True:
        length = boxes.readline()
        if length != '':
            width = boxes.readline()
            height = boxes.readline()
            volume = (int(length) * int(width) * int(height))
            if volume > largestvolume:
                largestvolume = volume
        else:
            break
    boxes.close()
    return largestvolume

for filename in os.listdir('../resources/'):
    print('%s: %d' % (filename, largestvolume('../resources/' + filename)))
