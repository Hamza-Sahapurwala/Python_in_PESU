
# ! Decorators

# * Decorators are functions 

# * used to modify the behaviour or result of another function

# * Basically, we don't want to change the source code of the original function

# * So we use another function to change some part, like the way arguments are given,etc.

# * to change the result given by the og function 

# * Example: We are only trying to divide some big no. by small no. so even if arguments are placed wrong, we just get what we want

def division(a,b):

    return a / b

def smart_div(func): # * Decorator

    def inner(a,b):

        if a < b:

            a, b = b, a

        return func(a, b) # * func is division

    return inner # * Callback

div1 = smart_div(division) # *div1 is now inner

print(div1(2, 4))

# * @ Symbol Usage for Decoration

def func_decorator(func):

    def inner_func():

        print('Before func_hello is called:')

        func() # * func_hello

        print('After func_hello')

    return inner_func # *Callback

@func_decorator # * This needs a function defined below it and the caller of that function

def func_hello():

    print('Hello')

func_hello()

# * Using @, we avoid the 2 lines we used to write previously

# h = func_decorator(func_hello)

# h()

def calculate(f):

    def inn(*a):

        print('Decorator')

        f(*a)

        print('End')

    return inn

@calculate

def fac(n):

    print(n)

@calculate

def maxi(a,b,c):

    print(max(a,b,c))

@calculate

def mini(a,b,c,d):

    print(min(a,b,c,d))

fac(15)

maxi(1,2,3)

mini(1,2,3,4)

# * Decorators Pt.2

def compute(f):

    def inner(a, b):

        print('Calculating Hypotenuse:')

        f(a,b)

        print('Done')

    return inner

@compute

def h(a, b):

    print((a ** 2 + b ** 2) ** 0.5)

h(5,12)

# * Chained Decorators

def dec_x(f):

    def inne():

        print('*' * 20)

        f()

        print('*' * 20)

    return inne

def dec_y(f):

    def inner():

        print('#' * 20)

        f()

        print('#' * 20)

    return inner

def h():

    print('Hello') 

a = dec_y(dec_x(h))

a()

# * Line 1170 will execute dec_y thing first and the dec_x to give us this pattern (ignore # * at start):

# * ####################
# * ********************
# * Hello
# * ********************
# * ####################

# * We can get the same thing by using @ symbol

@dec_y

@dec_x

def ar():

    print('Hello')

ar()