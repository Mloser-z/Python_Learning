# 请求头headers处理
import requests


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('https://baidu.com', headers=headers)
print(r.content)
r.encoding = 'utf-8'
print(r.text)
