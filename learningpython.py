
# * Lovely Programs

import csv

'''print('Hello World!!')

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
    
    # * kwargs is now a dictionary with the 'before =' as the keys and 'after=' as the values

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
'''
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