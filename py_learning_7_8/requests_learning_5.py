# 响应码code和响应头headers处理
import requests


r = requests.get('https://baidu.com')
if r.status_code == requests.codes.ok:
    print(r.status_code)    # 响应码
    print(r.headers)    # 响应头
    print(r.headers.get('content-type'))
else:
    r.raise_for_status()

# r.headers包含所有响应头的信息
# r.raise_for_status()主动产生一个异常，当响应码是4XX或5XX时，函数会抛出异常，否则返回None
