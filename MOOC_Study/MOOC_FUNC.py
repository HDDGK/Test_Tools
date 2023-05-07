import turtle
import time
def draw_Gap():
    turtle.penup()
    turtle.fd(5)

def draw_line(draw):
    draw_Gap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    draw_Gap()
    turtle.right(90)


def draw_Digit(digit):
    draw_line(True) if digit in [2,3,4,5,6,8,9]else draw_line(False)
    draw_line(True) if digit in [0,1,3,4,5,6,7,8,9]else draw_line(False)
    draw_line(True) if digit in [0,2,3,5,6,8,9]else draw_line(False)
    draw_line(True) if digit in [0,2,6,8]else draw_line(False)
    turtle.left(90)
    draw_line(True) if digit in [0,4,5,6,8,9]else draw_line(False)
    draw_line(True) if digit in [0,2,3,5,6,7,8,9]else draw_line(False)
    draw_line(True) if digit in [0,1,2,3,4,7,8,9]else draw_line(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def draw_Data(data):
    turtle.pencolor("red")
    for i in data:
        if i=="-":
            turtle.write('年',font=('Arial',38,"normal"))
            turtle.pencolor("Green")
            turtle.fd(65)
        elif i=="=":
            turtle.write('月',font=('Arial',38,"normal"))
            turtle.pencolor("blue")
            turtle.fd(65)
        elif i=="+":
            turtle.write('日',font=('Arial',38,"normal"))
        else:
            draw_Digit(eval(i))


def draw_Main():
    turtle.setup(1150,300,100,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    print(time.strftime('%Y-%m=%d+',time.gmtime()))
    draw_Data(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()

def main_TimeChange():
    int_NUM = time.strftime('%Y-%m=%d+%H:%M:%S', time.gmtime())[14:16]
    print(int_NUM)
    print( time.strftime('%Y-%m=%d+%H:%M:%S', time.gmtime()))
    while True:
        if int_NUM==time.strftime('%Y-%m=%d+%H:%M:%S', time.gmtime())[14:16]:
            print(time.strftime('%Y-%m=%d+%H:%M:%S', time.gmtime())[17:19])
            time.sleep(1)
        else:
            int_NUM =time.strftime('%Y-%m=%d+%H:%M:%S', time.gmtime())[14:16]
            print(time.strftime('%Y-%m=%d+%H:%M:%S', time.gmtime())[17:19])
            turtle.clearscreen()
            draw_Main()





if __name__=="__main__":
    main_TimeChange()



