
# ! This is a Continuation of file learningpython.py

import trialmodule as t # * When this is called, the print statement is also called

# * We renamed trialmodule as t

t.f1()

t.f2()

t.f3()

# t.a = t.a + 2 # * We can access the variables from trialmodule file

# print(t.a)

# * Or we can do specifically call functions using from keyword

from trialmodule import f1, f2

# * The print statement is not called

f1()

f2()

from trialmodule import *

# * The print statement is not called

f1()

f2()

f3()

a += 1 # * As the variable is present in the trialmodule file, now error is raised

# * When we comment the code of t.a above

print(a)

# ! __doc__ variable and help()

# * In Python, each object can be documented using Docstrings

# * e.g.

def adddddd():

    '''Performing Addition of two numbers'''
    
    print(a + 7)

print('Using __doc__, we get:')

print(adddddd.__doc__) # * Prints the triple quoted comments in the function

# ! The triple quotes should always be on top

print('Using help(), we get:')

help(adddddd) # * This by itself prints the triple quoted comment with more things which tells where the function is present

# ! __name__

# * If no modules is imported, __name__ = __main__

# * If modules are imported, __name__ = name of the file

print(__name__) # * Prints __main__

# ! Pytest

def testsqrt():

    assert (25 ** 0.5) == 5 # * Tells pytest to look at this statement speifically

    print((25 ** 0.50) == 8)