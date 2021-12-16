# 遍历节点树
from bs4 import BeautifulSoup

if __name__ == '__main__':
    soup = BeautifulSoup(open('index.html'), 'lxml')
    # BeautifulSoup会将HTML转化成文档树进行搜索
    # --------------------------------------------------------------------
    # 子节点
    # .contents可以将子节点以列表的形式输出
    print(soup.head.contents)
    # .children属性返回的是一个生成器，可以对tag的子节点进行循环
    for child in soup.head.children:
        print(child)
    # .contents和.children仅包含Tag的直接子节点
    # .descendants可以对Tag的子孙节点进行递归循环
    for child in soup.head.descendants:
        print(child)
    # 获取子节点内容.string, .strings, stripped_strings
    # stripped_strings可以去掉输出字符串中包含的空格或空行
    for string in soup.stripped_strings:
        print(repr(string))
    # ---------------------------------------------------------------------
    # 父节点: .parent, .parents
    print(soup.title.parent)
    # ----------------------------------------------------------------------
    # 兄弟节点，.next_sibling, .previous_sibling, .next_siblings, .previous_siblings
    print('-----------------------------------------------------------------')
    print(soup.p.next_sibling)
    print(soup.p.previous_sibling)
    print(soup.p.next_sibling.next_sibling)
    # ------------------------------------------------------------------------
    # 前后节点
    # .next_element, .previous_element, .next_elements, .previous_elements
    # 前后节点不区分层次
    for element in soup.a.next_elements:
        print(repr(element))
