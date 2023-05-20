# import tkinter
# from tkinter import messagebox
from tkinter import filedialog
def chooseFile(selectFileType: object, title: object) -> object:
    # tkinter.messagebox.showinfo("选择文件","选择一个{}类型文件".format(selectFileType))
    File_Path = filedialog.askopenfilename(title="选择需要转换的{}类型文件".format(selectFileType),filetypes=[('{}'.format(selectFileType), "*.{}".format(selectFileType)), ('All Files', "*")])
    print("你选择的文件路径：{}".format(File_Path))
    return File_Path