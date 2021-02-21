nm = list(input("INTEGER LIST: "))
print(max(nm))
print(abs(-20))
print(min(nm))
print(type(nm))

#the function above can be used inside function as well
def funh(*args):
    print(max(args))
    print(min(args))


def abs_finder(num):
    print("ABS OF ENTERED VALUE IS: ",abs(num))

funh(10,-12,-13,40)
abs_finder(-25)
abs_finder(25)
