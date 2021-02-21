"""
Inheritanc is the process where the methods declared in a class can be used, the class which contains the method class is called Parent class
The class which utilizes the method is called Child class
Overriding  is the act of change the way methods in the parent class are implemented
"""
#Creating a Parent class
class Human(object):
    def __init__(self):
        print("YOU HAVE CREATED THE TEMPLATE OF HUMAN")
    def eat(self):
        print("HUMAN CAN EAT")
    def drink(self):
        print("HUMAN CAN DRINK")

#Creating an instance of the Parent class
ch = Human()
ch.eat()
ch.drink()
print("*"*20)
#Creating the Child class(Child class will be able to use the attribute of the Parent class)
class Man(Human):
    def __init__(self):
        Human.__init__(self)
        print("YOU HAVE CREATED A MAN")
    #Oveerriding the eat method
    def eat(self):
        super().eat() #Sper() is used to call methods from the base class when overriding to use and add more feature
        #super(Man,self).eat()
        print("MAN CAN EAT")
    def candd(self):
        print("YOU CAN MAKE BABIES")

#
nb = Man()
nb.eat()
nb.drink()
