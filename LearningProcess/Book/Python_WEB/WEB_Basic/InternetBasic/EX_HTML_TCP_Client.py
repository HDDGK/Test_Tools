import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))
print("已连接")
info=''
while info!='bye':
    send_data=input("输入发送内容：")
    s.send(send_data.encode())
    if send_data=='bye':
        break
    info=s.recv(1024).decode()
    print('接收到的内容：'+info)
s.close()
