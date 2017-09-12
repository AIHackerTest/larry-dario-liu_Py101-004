"""
功能如下:
输入城市名，获取城市的天气状况；
输入指令，获取帮助信息；
输入指令，获取历史查询信息；
输入指令，退出程序。
有更新时间
第三方模块request
"""
from w2_test import fetchdata
history ={}
def index(city):#建立查找函数和立式
    if city  in ["quit","exit"]:
        print ("退出程序")
    elif city in ["help","h"]:
        print("帮助文档：\n \
        输入城市名，查询城市天气；\n \
        输入help，获取帮助文档；\n \
        输入history，获取查询历史;\n \
        输入quit，退出天气查询系统")
    elif city =="history":
        print(history)
    else:
        print(fetchdata(city))
        history[city]=fetchdata(city)
#3.循环呼入
user_input = " "
while user_input not in ["quit","exit"]:
    user_input = input ("输入城市名称：  ")
    try:
        index(user_input)
    except:
        print("not exist")
