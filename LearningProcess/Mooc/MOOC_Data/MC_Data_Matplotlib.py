import matplotlib
import numpy as np
from matplotlib import pyplot as plt

def EX_plt():
    # matplotlib.rcParams['font.family'] = 'LiSu'
    # matplotlib.rcParams['font.size'] = 20

    plt.plot([0,2,4,6,8],[3,1,4,5,2])
    plt.xlabel('横轴:时间',fontproperties='LiSu',fontsize=20)
    plt.ylabel('纵轴:震幅',fontproperties='LiSu',fontsize=20)
    plt.axis([-1,10,0,6])
    plt.savefig('test',dpi=600)
    # plt.show()


def EX_plt_area():
    # plt.subplot(3,2,4)#行列划分、区域指定绘制
    x=3
    y=2
    for i in range(x*y):
        plt.subplot(x, y, i+1)  # 行列划分、区域指定绘制
        EX_plt()
    plt.show()

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

def EX_Dijian():
    a = np.arange(0.0, 5.0, 0.02)
    plt.plot(a, f(a))

def EX_F():
    a = np.arange(0.0, 5.0, 0.02)
    plt.subplot(211)
    plt.plot(a, f(a))
    plt.subplot(2, 1, 2)
    plt.plot(a, np.cos(2 * np.pi * a), 'r--')

    plt.xlabel('横轴:时间',fontproperties='LiSu',fontsize=15,color='green')
    plt.ylabel('纵轴:震幅',fontproperties='LiSu',fontsize=15)
    plt.title(r'正弦波实例 $y=cos(2\pi x)$',fontproperties='LiSu',fontsize=15)
    # plt.text(2,1,r'$\mu=100$',fontsize=15)#\mu=μ
    plt.annotate(r'$\mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.1,width=1))
    plt.axis([-1,6,-2,2])
    plt.grid(True)#网格
    plt.show()


def EX_Style():
    a=np.arange(10)
    plt.plot(a,a*1.5,'go-',a,a*2.5,'rx',a,a*3.5,'*',a,a*4.5,'b-.')
    plt.show()


def EX_Design_area():
    plt.subplot2grid((3,3),(0,0),colspan=3)
    EX_Dijian()
    plt.subplot2grid((3,3),(1,0),colspan=2)
    EX_Dijian()
    plt.subplot2grid((3,3),(1,2),rowspan=2)
    EX_Dijian()
    plt.subplot2grid((3,3),(2,0))
    EX_Dijian()
    plt.subplot2grid((3,3),(2,1))
    EX_Dijian()
    plt.show()

def EX_Design_GridSpec():
    import matplotlib.gridspec as gridspec
    gs=gridspec.GridSpec(3,3)
    ax1=plt.subplot(gs[0,:])
    ax2=plt.subplot(gs[1,:-1])
    ax3=plt.subplot(gs[1,-1])
    ax4=plt.subplot(gs[2,0])
    ax5=plt.subplot(gs[2,1])


def main():
    #备注，一个个解开注释，案例相互干扰
    # EX_plt()
    # EX_plt_area()
    # EX_F()
    # EX_Style()
    EX_Design_area()

if __name__ == '__main__':
    main()