
# ! __doc__ variable and help()

# * In Python, each object can be documented using Docstrings

# * e.g.

a = 1

def adddddd():

    '''Performing Addition of two numbers'''
    
    print(a + 7)

print('Using __doc__, we get:')

print(adddddd.__doc__) # * Prints the triple quoted comments in the function

# ! The triple quotes should always be on top

print('Using help(), we get:')

help(adddddd) # * This by itself prints the triple quoted comment with more things which tells where the function is present

# ! __name__

# * If no modules is imported, __name__ = __main__

# * If modules are imported, __name__ = name of the file

print(__name__) # * Prints __main__