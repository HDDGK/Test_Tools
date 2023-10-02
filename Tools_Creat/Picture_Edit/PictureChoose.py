from tkinter import filedialog
import os
'''
内容：只做系统路径的调用，获取选择的文件夹下的图片文件列表并返回
返回值：指定文件夹下的图片列表
'''
str_k="-"*12
changeDir="处理后图片"

def show(Choose_file_path_list):
    for filepath in Choose_file_path_list:
        print(filepath)
    #列出选择的图片列表，并弹窗提示是否继续


def choose_Dir(*types):
    '''
    弹窗选择文件夹
    获取内部文件列表
    :return:文件夹下的JPG/PNG的格式列表
    '''
    Choose_file_path = []
    Choose_file_path_list = []

    # fileList=filedialog.askopenfilename
    print("-"*12,"获取文件【开始】","-"*12)
    choose_FileDir=filedialog.askdirectory()
    # choose_FileDir 获取选择的文件夹路径

    file_All_List=os.listdir(choose_FileDir)
    for file in file_All_List:
        for type in types:
            if type==file.split('.')[-1]:
                Choose_file_path = choose_FileDir +'/'+ file
                Choose_file_path_list.append(Choose_file_path)
    # file_All_List 获取选择的文件夹下的图片列表
    print("-"*12,"获取文件【结束】","-"*12)
    # show(Choose_file_path_list)
    return Choose_file_path_list

def savePath(fileDirPath,file_name,insert):
    print(str_k,"拼凑保存文件夹路径【开始】",str_k)
    changePath=fileDirPath+"\\"+str(insert)+"\\"+file_name
    print(str_k,"拼凑保存文件夹路径【完成】",str_k)
    return changePath

def CheckPath(filePath):
    # 这里是对传入的文件的地址，单个处理
    fileDirPath = os.path.abspath(filePath)
    file_path, file_name = os.path.split(fileDirPath)
    sp = savePath(file_path, file_name, changeDir)
    if not os.path.exists(file_path + '\\' + changeDir):
        os.makedirs(file_path + '\\' + changeDir)
    return sp
