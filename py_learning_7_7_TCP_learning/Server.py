# coding:utf-8
# 服务端创建一般需要五个步骤：
# 1）创建Socket，绑定Socket到本地IP与端口
# 2）开始监听连接
# 3）进入循环，不断接受客户端的连接请求
# 4）接收传来的数据，并不断发送给对方数据
# 5）传输完毕后，关闭Socket
import socket
import threading
import time


def deal_client(sock, addr):
    # 第四步：接收传来的数据，并发送给对方数据
    print("Accept new connection from %s:%s..." % addr)
    sock.send(b"Hello, I am server!")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print("----->>%s" % data.decode('utf-8'))
        sock.send(('Loop_Msg: %s!' % data.decode('utf-8')).encode('utf-8'))
    # 第五步：关闭Socket
    sock.close()
    print("Connection from %s:%s closed." % addr)


if __name__ == '__main__':
    # 第一步：创建一个基于IPv4和TCP协议的Socket
    # Socket绑定IP(本机IP)与端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('10.133.166.39', 9999))
    # 第二步：监听连接
    s.listen(5)
    print("Waiting for connection...")
    while True:
        # 第三步：接收一个新的连接
        new_socket, address = s.accept()
        # 创建一个新线程来处理TCP连接
        t = threading.Thread(target=deal_client, args=(new_socket, address))
        t.start()
