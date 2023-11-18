import os

import numpy as np
from PIL import Image

from ImageEx import ImageEx


class ImageEditStyle(ImageEx):

    def EStyleMenu(self, styleName):
        # print("1、进入Stylemenu")
        if os.path.exists(self.ImageFileAddress):  # 确定本地有图才继续
            # print("2、图片真实存在")

            if styleName == "极致色彩":
                # print("3、选择了这种模式：",styleName)
                im = self.Pic_HeavyColor
                self.ImageSavePathSet(styleName)
                im.save(self.ImageFileSaveAddress)
            elif styleName == "漫画风格":
                im = self.Pic_HandDraw
                self.ImageSavePathSet(styleName)
                im.save(self.ImageFileSaveAddress)

    @property
    def Pic_HeavyColor(self):
        im = np.array(Image.open(self.ImageFileAddress).convert("RGB"))
        # im = np.array(Image.open(self.ImageFileAddress).convert('L'))# 灰度值
        # im2 = Image.fromarray(im.astype('uint8'))
        GM = 255 * (im / 255) ** 2
        im = Image.fromarray(GM.astype('uint8'))
        return im

    @property
    def Pic_HandDraw(self):
        a = np.asarray(Image.open(self.ImageFileAddress).convert('L')).astype('float')

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
        return im

    @property
    def Pic_FillWords(self):
        self.txt_path = ""
        self.cloud_world = ""
        return ""
