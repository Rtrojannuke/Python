"""
Conditonal Statement are used to make decison based on some set of conditions
There are 3 types of conditional statement in Python which are if, elif and else
"""
age = float(input("Enter your age: "))

#Using if to restrict age less then 18
if(age<18):
    print("SORRY, YOU AREN'T WELCOME INTO THIS PLACE PLEASE")
elif(age>= 18):
    print("YOU ARE HIGHLY WELCOMED")

print("*******************************END OF FIRST SET OF CODE***************")


cge = int(input("Enter your age: "))

#Using if to restrict age less then 18
if(cge < 18):
    print("SORRY, YOU AREN'T WELCOME INTO THIS PLACE PLEASE")
    
elif(cge >= 18 and cge < 70):
    print("YOU ARE HIGHLY WELCOMED")
    
elif(cge == 71 or cge <= 100):
    print("YOU MIGHT DIE HERE OLDIE")

else:
    print("NO ENTRY")
