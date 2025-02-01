
# ! Functions

def areaofrectangle(a, b):

    return a * b

print('Area is:', areaofrectangle(5, 2))

def areaoftriangle(a, b):

    return 0.5 * a * b

print('Area of Triangle is:', areaoftriangle(5, 2))

def name(a):

    return f'First Name is {a.split()[0]}\t and\t Last Name is {a.split()[-1]}'

a = 'Hamza Shabbir Sahapurwala'

print(f'The output is :',name(a))

def d():

    print('Hello') 

d()

print(d()) # * For functions which have no return statements ans they are still called, they return None

d1 = d # * We are assigning function to another name

d()

del d # * We delete the old name

d1() # * This only works with new function name

def a(a,b,c):
    return a,b,c

print(a(1,2,3)) # * Returns a tuple


# There are 4 scenarios of Functions:
# With Argument, With return
# With Argument, Without return
# Without Argument, Without return
# Without Argument, With return

# ! Positional and Keyword Arguments

def b(c, n = 'Lol', a = 7): # * c is a positional argument while n and a are keyword arguments

    print(f'The name is {n} and my age is {a} and I got to go to {c}.')

b('Hhahaha',4) # * c = Hhahaha, n = 4 & a = 7(Cause a has default value)

b('Noice',a = 3, n = 'Bwahahahah') # * c = 'Noice'

b('Noice','AHAHAHHAHA',6) # * c = 'Noice', n = 'AHAHAHHAHA', a = 6

b(n = 'Yolo', c = 'Noice') # * We can change the position of c if we treat it like a keyword argument

# b(a = 7, n = 'SUI', 'Noice') # ! This won't work as for both in function header and in caller, the positional(non-default) argument/parameter is ALWAYS first

# ! Positional Arguments can't be inbetween or after the keyword(default) arguments/parameters

def aa(x,y):

    print(x - y)

x = 3; y = 4 # * ; acts as a separator so that x can have 3 as value and y has value 4

# aa(x,y)

a = eval(input('List:'))

print(type(a))

def bbb(*args):

    # * args returns a tuple

    print(args)

    print('With *:',*args) # * Returns the input but can't do anything with that

    # * args by itself is a tuple but *args is just a starred expression

    # for i in *args: # * This doesn't work

        # print(i)

    for i in args:

        print(i)

bbb('A','B','C','D')

def myFun(arg1, **kwargs):
    
    # * kwargs is now a dictionary with the 'before =' as the keys and '=after' as the values

    for key, value in kwargs.items():

        print("%s == %s" % (key, value))

# Driver code

myFun("Hi", first='Geeks', mid='for', last='Geeks')

def myFun(*args, **kwargs):

    print("args: ", args)

    # print('**kwargs: ',**kwargs) # * This doesn't work as all the first="Geeks", mid="for", last="Geeks" thing is just copy pasted and print is a function

    print("kwargs: ", kwargs)

# * Now we can use both *args ,**kwargs

# * to pass arguments to this function :

myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

def myFun(arg1, arg2, arg3):

    print("arg1:", arg1) # * for kwargs: arg1 = for

    print("arg2:", arg2) # * for kwargs: arg2 = Geeks

    print("arg3:", arg3) # * for kwargs: arg3 = Geeks

# * Now we can use *args or **kwargs to

# * pass arguments to this function :

args = ("Geeks", "for", "Geeks")

myFun(*args)

kwargs = {"arg3": "Geeks", "arg1": "for", "arg2": "Geeks"}

myFun(**kwargs) # * the positional parameter in the function should have the same name

# * as the keys in the dictionary named kwargs so that some output is achieved 

def f1(a,b,*ar):

    print(a,b,*ar) # * a = 12, b = 22, *ar = 2 6

    # * prints 12 22 2 6

f1(12,22,2,6)

# * * and ** make is easier to take tuple and dictionary input
