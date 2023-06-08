from MyQR import myqr


def Tool_pictureQR():
    myqr.run(words="http://www.baidu.com",
             picture=r"C:\Users\HK145-TP\Desktop\新建文件夹\五角星.png",
             colorized=True,
             save_name="二维码.png",
             save_dir=r"C:\Users\HK145-TP\Desktop\新建文件夹")


Tool_pictureQR()


def Tool_GifQR():
    myqr.run(words="http://www.baidu.com",
             picture=r"C:\Users\HK145-TP\Desktop\新建文件夹\Gif.gif",
             colorized=True,
             save_name="二维码.gif",
             save_dir=r"C:\Users\HK145-TP\Desktop\新建文件夹")


Tool_GifQR()
print("?")