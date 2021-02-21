#Dictionaries are datatypes that can save more than one value but in terms of key valu pairs
#Dictionary items are usually in a curly braces seperated by comma. Dictionaries can't be indexed
dv = {'goal':'Score', 'book':'school'}
#Printing all values in a dictionary
print(dv)

#Printing all needed 
b = dv['goal']
print(b)

#Printing values by keys in a dictionary
print(dv['book'])
#Empty dictionary
gm = {}

#Adding more values to dictionary
gm['sweet'] = 'Lollipop'
gm['biscuit'] = 'Shapes'
print(gm)

#Adding values f dictionary keys
sul = gm['sweet'] + gm['biscuit']
print(sul)
#Changing values of a key in a dictionary
gm['sweet'] = 'bobo'
print(gm)

#Dictionary(ies) can be nested in a dictionary
vb = {'lp':{'goal':'Score', 'book':'school'}, 'bo': gm}
print(vb)
#Accessing nested dictionary(ies)
#Access the main  dictionary then access the contained dictionary 
vb['bo']['sweet']
print(vb['bo']['sweet'])
#Saving values in a variable
kb = vb['lp']['goal']

#Dictionary Methods
#Viewing all keys in the dictionary
print(dv.keys())
print(vb.keys())
#Viewing all values in the dictionary
print(dv.values())
print(vb.values())
#Viewing keys and values
print(vb.items())
print(dv.items())

#Copying dictionary
vbs = vb.copy()
print(vbs)
#Clearin the values in a dictionary
vbs.clear
print(vbs)
#Removing values in a dictionary
print(vb.pop('lp'))
print(vb)
