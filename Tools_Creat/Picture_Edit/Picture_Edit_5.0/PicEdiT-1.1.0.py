# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PE2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import jieba,os,wordcloud,sys,tkinter,numpy as np,qdarkstyle
from PIL import Image
from imageio import imread
from tkinter import filedialog, messagebox
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.Qt import QSize, QImageReader
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QApplication,
                             QPushButton, QLabel, QFileDialog, QVBoxLayout,
                             QLineEdit, QComboBox)
'''
https://vimsky.com/examples/detail/python-method-qdarkstyle.load_stylesheet_pyqt5.html
https://vimsky.com/
'''


def info():
    '''
    【1.1.0】：产品设计
    增加功能：
    1、【新功能支持】:支持图片类型转换，针对文件夹转换，支持转换类型选择，方便选择特定文件
    2、【操作便捷优化】:支持cobolist列表展示选择文件夹下的图片，并针对选择的图片进行展示，图片处理
    3、【代码复用优化】:看是否可以优化整体的代码流程，优化类的方法，便于调用和理解
    4、【界面调整优化】：参考书上规范调用界面，考虑是否需要展示多界面，还是利用控件完成多界面的切换
    :return:
    '''

class mainwindow(QMainWindow):

    def __init__(self):
        super(mainwindow, self).__init__()

        layout = QVBoxLayout()
        w = QWidget()
        w.setLayout(layout)
        imageLabelWidth = int((mainwindow.screen(self).size().width() - 50) / 2)
        imageLabelHeight = int((mainwindow.screen(self).size().height() - 150))
        mainwindow.resize(self, mainwindow.screen(self).size())  # 设置屏幕为设备最大画面

        mainwindow.showMaximized(self)  # 最大化展示
        # self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)  # 禁止最小化

        img_layout = QHBoxLayout()
        self.setCentralWidget(w)

        self.image_label = QLabel()  # 展示选择图片的label
        self.image_label.setFixedSize(imageLabelWidth, imageLabelHeight)  # 设置label大小
        self.image_label.setAlignment(Qt.AlignCenter)  # 图片居中展示
        self.image_label.setStyleSheet("border: 2px solid black;")

        self.Fiximage_label = QLabel()  # 展示处理图片的label
        self.Fiximage_label.setFixedSize(imageLabelWidth, imageLabelHeight)  # 设置label大小
        self.Fiximage_label.setAlignment(Qt.AlignCenter)  # 图片居中展示
        self.Fiximage_label.setStyleSheet("border: 2px solid black;")

        img_layout.addWidget(self.image_label)
        img_layout.addWidget(self.Fiximage_label)
        layout.addLayout(img_layout)

        tmp_layout = QHBoxLayout()  # 增加布局类型，横向布局

        # 增加选择图片的按钮
        CPicBtn = QPushButton("选择图片路径")
        tmp_layout.addWidget(CPicBtn)
        CPicBtn.clicked.connect(self.load_image)  # 按钮关联动作

        # 增加处理图片的按钮：本次默认一种图片处理方法
        FPicBtn = QPushButton("处理图片")
        tmp_layout.addWidget(FPicBtn)
        FPicBtn.clicked.connect(self.show_image)  # 按钮关联动作

        # 增加处理图片的按钮：本次增加两个选择项
        self.stylecomboBox = QComboBox()
        self.stylecomboBox.setObjectName("styleBox")
        tmp_layout.addWidget(self.stylecomboBox)
        self.stylecomboBox.addItem("极致色彩")
        self.stylecomboBox.addItem("漫画风格")
        self.stylecomboBox.addItem("图案填充")

        # 增加文本展示条
        self.result = QLineEdit()
        self.result.setPlaceholderText("车牌展示")
        self.result.setReadOnly(True)
        tmp_layout.addWidget(self.result)
        layout.addLayout(tmp_layout)

        # 导入背景色样式，
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BG"))
        self.menuddd.setTitle(_translate("MainWindow", "主菜单"))
        self.menuPictureTool.setTitle(_translate("MainWindow", "PictureTool"))
        self.actionPicStyleChange.setText(_translate("MainWindow", "PicStyleChange"))
        self.actionPicConvertFormat.setText(_translate("MainWindow", "PicConvertFormat"))
        self.actionFilledText.setText(_translate("MainWindow", "PicFilledText"))

    def show_image(self):
        '''
        https://blog.csdn.net/daimashiren/article/details/106080827?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-106080827-blog-127706764.235%5Ev38%5Epc_relevant_sort_base3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-106080827-blog-127706764.235%5Ev38%5Epc_relevant_sort_base3&utm_relevant_index=6
        PIL 转 Qixmap
        :return:

        https://www.codeleading.com/article/34462366185/

        '''
        imageLabelWidth = int((mainwindow.screen(self).size().width() - 50) / 2)
        imageLabelHeight = int((mainwindow.screen(self).size().height() - 150))
        fname = self.result.text()
        # 获取comobox当前值
        chooseStyle = self.stylecomboBox.currentText()

        if fname is not None and fname != "":
            pc = PictureChange()
            pc.picturepath = fname
            if os.path.exists(pc.pictureSavePath(chooseStyle)):
                print("本地有哦！")
            else:
                if chooseStyle == "极致色彩":

                    im = pc.Pic_HeavyColor()
                    pc.pictureSavePath(chooseStyle)
                    pc.CheckPath(chooseStyle)
                    im.save(pc.pictureSavePath(chooseStyle))

                elif chooseStyle == "漫画风格":
                    pc = PictureChange()
                    pc.picturepath = fname
                    im = pc.Pic_HandDraw()
                    pc.pictureSavePath(chooseStyle)
                    pc.CheckPath(chooseStyle)
                    im.save(pc.pictureSavePath(chooseStyle))
            if chooseStyle == "图案填充":
                pc=PictureFillCloud_word()
                pc.picturepath=fname
                pc.CheckPath("图案填充")
                pc.run()
            # 下方独立处理，仅展示处理后图片，不处理图片

            fix_img = QImageReader(pc.pictureSavePath(chooseStyle))

            # 针对图片的长宽问题，选择合适的最大边作为比例展示全幅画面
            if fix_img.size().height() > fix_img.size().width():
                scale = imageLabelHeight / fix_img.size().height()
                Width = int(fix_img.size().width() * scale)
                fix_img.setScaledSize(QSize(Width, imageLabelHeight))
            else:
                scale = imageLabelWidth / fix_img.size().width()
                height = int(fix_img.size().height() * scale)
                fix_img.setScaledSize(QSize(imageLabelWidth, height))

            fix_img = fix_img.read()

            # 打开设置好的图片
            pixmap = QPixmap(fix_img)
            self.Fiximage_label.setPixmap(pixmap)
        else:
            self.load_image()

    def load_image(self):
        imageLabelWidth = int((mainwindow.screen(self).size().width() - 50) / 2)
        imageLabelHeight = int((mainwindow.screen(self).size().height() - 150))
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', 'c://', "Image files (*.jpg *.png *jpeg)")
        if fname is not None and fname != "":
            # fname != "" 避免点击后不选择的空值导致上一次选择的图片被刷

            # 还需要对图片进行重新调整大小
            img = QImageReader(fname)  # 通过传入选择的图片路径，读取图片

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
            self.image_label.setPixmap(pixmap)
            self.result.setText(fname)

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

        #下面是因为传入的地址参数变化，目前传入的就是savepath，调用之前的原地址代码，会在基础上创建两个
        # if not os.path.exists(file_path + '\\' + Cpath):
        #     os.makedirs(file_path + '\\' + Cpath)
        #     print(file_path + '\\' + Cpath)
        if not os.path.exists(file_path ):
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
    cloud_world=""
    # savePath = ""
    # pathList = []
    def run(self):
        self.get_TxtFilePath()
        if self.txt_path != "":
            self.get_Txt()
            print("文本获取成功")
            self.get_MianWord()
            if self.get_MianWord()=="":
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
        main_txt=open(self.txt_path,'r',encoding="utf-8").read()
        main_txt=''.join([i.strip(' ') for i in main_txt])
        for ch in '~！@#￥%……&*（）!@#$%^&*()_+——+-=:;\'；‘：",<，《。》.>?/？、【】、{}|[]\\123456789  ':
            main_txt =main_txt.replace(ch,' ')
        self.cloud_world=main_txt

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
            Folder_PNG_Path=self.picturepath
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
if __name__ == '__main__':
    app = QApplication([])
    font = QFont()
    font.setFamily("SimHei")
    font.setPointSize(14)
    app.setFont(font)
    m = mainwindow()
    m.show()
    sys.exit(app.exec())
