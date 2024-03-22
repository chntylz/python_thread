# -*- coding:utf-8 -*-
# @Time   : 2023-07-01
# @Author : Carl_DJ
import time

from sys import argv
import multiprocessing

g_counter = 10

def worker(name):
    print("Worker %s started" % (name))


if __name__ == '__main__':

    t1 = time.time()
    filename , processes, number = argv
    with multiprocessing.Pool(int(processes)) as pool:
        pool.map(worker, range(int(number)))

    '''
    with multiprocessing.Pool(int(processes)) as pool:
        for i in range(int(number)):
            pool.map(worker, str(i))
    '''
    t2 = time.time()
    print("t2-t1=%s"%(t2-t1))
    print('g_counter=%d' % (g_counter))


#https://blog.csdn.net/achitc/article/details/118379686
# Python多进程处理方法（Pool、apply_async、map_async）


#https://blog.csdn.net/2301_80240808/article/details/134387521
#性能爆炸！Python多进程模式实现多核CPU并行计算
