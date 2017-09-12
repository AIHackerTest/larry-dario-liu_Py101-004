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
data = open("w1.txt","rt").readlines()            #是否可以去掉此行
stuff={}
element=[]
for i in data:                      #单行城市天气对应关系截取出来
    element=i.split(",")
    stuff[element[0]]=element[1].strip() #readlines保留换行符，用strip去掉
    element.clear()              #清空临时list
#2.设立查找函数
history ={}
def index(city):#建立查找函数和立式
    if city  in stuff:
        print (stuff[city])
        history[city] = stuff[city]
    elif city == "help":
        print("帮助文档：\n \
        输入城市名，查询城市天气；\n \
        输入help，获取帮助文档；\n \
        输入history，获取查询历史;\n \
        输入quit，退出天气查询系统")
    elif city == "history":
        print (history)
    elif city == "quit":
        print ("退出程序")
    else:
        print ("请输入正确的城市名或者help查看帮助")
#3.循环呼入
while type != "quit":
    type = input ("输入城市名称：  ")
    index(type)
