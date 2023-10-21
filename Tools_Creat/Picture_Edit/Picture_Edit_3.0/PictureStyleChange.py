from tkinter import filedialog
import numpy as np
from PIL import Image
import os
str_k = "-" * 12
changeDir = "处理后图片"

class PictureChange:
    path=""
    savePath=""
    pathList=[]
    #这里用类的方式，给类传固定的地址，然后通过类自己的方法，返回不同地址值下的不同图片数据，

    def pictureSavePath(self,Change_text):
        print(str_k, "拼凑保存文件夹路径【开始】", str_k)
        fileDirPath = os.path.abspath(self.path)
        print("1"+fileDirPath)
        file_path, file_name = os.path.split(fileDirPath)
        print("2"+file_path)
        print("3"+file_name)

        changePath = os.path.abspath(file_path) + "\\" + str(Change_text) + "\\" + file_name
        self.savePath=changePath
        print(str_k, "拼凑保存文件夹路径【完成】", str_k)
        return changePath

    def CheckPath(self):
        # 这里是对传入的文件的地址，单个处理
        fileDirPath = os.path.abspath(self.savePath)
        file_path, file_name = os.path.split(fileDirPath)
        sp = self.pictureSavePath(changeDir)
        if not os.path.exists(file_path + '\\' + changeDir):
            os.makedirs(file_path + '\\' + changeDir)
        return sp

    def Pic_HeavyColor(self):
        # im = np.array(Image.open(picture_Address).convert('L'))
        # 灰度值
        # print(str_k,"处理图片【开始】",str_k)
        im = np.array(Image.open(self.path).convert("RGB"))
        im2 = Image.fromarray(im.astype('uint8'))
        GM = 255 * (im / 255) ** 2
        im2 = Image.fromarray(GM.astype('uint8'))
        print(str_k, "处理图片【结束】", str_k)
        # print(str_k,"保存文件夹【开始】",str_k)
        im2.save(self.savePath)
        print(str_k, "保存文件夹【结束】", str_k)

    def Pic_HandDraw(self):
        # print(str_k,"处理图片【开始】",str_k)
        a = np.asarray(Image.open(self.path).convert('L')).astype('float')

        depth = 20
        grad = np.gradient(a)
        grad_x, grad_y = grad
        grad_x = grad_x * depth / 100
        grad_y = grad_y * depth / 100
        A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
        uni_x = grad_x / A
        uni_y = grad_y / A
        uni_z = 1. / A

        vec_el = np.pi / 2.2
        vec_az = np.pi / 4.
        dx = np.cos(vec_el) * np.cos(vec_az)
        dy = np.cos(vec_el) * np.sin(vec_az)
        dz = np.sin(vec_el)

        b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
        b = b.clip(0.255)
        im = Image.fromarray(b.astype('uint8'))
        print(str_k, "处理图片【结束】", str_k)
        # print(str_k, "保存文件夹【开始】", str_k)
        im.save(self.savePath)
        print(str_k, "保存文件夹【结束】", str_k)


class PictureChoose:
    def choose_Dir(*types):
        '''
        弹窗选择文件夹
        获取内部文件列表
        :return:文件夹下的JPG/PNG的格式列表
        '''
        Choose_file_path = []
        Choose_file_path_list = []

        # fileList=filedialog.askopenfilename
        print("-" * 12, "获取文件【开始】", "-" * 12)
        choose_FileDir = filedialog.askdirectory()
        # choose_FileDir 获取选择的文件夹路径

        file_All_List = os.listdir(choose_FileDir)
        for file in file_All_List:
            for type in types:
                if type == file.split('.')[-1]:
                    Choose_file_path = choose_FileDir + '/' + file
                    Choose_file_path_list.append(Choose_file_path)
        # file_All_List 获取选择的文件夹下的图片列表
        print("-" * 12, "获取文件【结束】", "-" * 12)
        # show(Choose_file_path_list)
        return Choose_file_path_list




if __name__ == '__main__':
    # pco=PictureChoose()
    # path=pco.choose_Dir("png",'jpg')
    cp = PictureChange()
    path=r"C:\Users\HK145-TP\Desktop\选择\90892d94921f86f42f7d97314ae214f.jpg"
    cp.path=path
    cp.pictureSavePath("SS")
    cp.Pic_HandDraw()