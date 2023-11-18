import os
import tkinter
from tkinter import filedialog

import numpy as np
from PIL import Image
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImageReader, QPixmap
from imageio import imread


class ImageEx():

    def __init__(self):
        self.cloud_world = None
        self.txt_path = None

        self.ImageFileAddress = None
        self.ImageFileSaveAddress = None
        self.ImageFileAddressList = None
        self.imageLabelWidth = None
        self.imageLabelHeight = None

    def CheckImage(self, path):
        try:
            file_path, file_name = os.path.split(path)
            name, type = os.path.splitext(file_name)
            print(name, type)
            if type in (".jpg", ".png", ".jpeg"):
                return True
        except:
            print("出错了")
            return False

    def CheckPath(self):
        print("check")
        # 这里是对传入的文件的地址，单个处理
        fileDirPath = os.path.abspath(self.ImageFileSaveAddress)
        file_path, file_name = os.path.split(fileDirPath)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

    def ImageSavePathSet(self, styleName):
        fileDirPath = os.path.abspath(self.ImageFileAddress)
        file_path, file_name = os.path.split(fileDirPath)
        changePath = os.path.abspath(file_path) + "\\" + str(styleName) + "\\" + file_name
        self.ImageFileSaveAddress = changePath
        self.CheckPath()  # 先创建看看，后面不在单独check了
        return changePath

    def loadImage(self):
        img = QImageReader(self.ImageFileAddress)  # 通过传入选择的图片路径，读取图片

        # 针对图片的长宽问题，选择合适的最大边作为比例展示全幅画面
        if img.size().height() > img.size().width():
            scale = self.imageLabelHeight / img.size().height()
            Width = int(img.size().width() * scale)
            img.setScaledSize(QSize(Width, self.imageLabelHeight))
        else:
            scale = self.imageLabelWidth / img.size().width()
            height = int(img.size().height() * scale)
            img.setScaledSize(QSize(self.imageLabelWidth, height))

        img = img.read()
        # 打开设置好的图片
        pixmap = QPixmap(img)
        return pixmap

    def Pic_Shape(self):

        # from scipy.misc import imread
        if self.ImageFileAddress is None and self.ImageFileAddress == "":
            print("本地没有文件")
            tkinter.messagebox.showinfo("选择", "选择一个形状图片")
            Folder_PNG_Path = filedialog.askopenfilename(title="选择一个形状PNG图片",
                                                         filetypes=[('png', "*.png")])
        else:
            Folder_PNG_Path = self.ImageFileAddress
        mask = imread(Folder_PNG_Path, pilmode='L')
        return mask