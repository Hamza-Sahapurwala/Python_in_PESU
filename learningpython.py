
# * Lovely Programs

import csv

from tkinter import *

from tkinter import messagebox
'''
print('Hello World!!')

# This is test try for python

# * \n to print in new line 

print('Hello\nBye')

# * Bye will be printed in the next line

# * To take input from the user, use

a = input("Enter your name:\n")

print('Hello',a)

# ! comma provides a space!!!!!

a = input('Enter your name again:')

print('Hello',a)

print(len(a))

n = 10

k = 10

if n is k:
    print(True)

# * is function checks if the memory address are same or not

print(id(n))

print(id(k))

# ! This proves that python doesn't not store any values in the variables but rather the variables store the memory address of the values (the values pre-exist somewhere)

a = input('Enter your name:\n')

b = int(input('Enter your age:\n'))

print(type(a))

print(type(b))

if 18 <= int(input('Enter age:\n')):
    print('Eligible for voting')

else:
    print('Can\'t vote')

marks = 80

g = 'Good' if marks < 80 else 'b is min'

# ! Ternerary operators

a = 5
b = 10

if a > b:
    print('A is greater than B')

elif a == b:
    print('A is equal to B')

else:
    print('A is less than B')

name = input('Enter name:')

a = int(input('Enter Marks for subject 1:'))
b = int(input('Enter Marks for subject 2:'))
c = int(input('Enter Marks for subject 3:'))
d = int(input('Enter Marks for subject 4:'))
e = int(input('Enter Marks for subject 5:'))

if 90 <= ((a+b+c+d+e)/500)*100 <= 100:
    print('Grade S')

elif 80 <= ((a+b+c+d+e)/500)*100 < 90:
    print('Grade A')

elif 70 <= ((a+b+c+d+e)/500)*100 < 80:
    print('Grade B')
    
elif 60 <= ((a+b+c+d+e)/500)*100 < 70:
    print('Grade C')
    
elif 50 <= ((a+b+c+d+e)/500)*100 < 60:
    print('Grade D')
    
else:
    print('Grade F')

if True:
    print('Let\'s gooooooooooooo')

else:
    print('Its fine')

# ! While Loop:

i = 10

while i!=0:
    print('Hello')
    i-=1

i = 10

while i!=20:
    print(i)
    if i == 15:
        break
    i+=1
i = 10
while i!=20:
    if i == 15:
        i+=1
    print(i)
    i+=1

i = 10

while i < 21:
    if i>=15:
        i+=1
    print(i)
    i+=1

print(100//6)
print(100%6)

for i in range(6):
    print(i,end='')

print()

for i in 'python':
    print(i)

a = 1

for i in range(9):
    
    for j in range(1,4):
    
        print(a,'\t',j)

    a+=1
    
    if a == 4:
        
        break

for i in range(1,4):

    for j in range(1,4):

        print(i,'\t',j)

n = int(input())

while n!=0:
    d = n % 10
    print(d)
    n//=10

n = int(input())

r = 0

while n!=0:
    a=n%10
    r *= 10 + a
    n//=10

n = input('Enter a no.:')

if n==n[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')

n = int(input('Enter a no. for checking if it is amstrong or not:'))
s = 0
while n!=0:
    s = s + ((n%10)**3)

for i in range(1,6):
    for j in range(i):
        print(i,end='')
    print()

if 5 >= 5:
    print('True')

l = [5,2,4,1,3]
l.sort() # * sort(reverse=True) for descending order
l.append(6)
l.append([7,8])
l.insert(3, 10)
print(l)

def e():
    l.append(3)
print(e())
print(l)

for i in l[::-1]:
    print(i,end='')

for i in range(11):
    print(2<<i)

n = int(input('Enter a no.:'))
print(bin(n))
print(bin(n)[-1])
if bin(n)[-1] == '1':
    print('Is odd')
else:
    print('Is even')

n = int(input('Enter a no.:'))
print((n<<5) | n)

d ={(1,2):1}

d[1]='hello'

print(list(d.keys()))

# ! popitem pops the last key:value pair in the dictionary

# ! pop pops random value in the dictionary and returns the value of the associated key

# ! pop(<key>) this pops the specific key:value pair

print(d.get((1,2),1))

print(d.pop(1))

print(d)

print(type(d.items()))

print(type(d.values()))

print(type(d.keys()))

print(list(d.items()))

print(list(d.values()))

print(list(d.keys()))

print(list(d))

# * WAP to concatenate the following dictionaries to create a new dictionary

d1 = {1:10,2:25}

d2 = {3:30,4:45}

d3 = {5:50, 6:65}

d4 = {}

d4.update(d1)

d4.update(d2)

d4.update(d3)

print(d4)

s = {1,2,3,4,5}

print(type(s)) # * Returns set

a = {}

print(type(a)) # * Returns dictionary

# ! That's why we don't make sets like the above example as it returns dictionary type

print(s)

s1 = {1,2,3}

s2 = {5,3,4}

print(s1.union(s2))

print(s1.intersection(s2))

print(s1.difference(s2))

print(s1.symmetric_difference(s2))

print(s1 | s2) # * Union

print(s1 & s2) # * Intersection

print(s1  - s2) # * Difference

print(s1 ^ s2) # * Sysmmetric Difference

for i in s1:
    print(i)

s1 = {1, (1,2), 'hi', True, 3, 2}

print(s1) # * Elements are printed in a random order

# s1.remove(100) # ! Throws an error as the element is not present in the list

s1.discard(100) # ! doesn't return an error if element is not present

print(s1.pop()) # ! pops random values

s1.clear() # * clears the set

print(s1) # ! returns set()

print(sorted(s2,reverse=True)) # ! Returns a LIST

# ! Strings

s = 'p e s'

print(s.index('e')) # * Returns the index of the first occurence of given string in s (this will return 2) 

print(s.title()) # ! Uppercases all characters which are after space and first character

print(s.capitalize()) # ! Only first character is uppercased

s = ' p e s'

print(s.capitalize()) #  ! doesn't capitalize the first character if the the first character is not an alphabet

a = ' abc  xyz'

b = 'xyz'

print(a.join(b))

print(a.isalpha()) # * All characters should be alphabets to return True

t = 'Hello Sam!'

a = t.maketrans('S','p') # * This is replace function with extra steps

print(a)

print(t.translate(a)) # * This is the final step for replacing

print(b.partition('y'))

b = 'Hello My name'

print(b.partition('n')) # * This returns a tuple

# * Returns ('Hello My ', 'n', 'ame')

print(b.split('n')) # * This returns a list

print(b.encode(encoding='utf-8')) # * Encodes the string in utf-8

a = b.encode(encoding='utf-8')

print(a.decode()) # * Decodes the above encoded value

# ! File Handling

with open('biopic.txt') as f: # ! default mode of open is r (read mode)
    print(f.read())

# ! These Functions below work only in r,r+, w+ and a+

# * read() returns all the things contained in the text file 

# * readline() reads one line with \n included

# * readlines() returns a list which contain each line as an element (with \n included at each line)

with open('biopic.txt','w') as f: # ! w mode will create a new file if doesn't exist or overwrites(clears the file and starts from empty file)
    
    f.write('I am writing something new\n')

    f.write('If I don\'t add \\n this will be printed continuesly')

    f.write('Like so')

import csv

with open('t.csv','r',newline='\r\n') as d: # ! newline='\r\n' removes any empty lines present in the csv file for a more presentable output

    a = csv.reader(d) # * This produces a readable object (which means loop through it to get the values)

    print(a) # * This prints the object representation

    for i in a:

        print(i) # * This prints each value (row) in the csv file (except the empty rows as specified by newline='\r\n')

with open('t.csv','a',newline='') as d: # ! We just don't add any empty lines when adding new data by using newline = ''

    a=csv.writer(d) # * We created a writer object which will help us 

    a.writerow([1,2,3])

    a.writerow([10,11,12])
    
print('After Adding new things to the csv file:')

with open('t.csv','r',newline='\r\n') as d: # ! look at line 404

    a = csv.reader(d)

    head = next(a) # * Skips the header row

    for i in a:

        print(i)

#TODO learn about Dictreader and Dictwriter functions for csv

with open('t.csv','a',newline='') as d:

    a = {1:1,2:2,3:3}

    b = csv.DictWriter(d)

    b.writerow(a)

with open('t.csv','r',newline='\r\n') as d:

    a = csv.DictReader(d)

    for i in a:

        print(i)

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

# ! Recursion

# * Calling a function while the function itself is running

# * We can use the above property to solve problems

# * To use the above thing, the criteria of writing a recursive functions:

# * Base Case: The condition to stop recursion at this point

# * Recursive Case: Anything which is not the base case but takes some step towards the base case

# * Recursive Fucntions work like STACKS!!!

# * Using Recursive functions to find factorial of a no.

# * Depth: No. of steps to complete a problem

''''''
Advantages:

1. Used to simplify complex problems into smaller easier problems

2. Solving problems with repeated patterns

3. Handling unknown levels of depth

4. Mathematical & Algorithmic
''''''

def factorial(n):

    if n == 0: # * Base Case

        return 1
    
    else: # * Recursive Case

        return n * factorial(n - 1) # * This calls the function again and again until the argument doesn't become 0 to reach the base case and
    
    # * from there the functins keep repeating their values to their callers coming to this place at last which gives us the answer

print(factorial(5))

# * Using Recursive Function, find GCD b/w two no.

def gcd(a, b):

    if b == 0:

        return a
    
    else:

        return gcd(b, a % b)
    
print(gcd(91,65))

# * Using Recursive Function, print out the Fibonnaci Series

def fibonnaci(n):

    if n <= 1: # * Base Case

        return n

    else: # * Recursive Case

        return fibonnaci(n - 1) + fibonnaci(n - 2) # * Because Fibonnaci Series is basically nth postion no. = (n-2)th position no. + (n-1)th position no.

for i in range(0,6):

    print(fibonnaci(i),end = ' ') # * At that index, it returns the fibonnaci no. present there

print()

# * Using Recursive Function, print out the the Movements for the game of Tower of Hanoi

i = 0

def toh(n, src, aux, des):

    global i

    if n == 1:

        i+=1

        print(f'Move Disk 1 from source {src} to destination {des}.')

    else:

        i+=1

        toh(n - 1, src, des, aux)

        print(f'Move Disk {n} from source {src} to destination {aux}.')

        toh(n - 1, aux, src, des)

toh(6,'A','B','C')

print('The no. of moves it takes to solve the Tower of Hanoi',i)

# * Using Recursive function to print a simple pattern

def pattern(n):

    if n == 0: # * Base Case

        return
    
    print('*')

    pattern(n-1)

pattern(5)

# * Using Recursive function to add two no.

def add(x,y):

    if y == 0: # * Base Case

        return x

    return add(x,y-1) + 1

# * Using Recursive function to subtract two no.

def sub(x,y):

    if y == 0: # * Base Case

        return x

    return sub(x - 1,y - 1)

# * Using Recursive function to multiply two no.

def mul(x,y):

    if x < y:

        return mul(y,x)

    elif y != 0:

        return x + mul(x, y - 1)

    else: # * Base Case

        return 0

# * Using Recursive function to divide two no.


def div(x,y):

    if x < y: # * Base Case

        return 0

    else:

        return 1 + div(x-y, y)

# ! Callback Functions

# * Callback using built-in functions

s = ['Hello', 'Welcome', 'to', 'python','world']

print(sorted(s))

print(sorted(s, key=str.upper))

# * Callback using User-Defined functions

def function_name(x):

    return x[0] * x[1]

def c(f,x): 

    print(f) # * Returns something which relates to the function created above

    return f(x) # * Calls the above function

print(c(function_name, [3,23]))

# * Multiple Callback Functions

def fun(fun_list, x, y):

    for i in fun_list: # * i will have go through the list

        print(i)

        i(x, y) # * Functions are called respectively

def a(x, y):

    print(x + y)

def d(x, y):

    print(x // y)

c = [a, d] # * a and d are the function names

fun(c, 10, 5)

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
'''
# ! Tkinter

# * Tkinter is one of the GUI libraries in Python

# * As we have imported tkinter to variable t (Refer Line 6), let's not mess around by creating any new variable named t

# * If we use 'import tkinter as t' then above comment is in matter

# * But here we are just importing everything from tkinter to access all the widgets

# * So, no need to write root = t.Tk()

def click():

    # * For messagebox, we again have to import it separately cause it's Python :)

    messagebox.showinfo('Message', 'Button clicked') # * New window which will print the message i.e. Button clicked

def submittion():

    messagebox.askquestion('Form', 'Do you want to end this life?')

root = Tk() # * This is what creates the window

root.title('New BOI') # * The Name of the window

root.geometry('500x500') # * The Dimensions of the window (breath x length)

root.config(bg = 'white')

# ! Button in Tkinter

# * This creates the button widget

button = Button(root, text = 'Submit', command=click, pady=5, activebackground='orange',bg='white') 

# * command takes in func. name which will be called when the button is clicked

# * pady creates some space b/w text inside the button and the button

# * activebg changes the colour of the button in the duration it is clicked

# * bg is the const. colour of button

# ! Canvas in Tkinter

# * This creates the canvas window

# * Canvas is just the Drawing area in the window

canvas = Canvas(root, bg = 'white', height=300, width=300)

# * We are creating the circle in the window

coord = (10, 10, 300, 300)

arc1 = canvas.create_arc(coord, start=0,extent=150, fill='red')

arc2 = canvas.create_arc(coord, start=150,extent=215, fill='green')

# * We are adding an image to the window

canvas1 = Canvas(root, height=700,width=800)

filename = PhotoImage(file=r'C:\Users\Admin\Pictures\ip.png')

image = canvas1.create_image(20, 20, anchor=NW, image= filename)

# ! Checkbutton in Tkinter

# * User can enter more than one option

checkbutton = Checkbutton(root, command=click)

labellllll = Label(root, text = 'Select your hobbies')

checkbutton1 = IntVar() # * IntVar is something that holds integer data passed to the checkbutton widget

checkbutton2 = IntVar() # * IntVar is something that holds integer data passed to the checkbutton widget

checkbutton3 = IntVar() # * IntVar is something that holds integer data passed to the checkbutton widget

# * IntVar is used to store, retrieve and manage integer variables in Python 

cb1 = Checkbutton(root, text='Painting', variable = checkbutton1, onvalue = 1, offvalue=0)

cb2 = Checkbutton(root, text='Reading', variable = checkbutton2, onvalue = 1, offvalue=0)

cb3 = Checkbutton(root, text='Horse Riding', variable = checkbutton3, onvalue = 1, offvalue=0)

# ! Label in Tkinter

# * Label is used to print any text on the tkinter window

username = Label(root, text = 'Username')

password = Label(root, text = 'Password')

submitbutton = Button(root, text = 'Submit', command=submittion)

e1 = Entry(root, width = 20)

e2 = Entry(root, width = 20)

# ! Frame in Tkinter

# * Frame is used to make a region inside the window itself

# * And that becomes another window by itself

# * A window inside a window

# * And that helps us arrange stuff in a more better manner

# * And we can put as many widgets as we want in the frame

frame = Frame(root)

frame.pack(side=BOTTOM)

bb = Button(frame, text='Yes')

# ! Nested Frames

# * As the name suggests, It's a frame inside a frame

frame1 = Frame(root, bg='black',width=500,height=300)

frame2 = Frame(root, bg='Grey',width=100,height=100)

# ! Packing

button.pack(side=BOTTOM) # * This places the button on the window

# canvas.pack()

# canvas1.pack()

checkbutton.pack(side=BOTTOM)

labellllll.pack()

cb1.pack()

cb2.pack()

cb3.pack()

username.place(x = 30, y = 50)

password.place(x = 30, y= 90)

submitbutton.place(x = 30, y = 120)

e1.place(x = 100, y = 50)

e2.place(x = 100, y = 90)

bb.pack() # * This will be placed at the bottom of the window as the frame it is related to is packed at the bottom

frame1.pack()

frame2.pack(pady=20,padx=20)

# * pack(side=TOP) puts the widget on top of the window (default)

# * pack(side=BOTTOM) puts the widget on the bottom of the window 

root.mainloop() # * This keeps the window alive until we close it (this is always at end of the code)