import os,re
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
    :return:文件夹下的txt的格式列表
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

def chapter_Cut_Save(func):
    Dir,SaveDir,ChooseLists,Savelists=choose_Dir('txt')
    print("-"*12,"开始处理文件","-"*12)
    for i in range(len(ChooseLists)):
        if func=="小说章节分割":
            print('开始处理：',ChooseLists[i])
            chapter_Cut(ChooseLists[i],SaveDir,(SaveDir+''+ChooseLists[i].split('/')[-1]))
        else:
            print("??")
            print("-" * 12, "文件处理中断", "-" * 12)
            break
    print("-" * 12, "文件处理结束", "-" * 12)

def chapter_Cut(txt_Address,txt_SaveDir,txt_SaveAddress):
    print('开始处理2：',txt_Address)
    data=''
    txt_all=open(txt_Address,'r',encoding='utf-8')

    with open(txt_Address,'r',encoding='utf-8') as f:
        for line in f:
            line=line.replace(' ', '')
            line=line.replace('\n',' ')
            line=line.replace('  ', ' ')
            line=line.replace(' ','\n')
            data=data+line
    fw=open(txt_SaveAddress,'w',encoding='utf-8')
    fw.write(data)


        # pattern=re.compile(r'第[一二三四五六七八九十百千万壹贰参肆伍陆柒捌致拾佰仟]{1,6}章]')
        # txt_cut=re.split(pattern,txt)

    # chapter_name=re.findall(pattern,txt)
    # print(chapter_name)

    # for item in pattern.finditer(txt):
    #     # print(item.start())
    #     print(item.group())

    if os.path.exists(txt_SaveDir):
        # txt.save(txt_SaveAddress)
        print("-" * 12, "小说保存成功", "-" * 12)

    else :
        os.makedirs(txt_SaveDir)
        # txt.save(txt_SaveAddress)
        print("-" * 12, "小说保存成功", "-" * 12)
    print()

if __name__ == '__main__':
    chapter_Cut_Save('小说章节分割')