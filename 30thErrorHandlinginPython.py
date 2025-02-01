
# ! Error Handling

# * For Error handling, we use four blocks

# * try block contains the code contains the code that may throw an error (always needs 1 except or finally block after this)

# * except block contains the code to be run if an error is thrown in the try block (we can specify the error too)

# * else block contains the code to be run if no errors are raised

# * finally block which contains code which will run irrespective of any error is raised or not

try:

    a  = 3

    b = a / 0

except NameError:

    print('Variable doesn\'t exist')

except ZeroDivisionError:

    print('Tried to divide by zero')

else:

    print('Else code')

finally:

    print('Finally Blocks always runs')

# ! Raise

# * We can raise errors by ourselves using the the raise keyword

try:

    a = 4

    b = 3

    raise StopIteration # * Any error can be written here

except Exception as n:

    print('Raised error',n)

else:

    print('Runs when no error is raised')

finally:

    print('Always runs')