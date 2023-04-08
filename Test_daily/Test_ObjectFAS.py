class ClassFAS:
    "这里在尝试累的继承"

class Fruit:
    health="健康"
    def harvest(self,health):
        print("我这种水果吃了："+health)
        print("水果已经收获")
        print("水果本来应该是："+Fruit.health+"")

class Apple(Fruit):
    health = "比较健康"
    def __init__(self):
        print("我是苹果")

class Mushroom(Fruit):
    health = "可能健康"
    def __init__(self):
        print("我是蘑菇")
    #方法的重写
    def harvest(self,health):
        print("我这种蘑菇吃了：" + health)
        print("蘑菇已经收获")
        print("蘑菇本来应该是：" + Fruit.health + "")

apple=Apple()
print("这里刚创建好，下面对象用自身没有的方法【父类】")
apple.harvest(apple.health)
print("苹果类创建的时候，继承了父类的信息\n")
mushroom=Mushroom()
print("这里刚创建好，下面对象用自身重写的父类方法【重写】")
mushroom.harvest((mushroom.health))
print("蘑菇类创建的时候，继承了父类的信息，但【重写】了父类方法，\n")

#子类调用父类的构造方法
print("————————————————————————————")

# class Grandfather:
#     def __init__(self,minZu="汉"):
#         Grandfather.minZu=minZu
#     def jobMoney(self):
#         print("中国原来是"+Grandfather.minZu+"族的")
# class Father(Grandfather):
#     def __init__(self):
#         print("我是汉族")
# father=Father()
# father.jobMoney()
print("这里会报错,因为子类调用的父类方法，但父类方法中包含构造方法，构造方法没有调用，需要子类初始化。\nAttributeError: type object 'Grandfather' has no attribute 'minZu'\n")

class Grandfather:
    def __init__(self,minZu="汉"):
        Grandfather.minZu=minZu
    def jobMoney(self,minZu):
        print("爷爷原来是【父类】" + self.minZu + "族的")
        print("爷爷原来是【父类】"+Grandfather.minZu+"族的")
class Father(Grandfather):
    minZu = "中华民族"
    def __init__(self):
        print("我是爸爸,中华名族")
        super().__init__()
class Son(Grandfather):
    def __init__(self,minZu):
        print("我是儿子")
        super().__init__(minZu)
    def jobMoney(self,minZu):
        print("儿子原来是【子类】【重写】" + minZu + "族的")
        print("儿子原来是【子类】"+Grandfather.minZu+"族的")
father=Father()
father.jobMoney(father.minZu)
print("分析一下：father子类创建时，获取到的中华名族是子类中写死的，\n"
      "输出靠父类的构造中当前类调用，获取到的子类自己的汉族，是来源自GrandFather的父类的方法写的self，\n")
son=Son("共产主义")
son.jobMoney("中华人民共和国")
print("分析一下：son子类创建时，输入了名族，通过默认构造，调用了父类的构造，且重写了jobmoney，改成直接输出名族【这里是方法中调用，直接输出输入值】，\n"
      "第一次输出的是重写的办法中的minzu，打印的是当时方法输入的【中华人民共和国】，\n"
      "第二次输出父类的minzu时，因为构造时子类调用父类构造，并传值,所以应该是创建是的【共产主义】\n")
print("这里需要注意的是：\n"
      "1、子类调用父类，需要注意是否需要父类的构造，需要的话，需要在子类构造中提前调用加载\n"
      "2、子类重新父类办法时，如果子类之前有加载父类办法，并传值，后续调用父类时，输出值和子类调用父类方法时输入的值有关\n"
      "【即子类调用父类构造，创建实例时指定的】\n"
      "3、子类重新父类办法的时候，需要注意\n")