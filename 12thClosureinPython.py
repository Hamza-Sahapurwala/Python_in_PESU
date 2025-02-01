
# ! Closures in Python

# * Nested Function which can access the variables of it's outer function

# * Two examples which are similar are below:

def out():

    a = 1

    def inn():

        print(a)

    print('inn:',inn)

    return inn # *Returns function object of inn (Basically using callback)
    
d = out() # * d is now the function of inn

print('d:',d)

# * d and inn objects are the same proving that they are the same function

d()

def f1(): # * outer function

    a = 'Hello'

    def f2(): # * inner function

        print(a)

    print('f2:',f2)

    return f2

c = f1()

print('c:',c)

# * c and f2 have the same function object

c()

# * Example with changing local variables

def division(y): # * Outer function

    def div(x): # * Inner function

        print(x // y)

    return div

d1 = division(2) # * For d1, y will be 2

d2 = division(3) # * For d2, y will be 3

d1(20) # * This will be 20 // 2

d2(96) # * This will be 96 // 3

print('d1:',d1,'\nd2:',d2) # * d1 and d2 are different as the outer function parameters are different

# ! Closures Pt.2

# * Add 2 no. using Closures

def a(x): # * Outer

    def add(y): # * Inner

        print(x + y)

    return add

a1 = a(2) # * a1 is now the function where x = 2

a2 = a(3) # * a2 is now the function where x = 3

a1(4)

a2(2)

# * Multiply two no. using Closures

def m(x): # * Outer

    def multiply(y): # * Inner

        print(x * y)

    return multiply

m1 = m(3) # * Instance of function multiply where x = 3 

m2 = m(4) # * Instance of function multiply where x = 4

m1(5)

m2(5)

# * Greeting someone using Closures

def g():

    def greet():

        print('Hello')

    return greet

g1 = g() # * g1 is now the instance of function greet 

g1()

# * Find the all the odd no. until n using Closures

def o(n): # * Outer

    def odd(): # * Inner

        for i in range(1,n+1,2):

            print(i)

    return odd

o1 = o(10) # * o1 becomes the instance of the function odd() where n = 10

o1()

# ! nonlocal is a keyword that has to be studied

def compute(): # * Outer

    num = 1

    def inner(): # * Inner

        # * To change the value of num freely, use nonlocal keyword

        nonlocal num

        num +=1 # * We can't change the value of num, we can only access it if we don't use nonlocal keyword

        # * This is an example of nonlocal

        return num

    return inner

odd = compute()

print(odd())

# ! Closures Pt.3

def f1(): # * Outer

    def f2():

        print('Hello')

    return f2

a = f1()

del f1

a() # * Even after f1 is deleted, f2 still runs

def a1(x):

    def b1():

        print('Hello')

        print(x)

    return b1

a = a1(3)

del a1

a()

# * The function still works even after a1 is deleted

# * That means b1 stores the instance where a1 had the assigned value
