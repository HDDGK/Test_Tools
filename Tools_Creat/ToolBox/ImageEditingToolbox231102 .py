from IETwindow import ImageEditToolWindow
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
        self.pushButton_2.setText(_translate("MainWindow", "选择文件"))
        # self.pushButton_2.clicked.connect(self.show)
        # CPicBtn.clicked.connect(self.load_image)
        self.pushButton.setText(_translate("MainWindow", "处理文件"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.choosePicStyleCombo.addItem("极致色彩")
        self.choosePicStyleCombo.addItem("漫画风格")
        self.choosePicStyleCombo.addItem("图案填充")
        # 控件信息标注
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "图片效果编辑"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "图片文字填充"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "图片类型转换"))
        return _translate




if __name__ == '__main__':
    print("??")
    app = QtWidgets.QApplication([])
    ex = QtWidgets.QMainWindow()
    # ui=menu()
    ui=ImageEditToolWindow
    ui.setupUi(ex)
    ex.show()
    sys.exit(app.exec_())