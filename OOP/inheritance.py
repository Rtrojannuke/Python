"""
Inheritance is the process where the methods declared in a class can be used, the class which contains the method class is called Parent class
The class which utilizes the method is called Child class
"""
#Creating a Parent class
class Human(object):
    def __init__(self):
        print("YOU HAVE CREATED THE TEMPLATE OF HUMAN")
    def eat(self):
        print("HUMAN CAN EAT")
    def drink(self):
        print("HUMAN CAN EAT")

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

#
nb = Man()
nb.eat()
nb.drink()
