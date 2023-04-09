#支持导入整个文件，变量，或者是方法,这里练习在main.py 中调用模块
pineTree="我是全局变量中定义的一颗松树"
def fun_chirstmasTree():
    '''功能：做梦
        无返回值
    '''
    pineTree="我这里是局部变量中定义的一颗圣诞树，随对象创建而触发\n"
    print(pineTree)

if __name__=='__main__':
    fun_chirstmasTree()
    print(pineTree)
    #我觉得这里的main是指这个模块自己调用，其他人来调用，名字对不上，不调用这块
    
