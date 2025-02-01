
# ! Inheritance

# * Where one class takes or 'inherits' attributes(variables) or methods(functions) from other classes

class Curry:

    def __init__(self, name, temperature):
        
        print('In Class Curry Constructor')

        self.name = name

        self.temperature = temperature

    def display(self):

        print('In Class Curry Display')

class Vegetable(Curry): # * This leads to inheritance

    def __init__(self, name, temperature, batchno):

        self.batchno = batchno
        
        Curry.__init__(self, name, temperature) # * We can initialize the other variables using the other Parent's class's Constructor

        print(f'Taken from other class:\nName of Soup: {self.name}\nTemperature of Soup: {self.temperature}\nIs in this Vegetable Class:\nBatchno: {self.batchno}')

    def disp(self):
        
        print('In Class Vegetable Disp')

        Curry.display(self) # * We can use the Parent Class to call it's function

eng = Vegetable('Tomato Soup', 56, 101) # * When I call this, the constructor of Curry runs first

# eng.disp() # * Can call the method in this class itself

# eng.display() # * Can also call the method present inside Parent Class
