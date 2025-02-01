
# ! Polymorphism

# * Basically, Function Overloading but in Classes

# * What I mean is same function names across several classes

# * Where ever the required parameters meet, only then that particular function is called

class Shape:

    def cal(self):

        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        
        self.length = length

        self.width = width

    def cal(self):

        return self.length * self.width
    
class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def cal(self):

        return 3.14 * (self.radius ** 2)
    
rec = Rectangle(21, 4)

print(rec.cal())

cir = Circle(2)

print(cir.cal())