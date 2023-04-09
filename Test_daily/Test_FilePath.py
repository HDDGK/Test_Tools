import os
print(os.name)
print(os.linesep+"fff")

print("获取当前的工作路径"+os.getcwd())
print("mkdir尝试创建一级目录，尝试创建多级时会报错...FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'C:\\Users\\HK145-TP\\Desktop\\Test2\\Test\\BGM'\n")

path="C:\\Users\\HK145-TP\\Desktop\\Test"
path2="C:\\Users\\HK145-TP\\Desktop\\Test2\\Test\\BGM"
path3="C:\\Users\\HK145-TP\\Desktop\\Test2"
if not os.path.exists(path):
    os.mkdir(path)
    print("目录创建成功\n")
else:
    print("当前路径已有该文件夹\n")

print("\nmakedirs尝试创建多级目录...")
if not os.path.exists(path2):
    os.makedirs(path2)
    print("多级目录创建成功\n")
else:
    print("当前路径已有该文件夹\n")

print("尝试遍历目录")
for root,dirs,files in os.walk(path3,topdown=True):#遍历指定目录
    #这里不太理解三个参数是怎么识别的，需要看一下这个方法的定义
    #如果是指定的空文件夹，好像是不会输出内容
    for name in dirs:
        print("TT",os.path.join(root,name))
    for name in files:
        print("&",os.path.join(root,name))

print("删除空文件夹的方式：os.rmdir(path)")
os.rmdir(path)
print("创建的一级文件夹已删除")
os.rmdir(path2)
print("创建的多级文件夹已删除最里面的文件夹\n")

#这里定义一个时间转化的方式
def formatTime (longtime):
    '''格式化日期时间函数展示
        lontime，输入的要修改展示格式的时间
    '''
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))
def formatByte(number):
    '''
    格式化文件展示大小
    :param number: 文件大小字节数
    :return:
    '''

#字节大小格式展示，我没理解，暂时不手操一遍



fileInfo=os.stat("C:\\Users\\HK145-TP\\Desktop\\Test2\\new.txt")
print("索引号",(fileInfo.st_ino))
print("设备名",(fileInfo.st_dev))
print("文件大小",fileInfo.st_size,"Byte")
print("最后访问时间",formatTime(fileInfo.st_atime),"Time")
print("最后修改时间",formatTime(fileInfo.st_mtime),"Time")
print("最后状态变化时间",formatTime(fileInfo.st_ctime),"Time")


