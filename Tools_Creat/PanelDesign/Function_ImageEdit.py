import numpy as np
from PIL import Image

class ImageEdit():
    def Pic_HeavyColor(self):
        im = np.array(Image.open(self.ImageFileAddress).convert("RGB"))
        # im = np.array(Image.open(self.ImageFileAddress).convert('L'))# 灰度值
        # im2 = Image.fromarray(im.astype('uint8'))
        GM = 255 * (im / 255) ** 2
        im = Image.fromarray(GM.astype('uint8'))
        im = im.convert('RGB')
        return im
    def pic_hand_draw(self, image_file_address):
        a = np.asarray(Image.open(image_file_address).convert('L')).astype('float')

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
        im = im.convert('RGB')  # 将图像转换为 RGB，以便将其转换为 QImage
        return im