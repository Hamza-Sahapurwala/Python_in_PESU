
# * Lovely Programs

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
'

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
'''
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

    for i in a:

        print(i)

#TODO learn about Dictreader and Dictwriter functions for csv