import socket
s=socket.socket()
host='127.0.0.1'
port=8080
s.connect((host,port))
send_data=input("请输入请求原因")
s.send(send_data.encode())
recvData=s.recv(1024).decode()
print('接受到的数据：',recvData)
s.close()