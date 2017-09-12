stuff = "this is a line of nonsense"
lists = stuff.split(' ')

length = len(lists)
i=0
while i < length:
    i+=1
    print (lists)
    print (lists.pop(-1))
