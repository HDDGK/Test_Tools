from PIL import Image
from Tool_Choose_File import chooseFile as cF
from Tool_get_file_address import find_adress as fa
from Tool_get_file_address import find_File_type as ft





def ChooseFile():
    selectFile = cF("All Files", "选择{}类型文件".format("*"))
    if ft(selectFile)=="jpg":
        print(ft(selectFile),"转换成PNG")
        pictureTypeChange(selectFile, "png")
    elif ft(selectFile)=="png":
        print(ft(selectFile), "转换成JPG")
        TypeChange(selectFile, "jpg")
    else:
        print(ft(selectFile))

def TypeChange(selectFile, saveType):
    from PIL import Image
    im=Image.open(selectFile)
    if im.mode=="RGBA":im= im.convert("RGB")
    cname = input("请输入修改后文件名称：")
    im.save(fa(selectFile,cname,saveType))

def pictureTypeChange(filepath, cType):
    img = Image.open(filepath)
    cname = input("请输入修改后文件名称：")
    save_Adress_Name_Type = fa(filepath, cname, cType)
    img.save(save_Adress_Name_Type)



def print_MainMenu():
    list=[
        "-----开始----",
        "[1] PNG --> JPG",
        "[2] JPG --> PNG",
        "-----结束----",
    ]
    for i in list:
        print(i)
    ChooseFile()
    # choose = int(input("请输入选项："))
    # if choose == 1:
    #     print(1)
    #     # pictureTypeChange("png","jpg")
    # if choose == 2:
    #     pictureTypeChange("jpg","png")
    # else:
    #     print("输错：长点心。。。")
        # time.sleep(2)


if __name__ == '__main__':
    # import time
    #
    # while True:
    #     try:
    #         print_MainMenu()
    #     except:
    #         print("运行报错：长点心。。。")
    #         time.sleep(2)
    print_MainMenu()


