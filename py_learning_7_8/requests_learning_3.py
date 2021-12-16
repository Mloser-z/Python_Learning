# 响应与编码
import requests
import chardet


r = requests.get('https://www.baidu.com')
print('content--->')
print(r.content)
print('text--->'+r.text)
print('encoding--->'+r.encoding)
r.encoding = 'utf-8'
print('new text--->'+r.text)

# r.content返回的时字节形式，r.text返回的是文本形式，r.encoding返回的是根据HTTP头猜测的网页编码格式
# 'encoding--->'之后的是ISO-8859-1，出现乱码，手动改为utf-8后，不会出现乱码
# 下面使用一种更加简便的方法：chardet，这是一个非常优秀的字符串、文件编码检测模块

# chardet.detect()返回字典，其中confidence是检测精度值，encoding是编码形式
print(chardet.detect(r.content))
r.encoding = chardet.detect(r.content)['encoding']
print(r.text)

# 除了上面那种直接获取全部响应的方式，还有一种流模式：
print('流模式：')
rp = requests.get('https://baidu.com', stream=True)     # 设置stream=True标志位，使响应以字节流方式读取
print(r.raw.read(10))   # 指定读取的字节数
