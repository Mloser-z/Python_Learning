# 二进制文件操作
import pickle

with open('learning_txt.txt', 'w') as ft:
    s = "This is a learning example for file.\nThis is second line.\nThis is third line."
    ft.write(s)

with open('learning.dat', 'wb') as fw, open('learning_txt.txt', 'r') as ft:
    for line in ft:
        pickle.dump(line, fw)

with open('learning.dat', 'rb') as fw:
    while True:
        try:
            print(pickle.load(fw))
        except:
            break
