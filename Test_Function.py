def Findname():
    import datetime
    daily=["周一周一灵魂归西。",
           "周二抗战。",
           "周三劫难。",
           "周四麦当鸡。",
           "周五快乐归西。",
           "周六灵魂归位。",
           "周日肉体抗拒。"]
    day=datetime.datetime.now().weekday()
    print(daily[day])

def Findname(person="小姐姐",height=144,weight=44):
    print(person+"的体重是："+str(weight)+"kg，身高是："+str(height)+"cm")
#这里用类型转换，转成str输出
Findname("胡凯",175,55)
Findname(weight=56,height=170,person="固定")
#如果不记得参数位置，可以指定输入
Findname()


#这里是确定不定参个数
def printCoffee(*coffeename):
    print("\n我喜欢的coffee：")
    for i in coffeename:
        print(i)

printCoffee("奶","白","兔")

#这里是使用可变参
def fun_Print_List(*person):
    for listPerson in person:
        for ListName in listPerson:
            name=ListName[0]
            weight=ListName[1]
            height=ListName[2]
            print(name+" "+str(height)+" "+str(weight))
list_A=[("kk",12,134),("LL",23,123),("mm",34,124)]
list_B=[("BB",34,23),("CC",12,23),("DD",12,12)]
fun_Print_List(list_A,list_B)

#这里使用一组字典解决问题
def printSign(**sign):
    print()
    for key,value in sign.items():
        print("["+key+"]的意思是："+value)
printSign(GG="西内",jj="哟西")


#返回值
