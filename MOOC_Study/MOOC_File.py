
'''
print("路径可以绝对路径和相对路径，目的是为了找到文件")
r:只读，默认，不在报错
w:覆盖写，无则创建，有则完全覆盖
x:创建写，无则创建，存在就报错
a:追加写，无则创建，存在则在后面追加
b:二进制文件模式
t:文本文件模式，默认值
+:与r w a 一起使用，增加读写
'''

f=open("f.txt")#文本，只读，默认
f=open("f.txt","rt")#文本，只读，默认
f=open("f.txt","w")#文本，覆盖写
f=open("f.txt","a+")#文本，追加写+读
f=open("f.txt","x")#文本，创建写
f=open("f.txt","b")#二进制，只读
f=open("f.txt","wb")#二进制，覆盖写

'''
.read(size)
.readline()读一行
.readlines()读所有行
'''
fname=input("名称：")
fo=open(fname,"r")
for line in fo.readlines():
    print(line)
fo.write("ddd")
fo.writelines(["中国","美国","日志"])
fo.seek(0)#012,开头，当前，结尾
#注意指针位置
fo.close()