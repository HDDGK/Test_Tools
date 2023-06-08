import os
import time
from multiprocessing import Process
def child_1(interval):
    print("子线程执行，父进程为",os.getpid(),os.getppid())
    t_startTime=time.time()
    time.sleep(interval)
    t_endTime=time.time()
    print("子进程执行时间为，",(os.getpid(),t_endTime-t_startTime))
def child_2(interval):
    print("子线程执行，父进程为",(os.getpid(),os.getppid()))
    t_startTime=time.time()
    time.sleep(interval)
    t_endTime=time.time()
    print("子进程执行时间为，",(os.getpid(),t_endTime-t_startTime))


if __name__=='__main__':
    print("主进程开始")
    print("父进程为",os.getpid())
    p1 = Process(target=child_1, args=(1,))
    p2 = Process(target=child_2, name="mrsoft",args=(1,))
    p1.start()
    p2.start()
    print("子进程1是在运行【%s"%p1.is_alive(),"]")
    print("子进程1名称【%s"%p1.name)
    print("子进程1进程名【%s"%p1.pid)
    print("子进程2是在运行【%s"%p2.is_alive())
    print("子进程2名称【%s"%p2.name)
    print("str属性，如果带了（），就会提示TypeError: 'str' object is not callable")
    print("子进程2进程名【%s"%p2.pid)
    print("属性，如果带了（），就会提示TypeError: 'int' object is not callable")
    print("——————等待子进程——————")
    p1.join()
    p2.join()
    print("————父进程结束————")
