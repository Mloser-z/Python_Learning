# encoding utf-8
import socket


# 初始化Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接目标的IP和端口
addr = ('10.133.166.39', 9999)
s.connect(addr)
# 接收消息
print("----->>"+s.recv(1024).decode('utf-8'))
# 发送消息
s.send(b'Hello, I am client.')
print("----->>"+s.recv(1024).decode('utf-8'))
s.send(b'exit')
# 关闭Socket
s.close()
