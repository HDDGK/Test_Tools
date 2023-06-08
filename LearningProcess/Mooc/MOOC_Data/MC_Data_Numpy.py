import numpy as np
a=[0,1,2,3,4]
b=[9,8,7,6,5]
c=[]
def pysum(a,b):
    for i in range(len(a)):
        c.append(a[i]**2+b[i]**2)
    print("[81, 65, 53, 45, 41]")
    return c


def npsum(a,b):
    A=np.array(a)
    B=np.array(b)
    c=A**2+B**2
    #简化一维数据的计算
    print("[81 65 53 45 41]")
    return c


def np_ndarray():
    '''
    ndarray:多维数组对象
    1、实际数据
    2、描述 数据类型和数据维度
    一般要求元素类型相同，数组下标从0开始
    np.array([],())列表和元组可以混用，但是需要注意个数需要相同
    '''
    # for i in range(1):
    #     '''
    #         print(a.shape)
    #         print(a.ndim)
    #         print(a.size)
    #         print(a.dtype)
    #         print(a.itemsize)
    #     '''
    #     list=[[0, 1, 2, 3, 4],[9, 8, 7, 6, 5]]
    #     a=np.array(list)
    #     b=np.array(list,dtype=np.float32)
    #     print(a.shape)
    #     print(a.ndim)
    #     print(a.size)
    #     print(a.dtype)
    #     print(a.itemsize)
    #     print(b.dtype)
    # for i in range(1):
    #     '''
    #         np.range(n),生类似range
    #         np.ones(shape)：shape是元组类型，全是1的数组
    #         np.zeros(shape)：shape是元组类型，全是0的数组
    #         np.full(shape,value)：shape是元组类型，全是value的数组
    #         np.eye(n)：创建一个正方形元组n*N元组，对角线为1，其他为0
    #     '''
    #
    #     print(np.arange(10))
    #     print(np.ones((3,6)))
    #     print(np.zeros((3,6)))
    #     print(np.eye(5))
    #     print(np.ones((2,3,4)),np.ones((2,3,4)).shape)
    for i in range(1):
        '''
            .reshape(shape):不改变之前的数组，返回形状数组，原值不变
            .resize(shape):与reshape相同，但改变原数组
            .swapaxes(ax1,ax2)
            .flatten():对数组进行降维度
            .astype():改变数组类型
        '''
        a=np.ones((2,3,4))
        print(a.flatten())
        print(a)
        a=np.ones((2,3,4),dtype=int)
        b=a.astype(np.float32)#float32的区别
        print(b)



    # for i in range(1):
    #     '''
    #         np.ones_like(a)
    #         np.zeros_like(a)
    #         np.full_like(a,val)
    #         根据a数据的形状生成
    #         np.linspace()根据起始数，等间距生成
    #         np.concatenate()合并两个数组
    #     '''
    #     print(np.linspace(1,10,4))
    #     print(np.linspace(1,10,4,endpoint=False))#endpoint指最后一个是否为结尾
    #     print(np.linspace(1,10,4),np.linspace(1,10,4,endpoint=False))
    #     print("用于科学计算，所以会生成浮点值，便于计算")

def np_ndarry_math():
    '''
    np.xx
    .abs：绝对值
    .sqrt：平方根
    .square：平方
    .log()：
    .log10()
    .log2()
    .ceil：最大整数
    .floor：最小整数

    .rint
    .dmodf
    .cos
    .cosh

    .exp
    .sign
    :return:
    '''

    print()
if __name__ == '__main__':
    pysum(a, b)
    npsum(a, b)
    np_ndarray()