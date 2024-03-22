import multiprocessing


counter = 111
def process_task(args):
    # 这里是你要在进程中执行的任务
    #print(f"处理进程开始，参数1: {arg1}, 参数2: {arg2}, 参数3: {arg3}")
    # 假设这里有一些计算或者处理
    #result = arg1 + arg2 + arg3
    print(args[0], args[1], args[2], args[3])

if __name__ == "__main__":
    # 创建一个进程池
    pool = multiprocessing.Pool(processes=4)
    
    # 这里是你要传递给进程的任务参数
    args_list = [
        (counter, 1, 2, 3),
        (counter, 4, 5, 6),
        (counter, 7, 8, 9),
        (counter, 10, 11, 12)
    ]
    
    # 使用map方法将参数和函数映射，创建多个进程执行任务
    pool.map(process_task, args_list)
    
    # 关闭进程池并等待所有进程完成
    pool.close()
    pool.join()


    print(counter)
