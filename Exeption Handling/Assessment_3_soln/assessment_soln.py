car = {'model':3,'year':56,'maker':'bmw'}

try:
    print(car['colour'])
except:
    print("THAT ATTRIBUTE WAS DEFINED")
finally:
    print("END OF WORK")
