
# ! Dictionary

d ={(1,2):1}

d[1]='hello'

print(list(d.keys()))

# ! popitem pops the last key:value pair in the dictionary

# ! pop pops random value in the dictionary and returns the value of the associated key

# ! pop(<key>) this pops the specific key:value pair

print(d.get((1,2),1))

print(d.pop(1))

print(d)

print(type(d.items()))

print(type(d.values()))

print(type(d.keys()))

print(list(d.items()))

print(list(d.values()))

print(list(d.keys()))

print(list(d))

# * WAP to concatenate the following dictionaries to create a new dictionary

d1 = {1:10,2:25}

d2 = {3:30,4:45}

d3 = {5:50, 6:65}

d4 = {}

d4.update(d1)

d4.update(d2)

d4.update(d3)

print(d4)