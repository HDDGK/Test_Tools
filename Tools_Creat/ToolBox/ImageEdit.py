from tkinter import filedialog, messagebox

import jieba
import numpy as np
import os
import tkinter
import wordcloud
from PIL import Image
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImageReader, QPixmap
from PyQt5.QtWidgets import QFileDialog
from imageio import imread


class ImageEdit():
    ImageFileAddress = ""
    ImageFileAddressLisr = []

    def loadImage(self, screenX, screenY):
        imageLabelWidth = int((screenX - 50) / 2)
        imageLabelHeight = int((screenY - 150))
        ImageFileAddress, _ = QFileDialog.getOpenFileName(None, 'Open File', 'c://', "Image files (*.jpg *.png *jpeg)")
        # self.loadImageLabel.setText("?")
        if ImageFileAddress is not None and ImageFileAddress != "":
            # fname != "" 避免点击后不选择的空值导致上一次选择的图片被刷

            # 还需要对图片进行重新调整大小
            img = QImageReader(ImageFileAddress)  # 通过传入选择的图片路径，读取图片

            # 针对图片的长宽问题，选择合适的最大边作为比例展示全幅画面
            if img.size().height() > img.size().width():
                scale = imageLabelHeight / img.size().height()
                Width = int(img.size().width() * scale)
                img.setScaledSize(QSize(Width, imageLabelHeight))
            else:
                scale = imageLabelWidth / img.size().width()
                height = int(img.size().height() * scale)
                img.setScaledSize(QSize(imageLabelWidth, height))

            img = img.read()
            # 打开设置好的图片
            pixmap = QPixmap(img)
            return ImageFileAddress, pixmap


class PicEdit():
    picturepath = ""
    savePath = ""
    pathList = []

    def pictureSavePath(self, Change_text):
        fileDirPath = os.path.abspath(self.picturepath)
        file_path, file_name = os.path.split(fileDirPath)

        changePath = os.path.abspath(file_path) + "\\" + str(Change_text) + "\\" + file_name
        self.savePath = changePath
        return changePath

    def CheckPath(self, Cpath):
        # 这里是对传入的文件的地址，单个处理
        fileDirPath = os.path.abspath(self.savePath)
        file_path, file_name = os.path.split(fileDirPath)
        sp = self.pictureSavePath(Cpath)

        # 下面是因为传入的地址参数变化，目前传入的就是savepath，调用之前的原地址代码，会在基础上创建两个
        # if not os.path.exists(file_path + '\\' + Cpath):
        #     os.makedirs(file_path + '\\' + Cpath)
        #     print(file_path + '\\' + Cpath)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        return sp


class PictureChange(PicEdit):
    def Pic_HeavyColor(self):
        # im = np.array(Image.open(picture_Address).convert('L'))
        # 灰度值
        # print(str_k,"处理图片【开始】",str_k)
        im = np.array(Image.open(self.picturepath).convert("RGB"))
        im2 = Image.fromarray(im.astype('uint8'))
        GM = 255 * (im / 255) ** 2
        im2 = Image.fromarray(GM.astype('uint8'))
        print("-" * 12, "处理图片【结束】", "-" * 12)
        return im2

    def Pic_HandDraw(self):
        # print(str_k,"处理图片【开始】",str_k)
        a = np.asarray(Image.open(self.picturepath).convert('L')).astype('float')

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
        print("-" * 12, "处理图片【结束】", "-" * 12)
        return im


class PictureFillCloud_word(PicEdit):
    txt_path = ""
    cloud_world = ""

    # savePath = ""
    # pathList = []
    def run(self):
        self.get_TxtFilePath()
        if self.txt_path != "":
            self.get_Txt()
            print("文本获取成功")
            self.get_MianWord()
            if self.get_MianWord() == "":
                print("关键字获取失败，空")
            else:
                print("关键字获取成功", self.get_MianWord())
            if self.get_MianWord() != "":
                self.get_shape()
                print("形状获取成功")
                self.get_WordCloudPic()
                print("获取成功")

            else:
                print("选择的文件地址：", self.txt_path)
        else:
            print("选择的文件地址：", self.txt_path)

    def get_TxtFilePath(self):
        try:
            tkinter.messagebox.showinfo("选择", "选择一个txt文本文件")
            # self.txt_path = filedialog.askopenfilename(filetypes=[('txt', "*.txt"), ('All Files', "*")])
            self.txt_path = filedialog.askopenfilename(filetypes=[('txt', "*.txt")])
        except:
            print("???,好好选一下txt文件")

    def get_Txt(self):
        main_txt = open(self.txt_path, 'r', encoding="utf-8").read()
        main_txt = ''.join([i.strip(' ') for i in main_txt])
        for ch in '~！@#￥%……&*（）!@#$%^&*()_+——+-=:;\'；‘：",<，《。》.>?/？、【】、{}|[]\\123456789  ':
            main_txt = main_txt.replace(ch, ' ')
        self.cloud_world = main_txt

    def get_MianWord(self):
        ls = jieba.lcut(self.cloud_world)
        for i in ls:
            if len(i) == 1:
                ls.remove(i)

        txt = " ".join(ls)
        return txt

    def get_shape(self):

        # from scipy.misc import imread
        if self.picturepath is None and self.picturepath == "":
            print("本地没有文件")
            tkinter.messagebox.showinfo("选择", "选择一个形状图片")
            Folder_PNG_Path = filedialog.askopenfilename(title="选择一个形状PNG图片",
                                                         filetypes=[('png', "*.png")])
        else:
            Folder_PNG_Path = self.picturepath
        mask = imread(Folder_PNG_Path, pilmode='L')
        return mask

    def get_WordCloudPic(self):
        shape = self.get_shape()
        wordcloud_paint = wordcloud.WordCloud(
            width=1920,
            height=1080,
            # max_font_size=18,
            # min_font_size=6,
            # font_step=2,
            max_words=40,
            mask=shape,
            stopwords={"三", "二", "一", "的", "以"},
            font_path="STCAIYUN.TTF",
            background_color="white"
        )
        wordcloud_paint.generate(self.get_MianWord())
        self.CheckPath("图案填充")
        wordcloud_paint.to_file(self.savePath)
