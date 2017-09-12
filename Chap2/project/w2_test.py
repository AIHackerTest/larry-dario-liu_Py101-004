import ssl
from urllib import request, parse
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

KEY = 'qd6vjizg3shaoy3a'  # API key
UID = "U68AA46C76"  # 用户ID
API = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言

def fetchWeather(location):
    params = parse.urlencode({
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    })
    req = request.Request('{api}?{params}'.format(api=API, params=params))
    response = request.urlopen(req, context=gcontext).read().decode('UTF-8')
    return response #用jason更好


def fetchdata(your_input):
    list1=fetchWeather(your_input).split("{")
    list2=list1[4].split(",")
    bank = {}
    for i in list2:
        list3=i.split(":")
        bank[list3[0]]=list3[1]
    answer = "天气:"+bank['"text"']+" 温度:"+bank['"temperature"'] \
        +" 湿度:"+bank['"humidity"']+" 更新时间:"+bank['"last_update"']
    return answer
    list1.clear()
    list2.clear()
    list3.clear()
