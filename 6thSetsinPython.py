
# ! Sets

s = {1,2,3,4,5}

print(type(s)) # * Returns set

a = {}

print(type(a)) # * Returns dictionary

# ! That's why we don't make sets like the above example as it returns dictionary type

a = set() # * This makes an empty set 

print(s)

s1 = {1,2,3}

s2 = {5,3,4}

print(s1.union(s2))

print(s1.intersection(s2))

print(s1.difference(s2))

print(s1.symmetric_difference(s2))

print(s1 | s2) # * Union

print(s1 & s2) # * Intersection

print(s1  - s2) # * Difference

print(s1 ^ s2) # * Sysmmetric Difference

for i in s1:
    print(i)

s1 = {1, (1,2), 'hi', True, 3, 2}

print(s1) # * Elements are printed in a random order

# s1.remove(100) # ! Throws an error as the element is not present in the list

s1.discard(100) # ! doesn't return an error if element is not present

print(s1.pop()) # ! pops random values

s1.clear() # * clears the set

print(s1) # ! returns set()

print(sorted(s2,reverse=True)) # ! Returns a LIST