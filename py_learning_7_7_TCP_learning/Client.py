# encoding utf-8
# 客户端创建一般是三个步骤：
# 创建Socket，连接远端地址
# 连接后发送数据和接收数据
# 传输完毕后关闭Socket
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
