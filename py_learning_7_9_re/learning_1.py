import re

# 将正则表达式编译成pattern对象
pattern = re.compile(r'\d+')
# re.match（pattern, string[,flags])
# 方法匹配字符串，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern, '192abc')
if result1:
    print(result1.group())
else:
    print('False')

result2 = re.match(pattern, 'abc192')
if result2:
    print(result2.group())
else:
    print('False')

# re.search方法与match极其相似，区别在于match方法只从字符串的开始位置匹配，search方法会扫描整个string匹配
# search不只是从开头匹配,两者都返回一个子串
result3 = re.search(pattern, 'abc19e2')
if result3:
    print(result3.group())  # 输出19
else:
    print('False')

# re.split(pattern, string[, maxsplit])
# 按照能够匹配到的子串将string分割后返回列表，maxsplit用于指定最大分割次数，不指定时将全部分割
print(re.split(pattern, 'A1B2C3D4'))

# re.findall(pattern, string[, flags])
# 能够搜索整个string，以列表的形式返回能够匹配的全部子串
print(re.findall(pattern, 'A1B2C3D4'))

# re.finditer(pattern, string[, flags])
# 搜索整个string，以迭代器形式返回能够匹配的全部Match对象
matchiter = re.finditer(pattern, 'A1B2C3D4')
for match in matchiter:
    print(match.group())

# re.sub(pattern, repl, string[, count])
# 使用repl替换string中每一个匹配的子串后返回替换后的字符串
p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')     # 使用名称引用
s = 'i say, hello world!'
print(p.sub(r'\g<word2> \g<word1>', s))
p = re.compile(r'(\w+) (\w+)')      # 使用编号
print(p.sub(r'\2 \1', s))


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print(p.sub(func, s))

# re.subn(pattern, repl, string[, count])
# 返回(sub(repl, string[, count]), 替换次数)
print(p.subn(r'\2 \1', s))
print(p.subn(func, s))
