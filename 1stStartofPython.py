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

for i in range(11):

    print(2<<i) # * Left Shifting

n = int(input('Enter a no.:'))

print(bin(n))

print(bin(n)[-1])

if bin(n)[-1] == '1':

    print('Is odd')

else:

    print('Is even')

n = int(input('Enter a no.:'))

print((n<<5) | n)