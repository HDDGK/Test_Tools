from IETwindow import ImageEditToolWindow
from ImageEdit import ImageEdit
import jieba,os,wordcloud,sys,tkinter,numpy as np,qdarkstyle,tkinter as tk
from PIL import Image
from imageio import imread
from tkinter import filedialog, messagebox
from PyQt5.QtCore import Qt
from PyQt5.Qt import QSize, QImageReader
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QApplication,
                             QPushButton, QLabel, QFileDialog, QVBoxLayout,
                             QLineEdit, QComboBox)
from PyQt5 import QtCore, QtGui, QtWidgets
class menu(ImageEditToolWindow):
    def setInfoImageEditTab(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "修图工具"))
        self.loadImageLabel.setText(_translate("MainWindow", "图片加载区域"))
        self.showImageLabel.setText(_translate("MainWindow", "修改展示区域"))

        self.ImageChoicepushButton.setText(_translate("MainWindow", "选择图片"))
        self.ImageChoicepushButton.clicked.connect(self.loadImage)

        self.ImageFixpushButton.setText(_translate("MainWindow", "展示效果"))
        self.ImageFixpushButton.clicked.connect(self.showImage)


        self.RecoverButton.setText(_translate("MainWindow", "无效按钮"))
        self.RecoverButton.clicked.connect(self.Recover)


        self.WorkLonelyButton.setText(_translate("MainWindow", "单文件模式"))
        self.WorkLonelyButton.setChecked(True)
        self.WorkTogtherButton.setText(_translate("MainWindow", "文件夹模式"))
        self.choosePicStyleCombo.addItem("极致色彩")
        self.choosePicStyleCombo.addItem("漫画风格")
        self.choosePicStyleCombo.addItem("图案填充")

        self.listPicCombo.currentIndexChanged.connect(self.comboChoose)
        # 控件信息标注
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "图片效果编辑"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "图片文字填充"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "图片类型转换"))
        return _translate
    def Recover(self):
        self.result.setText("")
        self.listPicCombo.clear()
    def comboChoose(self):
        if self.listPicCombo.currentText()!="" and self.listPicCombo.currentText() is not None:
            self.result.setText(self.listPicCombo.currentText())
            ime = ImageEdit()
            ime.imageLabelWidth = int((self.screenX - 50) / 2)
            ime.imageLabelHeight = int((self.screenY - 150))
            if self.result.text()!="" or self.result.text() is not None :
                ime.ImageFileAddress=self.result.text()
                pixmap = ime.loadImage()
                self.loadImageLabel.setPixmap(pixmap)
    def loadImage(self):
        #独立出选择文件的操作，提取图片编辑类，并新增相同方法。调用方法获取图片的路径和pixmap
        ime=ImageEdit()
        ime.imageLabelWidth=int((self.screenX - 50) / 2)
        ime.imageLabelHeight=int((self.screenY - 150) )
        if self.WorkLonelyButton.isChecked():
            ime.ImageFileAddress, _ = QFileDialog.getOpenFileName(None, 'Open File', 'c://', "Image files (*.jpg *.png *jpeg)")
            if ime.ImageFileAddress is not None and ime.ImageFileAddress != "":
                # fname != "" 避免点击后不选择的空值导致上一次选择的图片被刷
                # 还需要对图片进行重新调整大小
                pixmap=ime.loadImage()
                self.loadImageLabel.setPixmap(pixmap)
                self.listPicCombo.addItem(ime.ImageFileAddress)
                self.result.setText(ime.ImageFileAddress)
        if self.WorkTogtherButton.isChecked():
            print("选择多文件模式")
            if self.listPicCombo.currentText()=="" or self.listPicCombo.currentText() is None :
                print("列表空啦")
                # name=QFileDialog.getOpenFileNames(None, 'Open File', 'c://', "Image files (*.jpg *.png *jpeg)")
                root = tk.Tk()
                root.withdraw()
                filedir=filedialog.askdirectory(title="选择需要转换的文件")
                if filedir is not None and filedir != "":
                    name=os.listdir(filedir)
                    imgs=ImageEdit()
                    for i in name:
                        if imgs.CheckImage(i):
                            print(i)
                            self.listPicCombo.addItem(os.path.join(filedir,i))
                            print("+")
                    print("?")
                    #尝试去重
                    # for i in range(self.listPicCombo.count()):
                    #     if self.listPicCombo.itemText(i-1)=="":
                    #         print()
                    #         self.listPicCombo.removeItem(i-1)
                    #     else:
                    self.result.setText(self.listPicCombo.currentText())
                    self.loadImage()
                    ime.ImageFileAddress = self.result.text()
                    pixmap = ime.loadImage()
                    self.loadImageLabel.setPixmap(pixmap)
                    self.listPicCombo.addItem(ime.ImageFileSaveAddress)
            else:
                print("列表有啦")
                ime.ImageFileAddress = self.result.text()
                pixmap = ime.loadImage()
                self.loadImageLabel.setPixmap(pixmap)
                self.listPicCombo.addItem(ime.ImageFileSaveAddress)


    def showImage(self):
        fixImageFilePath=self.result.text()
        choostyle=self.choosePicStyleCombo.currentText()
        if fixImageFilePath is not None and fixImageFilePath != "":
            imes = ImageEdit()
            imes.imageLabelWidth = int((self.screenX - 50) / 2)
            imes.imageLabelHeight = int((self.screenY - 150))
            imes.ImageFileAddress=fixImageFilePath
            imes.EStyleMenu(choostyle)
            self.listPicCombo.addItem(imes.ImageFileSaveAddress)
            # 下方独立处理，仅展示处理后图片，不处理图片
            fix_img = QImageReader(imes.ImageFileSaveAddress)

            # 针对图片的长宽问题，选择合适的最大边作为比例展示全幅画面
            if fix_img.size().height() > fix_img.size().width():
                scale = imes.imageLabelHeight / fix_img.size().height()
                Width = int(fix_img.size().width() * scale)
                fix_img.setScaledSize(QSize(Width, imes.imageLabelHeight))
            else:
                scale = imes.imageLabelWidth/ fix_img.size().width()
                height = int(fix_img.size().height() * scale)
                fix_img.setScaledSize(QSize(imes.imageLabelWidth, height))

            fix_img = fix_img.read()

            # 打开设置好的图片
            pixmap = QPixmap(fix_img)
            self.showImageLabel.setPixmap(pixmap)
        else:
            self.loadImage()

if __name__ == '__main__':
    print("??")
    app = QtWidgets.QApplication([])
    ex = QtWidgets.QMainWindow()
    ui=menu()
    # ui=ImageEditToolWindow()
    ui.setupUi(ex)
    ex.show()
    sys.exit(app.exec_())