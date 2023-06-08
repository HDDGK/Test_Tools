import multiprocessing
from multiprocessing import Process
import time
import os

class sub_process(Process):
    def __init__(self,interval,name=""):
    # def __init__(self,interval):
        Process.__init__(self)
        self.interval=interval
        if name:
            self.name=name
    def run(self):
        print("子进程(%s)开始执行，父进程为(%s)"%(os.getpid(),os.getppid()))
        t_start=time.time()
        time.sleep(self.interval)
        t_stop=time.time()
        print("子进程(%s)执行结束，执行时间(%0.2f)"%(os.getpid(),t_stop-t_start))


def printInfo(process):
    print(process.is_alive)
    print(process.name)
    print(process.pid)


if __name__=="__main__":
    print("父进程开始执行")
    print("父进程PID：(%s)"%os.getpid())
    p1=sub_process(interval=1,name='mi')
    p2=sub_process(interval=2)
    p1.start()
    p2.start()
    printInfo(p1)
    printInfo(p2)
    print("mi%s"%p1.name)
    print("等待子进程进程")
    p1.join()
    print("子进程1")
    p2.join()
    print("子进程2")
    print("父进程已结束")


print("这里一定要注意，导入的大小写问题，导入不对的话，乱七八糟的错误")

