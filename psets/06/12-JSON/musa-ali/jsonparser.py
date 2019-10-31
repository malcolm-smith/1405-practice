# Pset 6 Problem 12
# JSON


def jsontolist(string):
	out = []
	for key in string:
		out.append([key, string[key]])
	
	return out


def getvalue(jsonlist, key):
	keys = []
	for x in jsonlist:
		keys.append(x)
		if x[0] == key:
			return x[1]

	if key not in keys:
		return None


def setvalue(jsonlist, key, newvalue):
	for x in jsonlist:
		if x[0] == key:
			x[1] = newvalue


def listtojson(jsonlist):
	# [['firstname', 'musa'], ['lastname', 'mckenney'], ['position', 'instructor']]
	my_dict = {}
	i = 0
	for x in jsonlist:
		my_dict[x[0]] = x[1]
	
	return my_dict


def remove(jsonlist, key):
	keys = []
	for x in jsonlist:
		keys.append(x)
		if x[0] == key:
			jsonlist.remove(x)
			return True

	if key not in keys:
		return False


def add(jsonlist, key, value):
	keys = []
	for x in jsonlist:
		keys.append(x)
	if key not in keys:
		jsonlist.append([key, value])
		return True
	else:
		return False

# Test cases
jl = jsontolist('{"firstname":"dave","lastname":"mckenney","position":"instructor"}')
print(getvalue(jl, "positiofn"))
print(jl)
setvalue(jl, "firstname", "musa")
setvalue(jl, "lastname", "ali")
print(jl)
listtojson(jl)
remove(jl, "position")
print(jl)
add(jl, "position", "student")
print(jl)