import numpy as np
import rawpy
import cv2
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image

from ImageEx import ImageEx
class EditRawStyle(ImageEx):
    def Recover(self):
        '''
        https://www.php.cn/faq/594210.html
        https://wenku.csdn.net/answer/3d3946b9993941389e4cde8f449d356b
        https://blog.51cto.com/u_16213356/7242503
        https://blog.csdn.net/fengchengbenben/article/details/88425307
        https://qa.1r1g.com/sf/ask/3122111541/
        https://blog.csdn.net/yxyou_1124/article/details/130013120


        https://blog.csdn.net/zhoujinwang/article/details/128443039
        https://www.baidu.com/s?wd=python%20cv2%20%E4%B8%89%E9%80%9A%E9%81%93%20fastNlMeansDenoisingColored&rsv_spt=1&rsv_iqid=0x8f33b3e200864391&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&oq=python%2520%25E5%259B%25BE%25E7%2589%2587%25E7%25B2%25BE%25E5%25BA%25A6%25E4%25BF%25AE%25E5%25A4%258D&rsv_btype=t&inputT=13518&rsv_t=7897HEz%2FEHaxPPc6IeSodIBbsezLFcbFr0f1TryIwYB2k2%2B8TCIN%2BaD2Y%2FeD54j3z388&rsv_pq=8d0194a9005fca8c&rsv_n=2&rsv_sug2=0&rsv_sug4=14078
        :return:
        '''
        # self.imageLabelWidth = 1080
        # self.imageLabelHeight = 720
        # self.loadImage()
        image=cv2.imread("20231023093223.jpg")
        # converted_img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        converted_img = cv2.cvtColor(image, cv2.IMREAD_COLOR)
        denoised_image=cv2.fastNlMeansDenoisingColored(converted_img, None, 10, 10, 7, 21)
        blurred_image=cv2.GaussianBlur(denoised_image,(15,15),0)
        mask=Image.new('L',(image.shape[1],image.shape[0]),255)

        mask.paste((0),(100,100,300,300))
        in_image=cv2.inpaint(blurred_image,np.array(mask),3,cv2.INPAINT_TELEA)
        # cv2.imwrite('repair.jpg',in_image)
        cv2.imwrite('repair.jpg',converted_img)


pcd=EditRawStyle()
pcd.Recover()