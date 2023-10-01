import os
from PIL import Image
import numpy as np

from tkinter import filedialog
def chooseFile(selectFileType: object, title: object) -> object:
    # tkinter.messagebox.showinfo("选择文件","选择一个{}类型文件".format(selectFileType))
    File_Path = filedialog.askopenfilename(title="选择需要转换的{}类型文件".format(selectFileType),filetypes=[('{}'.format(selectFileType), "*.{}".format(selectFileType)), ('All Files', "*")])
    print("你选择的文件路径：{}".format(File_Path))
    return File_Path

def choose_Dir(*types):
    '''
    弹窗选择文件夹
    获取内部文件列表
    :return:文件夹下的JPG/PNG的格式列表
    '''
    # fileList=filedialog.askopenfilename
    print("-"*12,"获取文件开始","-"*12)
    choose_FileDir=filedialog.askdirectory()
    Save_FileDir=choose_FileDir+'/处理后文件/'
    # print(choose_FileDir)
    file_All_List=os.listdir(choose_FileDir)
    # print(file_All_List)
    file_Choose_SavePathList=[]
    file_Choose_ChooseList=[]
    file_Choose_NameList=[]
    for file in file_All_List:
        for type in types:
            if type==file.split('.')[-1]:
                file_Choose_NameList.append(file)
                file1=choose_FileDir+'/'+file
                file_Choose_ChooseList.append(file1)
                file = Save_FileDir +'/'+ file
                file_Choose_SavePathList.append(file)
                # print(file)
    # print(file_All_List)
    print(file_Choose_SavePathList)
    print(file_Choose_ChooseList)
    print("-"*12,"获取文件完成","-"*12)
    return choose_FileDir,Save_FileDir,file_Choose_ChooseList,file_Choose_SavePathList

def BQO_Image_Save(func):
    Dir,SaveDir,ChooseLists,Savelists=choose_Dir('jpg','png')
    print("-"*12,"开始处理图片","-"*12)
    for i in range(len(ChooseLists)):
        if func=="极致色彩":
            # print(ChooseLists[i])
            Pic_HeavyColor(ChooseLists[i],SaveDir,(SaveDir+'/'+ChooseLists[i].split('/')[-1]))
        elif func=="手绘风格":
            print()
            Pic_HandDraw(ChooseLists[i],SaveDir,(SaveDir+'/'+ChooseLists[i].split('/')[-1]))
        else:
            print("??")
            print("-" * 12, "图片处理中断", "-" * 12)
            break
    print("-" * 12, "图片处理结束", "-" * 12)



def Pic_HandDraw(picture_Address,picture_SaveDir,picture_SaveAddress):
    print(picture_Address)
    print(picture_SaveDir)
    print(picture_SaveAddress)
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
    # im.save(r"C:\Users\HK145-TP\Desktop\HandleDraw.png")
    if os.path.exists(picture_SaveDir):
        # print("打开完成2")
        # print(picture_SaveAddress)
        im.save(picture_SaveAddress)
        print("-" * 12, "图片保存成功", "-" * 12)

    else :
        os.makedirs(picture_SaveDir)
        # print("???")
        im.save(picture_SaveAddress)
        print("-" * 12, "图片保存成功", "-" * 12)

def Pic_HeavyColor(picture_Address,picture_SaveDir,picture_SaveAddress):
    # im = np.array(Image.open(picture_Address).convert('L'))
    # 灰度值

    im = np.array(Image.open(picture_Address).convert("RGB"))
    print(picture_SaveAddress)
    # print("打开完成")
    im2 = Image.fromarray(im.astype('uint8'))
    # print("打开完成1")
    # im2.save(r"C:\Users\HK145-TP\Desktop\125.png")
    GM= 255 * (im / 255) ** 2
    im2 = Image.fromarray(GM.astype('uint8'))
    if os.path.exists(picture_SaveDir):
        # print("打开完成2")
        # print(picture_SaveAddress)
        im2.save(picture_SaveAddress)
        print("-" * 12, "图片保存成功", "-" * 12)

    else :
        os.makedirs(picture_SaveDir)
        # print("???")
        im2.save(picture_SaveAddress)
        print("-" * 12, "图片保存成功", "-" * 12)



if __name__ == '__main__':
    BQO_Image_Save('极致色彩')
    # BQO_Image_Save('手绘风格')
