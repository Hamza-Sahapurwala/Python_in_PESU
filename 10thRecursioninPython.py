
# ! Recursion

# * Calling a function while the function itself is running

# * We can use the above property to solve problems

# * To use the above thing, the criteria of writing a recursive functions:

# * Base Case: The condition to stop recursion at this point

# * Recursive Case: Anything which is not the base case but takes some step towards the base case

# * Recursive Fucntions work like STACKS!!!

# * Using Recursive functions to find factorial of a no.

# * Depth: No. of steps to complete a problem

# Advantages:

# 1. Used to simplify complex problems into smaller easier problems

# 2. Solving problems with repeated patterns

# 3. Handling unknown levels of depth

# 4. Mathematical & Algorithmic

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