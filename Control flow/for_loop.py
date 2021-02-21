#Using for loopss
name = "ASMJUDIKTLOPFD"

for chr in name:
    print("CURRENT VALUE IS: ",chr)

print("***********************************************")
#for loop too access list 
h = [2,3,4,5,6,7,8,9]
for digits in h:
    print("Digit is: ",digits)

print("***********************************************")
#for loop too access dictionaries
p = {'k1':2,'k2':3}
for k,v in p.items():
    print(k)
    print(v)


print("***********************************************")
#for loop too access dictionaries
f = {'k1':2,'k2':3}
for digt in h:
    print(digt)

#using list in range
g = list(range(1,100))
print(g)
a = range(20,36)
print(a)
for dgt in g:
    print("VALUE ARE: ", dgt)


print("***********************************************")
L1 = [3,4,5,6,7,8]
L2 = [10,11,12,34,56]
for a,b in zip(L1,L2):
    print(a)
    print(b)
    if a < b:
        print("A IS GREATER")
    else:
        print("B IS GREATER")
    
               
