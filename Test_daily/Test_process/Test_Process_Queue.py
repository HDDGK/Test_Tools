from multiprocessing import Queue
if __name__=='__main__':
    q=Queue(3)
    q.put('消息1')
    q.put('消息2')
    print(q.full())
    q.put('消息3')
    print(q.full())
    try:
        q.put("消息4",True,2)
    except:
        print("已满：%s"%q.qsize())
    try:
        q.put_nowait("消息4")
    except:
        print("已满：%s"%q.qsize())
    if not q.empty():
        print("-----从队列获取信息------------")
        for i in range(q.qsize()):
            print(q.get_nowait())
    if not q.full():
        q.put_nowait("消息4")