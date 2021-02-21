x = int(input("Enter Number: "))

while x != 18:
    x = int(input("Enter Number: "))

print("YOU SCALED THROUGH")

print("***************@@@@@@@@@@@@@@************@@@@@@@@*****************")
k = []
n = 0
while n < 10:
    k.append(n)
    n+=1

print(k)

print("***************@@@@@@@@@@@@@@************@@@@@@@@*****************")
#Using Break statement in a while loop
j = []
p = 0
while p < 10:
    j.append(p)
    p+=1
    if p == 6:
        break
print(j)

print("***************@@@@@@@@@@@@@@************@@@@@@@@*****************")
#Using Break statement in a while loop
h = []
b = 0
while b < 10:
    h.append(b)
    b+=1
    if b == 6:
        continue
    print("uuuuuuuuuuuu")
print(h)

#Using Break statement in a while loop
d = []
b = 0
while b < 10:
    d.append(b)
    b+=1
else:
    print("yooo, am else")
print(d)
