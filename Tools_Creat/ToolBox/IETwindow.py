import qdarkstyle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtCore,QtWidgets

class ImageEditToolWindow(object):
    screenX=""
    screenY=""
    def setupUi(self, MainWindow):
        '''
        拆分细节，避免继承调整需要全部重写
        :param MainWindow:
        :return:
        '''
        #主窗口命名
        MainWindow.setObjectName("MainWindow")

        self.screenX=MainWindow.screen().size().width()
        self.screenY=MainWindow.screen().size().height()

        # 获取屏幕长宽通过主窗口设置窗体大小为全屏
        MainWindow.resize(self.screenX,self.screenY)

        screenX = int(self.screenX)
        screenY = int(self.screenY - 125)
        compareImageLabelX = int((screenX - 50) / 2)
        compareImageLabelY = int(screenY - 150)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.creatTabWindow(screenX, screenY)

        MainWindow.setCentralWidget(self.centralwidget)

        self.creatMenuBar(MainWindow)

        MainWindow.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def creatMenuBar(self, MainWindow):
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPicEdit = QtWidgets.QAction(MainWindow)
        self.actionPicEdit.setObjectName("actionPicEdit")
        self.actionPicShape = QtWidgets.QAction(MainWindow)
        self.actionPicShape.setObjectName("actionPicShape")
        self.menu.addAction(self.actionPicEdit)
        self.menu.addAction(self.actionPicShape)
        self.menubar.addAction(self.menu.menuAction())

    def creatTabWindow(self, screenX, screenY):
        '''
        尝试提取出来界面中的tab页面，单独方法调用生成
        :param screenX:获取屏幕的XY，来自动适配最大的画面
        :param screenY:
        :return:
        '''
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        # 设置控件画面大小，设置为全屏
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, screenX, screenY))
        self.tabWidget.setObjectName("tabWidget")
        self.creatImageEditTab()
        self.creatImageFill()
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")

    def creatImageFill(self):
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

    def creatImageEditTab(self):
        '''
        针对提取pictureEditTab的布局，单独配置
        :return:
        '''
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        # Tab界面插入控件
        # 先给Tab上个布局
        self.tab_1_verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.tab_1_verticalLayout.setObjectName("tab_1_verticalLayout")
        self.tab_1_horizontalLayout_1 = QtWidgets.QHBoxLayout(self.tab)
        self.tab_1_horizontalLayout_1.setObjectName("tab_1_horizontalLayout_1")

        # Tab中添加label，label放在横向布局中
        self.loadImageLabel = QtWidgets.QLabel(self.tab)
        self.loadImageLabel.setEnabled(True)
        self.loadImageLabel.setObjectName("loadImageLabel")
        self.loadImageLabel.setStyleSheet("border: 2px solid black;")
        self.loadImageLabel.setAlignment(Qt.AlignCenter)  # 图片居中展示
        self.tab_1_horizontalLayout_1.addWidget(self.loadImageLabel)

        self.showImageLabel = QtWidgets.QLabel(self.tab)
        self.showImageLabel.setEnabled(True)
        self.showImageLabel.setObjectName("showImageLabel")
        self.showImageLabel.setStyleSheet("border: 2px solid black;")
        self.showImageLabel.setAlignment(Qt.AlignCenter)  # 图片居中展示
        self.tab_1_horizontalLayout_1.addWidget(self.showImageLabel)

        self.tab_1_verticalLayout.addLayout(self.tab_1_horizontalLayout_1)
        # vtab布局中，新增布局横向，横向布局添加控件
        self.tab_1_horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.tab_1_horizontalLayout_2.setObjectName("tab_1_horizontalLayout_2")
        # 试图增加第2个横向布局中添加左侧的横向布局，以支持左右二分，左侧内部butten又二分一，限制大小
        self.tab_1_horizontalLayout_21 = QtWidgets.QHBoxLayout(self.tab)
        # 左侧内部butten又二分一，限制大小
        self.tab_1_verticalLayout_2111 = QtWidgets.QVBoxLayout()
        self.tab_1_verticalLayout_2112 = QtWidgets.QVBoxLayout()

        self.tab_1_verticalLayout_2111.setObjectName("tab_1_verticalLayout_21")
        self.ImageChoicepushButton = QtWidgets.QPushButton(self.tab)
        self.ImageChoicepushButton.setObjectName("ImageChoicepushButton")
        self.tab_1_verticalLayout_2111.addWidget(self.ImageChoicepushButton)
        self.ImageFixpushButton = QtWidgets.QPushButton(self.tab)
        self.ImageFixpushButton.setObjectName("ImageFixpushButton")
        self.tab_1_verticalLayout_2111.addWidget(self.ImageFixpushButton)
        self.RecoverButton = QtWidgets.QPushButton(self.tab)
        self.RecoverButton.setObjectName("RecoverButton")
        self.tab_1_verticalLayout_2111.addWidget(self.RecoverButton)
        # 增加新布局，下方按钮界面的竖向布局,[其实可以忽略，保留做补充]
        self.tab_1_horizontalLayout_211 = QtWidgets.QHBoxLayout()
        self.tab_1_horizontalLayout_211.setObjectName("tab_1_verticalLayout_22")
        # 增加选择图片风格的选择框
        self.choosePicStyleCombo = QtWidgets.QComboBox(self.tab)
        self.choosePicStyleCombo.setObjectName("choosePicStyleCombo")
        self.WorkLonelyButton = QtWidgets.QRadioButton(self.tab)
        # self.radioButton.setGeometry(QtCore.QRect(180, 90, 89, 16))
        self.WorkLonelyButton.setObjectName("WorkLonelyButton")
        self.WorkTogtherButton = QtWidgets.QRadioButton(self.tab)
        # self.radioButton_2.setGeometry(QtCore.QRect(180, 110, 89, 16))
        self.WorkTogtherButton.setObjectName("WorkTogtherButton")
        self.tab_1_horizontalLayout_21121 = QtWidgets.QHBoxLayout(self.tab)

        self.tab_1_horizontalLayout_21121.addWidget(self.WorkLonelyButton)
        self.tab_1_horizontalLayout_21121.addWidget(self.WorkTogtherButton)
        self.tab_1_verticalLayout_2112.addLayout(self.tab_1_horizontalLayout_21121)
        self.tab_1_verticalLayout_2112.addWidget(self.choosePicStyleCombo)


        # 增加文本选择框展示
        self.result = QLineEdit()
        self.result.setPlaceholderText("信息展示")
        # 设置只读
        self.result.setReadOnly(True)
        # 增加文本选择框展示选择的文件夹下的图片列表
        self.listPicCombo = QtWidgets.QComboBox(self.tab)
        self.listPicCombo.setObjectName("listPicCombo")
        # TAB1界面布局

        self.tab_1_horizontalLayout_211.addLayout(self.tab_1_verticalLayout_2111)
        self.tab_1_horizontalLayout_211.addLayout(self.tab_1_verticalLayout_2112)

        self.tab_1_horizontalLayout_21.addLayout(self.tab_1_horizontalLayout_211)
        self.tab_1_horizontalLayout_21.addWidget(self.listPicCombo)
        self.tab_1_horizontalLayout_2.addLayout(self.tab_1_horizontalLayout_21)

        # 上下两个横向布局中间插入文本条
        self.tab_1_verticalLayout.addWidget(self.result)
        # 窗口布局加入横向第二个主要横向布局
        self.tab_1_verticalLayout.addLayout(self.tab_1_horizontalLayout_2)
        # 第一个tab页面设置完毕，添加
        self.tabWidget.addTab(self.tab, "")

    def setInfoImageEditTab(self, MainWindow):
        '''
        提取针对pictureEditTab界面的初始化
        https://blog.51cto.com/techfanyi/6540034
        :param MainWindow:
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "修图工具"))
        self.loadImageLabel.setText(_translate("MainWindow", "图片加载区域"))
        self.showImageLabel.setText(_translate("MainWindow", "修改展示区域"))

        self.ImageChoicepushButton.setText(_translate("MainWindow", "选择图片"))

        self.ImageFixpushButton.setText(_translate("MainWindow", "展示效果"))


        self.RecoverButton.setText(_translate("MainWindow", "无效按钮"))
        self.WorkLonelyButton.setText(_translate("MainWindow", "单文件模式"))
        self.WorkLonelyButton.setChecked(True)
        self.WorkTogtherButton.setText(_translate("MainWindow", "文件夹模式"))
        self.choosePicStyleCombo.addItem("极致色彩")
        self.choosePicStyleCombo.addItem("漫画风格")
        self.choosePicStyleCombo.addItem("图案填充")
        # 控件信息标注
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "图片效果编辑"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "图片文字填充"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "图片类型转换"))

        return _translate

    def retranslateUi(self, MainWindow):
        _translate = self.setInfoImageEditTab(MainWindow)
        # menu控件信息标注
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionPicEdit.setText(_translate("MainWindow", "PicEdit"))
        self.actionPicShape.setText(_translate("MainWindow", "PicShape"))