

String_Chooice = ['[------------MOOC----------]',
                  '[1]温度转换',
                  '[2]绘制蛇',
                  '[3]绘制Z',
                  '[4]数据类型',
                  '[5]dayday_UP',
                  '[6]时间',
                  '[7]代理IP',
                  '[8]EX',
                  '[9]结束',
                  '[10]圆周率',
                  '[11]圆周率',

                  '[-----------Choose---------]'
                  ]

def Temple_FC():
    choose_tempstr = input("请输入带符号的温度：F/C")
    print(choose_tempstr[-1],'-',int(choose_tempstr[0:-1]))
    if choose_tempstr[-1] in ['F','f']:
        C=(eval(choose_tempstr[0:-1])-32)/1.8
        print("转换后的温度是{:.2f}C".format(C),'\n')
    elif choose_tempstr[-1] in['C','c']:
        F=1.8*eval(choose_tempstr[0:-1])+32
        print("转换后的温度是{:.2f}F".format(F),'\n')
    else:
        print("输入错误!请检查\n")
def Draw_Snack():
    import turtle
    import random
    turtle.setup(1080,1200,0,0)#设置窗体启动位置，非必须
    # a = turtle.Turtle()  # instantiate a new turtle object called 'a'
    # a.hideturtle()  # make the turtle invisible
    # a.penup()  # don't draw when turtle moves
    # a.goto(-200, -200)  # move the turtle to a location
    # a.showturtle()  # make the turtle visible
    # a.pendown()  # draw when the turtle moves
    # a.goto(50,-50)  # move the turtle to a new location
    turtle.penup()
    turtle.fd(-250)
    turtle.goto(0, 0)
    turtle.fd(random.randint(20,21))
    turtle.pendown()
    turtle.pensize(25)
    turtle.pencolor('Black')
    turtle.seth(-40)
    for i in range(4):
        turtle.colormode(255)

        x=random.randint(20,120)
        print(x)
        turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.circle(x,80)
        turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.circle(-x,80)
    turtle.circle(40,80/2)
    turtle.fd(40)
    turtle.circle(16,180)
    turtle.width(40)
    turtle.fd(40*2/3)
    turtle.exitonclick()

def Draw_Z():
    import turtle
    turtle.setup(1080, 960, 200, 200)  # 设置窗体启动位置，非必须
    turtle.left(45)
    turtle.fd(150)
    turtle.right(150)
    turtle.fd(150)
    turtle.left(150)
    turtle.fd(150)
    turtle.exitonclick()

def SJ_int_float():
    print("0.1+0.2==0.3:",0.1+0.2==0.3)
    print("round(0.1+0.2,1)==0.3:",round(0.1+0.2,1)==0.3)
    print("4.3e-3=",4.3e-3,"\n4.3e3=",4.3e3)
def dayday_UP():
    day_Factor=float(input("麻烦输入每天学习幅度："))
    day_UP=pow(1+float(day_Factor),365)
    day_Down=pow(1-float(day_Factor),365)
    print("学习的力量{:.2f},不学习的力量{:.2f}".format(day_UP,day_Down))

    day_UP_Down=1.0
    for i in range(365):
        if i % 7 in [6,0]:
            day_UP_Down=day_UP_Down*(1-day_Factor)
        else:
            day_UP_Down=day_UP_Down*(1+day_Factor)
    print("努力工作的社畜的力量：{:.2f}".format(day_UP_Down))
def Time_Try():
    import time
    import random
    time_Start=time.perf_counter()
    print("时间获取、格式化、计时")
    print("time.time():",time.time())
    print("ctime.time():",time.ctime())
    print("ctime.gmtime():",time.gmtime())
    t=time.gmtime()
    print("time.strftime(\"%Y-%m-%d %H:%M:%S\", t):", time.strftime("%Y-%m-%d %H:%M:%S", t))
    time.sleep(1.1)
    time_End=time.perf_counter()
    print("计时：",time_End-time_Start)
    scale=10
    print("-------开始-------")
    for i in range(scale+1):
        a="*"*i
        b="."*(scale-i)
        c=(i/scale)*100
        print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end="")
        time.sleep(random.random())
    print("\n-------结束-------")
    time_End = time.perf_counter()
    print("计时：",time_End-time_Start)
def Run_time():
    import time
    import random
    scale=10
    a = "*"
    b = "."
    int=0
    i=0
    print("\n-------开始-------")
    time_Start = time.perf_counter()
    while i < 100:
        raise_1=random.randint(1,5)
        if (i+raise_1)>100:
            i=100
            int=i//10
            print("\r{:^3.0f}%[{}->{}]".format(i, a*int, b*(10-int)),end="")

        else:
            i += raise_1
            time.sleep(random.random()/2)
            if i/10>int:
                int=(i//10)
                print("\r{:^3.0f}%[{}->{}]".format(i, a*int, b*(10-int)),end="")

    print("\n-------结束-------")
    time_End = time.perf_counter()
    print("加载时长：",time_End-time_Start)

def Run_EX():
    try:
        get=eval(input("请输入整数"))
    except NameError :
        import time
        import random
        for i in range(3):
            time.sleep(random.random()/2)
            print("玩呢{}".format("?"*(2*i+1)))
            time.sleep(random.random())

def Circle_Pai():
    pi=0
    n=100
    for k in range(n):
        pi +=1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
    print("圆周率为：",pi)


    from random import random
    from time import perf_counter
    Dos=1000*1000
    hits=0.0
    start=perf_counter()
    for i in range(1,Dos+1):
        x,y=random(),random()
        dis=pow(x**2+y**2,0.5)
        if dis <=1.0:
            hits=hits+1
    pi=4*(hits/Dos)
    print("圆周率为：{}".format(pi))
    print("运行时间是{}：".format(perf_counter()-start))


def math_DG(n):
    if n==0:
        return 1
    else:
        return n*math_DG(n-1)

    count=0
def hannuota(n,src,dst,mid):
    global count
    if n==1:
        print("{}:{}->{}".format(1,src,dst))
        count+=1
    else:
        hannuota(n-1, src,mid , dst)
        print("{}:{}->{}".format(n,src,dst))
        count+=1
        hannuota(n-1,mid, dst, src)


def print_MainMenu():
    for i in String_Chooice:
        print(i)
    choose = int(input("请输入选项："))
    if choose == 1:
        Temple_FC()
    elif choose == 2:
        Draw_Snack()
    elif choose == 3:
        Draw_Z()
    elif choose == 4:
        SJ_int_float()
    elif choose == 5:
        dayday_UP()
    elif choose == 6:
        Time_Try()
    elif choose == 7:
        Run_time()
    elif choose == 8:
        Run_EX()
    elif choose == 9:
        print("已结束")
    elif choose == 10:
        Circle_Pai()
    elif choose == 11:
        print(math_DG(23))
    elif choose == 12:
        print("13")
    elif choose == 13:
        hannuota(3,"A","B","C")
        print(count)
    else:
        print("输错：长点心。。。")
        time.sleep(2)
if __name__=='__main__':
    import time
    while True:
        try:
            print_MainMenu()
        except :
            print("运行报错：长点心。。。")
            time.sleep(2)
