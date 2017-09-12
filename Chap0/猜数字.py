import random
target = random.randint(0,20)
num = False
for i in range(1,11):
    guess=int(input("请输入20以内的数字  "))
    if target ==guess:
        print ("正确")
        num = True
        break
    elif target < guess:
        print ("大了")
    else:
        print ("小了")
if num:
    print ("Good job,你用第%d次机会猜中了"%i,"正确答案是%d"%target)
else:
    print ("很遗憾你花光了所有运气，也一事无成")
