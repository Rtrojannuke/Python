"""
Writng into file from a python code
FileIO: in inputting and outputting from a file with python
Modes of File IO in python are as follows 
w - write only mode
r - read only mode
r+ - read and write mode
a - append Mode
"""

#Writing to a file
ml = [2,3,4,5,6,7,8,9]
mf = open("free.csv","w")
for item in ml:
    mf.write(str(item)+ "\n")
mf.close()
#File has to be close bcos the file is currently open in the computer's memory and wo't be accessible(read) unless it is clossed


"""
Read from a file
to read  a file, the following methods are used
.read() -->Reading everything in the file at once
.readline() --> reading everything in the file line by line
"""


#Reading all from the file
md = open("free.csv","r")
print(str(md.read()))
md.close()


print("###"*5)

#Reading Line by line
mk = open("free.csv","r")
print(str(mk.readline()))
mk.close()

"""
Using with and as keyword in FILEIO give a turn about for users not to worry about closing the file
"""
#using with keyword
with open("kind.csv","w") as nana:
    nana.write("cooooloolololol")
print() #Not compulsory just an extra addition
print("About to read") #NC
with open("kind.csv","r") as rdn:
    print(str(rdn.read()))


