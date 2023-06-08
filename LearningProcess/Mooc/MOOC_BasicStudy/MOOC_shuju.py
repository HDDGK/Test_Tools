import jieba
def ji_he():
    '''
    集合
    1、数据去重 XX=set（X）   XXX=list(XX)

    S|T：两者合
    S-T：两者差
    S&T：两者成员合
    S^T：两者中
    S<T：是否子集关系
    s>T：是否包含关系
    '''
    A={"p","y",123}
    for item in A:
        print(item,end="")
    B=set("pypy123")
    print(A-B)
    print(A|B)
    print(A&B)
    print(A^B)
    print(A<B)
    print(A>B)
    A.add(1)
    print(A)
    A.discard(1)
    print(A)
    A.remove(123)
    print(A)
    C=A.copy()
    print(C)
    print(len(C))
    print("p"in C)
    print("p"not in C)
    for item in A:
        print(item,end="")
    print("\n--------------------")
    try:
        while True:
            print(A.pop(),end="")
    except:
        pass
def yuan_zu():
    '''
    元组：
    1、数据不可变，固定搭配场景
    2、包含序列的使用方式

    :return:
    '''
    craeture="cat","dog","tiger","human"
    color=(0x001100,"blue",craeture)
    print(color)
    print(craeture[::-1])#新元组
def lie_biao():
    '''
    列表：更灵活
    :return:
    '''
    ls=["cat","dog","tiger","human",1024]
    lt=ls#指针
    ls[1]
    print(ls)
    ls[1:2]=lt
    print(ls)
    del ls[1]
    print(ls)
    ls+=lt
    print(ls)
    ls*=2
    print(ls)
    ls.clear()
    print(ls)
    ls.append("s")
    print(ls)
    ltt=ls.copy()
    print(ltt)
    ltt.insert(1,"ee")
    print(ltt)
    ltt.remove("ee")
    print(ltt)
    ltt.pop(0)
    print(ltt)
def d():
    '''
    字典
    1、映射表达
    表达键值对数据，操作

    '''
    d={}#
    d["a"]=1#
    d["b"]=2#
    d["b"] = 3  #
    "C" in d
    print(len(d))
def jie_ba():
    import jieba
    name="中华人民共和国是伟大的蟒蛇语言"
    print(jieba.lcut(name))#精准模式
    print(jieba.lcut(name,cut_all=True))#全局模式
    print(jieba.lcut_for_search(name))#引擎模式
    jieba.add_word("蟒蛇语言")
    print(jieba.lcut(name))  # 精准模式
def get_txt():
    txt1=open("hamlet.txt", 'r').read()
    txt=txt1.lower()
    for ch in '~！@#￥%……&*（）!@#$%^&*()_+——+-=:;\'；‘：",<，《。》.>?/？、【】、{}|[]\\':
        txt =txt.replace(ch,' ')
    return txt
def get_word():
    txt1=open("sanguo.txt", 'r', encoding="utf-8").read()
    txt=txt1.lower()
    for ch in '~！@#￥%……&*（）!@#$%^&*()_+——+-=:;\'\n； ‘："“”,<，《。》.>?/？、【】、{}|[]\\':
        txt =txt.replace(ch,' ')
    return txt

def find_word():
    hamletT=get_txt()
    words=hamletT.split()
    conts={}
    for w in words:
        conts[w]=conts.get(w,0)+1
    items=list(conts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    for i in range(10):
        word,count=items[i]
        print("”{0:<10}“{1:>5}".format(word,count))

def find_china():
    saoguo=get_word()
    word=jieba.lcut(saoguo)
    counts={}
    for w in word:
        if len(word)==1:
            continue
        else:
            counts[w]=counts.get(w,0)+1
    item=list(counts.items())
    item.sort(key=lambda x:x[1],reverse=True)
    for i in range(15):
        w,c=item[i]
        print("“{0:<10}”{1:>5}".format(w,c))
    print("??")

d()
ji_he()
yuan_zu()
lie_biao()
get_txt()
find_word()
find_china()
jie_ba()
