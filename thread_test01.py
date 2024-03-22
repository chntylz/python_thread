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

    t2 = time.time()
    print("t2-t1=%s"%(t2-t1))
    print('g_counter=%d' % (g_counter))

'''
def task(name):
        pass
        #print(f"Running task {name}")

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
    print('count is %d' % (count))

    print("All tasks completed")
    t2 = time.time()
    print("t2-t1=%s"%(t2-t1))

'''


#https://blog.csdn.net/achitc/article/details/118379686
# Python多进程处理方法（Pool、apply_async、map_async）


#https://blog.csdn.net/2301_80240808/article/details/134387521
#性能爆炸！Python多进程模式实现多核CPU并行计算

#https://blog.csdn.net/baidu_39413110/article/details/122368297
#python multiprocessing多进程处理dataframe，快得飞起~
