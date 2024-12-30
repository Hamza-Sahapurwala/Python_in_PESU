
# ! This is a Continuation of file learningpython.py

# import trialmodule as t # * When this is called, the print statement is also called

# # * We renamed trialmodule as t

# t.f1()

# t.f2()

# t.f3()

# # t.a = t.a + 2 # * We can access the variables from trialmodule file

# # print(t.a)

# # * Or we can do specifically call functions using from keyword

# from trialmodule import f1, f2

# # * The print statement is not called

# f1()

# f2()

# from trialmodule import *

# # * The print statement is not called

# f1()

# f2()

# f3()

# a += 1 # * As the variable is present in the trialmodule file, now error is raised

# # * When we comment the code of t.a above

# print(a)

# # ! __doc__ variable and help()

# # * In Python, each object can be documented using Docstrings

# # * e.g.

# def adddddd():

#     '''Performing Addition of two numbers'''
    
#     print(a + 7)

# print('Using __doc__, we get:')

# print(adddddd.__doc__) # * Prints the triple quoted comments in the function

# ! The triple quotes should always be on top

# print('Using help(), we get:')

# help(adddddd) # * This by itself prints the triple quoted comment with more things which tells where the function is present

# # ! __name__

# * If no modules is imported, __name__ = __main__

# * If modules are imported, __name__ = name of the file

# print(__name__) # * Prints __main__

# ! Pytest

# def testsqrt():

#     assert (25 ** 0.5) == 5 # * Tells pytest to look at this statement speifically

#     print((25 ** 0.50) == 8)

# ! Doctest

# * We can give testcases in the docstring(triple quotes) and use doctest module to check if a function works or not

# import doctest

# def facto(n):

#     '''
#     >>> facto(5)
#     120
#     >>> facto(0)
#     1
#     '''

#     if n == 0:

#         n = 1

#     else:

#         n = n * facto(n - 1)

#     return n

# doctest.testmod(name='facto', verbose=True)

# * Verbose=True prints something even if all tests have passed

# ! Lambda Functions

# * Basically, One-Liners but for functions

# * lambda multiple arguments seperated by comma : expression which leads to output

square = lambda x: x * x

print(square(4), square,type(square)) # * Prints 16 lambda smt <class 'function'>

maxi = lambda a,b: a if a > b else b

print('The max is',maxi(3,2))

# * Lambda can also be used as an inner function

def funky(n):

    return lambda a: a * n # * The innerf function

innerboi = funky(4) # * Very similar to callback functions

print(innerboi(3))

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

# ! Filter Function

# * If we want to remove some elements from an iterable, we can use do it in one line

# * We can still keep the iterable

m = [59, 78, 90, 43]

r = list(filter(lambda x: x >= 70, m)) # * We want elements which are above 70

print(r)

# * Checking if vowels exist in a given word

a = list('hello')

r = list(filter(lambda x : x in 'aeiou', a))

print(r)

# * To check if no.s are divisible by 3

a = [1, 2, 3, 4, 5, 6]

print(list(filter(lambda x:x%3==0,a)))

# * Example of using both map and filter

a = ['Ram', 'Tejas', 'Aditya', 'Ravi', 'Dinesh', 'Raghu']

print(list(map(str.upper, filter(lambda x : len(x) > 5, a))))

# * For readability, we can write the above code as

r = filter(lambda x:len(x)> 5, a) # * Names with length above 5 are used

rr = map(str.upper, r) # * Used to uppercase the names we got above

print(list(rr))