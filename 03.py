# -*- coding:utf-8 -*-
# @Time   : 2023-07-01
# @Author : Carl_DJ
import time

from sys import argv
import multiprocessing

from HData_eastmoney_day import *

hdata=HData_eastmoney_day("usr","usr")

import datetime as datetime

nowdate=datetime.datetime.now().date()
nowdate=nowdate-datetime.timedelta(1)
print("nowdate is %s"%(nowdate.strftime("%Y-%m-%d")))

nowdate_df = hdata.get_data_from_hdata(\
        start_date=nowdate.strftime("%Y-%m-%d"), \
        end_date=nowdate.strftime("%Y-%m-%d")\
        )


data_list = np.array(nowdate_df)
data_list = data_list.tolist()


g_counter = 0

def worker(name):
    print("Worker %s started" % (name))
    return name


if __name__ == '__main__':

    t1 = time.time()
    mplist = []
    filename , processes, number = argv
    with multiprocessing.Pool(int(processes)) as pool:
        #pool.map(worker, range(int(number)))
        mplist.append(
            pool.map(worker, data_list))

    print("************************************************************************************")
    print(mplist)
    t2 = time.time()
    print("t2-t1=%s"%(t2-t1))
    print('g_counter=%d' % (g_counter))


#https://blog.csdn.net/achitc/article/details/118379686
# Python多进程处理方法（Pool、apply_async、map_async）


#https://blog.csdn.net/2301_80240808/article/details/134387521
#性能爆炸！Python多进程模式实现多核CPU并行计算
