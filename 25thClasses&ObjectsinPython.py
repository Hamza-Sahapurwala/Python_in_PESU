
# ! Classes and Objects

# * Start of OOPS

class Car:

    r = '1'

    def __init__(self, name): # * init function is a constructor which is called always whenever the class is called to make any object

        # * self is a reference to objects so that one object's data is not given another data
        
        print('Class Called')

        self.model = name

    def display(self):

        print('This is the model:', self.model)

    def gettingmodel(self): # * Getters are used to 'get' elements from the class
        
        return self.model

    def settingmodel(self, new_model): # * Setters are used to set new values for the elements 

        self.model = new_model

    def __del__(self): # * Deletor which deletes the object
        
        print('This deletes all parts of the objects') # * This gets printed evertime the program ends or when the object is deleted

car1 = Car('Ford')

print(car1.gettingmodel())

car1.settingmodel('Mustang') # * Changes value of model

print(car1.gettingmodel())

print(getattr(car1, 'r')) # * Only able to get variables which are not set by self thingy

setattr(car1,'r',2) # * Same condition as above but changes value of variables

print(getattr(car1, 'r')) # * Says which value has changed

print(hasattr(car1, 'r')) # * Returns True if variable is present in class else False

# delattr(car1, 'r') # * removes element r
