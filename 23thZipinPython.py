
# ! Zip Functions

# * Used to go through multiple lists together

# * For two lists, it groups the individual elements in a tuple which is another iterable(which we can specify)

a = [1, 2, 3]

b = [4, 5, 6]

print(list(zip(a, b)), dict(zip(a,b))) # * We can also use dictionaries with zip
