"""
Exception handling is way to handle errors either wanted or unwanted
There are three exception statements in Python which are try, except and finally
try block contains the code which should be executed or tried
except block contains the alternate code/message when there is an error in the try bloc
finally block ia always executed
except block is only executed when there is an error in the try block
Except block can be used to handle specific error specally
"""
"""
a = int(input("ENTER NUMBER: "))
b = int(input("ENTER NUMBER: "))
j = 'nams'

try:
    c = a/b
    print(c)
   
except ZeroDivisionError:
    print("THE VALUE YOU ARE DIVIDING IS POSSIBLE")
except TypeError:
    print("TYPE ERROR OCCURS")
finally:
    print("AM ALWAYS EXECUTED")

#OR
""" 
try:
    b = 2
    c = 1 + b
except:
    print("ERROR IS UNKNOWN")
    raise Exception("ERROR")
#Else is only executed if the except isn't executed/no error/no exception
else:
    print("NO EXCEPTION")
finally:
    print("ALWAYS EXECUTED")
#Raise exception is used to handle exception and to show stack trace
