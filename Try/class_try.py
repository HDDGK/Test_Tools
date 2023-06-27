def main():
    pass

class pictur_Edit:
    def __int__(self,orignAddress,saveAddress,Pictype):
        self.OrignAddress=orignAddress
        self.SaveAddress=saveAddress
        self.Pictype=Pictype

    def info(self):
        print(self.OrignAddress)
        print(self.SaveAddress)
        print(self.Pictype)


    def show(self,txt):
        print("show{}".format(txt))

if __name__ == '__main__':
    main()
    ori=r"C:\Users\HK145-TP\Desktop\新建文件夹 (2)\0b7e35c96247d98d8f6c6382bf80a831.jpg"
    sav=r"C:\Users\HK145-TP\Desktop\新建文件夹 (2)\新建文件夹 (2)\0b7e35c96247d98d8f6c6382bf80a831.jpg"
    pce=pictur_Edit(ori,sav,'png')

    print(pce.info())