# Queue用来在多个进程间实现通信
from multiprocessing import Process
from multiprocessing import Queue
import os
import time
import random


def proc_write(q, urls):
    print('Process(%s) is writing...' % os.getpid())
    for url in urls:
        # Put方法用以插入数据到队列中，两个可选参数：blocked和timeout。
        # 如果blocked 为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。
        # 如果超时，会抛出Queue.Full异常。如果blocked为False,但该 Queue已满，会立即抛出Queue.Full异常。
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())


def proc_read(q):
    print('Process(%s) is reading...' % os.getpid())

    while True:
        # Get方法可以从队列读取并且删除一个元素。同样，Get方法有两个可选参数：blocked和timeout。
        # 如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。
        # 如果blocked为False, 分两种情况：如果Queue 有 一个值可用， 则立即返回该值；否则，如果队列为空， 则立即抛出 Queue.Empty异常。
        url = q.get(True)
        print('Get %s from queue.' % url)


if __name__ == '__main__':
    # 父进程创建Queue，并传递给各个子进程
    q_test = Queue()
    proc_writer1 = Process(target=proc_write, args=(q_test, ['url_1', 'url_2', 'url_3']))
    proc_writer2 = Process(target=proc_write, args=(q_test, ['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read, args=(q_test,))
    # 启动子进程
    proc_writer1.start()
    proc_writer2.start()
    proc_reader.start()
    # 等待proc_writer结束
    proc_writer1.join()
    proc_writer2.join()
    # 强行终止proc_reader
    proc_reader.terminate()
