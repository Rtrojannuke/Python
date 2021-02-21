"""
Python is also an object oriented programming Language
Class is a template/blueprint that defines it objects
Class are created using the class keyword
"""
class cars(object):
    #wheels and screen are member variables since they are features that all cars have
    wheels = 4
    screen = "TINTED"
    #Creating an Instance of the class
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model
     #Creating an Instance of the class
    def infor(self):
        print("MAKER  OF THE CAR IS ", self.maker)
        print("MODEL  OF THE CAR IS ", self.model)


#instance of the class
bmw = cars("bmw", "ESD46")
bmw.infor()
print(bmw.wheels)
print(bmw.screen)

print("#"*20)
print(cars.wheels)
#Changing values of member variable
cars.wheels = 5

print("#"*20)
print(cars.wheels)
