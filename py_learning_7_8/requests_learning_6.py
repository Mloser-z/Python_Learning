# Cookie处理
import requests


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('https://baidu.com', headers=headers)
# 遍历所有的Cookie字段的值
for cookie in r.cookies.keys():
    print(cookie+':'+r.cookies.get(cookie))


#   如果想自定义Cookie值发出去，可以使用以下方式，示例如下：
cookies = dict(name='qiye', age='10')
r = requests.get('https://baidu.com', headers=headers, cookies=cookies)
print(r.text)
