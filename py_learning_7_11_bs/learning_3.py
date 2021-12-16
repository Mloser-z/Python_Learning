# 搜索文档树
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    soup = BeautifulSoup(open('index.html'), 'lxml')
    # find__all(name, attrs, recursive, text, **kwargs)
    # name参数
    # 传入字符串
    print(soup.find_all('b'))
    # name传入正则表达式，所有以b开头的标记
    for tag in soup.find_all(re.compile('^b')):
        print(tag.name)
    # 传入列表，会将与列表中任一元素匹配的内容返回
    print(soup.find_all(['a', 'b']))
    # 传入True，True可以匹配任何值
    for tag in soup.find_all(True):
        print(tag.name)

    # 定义函数，可以作为过滤器，返回所有使函数返回值为True的
    def has_class_id(i_tag):
        return i_tag.has_attr('class') and i_tag.has_attr('id')

    print(soup.find_all(has_class_id))
    # kwargs参数，表示keyword参数
    print(soup.find_all(href=re.compile('elsie')))      # 查找href属性中含有“elsie”
    print(soup.find_all(id='link2'))    # 指定id
    print(soup.find_all('a', class_='sisters'))     # 由于class在python中是关键字，所以在后面加下划线
    # text参数，搜索文档中的内容，类似与name的可选参数
    print(soup.find_all(text='Tillie'))
    print(soup.find_all(text=['Tillie', 'Elsie', 'Lacie']))
    print(soup.find_all(text=re.compile('Dormouse')))
    # limit参数，限制返回结果的数量
    # recursive参数，是否搜索孙节点，如果recursive=False，则只搜索tag的直接子节点
    print(soup.find_all('title'))
    print(soup.find_all('title', recursive=False))
