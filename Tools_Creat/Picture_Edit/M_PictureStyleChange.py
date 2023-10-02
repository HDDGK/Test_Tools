from Picture_Edit_Style import  Pic_HeavyColor,Pic_HandDraw
from PictureChoose import choose_Dir,CheckPath
from PictureEdit_Menu import mainMenu

'''
功能：只调用图片处理函数，以及调用保存
返回值：无返回值
'''
def main():
    mainList = ['图片处理', '极致色彩', '手绘风格', '功能选项']
    while True:
        mainMenu(mainList)
        choice = int(input("请选择："))
        if choice in range(0, 8):
            if choice == 0:
                answer = input('您确定是要退出系统吗？【Y/y】')
                if answer == 'y' or answer == 'Y':
                    print("感谢使用！！！")
                    break
                else:
                    continue
            elif choice == 1:
                getChoosefilelist = choose_Dir('png', 'jpg')
                for filePath in getChoosefilelist:  # 这里是循环选择的文件的地址，单个处理
                    sp = CheckPath(filePath)  # 检查文件路径是否存在，不存在则新建
                    Pic_HeavyColor(filePath, sp)
            elif choice == 2:
                getChoosefilelist = choose_Dir('png', 'jpg')
                for filePath in getChoosefilelist:  # 这里是循环选择的文件的地址，单个处理
                    sp = CheckPath(filePath)  # 检查文件路径是否存在，不存在则新建
                    Pic_HeavyColor(filePath, sp)
                    Pic_HandDraw(filePath, sp)

if __name__ == '__main__':
    main()




