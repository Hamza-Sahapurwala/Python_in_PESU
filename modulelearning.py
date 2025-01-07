
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

# square = lambda x: x * x

# print(square(4), square,type(square)) # * Prints 16 lambda smt <class 'function'>

# maxi = lambda a,b: a if a > b else b

# print('The max is',maxi(3,2))

# # * Lambda can also be used as an inner function

# def funky(n):

#     return lambda a: a * n # * The innerf function

# innerboi = funky(4) # * Very similar to callback functions

# print(innerboi(3))

# # ! Map() Function

# # * Used to apply one function to the individual elements of any variables

# # * Syntax: variable = map(function, iterable(s),...)

# a = (1, 2, 3, 4)

# result = map(lambda x: x + x, a) # * We are adding each individual element by themselves

# print(result, list(result)) # * Shows that result is a map object and list(result) returns us the list where the lambda function has been applied

# n1 = [4, 2, 9]

# n2 = [5, 7, 5]

# r = list(map(lambda x,y: x+y, n1, n2)) # * Adds individual elements of two lists then converting it into a list

# print(r)

# # ! Filter Function

# # * If we want to remove some elements from an iterable, we can use do it in one line

# # * We can still keep the iterable

# m = [59, 78, 90, 43]

# r = list(filter(lambda x: x >= 70, m)) # * We want elements which are above 70

# print(r)

# # * Checking if vowels exist in a given word

# a = list('hello')

# r = list(filter(lambda x : x in 'aeiou', a))

# print(r)

# # * To check if no.s are divisible by 3

# a = [1, 2, 3, 4, 5, 6]

# print(list(filter(lambda x:x%3==0,a)))

# # * Example of using both map and filter

# a = ['Ram', 'Tejas', 'Aditya', 'Ravi', 'Dinesh', 'Raghu']

# print(list(map(str.upper, filter(lambda x : len(x) > 5, a))))

# # * For readability, we can write the above code as

# r = filter(lambda x:len(x)> 5, a) # * Names with length above 5 are used

# rr = map(str.upper, r) # * Used to uppercase the names we got above

# print(list(rr))

# # ! Reduce Function

# # * Used to make an iterable into 1 value

# # * Part of functools module

# # * Syntax: reduce(function, iterable[,initializer])

# # * function must take 2 arguments as first argument is accumalated value and second is another element of the iterable

# # * iterable is any iterable

# # * initializer is used to as the first thing to add, subtract or multiply the iterable[0]

# # * e.g

# import functools

# a = [11, 22, 33, 44, 55]

# r = functools.reduce(lambda x,y: x * y, a, 100) # * 100 is an initializer i.e. It is multiplied to the first element and then each element is multiplied to each other

# print(r)

# r = functools.reduce(lambda x,y: x * y, a)

# print(r)

# # * Finding Factorial

# n = 5

# print('Finding Factorial using reduce():',functools.reduce(int.__mul__, range(1, n + 1)))

# # * Finding sum till n

# n = 10

# print('Adding all elements in the list:',functools.reduce(int.__add__, range(n)))

# # * To find max element

# a = [11, 22, 33, 44, 55]

# print('Max no.:',functools.reduce(lambda x,y: x if x > y else y, a))

# # ! List Comprehensions

# # Syntax: listvariable = [expression for <variable> in <iterable> [if condition]]

# l = [i for i in range(11) if i%2==0] # * Even no. are put in the list

# l = [i ** 3 for i in range(11)] # * Cube of no. till 10 are put in list

# words = ['Hi','how','are','you']

# items = [i[-1] for i in words] # * Last letter of each word is put in the list

# l1 = [1,2,3,4]

# l2 = [2,3,4,5]

# print([a for a in l1 for b in l2 if a == b]) # * To print similar elements

# city = ['Bangalore', 'Mysore', 'Chennai', 'Hyderabad']

# a = [[i,len(i)] for i in city] # * City with their length

# print(a)

# a = [i ** 2 for i in range(11) if i%2==1] # * Odd sqaures are printed

# print(a)

# # * Transpose of a matrix

# mat = [[1,2], [3,4], [5,6], [7,8]]

# transpose = [[row[i] for row in mat] for i in range(2)]

# # ! Zip Functions

# # * Used to go through multiple lists together

# # * For two lists, it groups the individual elements in a tuple which is another iterable(which we can specify)

# a = [1, 2, 3]

# b = [4, 5, 6]

# print(list(zip(a, b)), dict(zip(a,b))) # * We can also use dictionaries with zip

# ! Classes and Objects

# * Start of OOPS

class Car:

    r = '1'

    def __init__(self, name): # * init function is a constructor which is called always whenever the class is called to make any object

        # * self is a reference to objects so that one object's data is not given another data
        
        print('Class Called')

        self.model = name

    def display(self):

        print('This is the model:', self.model)

    def gettingmodel(self): # * Getters are used to 'get' elements from the class
        
        return self.model

    def settingmodel(self, new_model): # * Setters are used to set new values for the elements 

        self.model = new_model

    def __del__(self): # * Deletor which deletes the object
        
        print('This deletes all parts of the objects') # * This gets printed evertime the program ends or when the object is deleted

car1 = Car('Ford')

print(car1.gettingmodel())

car1.settingmodel('Mustang') # * Changes value of model

print(car1.gettingmodel())

print(getattr(car1, 'r')) # * Only able to get variables which are not set by self thingy

setattr(car1,'r',2) # * Same condition as above but changes value of variables

print(getattr(car1, 'r')) # * Says which value has changed

print(hasattr(car1, 'r')) # * Returns True if variable is present in class else False

# delattr(car1, 'r') # * removes element r

# ! Inheritance

# * Where one class takes or 'inherits' attributes(variables) or methods(functions) from other classes

class Curry:

    def __init__(self, name, temperature):
        
        print('In Class Curry Constructor')

        self.name = name

        self.temperature = temperature

    def display(self):

        print('In Class Curry Display')

class Vegetable(Curry): # * This leads to inheritance

    def __init__(self, name, temperature, batchno):

        self.batchno = batchno
        
        Curry.__init__(self, name, temperature) # * We can initialize the other variables using the other Parent's class's Constructor

        print(f'Taken from other class:\nName of Soup: {self.name}\nTemperature of Soup: {self.temperature}\nIs in this Vegetable Class:\nBatchno: {self.batchno}')

    def disp(self):
        
        print('In Class Vegetable Disp')

        Curry.display(self) # * We can use the Parent Class to call it's function

eng = Vegetable('Tomato Soup', 56, 101) # * When I call this, the constructor of Curry runs first

# eng.disp() # * Can call the method in this class itself

# eng.display() # * Can also call the method present inside Parent Class

# ! super() Function

# * How we used the Constructors of Parent class to spread info between 2 classes can be done in a more efficient way

class A:

    def disp(self):

        print("in disp A")

class B:

    def disp(self):

        print("in disp B")

class C(B, A): # * If the order is reversed, the print changes to '' in disp A '' (Also this is Multiple Inheritance)

    def disp(self):

        super().disp() # * This prints in disp B as B is the first Class to be inherited from

        # * '' in disp A '' is not printed as B is first inherited class

        print("in disp C")

c1 = C()

c1.disp()

# * Now super() use in defining variables across multiple classes

class Shape:

    def __init__(self, name): # * Here self.name variable is assigned the value

        self.name = name
    
    def info(self): # * This function is not called as the info function in it's Child Class(which is Polygon) is called by the super() in the other children classes

        return f"This is a {self.name}."
    
class Polygon(Shape):

    def __init__(self, name, sides):

        super().__init__(name)

        self.sides = sides # * self.sides is assigned here

    def info(self): # * This function is only called

        return f"A {self.name} is a polygon with {self.sides} sides."
    
class Triangle(Polygon):

    def __init__(self, name):

        super().__init__(name, 3)
class Quadrilateral(Polygon):

    def __init__(self, name):

        super().__init__(name, 4)

trig = Triangle('Triangle')

print(trig.info())

rec = Quadrilateral('Rectangle')

print(rec.info())