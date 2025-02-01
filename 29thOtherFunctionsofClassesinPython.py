
# ! super() Function

# * How we used the Constructors of Parent class to spread info between 2 classes can be done in a more efficient way

class A:

    def disp(self):

        print("in disp A")

class B:

    def disp(self):

        print("in disp B")

class C(B, A): # * If the order is reversed, the print changes to '' in disp A '' (Also this is Multiple Inheritance)

    def disp(self):

        super().disp() # * This prints in disp B as B is the first Class to be inherited from

        # * '' in disp A '' is not printed as B is first inherited class

        print("in disp C")

c1 = C()

c1.disp()

# * Now super() use in defining variables across multiple classes

class Shape:

    def __init__(self, name): # * Here self.name variable is assigned the value

        self.name = name
    
    def info(self): # * This function is not called as the info function in it's Child Class(which is Polygon) is called by the super() in the other children classes

        return f"This is a {self.name}."
    
class Polygon(Shape):

    def __init__(self, name, sides):

        super().__init__(name)

        self.sides = sides # * self.sides is assigned here

    def info(self): # * This function is only called

        return f"A {self.name} is a polygon with {self.sides} sides."
    
class Triangle(Polygon):

    def __init__(self, name):

        super().__init__(name, 3)
class Quadrilateral(Polygon):

    def __init__(self, name):

        super().__init__(name, 4)

trig = Triangle('Triangle')

print(trig.info())

rec = Quadrilateral('Rectangle')

print(rec.info())

# ! issubclass Function

# * Syntax: a = issubclass(childclassname, parentclassname) 

# * This gives True if child class is actually a child of Parent Class else False

print(issubclass(Triangle, Shape)) # * True

# ! isinstance Function

# * Syntax: a = isinstance(object, classname)

# * This gives True if a variable is an object of a class else False

print(isinstance(trig, Triangle)) # * True
