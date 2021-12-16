from multiprocessing import Pool
import os
import time
import random


def run_task(name):
    print('Task %s (pid = %s) is running...' % (name, os.getpid()))     # getpid()方法获取当前进程的ID
    time.sleep(random.random() * 3)
    print('Task %s end.' % name)


if __name__ == '__main__':
    print("Current process %s." % os.getpid())

    # 创建进程池对象
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()

    # join()方法实现进程间同步
    p.join()
    print('All subprocess done.')
