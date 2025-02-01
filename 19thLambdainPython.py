
# ! Lambda Functions

# * Basically, One-Liners but for functions

# * lambda multiple arguments seperated by comma : expression which leads to output

square = lambda x: x * x

print(square(4), square,type(square)) # * Prints 16 lambda smt <class 'function'>

maxi = lambda a,b: a if a > b else b

print('The max is',maxi(3,2))

# * Lambda can also be used as an inner function

def funky(n):

    return lambda a: a * n # * The innerf function

innerboi = funky(4) # * Very similar to callback functions

print(innerboi(3))
