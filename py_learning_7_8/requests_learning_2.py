import requests


payload = {'Keywords': 'blog:qiyeboy', 'pageindex': 1}
r = requests.get('https://zzk.cnblogs.com/s/blogpost', params=payload)
print(r.url)

# 另一种方式处理带参数的网址
# https://zzk.cnblogs.com/s/blogpost?Keywords=blog%3Aqiyeboy&pageindex=1
