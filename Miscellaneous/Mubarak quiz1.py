#Mubarak Arimiyah
#Mobile Product Team

#2, Create a tuple which consist of your name and Product team
nameaTeam = ("Mubarak Arimiyah", "Mobile team")

#3,Format a print statement to show “Hello your name, you are a member of the product team. Welcome to SeamlessHR”
greeting = "Hello %s, You are a Member of the %s. Welcome to SeamlessHR" % (nameaTeam)
print(greeting)

#4, Check if a number is even or odd
num = int(input("Enter Number you would like to check: "))

#4b, Conditional Statement to check if number is even
if(num % 2 == 0):
    print("THE NUMBER %d IS EVEN" % num)
else:
    print("THE NUMBER  %d IS ODD" % num)
