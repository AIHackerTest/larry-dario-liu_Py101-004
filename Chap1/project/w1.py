"""
功能如下:
输入城市名，获取城市的天气状况；
输入指令，获取帮助信息；
输入指令，获取历史查询信息；
输入指令，退出程序。

请输入指令或您要查询的城市名:"

帮助文档：
输入城市名，查询城市天气；
输入help，获取帮助文档；
输入history，获取查询历史；
输入quit，退出天气查询系统

whetherbank=dict()
for i in range(1,11):
    whetherbank[i]=str(i)+"a"
print (whetherbank)
"""
#1.建立城市天气查找字典
data = open("w1.txt","rt").read()  #随后考虑用ReadLine函数
data = data.split('\n')            #是否可以去掉此行
stuff={}
element=[]
for i in data:                      #单行城市天气对应关系截取出来
    element=i.split(",")
    stuff[element[0]]=element[1] #对应关系添加到字典
    element.clear()              #清空临时list
#2.设立查找函数
history ={}
def branch(type):               #分类查找
    if   type == "help":
        print("帮助文档：\n \
        输入城市名，查询城市天气；\n \
        输入help，获取帮助文档；\n \
        输入history，获取查询历史;\n \
        输入quit，退出天气查询系统")
    elif type == "history":
        print (history)
    elif type == "quit":
        print ("退出程序")
    else:
        index(type)
def index(city):#建立查找函数和立式
    if city  in stuff:
        print (stuff[city])
        history[city] = stuff[city]
    else:
        print ("请输入正确的城市名称，或者输入help查看帮助")
    return history
#yourcity =input("输入城市名称：  ")
#while yourcity !="quit":   #出现了一个问题，输入一个城市跑出N个结果
#    branch(yourcity)
#    if yourcity == "quit":
#        exit()
#3.确保持续输入while
while True:
    type = input("输入城市名称> ")
    branch(type)
    if type == "quit":
        break