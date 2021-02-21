#Contains a For loop which iterates the QA team list and print member(s) name and contains a conditional statement that prints out QA Team Lead” when the Member name is Timilehin
qateam = ["Timilehin", "Boluwatife", "Azeez", "Nathaniel", "Mutiu", "Nasifudeen", "John", "Mubarak"]

for member in qateam:
    print(member)
    if(member == "Timilehin"):
        print(member + "IS THE QA TEAM LEAD")
        print("YOU ARE THE TEAM LEAD OF SEAMLESSHR QA TEAM")

#Create a while loop to play the guess a number game(user guess a number, if it is right user proceeds, if wrong user enter another number till when the number entered by user is same with the guessing number)
guessnumber = int(input("Enter any number of your choice: "))
check = 9
while(guessnumber != check):
    print("YOU ARE WRONG")
    guessnumber = int(input("Enter any number of your choice: "))
    check = 9
    if(guessnumber == check):
        print("YOU ARE CORRECT")

#Create a dictionary which contains the QA team member as key and product team as the value
qteamp = {"Tife":"Non recurring Modules","Nate":"CoreHr","Azeez":"Performance","John":"Payroll","Mutiu":"Payroll","Dimeji":"Recurring Modules", "Mubarak":"Mobile(App and web)"}
for key,value in qteamp.items():
    print(key + " is the QA in charge of "+ value)


#Create a function that the number entered by the user raise to power of 10 (e.g 10**10) and prints out the value.
n = int(input("Enter number you want to check it's power of 10: "))
def powerof10(n):
    power10 = n**10
    print(power10)
    message= "YOU CHECKED THE POWER OF 10 OF %d WHICH IS %d "
    print(message %(n, power10))
    
powerof10(n)
