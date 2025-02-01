
# ! Map() Function

# * Used to apply one function to the individual elements of any variables

# * Syntax: variable = map(function, iterable(s),...)

a = (1, 2, 3, 4)

result = map(lambda x: x + x, a) # * We are adding each individual element by themselves

print(result, list(result)) # * Shows that result is a map object and list(result) returns us the list where the lambda function has been applied

n1 = [4, 2, 9]

n2 = [5, 7, 5]

r = list(map(lambda x,y: x+y, n1, n2)) # * Adds individual elements of two lists then converting it into a list

print(r)