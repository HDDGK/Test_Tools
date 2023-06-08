import socket
host=socket.gethostname()
port=12345
so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.bind((host,port))
so.listen()
sock,addr=so.accept()
print("已建立链接")
info=sock.recv(1024).decode()
while info !='Quit':
    if info:
        print("接受到的内容"+info)
    send_data=input("输入发送内容")
    sock.send(send_data.encode())
    if send_data=='Quit':
        break
    info=sock.recv(1024).decode()
sock.close()
so.close()