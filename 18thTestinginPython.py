
# ! Pytest

def testsqrt():

    assert (25 ** 0.5) == 5 # * Tells pytest to look at this statement speifically

    print((25 ** 0.50) == 8)

# ! Doctest

# * We can give testcases in the docstring(triple quotes) and use doctest module to check if a function works or not

import doctest

def facto(n):

    '''
    >>> facto(5)
    120
    >>> facto(0)
    1
    '''

    if n == 0:

        n = 1

    else:

        n = n * facto(n - 1)

    return n

doctest.testmod(name='facto', verbose=True)

# * Verbose=True prints something even if all tests have passed