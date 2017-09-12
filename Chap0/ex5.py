from sys import argv
script,input_file = argv
new_file=open(input_file)
#print (new_file.read())
#for i in range(1,4):
#    print (new_file.readline())
new_file.seek(0)
for i in range(1,4):
    print (new_file.readline())
