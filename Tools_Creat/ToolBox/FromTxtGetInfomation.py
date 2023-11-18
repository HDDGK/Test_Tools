import time

import wordcloud

from ImageEdit import ImageEdit
from tkinter import filedialog

import jieba


class FromTxtGetInfomation:
    def __init__(self):
        self.TXTPickWord = None
        self.TXTOrignl = None
        self.TXTINFO = None
        self.TXTPATH = None
        self.PicKOut=list('''·1234567890-=【】、；’，。/`[]\;\',./~！@#￥%……&*（）——+{}|：“《》？ 
''')
        self.Length=2
    def show(self):
        print(self.TXTPATH)
        # print(self.TXTOrignl)
        # print(self.TXTINFO)


    def Pick(self,length):

        print(list)

    def GetFileTXT(self):
        try:
            # tkinter.messagebox.showinfo("选择", "选择一个txt文本文件")
            # filedialog.askopenfilename(filetypes=[('txt', "*.txt"), ('All Files', "*")])
            #获取选择的图片路径
            self.TXTPATH = filedialog.askopenfilename(filetypes=[('txt', "*.txt")])
            #获取指定路径下的文本，注意，这里是列表
            self.TXTOrignl=All_Txt = open(self.TXTPATH, 'r', encoding="utf-8").read()
            #把列表拼接成一个大文本，以便于处理
            All_Txt = ''.join([i.strip(' ') for i in All_Txt])
            #指定剔除字符，单个依次进行全文替换，
            for ch in self.PicKOut:
                self.TXTINFO=All_Txt = All_Txt.replace(ch, ' ')
            #替换后的全文本，通过之前替换的空格，切成列表
            listWord = self.TXTINFO.split(" ")
            #新增一个列表，用来保存后续查找的不合适值的序号
            list=[]
            # 这里循环一次遍历，找出不符合标准的值，标记序号
            for i in range(len(listWord)):
                print(i, ":", listWord[i])
                if len(listWord[i]) < self.Length:
                    list.append(i)
            # 这里把列表中找出的序列倒序
            list.sort(reverse=True)
            # 通过倒序删除的方式一次性删除干净
            for i in list:
                # 记住，列表删除序号对应值和remove指定值不同
                del listWord[i]
            #拼接成一个大文本，准备传递给函数
            self.TXTINFO= ' '.join([i.strip(' ') for i in listWord])
            self.TXTPickWord=jieba.lcut(self.TXTINFO)
            for i in self.TXTPickWord:
                if len(i) == 1:
                    self.TXTPickWord.remove(i)
            self.TXTPickWord= ' '.join([i.strip(' ') for i in self.TXTPickWord])

            time.sleep(3)
            shapePic=ImageEdit()
            shapePic.ImageFileAddress=r"C:\Users\HK145-TP\Desktop\新建文件夹\d3325fa618022c87fb5cbddcdfb1fe6.png"
            shape=shapePic.Pic_Shape()
            print("shape")
            wordcloud_paint = wordcloud.WordCloud(
                width=1920,
                height=1080,
                # max_font_size=18,
                # min_font_size=6,
                # font_step=2,
                max_words=40,
                mask=shape,
                stopwords={"三", "二", "一", "的", "以"},
                font_path="STCAIYUN.TTF",
                background_color="white"
            )
            print(self.TXTPickWord)
            print("paint")
            wordcloud_paint.generate(self.TXTPickWord)
            print("patn")
            shapePic.ImageSavePathSet("图案填充")
            print("svae")
            wordcloud_paint.to_file(shapePic.ImageFileSaveAddress)

        except:
            if self.TXTPATH=="":
                print("好好选文件")
                self.GetFileTXT()
            print("报错了哥")


if __name__ == '__main__':
    FTG=FromTxtGetInfomation()
    FTG.GetFileTXT()
    FTG.show()
