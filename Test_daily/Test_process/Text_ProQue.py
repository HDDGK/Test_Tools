from multiprocessing import Process,Queue
import time

def write_task(q):
    if not q.full():
        for i in range(5):
            message="消息"+str(i)
            q.put(message)
            print("写入%s"%message)
def read_task(q):
    time.sleep(1)
    while not q.empty():
        print("读取：%s"%q.get(True,2))

if __name__=='__main__':
    print("---父进程---")
    q=Queue()
    pw=Process(target=write_task,args=(q,))
    pr=Process(target=read_task(q))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print('父进程结束')