#List are a collection of informations. They are a type of variable in a square brackets
#Empty list
cars = []
#List with variables
bike = ["Bajaj","TVS", "JINCHENG", 5,8]

#Accessing the values in a list
#printing all values in a list
print(bike)
#Printing values in a list using index
print(bike[0])
print(bike[2])
#Summing values in a list
k = [2,3,4,5]
s = k[0] + k[1] + k[2]
print("THE SUM IS: ",s)

#Changing the values in a list
bike[2] = "Youppi"

#checking the length of a list
length = len(bike)
print("Length is: ", length)

#Adding more values to the end of the list using append methods
cars.append("Benz")
cars.append("BBG")
print(cars)
#Adding more values to an index of chooice
cars.insert(1, "ROVER")
print(cars)
#How to check the index of an element in a list
c = cars.index("Benz")
print("Index of Benz is ",c)

#Removing items on a list
#pop() method removes from the end 
cars.pop()
print(cars)
#remove() removes any item of choice
cars.remove("ROVER")
print(cars)
#Slicing a list
#Saves the value of index 1 to the end in another variable
slc = bike[1:]
print(slc)
#saveing from index 0 to 1 
sdc = bike[0:2]
#Sorting the values in a list
bike.sort()
print(bike)
