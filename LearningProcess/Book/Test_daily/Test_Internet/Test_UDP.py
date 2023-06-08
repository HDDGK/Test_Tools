import  socket
soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soc.bind(('127.0.0.1',8888))
print("绑定UDP到8888端口")
data,addr=soc.recvfrom(1024)
data=float(data)*1.8+32
send_data="转换后的温度："+str(data)
print('received from%s:%s'%addr)
soc.sendto(send_data.encode(),addr)
soc.close()