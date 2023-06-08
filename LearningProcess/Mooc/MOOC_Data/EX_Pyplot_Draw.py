from matplotlib import pyplot as plt
import matplotlib
import numpy as np
from scipy.io import wavfile

def info():
    '''
    .plot：坐标图
    .boxplot：箱型图
    .bar：条形图
    .barh：横向条形图
    .polar：极坐标图
    .pie：饼图

    .psd：功率密度图
    .specgram：谱图
    .cohere：X-Y相关性
    .scatter：散点图
    .step：步阶图
    .hist：直方图

    .contour：等值图
    .vline：垂直图
    .stem：柴火图
    .plot_date：数据日期
    :return:
    '''
    pass
def EX_pie():
    '''
    饼图
    :return:
    '''
    labels='Frogs','Hogs','Dogs','Logs'
    sizes=[15,30,45,10]
    explode=(0,0.1,0,0)
    plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
    plt.show()


def EX_hist():
    np.random.seed(0)
    mu,sigma=100,20
    a=np.random.normal(mu,sigma,size=100)

    # plt.hist(a,20,normed=1,histtype='stepfilled',facecolor='b',alpha=0.75)
    plt.hist(a,20,density=0,histtype='stepfilled',facecolor='b',alpha=0.75)
    #AttributeError: Polygon.set() got an unexpected keyword argument 'normed'
    #这里弃用了normed，启用density
    plt.title('Histogram')
    plt.show()


def EX_ploar():
    N=20
    theta=np.linspace(0.0,2*np.pi,N,endpoint=False)
    radii=10*np.random.rand(N)
    width=np.pi/4*np.random.rand(N)

    ax=plt.subplot(111,projection='polar')
    bars=ax.bar(theta,radii,width=width,bottom=0.0)

    for r,bar in zip(radii,bars):
        bar.set_facecolor(plt.cm.viridis(r/10.))
        bar.set_alpha(0.5)
    plt.show()


def EX_scatter():
    fig,ax=plt.subplots()
    ax.plot(10*np.random.rand(100),10*np.random.rand(100),'o')
    ax.set_title('scatter')

    plt.show()


def EX_YLB():
    '''
    引力波绘制
    :return:
    http://python123.io/dv/grawave.html
    http://python123.io/dv/H1_Strain.wav
    http://python123.io/dv/L1_Strain.wav
    http://python123.io/dv/wf_template.txt
    '''
    rate_h,hstrain=wavfile.read(r'H1_Strain.wav', 'rb')
    rate_l,lstrain=wavfile.read(r'L1_Strain.wav', 'rb')
    reftime,ref_H1=np.genfromtxt('wf_template.txt').transpose()

    htime_interval=1/rate_h
    ltime_interval=1/rate_l

    htime_len=hstrain.shape[0]/rate_h
    htime=np.arange(-htime_len/2,htime_len/2,htime_interval)
    ltime_len=lstrain.shape[0]/rate_h
    ltime=np.arange(-ltime_len/2,ltime_len/2,ltime_interval)

    fig=plt.figure(figsize=(12,6))

    plth=fig.add_subplot(221)
    plth.plot(htime,hstrain,'y')
    plth.set_xlabel('Time (Seconds)')
    plth.set_ylabel('H1 Strain')
    plth.set_title('H1 Strain')

    plth = fig.add_subplot(222)
    plth.plot(ltime, lstrain, 'g')
    plth.set_xlabel('Time (Seconds)')
    plth.set_ylabel('L1 Strain')
    plth.set_title('L1 Strain')

    plth = fig.add_subplot(212)
    plth.plot(reftime,ref_H1)
    plth.set_xlabel('Time (Seconds)')
    plth.set_ylabel('Template Strain')
    plth.set_title('Template')

    fig.tight_layout()
    plt.savefig(r"C:\Users\HK145-TP\Desktop\YLB.png")
    plt.show()
    plt.close(fig)

def main():
    EX_pie()
    EX_hist()
    EX_ploar()
    EX_scatter()
    EX_YLB()
if __name__ == '__main__':
    main()
    info()