# 基本的四个对象
from bs4 import BeautifulSoup

if __name__ == '__main__':
    soup = BeautifulSoup(open('index.html'), 'lxml')  # 创建BeautifulSoup对象
    print(soup.prettify())      # 打印soup对象的内容，格式化输出
    print("Title is :")
    print(soup.title)       # 抽取title和a等Tag对象
    print(soup.a)           # 利用这种方式，查找的是所有内容中第一个符合要求的标记
    # Tag
    # 每个Tag对象都有两个最重要的属性：name和attributes，可以打印或赋值
    print("Title's name: "+soup.title.name)
    # 对于attributes，采用与字典类似的方法
    print(soup.p['class'])
    print(soup.p.get('class'))
    # 也可以获取所有属性
    print(soup.p.attrs)
    # NavigableString
    # Beautiful Soup用NavigableString类来包装Tag中的字符串
    print(soup.p.b.string)    # 获取标记内部的文字，前提是精确到只有一对标签，否则用text
    # BeautifulSoup
    # BeautifulSoup对象表示的是一个文档的全部内容
    # Comment
    print(soup.a.string)
    print(type(soup.a.string))
