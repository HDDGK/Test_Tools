import pandas as pd
import numpy as np




def EX_Data_series():
    '''
    series:数据和索引
    通过以下类型创建
    :return:
    '''
    # 自定义索引
    a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
    a1 = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
    # a = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])
    print(a)
    # 通过以下类型创建
    # 标量
    s = pd.Series(25, ['a', 'b', 'c', 'd'])
    print(s)
    # 字典
    d = pd.Series({'a': 9, 'b': 8, 'c': 7}, index=['c', 'a', 'b', 'd'])
    print(d)
    #ndarray
    n=pd.Series(np.arange(5))
    n=pd.Series(np.arange(5),np.arange(9,4,-1))
    print(n)

    #操作
    print(a.index)
    print(a.values)

    print(a['b'])
    print(a[1])

    print(a[3])
    print(d[:3])
    print(a[a>a.median()])
    print(np.exp(a))

    print(9 in a)
    print('b' in a)
    print(a+d)
    d.name="??"
    d.index.name='...'
    print(d)

EX_Data_series()


def EX_Data_dataframe():
    '''
    dataframe:二维带标签的数据
    共用同一列索引=表格

    :return:
    '''
    d=pd.DataFrame(np.arange(10).reshape(2,5))
    print(d[0][0])

    #一维ndarray对象字典创建
    dt={
        'one': pd.Series([1, 2, 3],index=['a','b','c']),
        'two': pd.Series([9,8,7,6],index=['a','b','c','d']),
    }
    d1=pd.DataFrame(dt)
    print(d1)
    d2=pd.DataFrame(dt,index=['b','c','d'],columns=['tow','three'])
    print(d2)

    #列表类型字典
    d3={'one':[1, 2, 3,4], 'tow':[9,8,7,6]}
    d4=pd.DataFrame(d3,index=['a','b','c','d'])
    print(d4,'\n')
    print(d4['one'])
    # print(d4.ix['a'])
    # ix 不在推荐
    print(d4['one'][2])

    d4.reindex(columns=['tow','one'])
    print(d4)
    print(d4.reindex(columns=['tow','one']))
    d5=d4.columns.insert(2,'new')
    d6=d4.reindex(columns=d5,fill_value=0)
    print(d6)
    d7=d6.columns.delete(2)
    d8=d6.index.insert(4,'e')
    print(d8)
    # d8=d6.reindex(index=d8,columns=d7,method='ffill')
    # d8=d6.reindex(index=d8,columns=d7)
    # d8=d6.reindex(index=d8,columns=d7,fill_value=0)
    print(d8)
    print(d6.drop('a'))
    print(d6.drop('one',axis=1))
    print()


EX_Data_dataframe()

def EX_Data_math():
    a=pd.DataFrame(np.arange(12).reshape(3,4))
    b=pd.DataFrame(np.arange(20).reshape(4,5))
    c=pd.Series(np.arange(4))
    d=pd.DataFrame(np.arange(12,0,-1).reshape(3,4))
    print(a)
    print(b)
    print('\na+b')
    print(a+b)
    print('\na*b')
    print(a*b)
    print('\nb.add(a,fill_value=100)')
    print(b.add(a,fill_value=100))
    print(a.mul(b,fill_value=0))

    print(c-10)
    print(b-c)
    print(b.sub(c,axis=0))
    #横着减少和竖着减少
    print(a>d)
    print(a<d)
    print(a==d)
EX_Data_math()

def EX_Data_feature():
    '''
    数据特征
    :return:
    '''
    a = pd.DataFrame(np.arange(12).reshape(3, 4),index=['a', 'b', 'c'])
    b = pd.DataFrame(np.arange(20).reshape(4, 5),index=['c','a', 'b', 'd'])
    c = pd.Series(np.arange(4))
    d = pd.DataFrame(np.arange(12, 0, -1).reshape(3, 4))
    print(b)
    print()
    print(b.sort_index())
    print()
    print(b.sort_index(ascending=False))
    print()
    print((b.sort_index(ascending=False)).sort_index(axis=1,ascending=False))
    print()
    # print(b.sort_values(axis=0,ascending=False))#如果b是一列OK
    print(b.sort_values(2,axis=0,ascending=False))
    print(b.sort_values('a',axis=1,ascending=False))
    c = a + b
    print(c)
    print(c.sort_values(2,axis=0,ascending=False))
    print(c.sort_values(2,axis=0,ascending=True))

EX_Data_feature()


def EX_Data_analysis():

    print()


EX_Data_analysis()