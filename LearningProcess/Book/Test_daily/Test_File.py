
file=open(r"C:\Users\HK145-TP\Desktop\new1.txt",'w')
#注意\n的存在，需要指明地址,当文件不存在时，报错FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\HK145-TP\\Desktop\\new1.txt'
print("如果文件不存在，则报错\n"
      "FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\HK145-TP\\Desktop\\new1.txt'\n"
      "或者加上参数w w+ ...")
print("文件已找到，打开中...\n")
file.close()
#打开文件，往里面塞东西

file2=open(r"C:\Users\HK145-TP\Desktop\new.txt",'w',encoding="utf-8")
print("\n这里是print输出，\n"
      "1、打开文件时，不同模式之间的区别，比如rb、rb+等二进制方式打开后，不支持设置编码参数\n"
      "2、如果文档不是默认的GBK，打开会报错，需要在open指定：encoding=\"utf-8\"\n")



file2.write("我想在文档里写点东西1234,\n这里是写进了文档里【覆盖原内容】，\n"
      "1、打开文件时，不同模式之间的区别，比如rb、rb+等二进制方式打开后，不支持设置编码参数\n"
      "2、如果文档不是默认的GBK，打开会报错，需要在open指定：encoding=\"utf-8\"\n")

file2=open(r"C:\Users\HK145-TP\Desktop\new.txt",'r',encoding="utf-8")
print(file2.read())
file2.close()

for i in range(2):
    file3 = open(r"C:\Users\HK145-TP\Desktop\new1.txt", 'a', encoding="utf-8")
    file3.write("我\n")
    file3.write("我这句\n")
    file3.write("我这句和上面两句\n")
    file3.write("我这句和上面两句，都是\n")
    file3.write("我这句和上面两句，都是插入的\n")
    file3.write("我这句和上面两句，都是插入的，跟在屁股后面\n")
    file3.write("这里是第"+str(i+1)+"次写完文件并关闭，之前的有保留\n")
    file3.close()

#未关闭就是空的
file3=open(r"C:\Users\HK145-TP\Desktop\new1.txt",'r',encoding="utf-8")
print(file3.read())

print("这里需要搞清楚一点，W模式下，只要系统文件关闭，再次打开时，就会清理掉之前的记录，但是a模式下，即使文件关闭，后续还是可以续写\n"
      "且w和a，两种方式在，文件未关闭时，是可以一直接着后面写的，不会覆盖。")
for i in range(2):
    file3 = open(r"C:\Users\HK145-TP\Desktop\new2.txt", 'w', encoding="utf-8")
    file3.write("我\n")
    file3.write("我这句\n")
    file3.write("我这句和上面两句\n")
    file3.write("我这句和上面两句，都是\n")
    file3.write("我这句和上面两句，都是插入的\n")
    file3.write("我这句和上面两句，都是插入的，跟在屁股后面\n")
    file3.write("这里是第" + str(i+1) + "次写完文件并关闭，之前的好像覆盖了\n")
    file3.close()

#未关闭就是空的
file4=open(r"C:\Users\HK145-TP\Desktop\new2.txt",'r',encoding="utf-8")
print(file4.read())


#下面是读取文件的方式
#读取指定字符
file5=open(r"C:\Users\HK145-TP\Desktop\new2.txt",'r',encoding="utf-8")
txtStr=file5.read(1)
print(txtStr)
print("上面是默认从读取开头取对应字符")
print("下面是从指定位置取字符")
file5.seek(22)#插入到这个位置
txtSeekStr=file5.read(1)
print(txtSeekStr)

#这里是通过循环读取line，把所有的内容读取
with open(r"C:\Users\HK145-TP\Desktop\new2.txt",'r',encoding="utf-8")as file6:
    number=0
    while True:
        number+=1
        line=file6.readline()
        if line=="":
            break
        print(number,line,end="")

#这里是通过一次读取的方法直接获取所以行组成的字符串列表
print("\n下面是一次读取的line的列表")
with open(r"C:\Users\HK145-TP\Desktop\new2.txt",'r',encoding="utf-8")as file7:
    message=file7.readlines()
    print(message)
print("逐个打印出来")
for mess in message:
    print(mess)