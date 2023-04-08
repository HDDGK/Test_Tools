#类的定义
class TestTry:
    "学习测试类"
    def __init__ (self,beak,wing,claw):
        #注意init，拼写，这里是默认执行的，创建时执行，无需调用
        print("我是个学习大雁测试类，我有以下特征")
        print(beak)
        print(wing)
        print(claw)
    def funName(self,parameterlist):
        print(parameterlist)
        #statement:   类体
        #pass

#创建实例
beak_1="鸟喙较大"
wing_1="翅膀长尖"
claw_1="爪子带蹼"
testMan1=TestTry(beak_1,wing_1,claw_1)
testMan1.funName("我是创建的实例的方法运行输出\n")
#print(testMan1)


class Geese:
    "雁类"
    neck = "长脖子"
    wing = "大翅膀"
    leg="细短足"
    number=0
    def __init__(self):
        print("我是雁类，这里是创建时调用，下面输出类的属性")
        Geese.number+=1
        print(self.neck)
        print(self.wing)
        print(self.leg)
list1=[]
for i in range(4):
    list1.append(Geese())
print("内部繁衍后，我们的族群有："+str(Geese.number))
Geese.number=2
print("外部干扰后，我们的族群有："+str(Geese.number)+"\n")


class Geese2:
    "雁类"

    number=0
    def __init__(self):
        self.neck = "长脖子"
        self.wing = "大翅膀"
        self.leg = "细短足"
        print("我是雁类实例的属性定义，我现在在实例的方法中")

        print("我是雁类，这里是创建时调用，下面输出实例的属性")
        Geese.number+=1
        print(self.neck)
        print(self.wing)
        print(self.leg)
geese2=Geese2()
print("如果这个时候用类去访问创建的实例才有的属性，应该会报错，如下")
print(" print(Geese2.leg)：AttributeError: type object 'Geese2' has no attribute 'leg'\n")

#访问限制
print("__XX__,这个是系统定义，比如__init__")
print("__XX,这个是私有")

class Geese3:
    "这里的区别是访问限制"
    __neck="我是隐藏的舌头"
    def __init__(self):
        print("__init__中，内部访问__neck",Geese3.__neck)
geese3=Geese3()
print("加入类名访问，geese3._Geese3__neck的结果",geese3._Geese3__neck)
print("如果下划线错误提示为AttributeError: 'Geese3' object has no attribute '__Geese3__neck'. Did you mean: '_Geese3__neck'?")

#属性
print("\n通过@property,讲方法转化为属性用于计算")
class RectArea:

    def __init__(self,width,heigth):
        self.width=width
        self.heigth=heigth
    @property
    def area(self):
        return self.width*self.heigth


rc=RectArea(800,200)
print(rc.area)
print("@property转换后，属性无法重新赋值，作为保护机制只读"
      "\n比如rc.area=90，否则报错，\nAttributeError: property 'area' of 'RectArea' object has no setter")


class RecName:
    Rec_list=["长方形","正方形","圆形"]
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value in RecName.Rec_list:
            self.__name="你选择了"+value
        else:
            self.__name="你选了个啥？"
print("\n@show.setter 转换后，属性可以重新赋值，且可以限制修改值")
rec=RecName("正方形")
print("这里已经创建实例，这个实例的属性私有\n")

print(rec.name)
print("这里获取之前创建时的信息，正方形\n")

rec.name="长方形d"
print(rec.name)
print("这里获取的提供修改方法后的修改值，`\n修改不成功时，注意检查代码是否改名\n")

