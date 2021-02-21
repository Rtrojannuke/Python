filewr =open("/Users/seamlesshr/Documents/Cds/Py/ttt.txt")
#inp = filewr.read()
print(filewr)
count = 0
for lines in filewr:
    count = count + 1
    print(count)


filewr =open("/Users/seamlesshr/Documents/Cds/Py/ttt.txt")
inp = filewr.read()
print(len(inp))


filewr =open("/Users/seamlesshr/Documents/Cds/Py/ttt.txt")
for line in filewr:
    line = line.rstrip()
    if line.startswith('Software '):
        print(line)

try:
    filer =open("/Users/seamlesshr/Documents/Cds/Py/pxta.txt")
except:
      print('file cannot be opened: ')
finally:
    print('file cannot be opened: ')
    #quit()

