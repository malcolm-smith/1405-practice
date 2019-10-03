volume = {
    'rectprism':[lambda dim: dim[0]*dim[1]*dim[2], "length", "width", "height"],
    'cyl':[lambda dim: 3.14*dim[0]*dim[0]*dim[1], "rad", "height"]

}
print ("Volume calc. Shapes available are ")
for key in volume.keys():
    print ("\t" + str(key))
shape = str(input ("Enter the shape: ")).lower()
dimensions = []
for item in volume[shape][1:]:
    dimensions.append (float(input ("Enter dimension \"" + item + "\": ")))
print ("Volume is " + str(volume[shape][0](dimensions)))