String_Chooice = ['[------------MOOC----------]',
                  '[1]温度转换',
                  '[2]绘制图形',
                  '[3]获取响应头',
                  '[4]JSON',
                  '[5]二进制图片',
                  '[6]复杂请求',
                  '[7]代理IP',
                  '[8]上传文件',
                  '[9]结束',
                  '[-----------Choose---------]'
                  ]

def Temple_FC():
    choose_tempstr = input("请输入带符号的温度：F/C")
    print(choose_tempstr[-1],'-',int(choose_tempstr[0:-1]))
    if choose_tempstr[-1] in ['F','f']:
        C=(eval(choose_tempstr[0:-1])-32)/1.8
        print("转换后的温度是{:.2f}C".format(C),'\n')
        print_MainMenu()
    elif choose_tempstr[-1] in['C','c']:
        F=1.8*eval(choose_tempstr[0:-1])+32
        print("转换后的温度是{:.2f}F".format(F),'\n')
        print_MainMenu()
    else:
        print("输入错误!请检查\n")
        print_MainMenu()


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
    turtle.done
    print_MainMenu()


def Draw_Z():
    import turtle
    import random
    turtle.setup(1080, 960, 200, 200)  # 设置窗体启动位置，非必须
    turtle.left(45)
    turtle.fd(150)
    turtle.right(150)
    turtle.fd(150)
    turtle.left(150)
    turtle.fd(150)
    turtle.done
    turtle.exitonclick()

    print_MainMenu()


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
    # elif choose == 4:
    #     ullib3_JSON()
    # elif choose == 5:
    #     ullib3_2JingZhi()
    # elif choose == 6:
    #     ullib3_GET2()
    # elif choose == 7:
    #     ullib3_SetProxy()
    # elif choose == 8:
    #     ullib3_PutFile()
    elif choose == 9:
        print("已结束")


if __name__=='__main__':
    print_MainMenu()