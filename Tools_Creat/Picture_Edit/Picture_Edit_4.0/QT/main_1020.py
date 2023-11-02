# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PE2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys, time
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QApplication,
                             QPushButton, QLabel, QFileDialog, QVBoxLayout,
                             QLineEdit)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.Qt import QSize, QImageReader
import qdarkstyle
from PyQt5 import QtCore

'''
https://vimsky.com/examples/detail/python-method-qdarkstyle.load_stylesheet_pyqt5.html
https://vimsky.com/

20:
1、增加高分辨率图片的展示，适配
2、针对较长边的展示优化，保证全幅画面展示
'''
imageLabelWidth=500
imageLabelHeight=500
class mainwindow(QMainWindow):


    def __init__(self):
        super(mainwindow, self).__init__()

        layout = QHBoxLayout()
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.image_label = QLabel()
        self.image_label.setFixedSize(imageLabelWidth, imageLabelHeight)
        self.Fiximage_label = QLabel()
        self.Fiximage_label.setFixedSize(imageLabelWidth, imageLabelHeight)
        layout.addWidget(self.image_label)
        layout.addWidget(self.Fiximage_label)

        tmp_layout = QVBoxLayout()
        btn = QPushButton("选择图片路径")
        tmp_layout.addWidget(btn)
        btn.clicked.connect(self.load_image)

        self.result = QLineEdit()
        self.result.setPlaceholderText("车牌展示")
        self.result.setReadOnly(True)
        tmp_layout.addWidget(self.result)
        layout.addLayout(tmp_layout)

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def load_image(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File','C://', "Image files (*.jpg *.png)")
        if fname is not None and fname != "":
            #fname != "" 避免点击后不选择的空值导致上一次选择的图片被刷新
            # print("fname:",fname)#检查选择的名称问题

            # 还需要对图片进行重新调整大小
            img = QImageReader(fname)#通过传入选择的图片路径，读取图片

            #针对图片的长宽问题，选择合适的最大边作为比例展示全幅画面
            if img.size().height()>img.size().width():
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


if __name__ == '__main__':
    app = QApplication([])
    font = QFont()
    font.setFamily("SimHei")
    font.setPointSize(14)
    app.setFont(font)
    m = mainwindow()
    m.show()
    sys.exit(app.exec())