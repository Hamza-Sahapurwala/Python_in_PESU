
# ! Reduce Function

# * Used to make an iterable into 1 value

# * Part of functools module

# * Syntax: reduce(function, iterable[,initializer])

# * function must take 2 arguments as first argument is accumalated value and second is another element of the iterable

# * iterable is any iterable

# * initializer is used to as the first thing to add, subtract or multiply the iterable[0]

# * e.g

import functools

a = [11, 22, 33, 44, 55]

r = functools.reduce(lambda x,y: x * y, a, 100) # * 100 is an initializer i.e. It is multiplied to the first element and then each element is multiplied to each other

print(r)

r = functools.reduce(lambda x,y: x * y, a)

print(r)

# * Finding Factorial

n = 5

print('Finding Factorial using reduce():',functools.reduce(int.__mul__, range(1, n + 1)))

# * Finding sum till n

n = 10

print('Adding all elements in the list:',functools.reduce(int.__add__, range(n)))

# * To find max element

a = [11, 22, 33, 44, 55]

print('Max no.:',functools.reduce(lambda x,y: x if x > y else y, a))
