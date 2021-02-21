"""
Function with Argument and return statement
We can also give default values to the parameters/arguments in a function
"""
def mulp(n2=50):
    nv = int(input("Enter a number: "))
    nb = 0
    while n2 != 0:
        nb = n2 * nv
        print("Multiplication of %i * %i IS: %i"%(nv,n2,nb))
        n2-=1
    return nb


#Calling the function without an argument will work bcos we have given the function argument/parameter a value while creating it 
k = mulp()
print("Value of k is: ",k)

#Calling the function with argument will work but the value in it will replace the value given to the argument while creating the function
g = mulp(30)
print("Value of g is: ",g)

"""
Variables defined outside a function are not used in the function unless the functtionis specified to use the variabl
The Using of the variable is don by using the global keyword
"""
name = input("ENTER YOUR NAME: ")
print(name)

def greeting():
    global name #Uses the variable name defined above the variable
    print("HELLO ",name)
#If the global keyword is used, the changes made to the variable affects not only within the block but outside as well
    name = "SOLO"

greeting()
print(name)
