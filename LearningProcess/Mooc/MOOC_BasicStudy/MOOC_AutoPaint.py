import turtle as t

t.title("自动")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

datals=[]
f=open("data.txt")
for line in f:
    line=line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
f.close()
for i in range(len(datals)):
    t.pencolor(datals[1][3],datals[1][4],datals[1][5])
    t.fd(datals[1][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

