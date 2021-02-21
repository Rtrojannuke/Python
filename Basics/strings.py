"""
Strings are sequence of characters which are placed in either single quotes or double quotes
"""

name = "Nunu"
print("Name is: ",name)
mi = 'Mirror'
print("MI is: ",mi)

#Don't use double quotes in double quote and Single quote inside single quotes
d = "My name is 'namae' in hyper"
print("D is: ",d)
g = 'Gmaers like "food" alot'
print("G is: ",g)

#Usin the \ \ escape sequence which ingores the double quotes whithout stopping at that point
f = "My home is at \"yoyoyo\" lagos"
print("F is: ",f)
 
"""
Strings can be manipulated in many ways which can be seen below:
"""
#Accessing strings characters: since strings are sequence that means that each character can be used seperately by accessing with their index
nt = "Airtel"
print(nt[0])
print(nt[1])
print(nt[2])
print(nt[3])
print(nt[4])
print(nt[5])
#print(nt[6]) #Out of range error

"""
len(): used to get the length of the charaters in a string
lower(): change all alphabet to small letter
upper(): change all aplphabet to capital letter
str(): used to add more values to a string
"""

print("The lower form of F is: ", f.lower())
print("The capital form of F is: ", f.upper())
print("The length of f is:", len(f))

sb = f + str(" GO home")
print("New string gotten from F is: ", sb)

#Concantenation: is the adding of two or more strings to give a new single strings
a = "Hello"
b = 'World'
conct = a + b
print("Concatenated string is: ", conct)

# Replacing a string character is done used the replace() function
bl = "BUGGATTI"
print(bl.replace('G','TT'))
#Count can also be used with count
print(bl.replace('G','TT',2))

#Creating a substrings
r = bl[1]
print(r) #or
vn = bl[0:4]
print(vn) #or
vb = bl[0:6:2]
print(vb)

#getting the values from behind(From the Last value)
jk = bl[-3]
#Getting all values except the last value
jp = bl[:-1]
#Getting all values except the last value
jm = bl[:len(bl)-1]
print("Value of jm is ",jm)
#Getting values from a string in the sequence of a number(It omits in order of number given)
jf = bl[::3]
print("Value of jf is ",jf)
#Turning around the string (Arrangeing it from the last value from behind)
jv = bl[::-1]
print("Value of jv is ",jv)


print("THIS IS A STRING AND IT'S VALUE IS %s" %(conct))

print("THIS IS A STRING AND IT'S VALUE IS %s, THIS IS A STRING AND IT'S VALUE IS %s" %(bl, conct))
