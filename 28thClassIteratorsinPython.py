
# ! Class Iterators

# * __iter__ is basically the thing which is actually the iterator

# * __next__ is similar to that of step in range function

class MyContainer:
    def __init__(self, mylist):

        self.mylist = mylist   

    def __iter__(self): # * Returns the iterable thing to tt

        self.i=0 # * We set iterable i here

        return self
    
    def __next__ (self):

        self.i += 1

        if self.i >= len(self.mylist):

            raise StopIteration

        return self.mylist[self.i - 1] # * We do -1 so that 1 - 1 happens to give us 0 so that we get from the start
        
tt = MyContainer([1,2,3,4,5])

for i in tt:

    print(i)

class SquareNum:

    def __init__(self, n):

        self.n = n

        self.current = 0

    def __iter__(self): # * Returns the iterable thing to variable sq

        return self
    
    def __next__(self):

        if self.current >= self.n:

            raise StopIteration # * Stops the loop after condition is met
        
        square = self.current ** 2 # * Square no. are printed

        self.current += 1

        return square
    
sq = SquareNum(5)

for i in sq:

    print(i)