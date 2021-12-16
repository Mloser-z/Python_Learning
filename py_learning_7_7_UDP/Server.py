# coding utf-8
# Server端创建需要三个步骤：
# 1）创建Socket，绑定指定的IP和端口
# 2）直接发送数据和接收数据
# 3)关闭Socket

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('10.133.166.39', 9999))
print('Bind UDP on 9999...')
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
