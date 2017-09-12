'''
things= "1st,2ed,3rd,4th,5th,6th,7th,8th,9th,10th"
list =things.split(",")
print ("--".join(list[2:4]))
print (list.pop(0))
'''
dict = {1:"d",2:"c"}
print (dict)
dict.clear()
for i in range(1,11):
    dict[i]=str(i)+"item"
print (dict.keys())
print (dict.values())
print (dict.items())
