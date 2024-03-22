# -*- coding:utf-8 -*-
# @Time   : 2023-07-01
# @Author : Carl_DJ
import time

from sys import argv
import multiprocessing



def task(name):
    print("Worker %s started" % name)

if __name__ == "__main__":

    filename , processes, number = argv

    t1 = time.time()
    # 创建进程池，最大进程数为4
    pool = multiprocessing.Pool(int(processes))

    # 提交任务到进程池
    for i in range(int(number)):
        pool.apply_async(task, args=(i,))

    # 关闭进程池，不再接受新的任务
    pool.close()

    #待所有任务完成
    pool.join()

    t2 = time.time()
    print("t2-t1=%s"%(t2-t1))

