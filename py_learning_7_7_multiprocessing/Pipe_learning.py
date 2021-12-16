# Pipe常用来在两个进程间进行通信，两个进程分别位于管道的两端。
# Pipe方法返回(conn1, conn2)代表一个管道的两个端。
# Pipe方法有duplex参数，如果 duplex参数为True（默认值），那么这个管道是全双工模式，也就是说conn1和conn2均可收发。
# 若duplex为False, conn1只负责 接收消息，conn2只负责发送消息。
# send和recv方法分别是发送和接收消息的方法。例如，在全双工模式下，可以调用conn1.send发送消息， conn1.recv 接收消息。
# 如果没有消息可接收，recv方法会一直阻塞。如果管道已经被关闭，那么recv方法会抛出EOFError。

import multiprocessing
import random
import time
import os


def proc_send(pipe, urls):
    for url in urls:
        print("Process(%dS) send: %s" % (os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe):
    while True:
        print("Process(%s) rev: %s" % (os.getpid(), pipe.recv()))
        time.sleep(random.random())


if __name__ == '__main__':
    pipe_test = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc_send, args=(pipe_test[0], ['url_'+str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_recv, args=(pipe_test[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
