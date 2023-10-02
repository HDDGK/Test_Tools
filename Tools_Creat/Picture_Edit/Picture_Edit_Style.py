import numpy as np
from PIL import Image

'''
功能：独立只做函数的调用，单独处理照片效果，不处理其他问题，
返回值：只返回处理后的图片数据
'''
str_k="-"*12
def Pic_HeavyColor(picture_Address,picture_SaveAddress):
    # im = np.array(Image.open(picture_Address).convert('L'))
    # 灰度值
    # print(str_k,"处理图片【开始】",str_k)
    im = np.array(Image.open(picture_Address).convert("RGB"))
    im2 = Image.fromarray(im.astype('uint8'))
    GM= 255 * (im / 255) ** 2
    im2 = Image.fromarray(GM.astype('uint8'))
    print(str_k,"处理图片【结束】",str_k)
    # print(str_k,"保存文件夹【开始】",str_k)
    im2.save(picture_SaveAddress)
    print(str_k,"保存文件夹【结束】",str_k)


def Pic_HandDraw(picture_Address,picture_SaveAddress):
    # print(str_k,"处理图片【开始】",str_k)
    a = np.asarray(Image.open(picture_Address).convert('L')).astype('float')

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
    print(str_k, "处理图片【结束】", str_k)
    # print(str_k, "保存文件夹【开始】", str_k)
    im.save(picture_SaveAddress)
    print(str_k, "保存文件夹【结束】", str_k)