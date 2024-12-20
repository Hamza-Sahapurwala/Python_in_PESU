
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