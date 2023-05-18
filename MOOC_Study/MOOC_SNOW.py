import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)
    input_size=eval(input("输入大小：500左右"))
    input_Level=eval(input("输入层级:3"))
    koch(input_size, input_Level)
    turtle.right(120)
    koch(input_size, input_Level)
    turtle.right(120)
    koch(input_size, input_Level)
    turtle.hideturtle()
if __name__=="__main__":
    main()