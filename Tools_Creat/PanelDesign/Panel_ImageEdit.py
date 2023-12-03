import os

import qdarkstyle
from PyQt5.QtCore import Qt
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QDesktopWidget, QFileDialog, QSlider
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PIL import Image
import numpy as np
from PyQt5.QtGui import QTransform

class PanelImageEdit(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 初始化面板的 UI 和属性
        self.initUI()

    def initUI(self):
        # 在类中添加一个变量来存储原始 QPixmap 和累积的旋转角度
        self.original_pixmap = None
        self.rotation_angle = 0

        _translate = QtCore.QCoreApplication.translate
        # 在这里添加自定义面板的 UI 组件和设置
        main_layout = QVBoxLayout()
        main_layout.setObjectName("main_layout")
        # 设计3个横向布局，一个的顶部工具栏，一个是图片区，一个是按钮区
        Tool_Layout = QHBoxLayout()
        Tool_Layout.setObjectName("Tool_Layout")
        Image_Layout= QHBoxLayout()
        Image_Layout.setObjectName("Image_Layout")
        Button_Layout= QHBoxLayout()
        Button_Layout.setObjectName("Button_Layout")

        # 创建 loadImageLabel 和 showImageLabel 对象，并将它们添加为类属性,并添加到布局中
        self.loadImageLabel = QtWidgets.QLabel()
        self.loadImageLabel.setEnabled(True)
        self.loadImageLabel.setObjectName("loadImageLabel")
        self.loadImageLabel.setStyleSheet("border: 2px solid black;")
        self.loadImageLabel.setAlignment(Qt.AlignCenter)  # 图片居中展示
        self.loadImageLabel.setText(_translate("MainWindow", "图片加载区域"))

        self.showImageLabel = QtWidgets.QLabel()
        self.showImageLabel.setEnabled(True)
        self.showImageLabel.setObjectName("showImageLabel")
        self.showImageLabel.setStyleSheet("border: 2px solid black;")
        self.showImageLabel.setAlignment(Qt.AlignCenter)  # 图片居中展示
        self.showImageLabel.setText(_translate("MainWindow", "修改展示区域"))
        Image_Layout.addWidget(self.loadImageLabel)
        Image_Layout.addWidget(self.showImageLabel)




        # 在按钮区横向布局中，创建两个竖向的布局，竖向布局中插入按钮，和list列表，以及的展示信息，按钮，列表，展示信息界面按2、4、12
        #第一列按钮布局
        Button_Button_VLayout = QVBoxLayout()
        Button_Button_VLayout.setObjectName("Button_Button_VLayout")
        self.ImageChoicepushButton = QtWidgets.QPushButton()
        self.ImageChoicepushButton.setObjectName("ImageChoicepushButton")
        self.ImageChoicepushButton.setText(_translate("MainWindow", "选择图片"))
        self.ImageChoicepushButton.clicked.connect(self.handle_image_choice)

        self.ImageFixpushButton = QtWidgets.QPushButton()
        self.ImageFixpushButton.setObjectName("ImageFixpushButton")
        self.ImageFixpushButton.setText(_translate("MainWindow", "展示效果"))
        self.ImageFixpushButton.clicked.connect(self.process_and_display_effect)


        self.ClearButton = QtWidgets.QPushButton()
        self.ClearButton.setObjectName("ClearButton")
        self.ClearButton.setText(_translate("MainWindow", "清空按钮"))
        self.ClearButton.clicked.connect(self.clear_labels_and_history)

        Button_Button_VLayout.addWidget(self.ImageChoicepushButton)
        Button_Button_VLayout.addWidget(self.ImageFixpushButton)
        Button_Button_VLayout.addWidget(self.ClearButton)

        # 第二列功能布局
        Button_Function_VLayout = QVBoxLayout()
        Button_Function_VLayout.setObjectName("Button_Function_VLayout")
        Button_Function_HLayout = QHBoxLayout()
        Button_Function_HLayout.setObjectName("Button_Function_HLayout")
        self.WorkLonelyButton = QtWidgets.QRadioButton()
        self.WorkLonelyButton.setObjectName("WorkLonelyButton")
        self.WorkLonelyButton.setText(_translate("MainWindow", "单文件模式"))
        self.WorkLonelyButton.setChecked(True)
        self.WorkTogtherButton = QtWidgets.QRadioButton()
        self.WorkTogtherButton.setObjectName("WorkTogtherButton")
        self.WorkTogtherButton.setText(_translate("MainWindow", "文件夹模式"))
        Button_Function_HLayout.addWidget(self.WorkLonelyButton)
        Button_Function_HLayout.addWidget(self.WorkTogtherButton)
        Button_Function_VLayout.addLayout(Button_Function_HLayout)

        #增加一个图片旋转功能
        Button_RotateButton_HLayout = QHBoxLayout()
        Button_RotateButton_HLayout.setObjectName("Button_Function_HLayout")
        self.ImageRotateButton = QtWidgets.QPushButton()
        self.ImageRotateButton.setObjectName("ImageRotateButton")
        self.ImageRotateButton.setText(_translate("MainWindow", "旋转原图"))
        self.ImageRotateButton.clicked.connect(self.on_rotate_load_image_label_button_clicked)
        self.ImageRotateButton2 = QtWidgets.QPushButton()
        self.ImageRotateButton2.setObjectName("ImageRotateButton")
        self.ImageRotateButton2.setText(_translate("MainWindow", "旋转处理图"))
        self.ImageRotateButton2.clicked.connect(self.on_rotate_show_image_label_button_clicked)

        Button_RotateButton_HLayout.addWidget(self.ImageRotateButton)
        Button_RotateButton_HLayout.addWidget(self.ImageRotateButton2)
        Button_Function_VLayout.addLayout(Button_RotateButton_HLayout)

        #增加图片处理选中列表
        self.choosePicStyleCombo = QtWidgets.QComboBox()
        self.choosePicStyleCombo.setObjectName("choosePicStyleCombo")
        self.choosePicStyleCombo.addItem("极致色彩")
        self.choosePicStyleCombo.addItem("漫画风格")
        self.choosePicStyleCombo.addItem("图案填充")
        self.choosePicStyleCombo.currentIndexChanged.connect(self.process_and_display_effect)
        self.choosePicStyleCombo.currentIndexChanged.connect(self.update_slider_value)
        Button_Function_VLayout.addWidget(self.choosePicStyleCombo)

        #第三列信息布局
        Button_Infomation_VLayout = QVBoxLayout()
        Button_Infomation_VLayout.setObjectName("Button_Infomation_VLayout")
        self.result = QLineEdit()
        self.result.setPlaceholderText("信息展示")
        self.result.setReadOnly(True)# 设置只读
        self.listPicCombo = QtWidgets.QComboBox()# 增加文本选择框展示选择的文件夹下的图片列表
        self.listPicCombo.setObjectName("listPicCombo")
        self.listPicCombo.currentIndexChanged.connect(self.update_load_image_label)

        # 创建滑动选择器
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)  # 设置最小值
        self.slider.setMaximum(100)  # 设置最大值
        self.slider.setValue(20)  # 设置初始值
        self.slider.valueChanged.connect(self.process_and_display_effect)

        # 将滑动选择器添加到 Button_Infomation_VLayout 布局中
        Button_Infomation_VLayout.addWidget(self.slider)
        Button_Infomation_VLayout.addWidget(self.listPicCombo)
        Button_Infomation_VLayout.addWidget(self.result)

        Button_Layout.addLayout(Button_Button_VLayout)
        Button_Layout.addLayout(Button_Function_VLayout)
        Button_Layout.addLayout(Button_Infomation_VLayout)

        Button_Layout.setStretchFactor(Button_Button_VLayout, 2)
        Button_Layout.setStretchFactor(Button_Function_VLayout, 4)
        Button_Layout.setStretchFactor(Button_Infomation_VLayout, 12)

        #住布局把三大主要布局加载进去
        # main_layout.addLayout(Tool_Layout)
        main_layout.addLayout(Image_Layout)
        main_layout.addLayout(Button_Layout)

        # 设置 main_layout 为窗口的布局
        self.setLayout(main_layout)
        # 设置布局的比例
        main_layout.setStretchFactor(Tool_Layout, 1)
        main_layout.setStretchFactor(Image_Layout, 13)
        main_layout.setStretchFactor(Button_Layout, 2)

        # 获取设备本地显示的分辨率
        screen_resolution = QDesktopWidget().screenGeometry()
        screen_width = screen_resolution.width()
        screen_height = screen_resolution.height()

        # 按显示的分辨率适应性的限制最小大小
        self.setMinimumSize(int(screen_width * 0.5), int(screen_height * 0.5))

    def clear_labels_and_history(self):
        # 清空 result label 和 listPicCombo
        self.result.clear()
        self.listPicCombo.clear()

        # 清空 loadImageLabel 和 showImageLabel 中的图片
        self.loadImageLabel.clear()
        self.showImageLabel.clear()
    def handle_image_choice(self):
        if self.WorkTogtherButton.isChecked():
            self.choose_and_add_folder_images()
        else:
            self.choose_and_display_image()
    def display_image_on_label(self, image_file_path, label):
        image = QImage(image_file_path)
        pixmap = QPixmap.fromImage(image)
        # 将原始 QPixmap 存储在类变量中，并重置旋转角度
        self.original_pixmap = pixmap
        self.rotation_angle = 0
        # 根据 label 大小调整 pixmap 大小，同时保持宽高比
        scaled_pixmap = pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_pixmap)

    def choose_and_add_folder_images(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_name = QFileDialog.getExistingDirectory(None, "选择文件夹", "", options=options)

        if folder_name:
            for file in os.listdir(folder_name):
                if file.lower().endswith(('.jpeg', '.jpg', '.png')):
                    image_file_path = os.path.join(folder_name, file)
                    index = self.listPicCombo.findText(image_file_path)
                    if index == -1:  # 检查图片路径是否已存在
                        self.listPicCombo.addItem(image_file_path)
                    else:
                        self.listPicCombo.setCurrentIndex(index)

    def choose_and_display_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(None, "选择图片", "", "Images (*.jpeg *.jpg *.png);;All Files (*)", options=options)

        if file_name:
            index = self.listPicCombo.findText(file_name)
            if index == -1:  # 检查图片路径是否已存在
                self.result.setText(file_name)  # 更新 result label
                self.listPicCombo.addItem(file_name)  # 向 listPicCombo 添加图片路径
                self.display_image_on_label(file_name, self.loadImageLabel)
            else:
                self.listPicCombo.setCurrentIndex(index)

    def Pic_HeavyColor(self, image_file_address, gamma=2, brightness_factor=1.2):
        im = np.array(Image.open(image_file_address).convert("RGB"))
        GM = 255 * (im / 255) ** gamma

        # 提高亮度
        GM = np.clip(GM * brightness_factor, 0, 255)

        im = Image.fromarray(GM.astype('uint8'))
        im = im.convert('RGB')
        return im

    def pic_hand_draw(self, image_file_address, depth=30, vec_el=np.pi / 2.2, vec_az=np.pi / 4):
        """
        将输入的图像转换为素描风格。

        :param image_file_address: 输入图像的文件路径
        :param depth: 深度参数，用于控制素描效果的强度，默认值为 20
        :param vec_el: 俯仰角，用于控制光源方向，默认值为 pi/2.2
        :param vec_az: 方位角，用于控制光源方向，默认值为 pi/4
        :return: 转换后的素描图像（PIL.Image 对象）
        """
        a = np.asarray(Image.open(image_file_address).convert('L')).astype('float')

        grad = np.gradient(a)
        grad_x, grad_y = grad
        grad_x = grad_x * depth / 100
        grad_y = grad_y * depth / 100
        A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
        uni_x = grad_x / A
        uni_y = grad_y / A
        uni_z = 1. / A

        dx = np.cos(vec_el) * np.cos(vec_az)
        dy = np.cos(vec_el) * np.sin(vec_az)
        dz = np.sin(vec_el)

        b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
        b = b.clip(0, 255)

        im = Image.fromarray(b.astype('uint8'))
        im = im.convert('RGB')  # 将图像转换为 RGB，以便将其转换为 QImage
        return im

    def update_slider_value(self, index):
        if self.choosePicStyleCombo.itemText(index) == "漫画风格":
            self.slider.setValue(20)
        elif self.choosePicStyleCombo.itemText(index) == "极致色彩":
            self.slider.setValue(30)
        else:
            self.slider.setValue(1)

    def process_and_display_effect(self):
        image_file_path = self.result.text()
        if not image_file_path:
            self.choose_and_display_image()  # 如果没有图片路径，重新选择图片
            return

        current_style = self.choosePicStyleCombo.currentText()
        if current_style == "极致色彩":
            gamma = self.slider.value() / 10  # 将滑动选择器的值转换为 gamma 值
            effect_image = self.Pic_HeavyColor(image_file_path, gamma=gamma)
        elif current_style == "漫画风格":
            depth = max(20, self.slider.value())  # 将默认值设置为 20，但允许用户手动调整
            effect_image = self.pic_hand_draw(image_file_path, depth=depth)
        else:
            print("wait")
        # ... 处理其他效果 ...

        qimage = QImage(effect_image.tobytes("raw", "RGB"), effect_image.width, effect_image.height,
                        QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)

        # 根据 showImageLabel 大小调整 pixmap 大小
        scaled_pixmap = pixmap.scaled(self.showImageLabel.width(), self.showImageLabel.height(), Qt.KeepAspectRatio,
                                      Qt.SmoothTransformation)
        self.showImageLabel.setPixmap(scaled_pixmap)

    def update_load_image_label(self, index):
        if index == -1:
            return

        image_file_path = self.listPicCombo.itemText(index)
        self.result.setText(image_file_path)  # 更新 result label
        self.display_image_on_label(image_file_path, self.loadImageLabel)


    def on_rotate_show_image_label_button_clicked(self):
        angle = 90  # 您可以根据需要设置旋转角度
        self.rotate_image_label(self.showImageLabel, angle)

    def on_rotate_load_image_label_button_clicked(self):
        angle = 90  # 您可以根据需要设置旋转角度
        self.rotate_image_label(self.loadImageLabel, angle)


    def rotate_image_label(self, image_label, angle):
        if self.original_pixmap is None:
            return

        # 更新累积的旋转角度
        self.rotation_angle += angle

        # 旋转原始 QPixmap
        transform = QTransform()
        transform.rotate(self.rotation_angle)
        rotated_pixmap = self.original_pixmap.transformed(transform, Qt.SmoothTransformation)

        # 根据 QLabel 大小重新调整 QPixmap 大小
        scaled_pixmap = rotated_pixmap.scaled(
            image_label.width(), image_label.height(),
            Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

        # 将调整后的 QPixmap 设置为 QLabel 的内容
        image_label.setPixmap(scaled_pixmap)