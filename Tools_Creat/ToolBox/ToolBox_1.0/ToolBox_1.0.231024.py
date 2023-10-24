# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout
# Form implementation generated from reading ui file 'ToolBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #主窗口命名
        MainWindow.setObjectName("MainWindow")

        screenX=MainWindow.screen().size().width()
        screenY=MainWindow.screen().size().height()

        # 获取屏幕长宽通过主窗口设置窗体大小为全屏
        MainWindow.resize(screenX,screenY)

        screenX = int(screenX)
        screenY = int(screenY - 75)
        compareImageLabelX = int((screenX - 50) / 2)
        compareImageLabelY = int(screenY - 150)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        #设置控件画面大小，设置为全屏
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, screenX,screenY))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        #Tab界面插入控件
        #先给Tab上个布局
        self.tab_1_verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.tab_1_verticalLayout.setObjectName("tab_1_verticalLayout")
        self.tab_1_horizontalLayout_1 = QtWidgets.QHBoxLayout(self.tab)
        self.tab_1_horizontalLayout_1.setObjectName("tab_1_horizontalLayout_1")

        #Tab中添加label，label放在横向布局中
        self.loadImageLabel = QtWidgets.QLabel(self.tab)
        self.loadImageLabel.setEnabled(True)
        self.loadImageLabel.setObjectName("loadImageLabel")
        self.tab_1_horizontalLayout_1.addWidget(self.loadImageLabel)
        self.showImageLabel = QtWidgets.QLabel(self.tab)
        self.showImageLabel.setEnabled(True)
        self.showImageLabel.setObjectName("showImageLabel")
        self.tab_1_horizontalLayout_1.addWidget(self.showImageLabel)
        self.tab_1_verticalLayout.addLayout(self.tab_1_horizontalLayout_1)

        #vtab布局中，新增布局横向，横向布局添加控件
        self.tab_1_horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.tab_1_horizontalLayout_2.setObjectName("tab_1_horizontalLayout_2")
        self.tab_1_verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.tab_1_verticalLayout_21.setObjectName("tab_1_verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tab_1_verticalLayout_21.addWidget(self.pushButton_2)


        self.choosePicCombo=QtWidgets.QComboBox(self.tab)
        self.choosePicCombo.setObjectName("choosePicCombo")
        self.tab_1_verticalLayout_21.addWidget(self.choosePicCombo)


        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.tab_1_verticalLayout_21.addWidget(self.pushButton)

        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tab_1_verticalLayout_21.addWidget(self.pushButton_3)
        #
        # self.showinfolabel = QtWidgets.QLabel(self.tab)
        # self.showinfolabel.setEnabled(True)
        # self.showinfolabel.setObjectName("showinfolabel")

        self.tab_1_horizontalLayout_2.addLayout(self.tab_1_verticalLayout_21)
        # self.tab_1_horizontalLayout_2.addWidget(self.showinfolabel)
        # self.tab_1_horizontalLayout_2.addWidget(self.showinfolabel)

        self.tab_1_verticalLayout.addLayout(self.tab_1_horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")


        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)


        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        # self.menubar.setObjectName("menubar")
        # self.menu = QtWidgets.QMenu(self.menubar)
        # self.menu.setObjectName("menu")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        # self.actionPicEdit = QtWidgets.QAction(MainWindow)
        # self.actionPicEdit.setObjectName("actionPicEdit")
        # self.actionPicShape = QtWidgets.QAction(MainWindow)
        # self.actionPicShape.setObjectName("actionPicShape")
        # self.menu.addAction(self.actionPicEdit)
        # self.menu.addAction(self.actionPicShape)
        # self.menubar.addAction(self.menu.menuAction())



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadImageLabel.setText(_translate("MainWindow", "加载图片"))
        self.showImageLabel.setText(_translate("MainWindow", "展示图片"))
        self.pushButton_2.setText(_translate("MainWindow", "选择文件"))
        self.pushButton.setText(_translate("MainWindow", "处理文件"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.choosePicCombo.addItem("极致色彩")
        self.choosePicCombo.addItem("漫画风格")
        self.choosePicCombo.addItem("图案填充")
        # 控件信息标注
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "图片效果编辑"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "图片文字填充"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "图片类型转换"))

        # menu控件信息标注
        # self.menu.setTitle(_translate("MainWindow", "菜单"))
        # self.actionPicEdit.setText(_translate("MainWindow", "PicEdit"))
        # self.actionPicShape.setText(_translate("MainWindow", "PicShape"))



if __name__ == '__main__':
    print("??")
    app = QtWidgets.QApplication([])
    ex = QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(ex)
    ex.show()
    sys.exit(app.exec_())