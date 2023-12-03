from PyQt5.Qt import QSize, QImageReader
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QApplication,
                             QPushButton, QLabel, QFileDialog, QVBoxLayout,QDesktopWidget,
                             QLineEdit, QComboBox)
from PyQt5 import QtCore, QtGui, QtWidgets
from Panel_ImageEdit import PanelImageEdit
from PyQt5.QtWidgets import QMenuBar, QMenu, QAction
from  Function_StyleController import StyleController

class CustomMenuBar(QMenuBar):
    def __init__(self, main_window, style_controller, parent=None):
        super().__init__(parent)

        self.main_window = main_window
        self.style_controller = style_controller


        # 创建操作菜单
        menu = QMenu("设置", self)
        self.addMenu(menu)
        # 添加最大化操作
        maximize_action = QAction("最大化显示", self)
        maximize_action.triggered.connect(self.main_window.showMaximized)
        menu.addAction(maximize_action)

        # 添加全屏操作
        fullscreen_action = QAction("全屏显示", self)
        fullscreen_action.triggered.connect(lambda: self.main_window.showFullScreen() if not self.main_window.isFullScreen() else self.main_window.showNormal())
        menu.addAction(fullscreen_action)

        # 添加退出操作
        exit_action = QAction("退出程序", self)
        exit_action.triggered.connect(self.main_window.close)
        menu.addAction(exit_action)

        # 创建样式子菜单
        style_menu = QMenu("界面样式", self)
        self.addMenu(style_menu)

        # 添加夜间模式操作
        night_mode_action = QAction("夜间模式", self)
        night_mode_action.triggered.connect(lambda: self.set_night_mode(self.main_window))
        style_menu.addAction(night_mode_action)

        # 添加白天模式操作
        day_mode_action = QAction("白天模式", self)
        day_mode_action.triggered.connect(lambda: self.set_day_mode(self.main_window))
        style_menu.addAction(day_mode_action)

        # 添加轻度护眼模式操作
        light_eye_protection_mode_action = QAction("轻度护眼模式", self)
        light_eye_protection_mode_action.triggered.connect(lambda: self.set_light_eye_protection_mode(self.main_window))
        style_menu.addAction(light_eye_protection_mode_action)

        # 添加中度护眼模式操作
        medium_eye_protection_mode_action = QAction("中度护眼模式", self)
        medium_eye_protection_mode_action.triggered.connect(lambda: self.set_medium_eye_protection_mode(self.main_window))
        style_menu.addAction(medium_eye_protection_mode_action)

        # 添加重度护眼模式操作
        strong_eye_protection_mode_action = QAction("重度护眼模式", self)
        strong_eye_protection_mode_action.triggered.connect(lambda: self.set_strong_eye_protection_mode(self.main_window))
        style_menu.addAction(strong_eye_protection_mode_action)


        #在每个样式切换操作的槽函数中，将 style_controller.auto_update 设置为 False
        night_mode_action.triggered.connect(
            lambda: (self.set_night_mode(self.main_window), setattr(self.style_controller, "auto_update", False)))
        day_mode_action.triggered.connect(
            lambda: (self.set_day_mode(self.main_window), setattr(self.style_controller, "auto_update", False)))
        light_eye_protection_mode_action.triggered.connect(lambda: (
        self.set_light_eye_protection_mode(self.main_window), setattr(self.style_controller, "auto_update", False)))
        medium_eye_protection_mode_action.triggered.connect(lambda: (
        self.set_medium_eye_protection_mode(self.main_window), setattr(self.style_controller, "auto_update", False)))
        strong_eye_protection_mode_action.triggered.connect(lambda: (
        self.set_strong_eye_protection_mode(self.main_window), setattr(self.style_controller, "auto_update", False)))

    def set_night_mode(self, MainWindow):
        night_style = """
            QWidget {
                background-color: #333;
                color: #CCC;
            }
            QMenuBar::item:selected {
                background-color: #555;
            }
            QTabBar::tab {
                background-color: #444;
                color: #CCC;
                border: 1px solid #555;
            }
            QTabBar::tab:selected {
                background-color: #555;
                color: #CCC;
                border: 1px solid #666;
            }
        """
        MainWindow.setStyleSheet(night_style)

    def set_day_mode(self, MainWindow):
        MainWindow.setStyleSheet("")

    def set_light_eye_protection_mode(self, MainWindow):
        light_eye_protection_style = """
            QWidget {
                background-color: #E6E6E6;
                color: #000;
            }
            QTabBar::tab {
                background-color: #D1D1D1;
                color: #000;
            }
            QTabBar::tab:selected {
                background-color: #BFBFBF;
                color: #000;
            }
        """
        MainWindow.setStyleSheet(light_eye_protection_style)

    def set_medium_eye_protection_mode(self, MainWindow):
        medium_eye_protection_style = """
            QWidget {
                background-color: #D1D1D1;
                color: #000;
            }
            QTabBar::tab {
                background-color: #BFBFBF;
                color: #000;
            }
            QTabBar::tab:selected {
                background-color: #A8A8A8;
                color: #000;
            }
        """
        MainWindow.setStyleSheet(medium_eye_protection_style)

    def set_strong_eye_protection_mode(self, MainWindow):
        strong_eye_protection_style = """
            QWidget {
                background-color: #BFBFBF;
                color: #000;
            }
            QTabBar::tab {
                background-color: #A8A8A8;
                color: #000;
            }
            QTabBar::tab:selected {
                background-color: #909090;
                color: #000;
            }
        """
        MainWindow.setStyleSheet(strong_eye_protection_style)