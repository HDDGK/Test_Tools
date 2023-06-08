import time,threading

class sub_thread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg="子进程"+self.name+'执行，i='+str(i)
            print(msg)
if __name__=='__main__':
    print('主进程开始')
    t1=sub_thread()
    t2=sub_thread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主线程结束')