
# ! Generators

# * Functions that behave like iterators (like range())

# * They store elements which we can loop over to get

# * We use 'yield' keyword to make any function like a generator

def gen():

    yield 1

    yield 2

    yield 3

print(gen()) # * This tells us the generator object's memory address

# * It doesn't return any thing else

for i in gen():

    print(i) # * This gives us the 1 2 3 result

print(type(gen())) # * <class 'generator'>

# print(gen()[1]) # * TypeError: 'generator' object is not subsicriptable i.e. you can't find any particular element

# ! Generators Pt.2

# * next() function is used to for going to the next element in the iterator

def gen_fun():

    yield 10

    yield 20
     
    yield 30

o = gen_fun() # * Like how we can do a = range(5), this stores all the elements from 0 to 4 in an object which is variable a

print(next(o))

print(next(o))

print(next(o))

# print(next(o)) # * Gives an error as generator is out of objects to iterate

# * Fibonnaci in Generator

def fib(n):

    x, y = 0, 1

    for i in range(n):

        x, y = y, y + x

        yield x

def sqq(a): # * Generator

    for i in a:

        yield i ** 2

print(sum(sqq(fib(3)))) # * prints 6

# * Generator Expressions

# * We can basically use list(or tuple comprehensions) to do the same thing like an generator

gen_exp = (i ** 2 for i in range(5) if i % 2 == 0)

print(gen_exp) # * This prints the gen_exp object thingy

# * If the brackets were changed to [] in line 1272, then it would print a list

for i in gen_exp:

    print(i) # * This prints the individual elements of the generator