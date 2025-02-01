
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