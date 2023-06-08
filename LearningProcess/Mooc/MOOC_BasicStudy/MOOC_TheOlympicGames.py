from random import random


def printInfo():
    print("这个是A、B两个选手之间的竞技比赛")
    print("程序运行需要A、B的能力值(以0-1之间的小数表示)")


def getInputs():
    a=eval(input("请输入A的能力值（0-1）："))
    b=eval(input("请输入B的能力值（0-1）："))
    n=eval(input("模拟比赛的场次："))
    return a,b,n


def printSummary(winsA, winsB):
    n=winsA+winsB
    print(n)
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))


def gameOver(scoreA,scoreB):
    return scoreA==15 or scoreB==15

def simOneGames(proA, proB):
    scoreA=0
    scoreB=0
    serving="A"
    while not gameOver(scoreA,scoreB):
        if serving=="A":
            if random()<proA:
                scoreA+=1
                # print("WA")
            else:
                serving="B"
        else:
            if random()<proB:
                scoreB+=1
                # print("WB")
            else:
                serving="A"
        return scoreA,scoreB

def simNGames(n, proA, proB):
    winsA=0
    winsB=0
    for i in range(n):
        # print(i)
        scoreA,scoreB=simOneGames(proA,proB)
        if scoreA>scoreB:
            winsA+=1
            # print("WinA")

        else:
            winsB+=1
            # print("WinB")
    # print(winsA,winsB)
    return winsA,winsB


def main():
    # print("步骤一")
    printInfo()
    # print("步骤二")
    proA,proB,n=getInputs()
    # print("步骤三")
    winsA,winsB=simNGames(n,proA,proB)
    # print("步骤四")
    printSummary(winsA,winsB)

if __name__ == '__main__':
    main()