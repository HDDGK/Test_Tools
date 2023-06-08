import time,threading
def process():
    for i in range(3):
        time.sleep(1)
        print("线程名称%s"%threading.current_thread().name)
if __name__=='__main__':
    print("主进程开始")
    threads=[threading.Thread(target=process)for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("主进程结束")
