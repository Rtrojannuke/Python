# Adding numbers together
a = 5
b = 6

c = a + b
print("the addition of the numbers are: {}".format(c))

# Printing the cube of a number
x = int(input("Enter any number: "))

z = x**3

print("the cube of the number is: {}".format(z))

#ASSIGNING VALUES TO L1 & L2
L1 = [10, 20, 30, 25, 32, 45, 50]
L2 = [80, 70, 78, 55, 62]

# SUMMING L1 & L2 TO S1 & S2
S1 = sum(L1)
print("THE TOTAL VALUE IN LIST1(L1) IS: {} " .format(S1))

S2 = sum(L2)
print("THE TOTAL VALUE IN LIST2(L2) IS: {} " .format(S2))

s3 = S1 - S2
print(s3)

def multiplier(x):
    g = x * 0.0026
    print(g)

multiplier(70)

import calendar

cal = calendar.month(1999,6)
print(cal)
