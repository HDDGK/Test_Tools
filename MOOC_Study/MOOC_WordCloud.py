import tkinter.messagebox
from Tool_get_file_address import *



def get_chooice():
    from tkinter import filedialog,messagebox
    tkinter.messagebox.showinfo("选择","选择一个txt文本文件")
    Folder_Path=filedialog.askopenfilename(filetypes=[('txt',"*.txt"),('All Files',"*")])
    # try:
    #     file_list=os.listdir(Folder_Path)
    #     for file in file_list:
    #         if file.endswith('.txt'):
    #             print(file)
    # except FileNotFoundError:
    #     print("未选择文件夹")
    print("选择的文件地址：",Folder_Path)
    return Folder_Path

def get_FilePath():
    try:
        file_Path=get_chooice()
    except:
        print("???,好好选一下txt文件")
        # file_Path=r"C:\Users\HK145-TP\Desktop\关于实施乡村振兴战略的意见.txt"
    return file_Path
def get_Txt():
    main_txt=open(get_FilePath(),'r',encoding="utf-8").read()
    main_txt=''.join([i.strip(' ') for i in main_txt])
    for ch in '~！@#￥%……&*（）!@#$%^&*()_+——+-=:;\'；‘：",<，《。》.>?/？、【】、{}|[]\\  ':
        main_txt =main_txt.replace(ch,' ')
    return main_txt

def get_MianWord(mainTxt):
    import jieba
    ls=jieba.lcut(mainTxt)
    for i in ls:
        if len(i)==1:
            ls.remove(i)

    txt=" ".join(ls)
    return txt
def get_shape():

    # from scipy.misc import imread
    from imageio import imread
    from tkinter import filedialog,messagebox
    tkinter.messagebox.showinfo("选择","选择一个形状图片")
    Folder_PNG_Path = filedialog.askopenfilename(title="选择一个形状PNG图片",filetypes=[('png', "*.png"), ('All Files', "*")])
    print("")
    mask=imread(Folder_PNG_Path,pilmode='L')
    return mask
def get_WordCloud(mainWord):
    import wordcloud
    shape=get_shape()
    wordcloud_paint = wordcloud.WordCloud(
        width=1920,
        height=1080,
        # max_font_size=18,
        # min_font_size=6,
        # font_step=2,
        max_words=40,
        mask=shape,
        stopwords={"三","二","一","的","以"},
        font_path="STCAIYUN.TTF",
        background_color="white"
    )
    print(mainword)
    wordcloud_paint.generate(mainWord)
    wordcloud_paint.to_file(r"C:\Users\HK145-TP\Desktop\新建文件夹\auto_print.png")

txt=get_Txt()
mainword=get_MianWord(txt)
get_WordCloud(mainword)
html="https://python123.io/resources/pye/%E5%85%B3%E4%BA%8E%E5%AE%9E%E6%96%BD%E4%B9%A1%E6%9D%91%E6%8C%AF%E5%85%B4%E6%88%98%E7%95%A5%E7%9A%84%E6%84%8F%E8%A7%81.txt"