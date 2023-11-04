from IETwindow import ImageEditToolWindow
from ImageEdit import ImageEdit
import jieba,os,wordcloud,sys,tkinter,numpy as np,qdarkstyle
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
        self.loadImageLabel.setText(_translate("MainWindow", "加载图片"))
        self.showImageLabel.setText(_translate("MainWindow", "展示图片"))
        self.ImageChoicepushButton.setText(_translate("MainWindow", "选择图片"))
        self.ImageChoicepushButton.clicked.connect(self.loadImage)
        # CPicBtn.clicked.connect(self.load_image)
        self.ImageFixpushButton.setText(_translate("MainWindow", "展示效果"))
        self.pushButton_3.setText(_translate("MainWindow", "无效按钮"))
        self.choosePicStyleCombo.addItem("极致色彩")
        self.choosePicStyleCombo.addItem("漫画风格")
        self.choosePicStyleCombo.addItem("图案填充")
        # 控件信息标注
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "图片效果编辑"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "图片文字填充"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "图片类型转换"))
        return _translate

    def loadImage(self):
        #独立出选择文件的操作，提取图片编辑类，并新增相同方法。调用方法获取图片的路径和pixmap
        ime=ImageEdit()
        fname,pixmap=ime.loadImage(self.screenX,self.screenY)
        self.listPicCombo.addItem(fname)
        self.loadImageLabel.setPixmap(pixmap)
        self.result.setText(fname)
    # def showImage(self):


if __name__ == '__main__':
    print("??")
    app = QtWidgets.QApplication([])
    ex = QtWidgets.QMainWindow()
    ui=menu()
    # ui=ImageEditToolWindow()
    ui.setupUi(ex)
    ex.show()
    sys.exit(app.exec_())