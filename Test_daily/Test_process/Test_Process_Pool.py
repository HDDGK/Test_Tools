from multiprocessing import Pool,Process
import os,time
def plus():
    print('-----------子进程1开始---------------')
    global g_num
    print(g_num)
    g_num += 50
    print('g_sum is %d'%g_num)
    print('-----------子进程1结束---------------')
def minus():
    print('-----------子进程2开始---------------')
    global g_num
    print(g_num)
    g_num -= 50
    print('g_sum is %d'%g_num)
    print('-----------子进程2结束---------------')




def task(name):
    print("子进程(%s)执行task：%s"%(os.getpid(),name))
    time.sleep(1)

g_num=100

if __name__=='__main__':
    print("父进程(%s)"%os.getpid())
    p1=Pool(3)
    for i in range(10):
        p1.apply_async(task,args=(i,))
    print('等待所以子进程结束')
    p1.close()
    p1.join()
    print('所有子进程结束')

    print("--------------新的主进程开始--------------")
    print('g_sum is %d' % g_num)

    p2=Process(target=plus())
    p3=Process(target=minus())
    p3.start()


    p2.start()
    p2.join()
    p3.join()
    print("--------------新的主进程结束--------------")
    print("笑死了，和书上不一样，全局值被改了,怎么同时运行呢？")
