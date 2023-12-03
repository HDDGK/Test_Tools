from PyQt5.Qt import QSize, QImageReader
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QApplication,
                             QPushButton, QLabel, QFileDialog, QVBoxLayout,QDesktopWidget,
                             QLineEdit, QComboBox)
from PyQt5 import QtCore, QtGui, QtWidgets
from Panel_ImageEdit import PanelImageEdit
from PyQt5.QtWidgets import QMenuBar, QMenu, QAction
from Panel_MenuBar import CustomMenuBar
from Function_StyleController import StyleController
from PyQt5.QtCore import QTime,QTimer

class MainInterfacePanel(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("工具箱")

        # 获取设备本地显示的分辨率【非最大化时，也尽量保持满屏幕】
        screen_resolution = QDesktopWidget().screenGeometry()
        screen_width = screen_resolution.width()
        screen_height = screen_resolution.height()
        MainWindow.resize(screen_width,screen_height)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)

        # 创建自定义菜单栏并设置为 MainWindow 的菜单栏
        custom_menubar = CustomMenuBar(MainWindow, MainWindow)
        MainWindow.setMenuBar(custom_menubar)

        # 创建 StyleController 实例以根据时间自动更新样式
        # self.style_controller = StyleController(MainWindow, custom_menubar)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.ImageEditTab = QtWidgets.QWidget()
        self.ImageEditTab.setObjectName("ImageEditTab")

        self.ImageTabLayout = QtWidgets.QVBoxLayout(self.ImageEditTab)
        self.ImageTabLayout.setObjectName("ImageTabLayout")

        self.tabScrollArea = QtWidgets.QScrollArea(self.ImageEditTab)
        self.tabScrollArea.setWidgetResizable(True)
        self.tabScrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 572))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # 实例化 PanelImageEdit 并将其添加到 scrollAreaWidgetContents 中
        image_edit = PanelImageEdit()
        scrollAreaLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        scrollAreaLayout.addWidget(image_edit)
        self.scrollAreaWidgetContents.setLayout(scrollAreaLayout)

        # 将 scrollAreaWidgetContents 添加到 tabScrollArea 中
        self.tabScrollArea.setWidget(self.scrollAreaWidgetContents)
        # 将 tabScrollArea 添加到 ImageTabLayout 中
        self.ImageTabLayout.addWidget(self.tabScrollArea)

        self.tabWidget.addTab(self.ImageEditTab, "图片模式编辑")
        self.tabWidget.addTab(QtWidgets.QWidget(), "待定")
        self.mainLayout.addWidget(self.tabWidget)


    def update_style_based_on_time(self, MainWindow, custom_menubar):
        current_time = QTime.currentTime()

        if QTime(20, 0) <= current_time < QTime(22, 0):
            custom_menubar.set_medium_eye_protection_mode(MainWindow)
        elif QTime(22, 0) <= current_time < QTime(24, 0) or QTime(0, 0) <= current_time < QTime(6, 0):
            custom_menubar.set_strong_eye_protection_mode(MainWindow)
        elif QTime(6, 0) <= current_time < QTime(7, 0):
            custom_menubar.set_medium_eye_protection_mode(MainWindow)
        elif QTime(7, 0) <= current_time < QTime(8, 0):
            custom_menubar.set_light_eye_protection_mode(MainWindow)
        elif QTime(8, 0) <= current_time < QTime(9, 0):
            custom_menubar.set_day_mode(MainWindow)
        elif QTime(18, 0) <= current_time < QTime(20, 0):
            custom_menubar.set_light_eye_protection_mode(MainWindow)
        else:
            custom_menubar.set_day_mode(MainWindow)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    ui = MainInterfacePanel()
    ui.setupUi(window)
    window.showMaximized()
    app.exec_()