"""
method is a group of statements/code to complete a specific action
A function is defined by using the word def first, functions can either take in argument or not
"""

#Without Argument and return statement
def multyp():
    num = int(input("Enter a number: "))
    tble = 100
    n = 0
    while tble != 0:
        n = tble * num
        print("Multiplication of %i * %i IS: %i"%(num,tble,n))
        tble-=1

#Calling the function
multyp()

#Accepting Arguments but no return statement
def multp(n1):
    num = int(input("Enter a number: "))
    n = 0
    while n1 != 0:
        n = n1 * num
        print("Multiplication of %i * %i IS: %i"%(num,n1,n))
        n1-=1

#Calling the function
multp(20)


#Function with return statement but not accepting arguments
def mulyp():
    num = int(input("Enter a number: "))
    tble = 100
    n = 0
    while tble != 0:
        n = tble * num
        print("Multiplication of %i * %i IS: %i"%(num,tble,n))
        tble-=1
    return n

#Calling the function
v = mulyp()
print("Value of v is: ",v)

#Function with Argument and return statement
def mulp(n2):
    nv = int(input("Enter a number: "))
    nb = 0
    while n2 != 0:
        nb = n2 * nv
        print("Multiplication of %i * %i IS: %i"%(nv,n2,nb))
        n2-=1
    return nb

#Calling the function
g = mulp(30)
print("Value of g is: ",g)

#Using list in function
def housech(name):
    strt = ['ASMOL','LUBE','KATO','NERO']
    if name in strt:
        return True
    else:
        return False
b = housech("GHANE")
print(b)
