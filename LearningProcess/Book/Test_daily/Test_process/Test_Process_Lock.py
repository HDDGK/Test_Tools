from threading import Thread,Lock
import time
n=100
def task():
    global n
    mutex.acquire()
    temp=n
    time.sleep(1)
    n=temp-1
    print("抢票成功，剩余%d张票"%n)
    mutex.release()


if __name__=='__main__':
    mutex=Lock()
    t_I=[]
    for i in range(50):
        t=Thread(target=task)
        t_I.append(t)
        t.start()
    for t in t_I:
        t.join